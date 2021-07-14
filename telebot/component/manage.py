import logging

from telegram import Update, BotCommand
from telegram.ext import CommandHandler, CallbackContext

from telebot.updater import updater
from telebot.qclient import qclient

logger = logging.getLogger(__name__)


def resume_all(update: Update, context: CallbackContext):
    logger.info('resume all command from %s', update.message.from_user.first_name)

    qclient.resume_all()

    update.message.reply_text('所有任务已经启动!')


def pause_all(update: Update, context: CallbackContext):
    logger.info('pause all command from %s', update.message.from_user.first_name)

    qclient.pause_all()

    update.message.reply_text('所有任务已经暂停!')


updater.add_handler(CommandHandler(['resumeall'], resume_all), bot_command=BotCommand("resumeall", "启动所有任务"))
updater.add_handler(CommandHandler(['pauseall'], pause_all), bot_command=BotCommand("pauseall", "暂停所有任务"))
