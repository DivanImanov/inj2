import telebot
import os

TOKEN = os.environ.get("TGBOT_TOKEN", default='123:abc')
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

