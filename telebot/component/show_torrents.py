import logging

from telegram import Update, BotCommand, ParseMode
from telegram.ext import CommandHandler, CallbackContext

from telebot.updater import updater
from telebot.qclient import qclient
from utils.bytes_utils import bytes_to_human

logger = logging.getLogger(__name__)


def list_all_torrents(update: Update, context: CallbackContext):
    logger.info('torrents list from %s', update.message.from_user.first_name)

    torrs = qclient.get_all_torrents()
    if not torrs:
        update.message.reply_text('没有torrent!')
        return

    torrs_list = list()

    for torrent in torrs:
        size = bytes_to_human(torrent.size)
        logger.info('%s: %s (%s)', torrent.name, torrent.state, size)
        torrs_list.append('{0}: {1} ({2})'.format(torrent.name, torrent.state, size))

    logger.info(torrs_list)

    context.bot.send_message(
        update.effective_chat.id,
        '\n----------------------\n'.join(torrs_list),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def list_downloading_torrents(update: Update, context: CallbackContext):
    logger.info('torrents list from %s', update.message.from_user.first_name)

    torrs = qclient.get_downloading_torrents()
    if not torrs:
        update.message.reply_text('没有正在下载的torrent!')
        return

    torrs_list = list()

    for torrent in torrs:
        speed = f'{bytes_to_human(torrent.dlspeed)}/s'
        size = bytes_to_human(torrent.size)
        progress = '%.2f%%' % (torrent.progress * 100)
        logger.info('%s: %s %s %s (%s)', torrent.name, size, progress, torrent.state, speed)
        torrs_list.append('{0}: {1} ({2} {3} {4})'.format(torrent.name, torrent.state, size, progress, speed))

    logger.info(torrs_list)

    context.bot.send_message(
        update.effective_chat.id,
        '\n----------------------\n'.join(torrs_list),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def list_uploading_torrents(update: Update, context: CallbackContext):
    logger.info('torrents list from %s', update.message.from_user.first_name)

    torrs = qclient.get_uploading_torrents()
    if not torrs:
        update.message.reply_text('没有正在上传的torrent!')
        return

    torrs_list = list()

    for torrent in torrs:
        speed = f'{bytes_to_human(torrent.upspeed)}/s'
        size = bytes_to_human(torrent.size)
        logger.info('%s: %s %s (%s)', torrent.name, size, torrent.state, speed)
        torrs_list.append('{0}: {1} ({2} {3})'.format(torrent.name, torrent.state, size, speed))

    logger.info(torrs_list)

    context.bot.send_message(
        update.effective_chat.id,
        '\n----------------------\n'.join(torrs_list),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def list_paused_torrents(update: Update, context: CallbackContext):
    logger.info('torrents list from %s', update.message.from_user.first_name)

    torrs = qclient.get_paused_torrents()
    if not torrs:
        update.message.reply_text('没有暂停的torrent!')
        return

    torrs_list = list()

    for torrent in torrs:
        logger.info('%s: %s (%s)', torrent.hash[-6:], torrent.name, torrent.state)
        torrs_list.append('{0}: {1} ({2})'.format(torrent.hash[-6:], torrent.name, torrent.state))

    logger.info(torrs_list)

    context.bot.send_message(
        update.effective_chat.id,
        '\n----------------------\n'.join(torrs_list),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def list_completed_torrents(update: Update, context: CallbackContext):
    logger.info('torrents list from %s', update.message.from_user.first_name)

    torrs = qclient.get_completed_torrents()
    if not torrs:
        update.message.reply_text('没有已完成的torrent!')
        return

    torrs_list = list()

    for torrent in torrs:
        size = bytes_to_human(torrent.size)
        logger.info('%s: %s (%s)', torrent.name, torrent.state, size)
        torrs_list.append('{0}: {1} ({2})'.format(torrent.name, torrent.state, size))

    logger.info(torrs_list)

    context.bot.send_message(
        update.effective_chat.id,
        '\n----------------------\n'.join(torrs_list),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


updater.add_handler(CommandHandler('list', list_all_torrents),
                    bot_command=BotCommand("list", "展示所有的torrent"))
updater.add_handler(CommandHandler('downloading', list_downloading_torrents),
                    bot_command=BotCommand("downloading", "展示正在下载的torrent"))
updater.add_handler(CommandHandler('uploading', list_uploading_torrents),
                    bot_command=BotCommand("uploading", "展示正在上传的torrent"))
updater.add_handler(CommandHandler('paused', list_paused_torrents),
                    bot_command=BotCommand("paused", "展示已暂停的torrent"))
updater.add_handler(CommandHandler('completed', list_completed_torrents),
                    bot_command=BotCommand("completed", "展示已完成的torrent"))
