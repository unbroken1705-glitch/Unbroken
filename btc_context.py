from core.market_regime import (
    get_market_regime
)

from config.assets import (
    ASSET_CONFIGS
)


def is_trade_allowed(symbol):

    regime = get_market_regime()

    allowed = ASSET_CONFIGS[
        symbol
    ]["allowed_regimes"]

    return regime in allowed


def get_current_regime():

    return get_market_regime()