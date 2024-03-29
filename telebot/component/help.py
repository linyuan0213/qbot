import logging

from telegram import Update, BotCommand
from telegram.ext import CommandHandler, CallbackContext

from telebot.updater import updater


logger = logging.getLogger(__name__)

SHOW_MESSAGE = """<b>使用</b>:
• /help: 帮助
• /list: 展示所有任务
• /downloading: 展示正在下载的任务
• /uploading: 展示正在上传的任务
• /completed: 展示已完成的任务
• /paused: 展示已暂停的任务
• /pauseall: 暂停所有任务
• /resumeall: 启动所有任务
• /startnotify: 开启下载完成提醒
• /stopnotify: 关闭下载完成提醒
• /setpath: 设置下载路径 (不加参数获取当前路径), Usage: /setpath /download
• /setcategory: 设置下载分类 (不加参数获取当前分类), Usage: /setcategory abc
• /reset: 重置下载路径和分类
• 将链接或者文件发送到 Bot 以添加任务
"""


def on_help(update: Update, context: CallbackContext):
    logger.info('/help from %s', update.message.from_user.first_name)

    update.message.reply_html(SHOW_MESSAGE)


updater.add_handler(CommandHandler('help', on_help), bot_command=BotCommand("help", "帮助!"))
