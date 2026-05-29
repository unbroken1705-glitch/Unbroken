from core.position_manager import (
    get_all_positions,
    update_position
)

from core.execution_engine import (
    execute_exit
)

from core.exchange import (
    get_price
)

from config.settings import (
    BREAK_EVEN_ENABLED
)


def monitor_positions():

    positions = get_all_positions()

    for symbol, position in positions.items():

        try:

            current_price = get_price(
                symbol
            )

            side = position["side"]

            entry = position["entry"]

            stop = position["stop"]

            target = position["target"]

            # =====================
            # LONG
            # =====================

            if side == "LONG":

                # TP

                if current_price >= target:

                    execute_exit(
                        symbol=symbol,
                        exit_price=current_price
                    )

                    continue

                # SL

                if current_price <= stop:

                    execute_exit(
                        symbol=symbol,
                        exit_price=current_price
                    )

                    continue

                # BREAK EVEN

                if BREAK_EVEN_ENABLED:

                    move_trigger = (
                        target - entry
                    ) * 0.5

                    if (
                        current_price
                        >=
                        entry + move_trigger
                    ):

                        if stop < entry:

                            update_position(
                                symbol,
                                "stop",
                                entry
                            )

            # =====================
            # SHORT
            # =====================

            elif side == "SHORT":

                # TP

                if current_price <= target:

                    execute_exit(
                        symbol=symbol,
                        exit_price=current_price
                    )

                    continue

                # SL

                if current_price >= stop:

                    execute_exit(
                        symbol=symbol,
                        exit_price=current_price
                    )

                    continue

                # BREAK EVEN

                if BREAK_EVEN_ENABLED:

                    move_trigger = (
                        entry - target
                    ) * 0.5

                    if (
                        current_price
                        <=
                        entry - move_trigger
                    ):

                        if stop > entry:

                            update_position(
                                symbol,
                                "stop",
                                entry
                            )

        except Exception as e:

            print(
                f"POSITION MONITOR ERROR {symbol}: {e}"
            )