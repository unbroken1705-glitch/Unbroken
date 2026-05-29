import ccxt

from config.settings import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)

if not BINANCE_API_KEY or not BINANCE_API_SECRET:
    raise Exception(
        "BINANCE_API_KEY or BINANCE_API_SECRET missing in .env"
    )

exchange = ccxt.binance({
    "apiKey": BINANCE_API_KEY,
    "secret": BINANCE_API_SECRET,
    "enableRateLimit": True,
    "options": {
        "defaultType": "future"
    }
})

exchange.load_markets()


def test_connection():

    try:

        balance = exchange.fetch_balance()

        usdt = balance["USDT"]["total"]

        print(
            f"✅ Binance connected | Balance: {usdt:.2f} USDT"
        )

        return True

    except Exception as e:

        print(
            f"❌ Binance connection failed: {e}"
        )

        return False


def get_balance():

    balance = exchange.fetch_balance()

    return float(
        balance["USDT"]["free"]
    )


def get_total_balance():

    balance = exchange.fetch_balance()

    return float(
        balance["USDT"]["total"]
    )


def get_price(symbol):

    ticker = exchange.fetch_ticker(symbol)

    return float(
        ticker["last"]
    )


def fetch_ohlcv(
    symbol,
    timeframe="15m",
    limit=300
):

    return exchange.fetch_ohlcv(
        symbol=symbol,
        timeframe=timeframe,
        limit=limit
    )


def set_leverage(
    symbol,
    leverage
):

    try:

        market = symbol.replace("/", "")

        exchange.set_leverage(
            leverage,
            market
        )

        return True

    except Exception as e:

        print(
            f"Leverage error: {e}"
        )

        return False


def open_long(
    symbol,
    amount
):

    return exchange.create_market_buy_order(
        symbol,
        amount
    )


def open_short(
    symbol,
    amount
):

    return exchange.create_market_sell_order(
        symbol,
        amount
    )


def close_long(
    symbol,
    amount
):

    return exchange.create_market_sell_order(
        symbol,
        amount
    )


def close_short(
    symbol,
    amount
):

    return exchange.create_market_buy_order(
        symbol,
        amount
    )


def get_open_positions():

    try:

        positions = exchange.fetch_positions()

        active = []

        for pos in positions:

            contracts = float(
                pos.get(
                    "contracts",
                    0
                )
            )

            if contracts > 0:
                active.append(pos)

        return active

    except Exception as e:

        print(
            f"Position error: {e}"
        )

        return []