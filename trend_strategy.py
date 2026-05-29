from core.exchange import fetch_ohlcv

from config.assets import ASSET_CONFIGS

from utils.indicators import add_indicators


def get_signal(symbol):

    cfg = ASSET_CONFIGS[symbol]

    candles = fetch_ohlcv(
        symbol,
        timeframe=cfg["timeframe"],
        limit=300
    )

    import pandas as pd

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

    df = add_indicators(
        df,
        cfg["ema_fast"],
        cfg["ema_slow"],
        cfg["rsi_period"]
    )

    last = df.iloc[-1]

    if (
        last["ema_fast"] >
        last["ema_slow"]
        and
        last["rsi"] >
        cfg["rsi_long"]
    ):
        return "LONG"

    if (
        last["ema_fast"] <
        last["ema_slow"]
        and
        last["rsi"] <
        cfg["rsi_short"]
    ):
        return "SHORT"

    return None