import pandas as pd
import ta

from core.exchange import fetch_ohlcv


def get_market_regime():

    candles = fetch_ohlcv(
        "BTC/USDT",
        timeframe="1h",
        limit=300
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

    df["ema50"] = ta.trend.ema_indicator(
        df["close"],
        window=50
    )

    df["ema200"] = ta.trend.ema_indicator(
        df["close"],
        window=200
    )

    df["atr"] = ta.volatility.average_true_range(
        df["high"],
        df["low"],
        df["close"],
        window=14
    )

    last = df.iloc[-1]

    atr_percent = (
        last["atr"] /
        last["close"]
    ) * 100

    if (
        last["ema50"] >
        last["ema200"]
    ):

        if atr_percent > 2.5:
            return "STRONG_BULL"

        return "BULL"

    if (
        last["ema50"] <
        last["ema200"]
    ):

        if atr_percent > 2.5:
            return "PANIC"

        return "BEAR"

    return "RANGE"