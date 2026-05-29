import telebot

from config.settings import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID,
    TELEGRAM_ENABLED
)

if TELEGRAM_ENABLED:

    bot = telebot.TeleBot(
        TELEGRAM_TOKEN
    )

else:

    bot = None


def send_message(text):

    if not TELEGRAM_ENABLED:
        return

    try:

        bot.send_message(
            TELEGRAM_CHAT_ID,
            text
        )

    except Exception as e:

        print(
            f"Telegram error: {e}"
        )


def send_startup():

    send_message(
        "🚀 SHADOWBOT V11 STARTED"
    )


def send_shutdown():

    send_message(
        "⛔ SHADOWBOT V11 STOPPED"
    )


def send_error(error):

    send_message(
        f"❌ ERROR\n\n{error}"
    )


def send_open_trade(
    symbol,
    side,
    entry,
    sl,
    tp,
    confidence,
    regime
):

    text = f"""
🚀 OPEN TRADE

💰 {symbol}
📈 {side}

💵 Entry: {entry}

🎯 TP: {tp}
🛑 SL: {sl}

🧠 Confidence: {confidence}%

📊 Regime: {regime}
"""

    send_message(text)


def send_close_trade(
    symbol,
    side,
    entry,
    exit_price,
    pnl_percent,
    pnl_usdt,
    balance
):

    emoji = "🟢" if pnl_usdt >= 0 else "🔴"

    text = f"""
{emoji} TRADE CLOSED

💰 {symbol}
📈 {side}

💵 Entry: {entry}
💵 Exit: {exit_price}

📊 PNL: {pnl_percent:.2f}%

💲 PNL: {pnl_usdt:.2f}

🏦 Balance: {balance:.2f}
"""

    send_message(text)