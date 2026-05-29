import pandas as pd
import ta

from core.exchange import fetch_ohlcv

from config.assets import ASSET_CONFIGS


def get_signal(symbol):

    cfg = ASSET_CONFIGS[symbol]

    candles = fetch_ohlcv(
        symbol,
        timeframe=cfg["timeframe"],
        limit=200
    )

    df = pd.DataFrame(
        candles,
        columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    )

    bb = ta.volatility.BollingerBands(
        close=df["close"],
        window=20
    )

    df["upper"] = bb.bollinger_hband()
    df["lower"] = bb.bollinger_lband()

    df["rsi"] = ta.momentum.rsi(
        df["close"],
        window=14
    )

    last = df.iloc[-1]

    if (
        last["close"] <= last["lower"]
        and
        last["rsi"] < 30
    ):
        return "LONG"

    if (
        last["close"] >= last["upper"]
        and
        last["rsi"] > 70
    ):
        return "SHORT"

    return None