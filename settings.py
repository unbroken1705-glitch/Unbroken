import os

from dotenv import load_dotenv

load_dotenv()


# ==================================================
# BINANCE
# ==================================================

BINANCE_API_KEY = os.getenv(
    "BINANCE_API_KEY"
)

BINANCE_API_SECRET = os.getenv(
    "BINANCE_API_SECRET"
)


# ==================================================
# TELEGRAM
# ==================================================

TELEGRAM_ENABLED = True

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)


# ==================================================
# GENERAL
# ==================================================

BOT_NAME = "SHADOWBOT V11"

CHECK_INTERVAL = 60

LOG_LEVEL = "INFO"


# ==================================================
# RISK MANAGEMENT
# ==================================================

MAX_RISK_PER_TRADE = 0.015

MAX_DAILY_DRAWDOWN = 0.05

MAX_ACCOUNT_DRAWDOWN = 0.20

MAX_SIMULTANEOUS_POSITIONS = 3

MAX_CORRELATED_POSITIONS = 2

DEFAULT_LEVERAGE = 5


# ==================================================
# POSITION MANAGEMENT
# ==================================================

ENABLE_TRAILING_STOP = True

TRAILING_STOP_ATR_MULTIPLIER = 2.0

BREAK_EVEN_ENABLED = True


# ==================================================
# CONFIDENCE FILTER
# ==================================================

MIN_CONFIDENCE_SCORE = 70


# ==================================================
# DATABASE
# ==================================================

DATABASE_PATH = "data/trades.db"


# ==================================================
# MARKET REGIME
# ==================================================

BTC_REGIME_TIMEFRAME = "1h"

BTC_FAST_EMA = 50

BTC_SLOW_EMA = 200

BTC_ATR_PERIOD = 14


# ==================================================
# NOTIFICATIONS
# ==================================================

SEND_STARTUP_MESSAGE = True

SEND_TRADE_OPEN = True

SEND_TRADE_CLOSE = True

SEND_ERRORS = True


# ==================================================
# SAFETY CHECKS
# ==================================================

ALLOW_SHORTS = True

ALLOW_LONGS = True

ALLOW_MULTIPLE_POSITIONS = True


# ==================================================
# DEBUG
# ==================================================

DEBUG_MODE = False