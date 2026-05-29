import pandas as pd
import ta


def atr_filter(
    df,
    period=14,
    minimum=0.5
):
    atr = ta.volatility.average_true_range(
        df["high"],
        df["low"],
        df["close"],
        window=period
    )

    current_atr = atr.iloc[-1]

    return current_atr > minimum