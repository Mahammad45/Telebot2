import os
import sys

import logging
from random import randint, choice
from datetime import datetime, timedelta


import telebot
from telebot import types

from core.settings import TOKEN, PGCONN


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, "Hello, I'm a bot!")


if __name__ == "__main__":
    try:
        
        logger.info("Starting the application...")
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
