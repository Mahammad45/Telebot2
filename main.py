import os
import sys

import logging
from random import randint, choice
from datetime import datetime, timedelta


import telebot
from telebot import types

from core.setting import TOKEN, PGCONNECTION


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



if __name__ == "__main__":
    try:
        
        logger.info("Starting the application...")
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"An error occurred: {e}")