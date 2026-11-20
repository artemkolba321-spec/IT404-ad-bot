import os

import telebot
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан")

if not WEBHOOK_SECRET:
    raise RuntimeError("WEBHOOK_SECRET не задан")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)


@app.get("/")
def home():
    return "IT404 Bot is running!", 200


@app.post("/webhook")
def webhook():
    secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")

    if secret != WEBHOOK_SECRET:
        return "Forbidden", 403

    update = telebot.types.Update.de_json(
        request.get_data(as_text=True)
    )
    bot.process_new_updates([update])

    return "OK", 200


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в рекламную систему IT404! 🚀"
    )