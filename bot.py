import os
import secrets

import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

if not BOT_TOKEN:
    raise RuntimeError("Не найден BOT_TOKEN")

if not WEBHOOK_SECRET:
    raise RuntimeError("Не найден WEBHOOK_SECRET")

bot = telebot.TeleBot(BOT_TOKEN)

if __name__ == "__main__":
    print("IT404: токен загружен.")
    print("Для локального тестирования позже настроим отдельный режим.")