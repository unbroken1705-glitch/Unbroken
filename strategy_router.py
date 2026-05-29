from config.assets import ASSET_CONFIGS

from strategies.trend_strategy import (
    get_signal as trend_signal
)

from strategies.breakout_strategy import (
    get_signal as breakout_signal
)

from strategies.range_strategy import (
    get_signal as range_signal
)


def get_signal(symbol):

    strategy = ASSET_CONFIGS[
        symbol
    ]["strategy"]

    if strategy == "trend":
        return trend_signal(symbol)

    if strategy == "breakout":
        return breakout_signal(symbol)

    if strategy == "range":
        return range_signal(symbol)

    return None