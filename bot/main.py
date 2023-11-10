import json
from telegram import Bot

from portfolio.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(TELEGRAM_BOT_TOKEN)

def send_getintouch(name, email, message):
    text = f"{name}\n{email}\n\n{message}"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text, disable_notification=True)


def send_data(data):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID,
                     text=f"```json\n{json.dumps(data, indent=4)}```", parse_mode="markdown", disable_notification=True)
