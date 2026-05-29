import time
import requests

from config.settings import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID
)

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

LAST_UPDATE_ID = None

BOT_STATE = {
    "running": True,
    "mode": "BALANCED"
}


def send_message(text):

    requests.post(
        f"{BASE_URL}/sendMessage",
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        }
    )


def get_updates():

    global LAST_UPDATE_ID

    url = f"{BASE_URL}/getUpdates"

    if LAST_UPDATE_ID is not None:
        url += f"?offset={LAST_UPDATE_ID + 1}"

    try:

        response = requests.get(
            url,
            timeout=10
        ).json()

        return response.get(
            "result",
            []
        )

    except Exception:
        return []


def process_command(text):

    if text == "/pause":

        BOT_STATE["running"] = False

        send_message(
            "⛔ Bot paused"
        )

    elif text == "/resume":

        BOT_STATE["running"] = True

        send_message(
            "✅ Bot resumed"
        )

    elif text == "/status":

        send_message(
            f"🤖 SHADOWBOT V11\n\n"
            f"Running: {BOT_STATE['running']}\n"
            f"Mode: {BOT_STATE['mode']}"
        )

    elif text == "/ping":

        send_message(
            "🏓 Pong"
        )


def telegram_polling():

    global LAST_UPDATE_ID

    while True:

        try:

            updates = get_updates()

            for update in updates:

                LAST_UPDATE_ID = update["update_id"]

                if "message" not in update:
                    continue

                chat_id = str(
                    update["message"]["chat"]["id"]
                )

                if chat_id != str(
                    TELEGRAM_CHAT_ID
                ):
                    continue

                text = update[
                    "message"
                ].get(
                    "text",
                    ""
                )

                process_command(text)

        except Exception as e:

            print(
                f"Telegram polling error: {e}"
            )

        time.sleep(3)