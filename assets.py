ASSET_CONFIGS = {

    # ==================================================
    # BTC
    # ==================================================

    "BTC/USDT": {

        "strategy": "trend",

        "timeframe": "15m",

        "ema_fast": 50,
        "ema_slow": 200,

        "rsi_period": 14,

        "rsi_long": 55,
        "rsi_short": 45,

        "leverage": 4,

        "risk_multiplier": 1.0,

        "allowed_regimes": [
            "BULL",
            "STRONG_BULL",
            "BEAR"
        ]
    },

    # ==================================================
    # ETH
    # ==================================================

    "ETH/USDT": {

        "strategy": "trend",

        "timeframe": "15m",

        "ema_fast": 34,
        "ema_slow": 200,

        "rsi_period": 14,

        "rsi_long": 54,
        "rsi_short": 46,

        "leverage": 5,

        "risk_multiplier": 1.1,

        "allowed_regimes": [
            "BULL",
            "STRONG_BULL",
            "BEAR"
        ]
    },

    # ==================================================
    # SOL
    # ==================================================

    "SOL/USDT": {

        "strategy": "breakout",

        "timeframe": "15m",

        "ema_fast": 21,
        "ema_slow": 100,

        "rsi_period": 14,

        "rsi_long": 58,
        "rsi_short": 42,

        "leverage": 4,

        "risk_multiplier": 0.9,

        "allowed_regimes": [
            "BULL",
            "STRONG_BULL"
        ]
    },

    # ==================================================
    # BNB
    # ==================================================

    "BNB/USDT": {

        "strategy": "trend",

        "timeframe": "15m",

        "ema_fast": 50,
        "ema_slow": 150,

        "rsi_period": 14,

        "rsi_long": 54,
        "rsi_short": 46,

        "leverage": 5,

        "risk_multiplier": 1.0,

        "allowed_regimes": [
            "BULL",
            "STRONG_BULL",
            "BEAR"
        ]
    },

    # ==================================================
    # XRP
    # ==================================================

    "XRP/USDT": {

        "strategy": "range",

        "timeframe": "15m",

        "ema_fast": 20,
        "ema_slow": 50,

        "rsi_period": 14,

        "rsi_long": 30,
        "rsi_short": 70,

        "leverage": 3,

        "risk_multiplier": 0.8,

        "allowed_regimes": [
            "RANGE",
            "BULL"
        ]
    }
}