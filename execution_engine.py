from datetime import datetime

from core.exchange import (
    open_long,
    open_short,
    close_long,
    close_short,
    get_total_balance
)

from core.position_manager import (
    add_position,
    remove_position,
    get_position,
    has_position
)

from core.database import save_trade

from core.notifier import (
    send_open_trade,
    send_close_trade
)

from risk.risk_engine import (
    calculate_position_size
)


def execute_entry(
    symbol,
    side,
    entry_price,
    stop_price,
    target_price,
    confidence,
    regime
):
    """
    Открытие позиции
    """

    if has_position(symbol):
        return False

    try:

        balance = get_total_balance()

        size = calculate_position_size(
            balance=balance,
            entry_price=entry_price,
            stop_price=stop_price
        )

        if size <= 0:
            return False

        if side == "LONG":

            open_long(
                symbol=symbol,
                amount=size
            )

        elif side == "SHORT":

            open_short(
                symbol=symbol,
                amount=size
            )

        else:
            return False

        position = {
            "symbol": symbol,
            "side": side,
            "entry": entry_price,
            "stop": stop_price,
            "target": target_price,
            "size": size,
            "confidence": confidence,
            "regime": regime,
            "opened_at": datetime.now()
        }

        add_position(
            symbol,
            position
        )

        save_trade(
            symbol=symbol,
            side=side,
            entry=entry_price,
            exit_price=0,
            pnl=0,
            status="OPEN",
            opened_at=str(datetime.now()),
            closed_at=""
        )

        send_open_trade(
            symbol=symbol,
            side=side,
            entry=entry_price,
            sl=stop_price,
            tp=target_price,
            confidence=confidence,
            regime=regime
        )

        print(
            f"OPENED {symbol} {side} | size={size}"
        )

        return True

    except Exception as e:

        print(
            f"ENTRY ERROR {symbol}: {e}"
        )

        return False


def execute_exit(
    symbol,
    exit_price
):
    """
    Закрытие позиции
    """

    position = get_position(symbol)

    if not position:
        return False

    try:

        side = position["side"]
        size = position["size"]
        entry_price = position["entry"]

        if side == "LONG":

            close_long(
                symbol=symbol,
                amount=size
            )

            pnl_percent = (
                (exit_price - entry_price)
                / entry_price
            ) * 100

        elif side == "SHORT":

            close_short(
                symbol=symbol,
                amount=size
            )

            pnl_percent = (
                (entry_price - exit_price)
                / entry_price
            ) * 100

        else:
            return False

        pnl_usdt = (
            pnl_percent / 100
        ) * (
            entry_price * size
        )

        balance = get_total_balance()

        send_close_trade(
            symbol=symbol,
            side=side,
            entry=entry_price,
            exit_price=exit_price,
            pnl_percent=pnl_percent,
            pnl_usdt=pnl_usdt,
            balance=balance
        )

        save_trade(
            symbol=symbol,
            side=side,
            entry=entry_price,
            exit_price=exit_price,
            pnl=pnl_usdt,
            status="CLOSED",
            opened_at=str(
                position["opened_at"]
            ),
            closed_at=str(
                datetime.now()
            )
        )

        remove_position(symbol)

        print(
            f"CLOSED {symbol} | pnl={round(pnl_usdt, 2)} USDT"
        )

        return True

    except Exception as e:

        print(
            f"EXIT ERROR {symbol}: {e}"
        )

        return False


def get_position_info(symbol):

    return get_position(symbol)


def has_open_position(symbol):

    return has_position(symbol)