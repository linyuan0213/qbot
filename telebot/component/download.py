import logging
from os import confstr
from telebot.telebot import TeleBot

from telegram import Update, BotCommand, ParseMode
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters

from telebot.updater import updater
from telebot.qclient import qclient

from config.config import conf


logger = logging.getLogger(__name__)


def download_from_magnet(update: Update, context: CallbackContext):

    logger.info('Magnet from %s', update.effective_user.first_name)

    save_path = conf.get_conf()['qbittorrent']['save_path']
    category = conf.get_conf()['qbittorrent']['category']

    magnet = update.message.text

    res = qclient.add_link(link=magnet, save_path=save_path, category=category, is_paused=False)
    logger.debug('add status: %s', res)

    update.message.reply_html(
        'Magnet 已添加',
        quote=True
    )

    if res == 'Ok.':
        text = "添加成功: <code>{}</code>".format(
            magnet
        )
    else:
        text = "添加失败: <code>{}</code>".format(
            magnet
        )

    context.bot.send_message(
        update.effective_chat.id,
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )

def download_from_url(update: Update, context: CallbackContext):

    logger.info('Url from %s', update.effective_user.first_name)

    save_path = conf.get_conf()['qbittorrent']['save_path']
    category = conf.get_conf()['qbittorrent']['category']

    torrent_url = update.message.text

    res = qclient.add_link(link=torrent_url, save_path=save_path, category=category, is_paused=False)
    logger.debug('add status: %s', res) 

    update.message.reply_text('Torrent url 已添加', quote=True)

    if res == 'Ok.':
        text = "Url 添加成功: {}".format(
            torrent_url
        )
    else:
        text = "Url 添加失败: {}".format(
            torrent_url
        )
    context.bot.send_message(update.effective_chat.id, text)

def download_from_file(update: Update, context: CallbackContext):
    
    logger.info('application/x-bittorrent document from %s', update.effective_user.first_name)

    save_path = conf.get_conf()['qbittorrent']['save_path']
    category = conf.get_conf()['qbittorrent']['category']

    document = update.message.document
    if document.mime_type != "application/x-bittorrent" and not document.file_name.lower().endswith(".torrent"):
        logger.info('invalid document from %s (mime type: %s; file name: %s)', update.effective_user.full_name,
                    document.mime_type, document.file_name)

        update.message.reply_markdown(
            'Torrent 文件无效 (`.torrent` extension or `application/x-bittorrent` mime type)',
            quote=True
        )
        return

    file_id = document.file_id
    torrent_file = context.bot.get_file(file_id)

    file_path = 'resources/{}'.format(document.file_name)
    torrent_file.download(file_path)

    res = qclient.add_torrent(file_name=file_path, save_path=save_path, category=category, is_paused=False)

    update.message.reply_text('Torrent 已添加', quote=True)

    # os.remove(file_path)

    text = "添加 torrent 文件 {}".format(
        document.file_name or "[unknown file name]"
    )

    context.bot.send_message(update.effective_chat.id, text)


updater.add_handler(MessageHandler(Filters.text & Filters.regex(r'^magnet:\?.*'), download_from_magnet))
updater.add_handler(MessageHandler(Filters.text & Filters.regex(r"^https?:\/\/.*(jackett|\.torren|\/torrent).*"), download_from_url))
updater.add_handler(MessageHandler(Filters.document, download_from_file))