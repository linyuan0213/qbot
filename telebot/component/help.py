import logging
from telebot.telebot import TeleBot

from telegram import Update, BotCommand
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters

from telebot.updater import updater


logger = logging.getLogger(__name__)

def on_help(update: Update, context: CallbackContext):
    logger.info('/help from %s', update.message.from_user.first_name)

    update.message.reply_html('Help')

updater.add_handler(CommandHandler('help', on_help), bot_command=BotCommand("help", "帮助"))
updater.add_handler(MessageHandler(Filters.regex(r'^\/help$'), on_help))