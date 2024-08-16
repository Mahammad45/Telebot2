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


def create_user_table():
    with PGCONN.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reg_users (
                id SERIAL PRIMARY KEY,
                user_id BIGINT UNIQUE,
                username VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                phone VARCHARD(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        PGCONN.commit()    
        logger.info("User table created successfully.")



def insert_user(message: types.Message):
    with PGCONN.cursor() as cursor:
        cursor.execute("""
            INSERT INTO reg_users (user_id, username, first_name, last_name, phone)
            VALUES (%s, %s, %s, %s, %s)
        """, (message.from_user.id, message.from_user.username, 
              message.from_user.first_name, message.from_user.last_name,
              message.contact.phone_number))
        PGCONN.commit()
        logger.info(f"User {message.from_user.id} inserted successfully")




def check_user(user: types.User):
    with PGCONN.cursor() as cursor:
        cursor.execute(f"SELECT * FROM reg_users WHERE user_id = {user.id}")
        result = cursor.fetchone()
        return result if result else None


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, "Hello, I'm a bot!")


if __name__ == "__main__":
    try:
        
        logger.info("Starting the application...")
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
