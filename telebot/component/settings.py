import logging

from telegram import Update, BotCommand
from telegram.ext import CommandHandler, CallbackContext

from telebot.updater import updater
from config.config import conf

logger = logging.getLogger(__name__)


def set_path(update: Update, context: CallbackContext):
    logger.info('Set path from %s', update.message.from_user.first_name)

    if not context.args:
        update.message.reply_text('当前位置: {}'.format(conf.get_conf()['qbittorrent']['save_path']))
        return

    save_path = context.args[0]
    conf.set_save_path(save_path=save_path)
    update.message.reply_text('下载路径设置成功，当前位置: {}'.format(conf.get_conf()['qbittorrent']['save_path']))


def set_categroy(update: Update, context: CallbackContext):
    logger.info('Set category from %s', update.message.from_user.first_name)

    if not context.args:
        update.message.reply_text('当前分类: {}'.format(conf.get_conf()['qbittorrent']['category']))
        return

    category = context.args[0]

    conf.set_category(category=category)
    update.message.reply_text('分类设置成功，当前分类: {}'.format(conf.get_conf()['qbittorrent']['category']))


def reset(update: Update, context: CallbackContext):
    logger.info('Reset from %s', update.message.from_user.first_name)

    conf.reset()
    logger.debug('config: %s', conf.get_conf()['qbittorrent']['save_path'])
    update.message.reply_text('重置成功!')


updater.add_handler(CommandHandler(['setpath'], set_path), bot_command=BotCommand("setpath", "设置下载路径"))
updater.add_handler(CommandHandler(['setcategory'], set_categroy), bot_command=BotCommand("setcategory", "设置分类"))
updater.add_handler(CommandHandler(['reset'], reset), bot_command=BotCommand("reset", "重置配置"))
