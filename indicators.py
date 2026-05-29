import pandas as pd
import ta


def add_indicators(
    df,
    ema_fast,
    ema_slow,
    rsi_period
):

    df["ema_fast"] = ta.trend.ema_indicator(
        df["close"],
        window=ema_fast
    )

    df["ema_slow"] = ta.trend.ema_indicator(
        df["close"],
        window=ema_slow
    )

    df["rsi"] = ta.momentum.rsi(
        df["close"],
        window=rsi_period
    )

    return df