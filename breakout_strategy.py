from core.exchange import fetch_ohlcv

from config.assets import ASSET_CONFIGS

import pandas as pd


def get_signal(symbol):

    cfg = ASSET_CONFIGS[symbol]

    candles = fetch_ohlcv(
        symbol,
        timeframe=cfg["timeframe"],
        limit=100
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

    last = df.iloc[-1]

    recent_high = (
        df["high"]
        .tail(20)
        .max()
    )

    recent_low = (
        df["low"]
        .tail(20)
        .min()
    )

    if last["close"] > recent_high:
        return "LONG"

    if last["close"] < recent_low:
        return "SHORT"

    return None