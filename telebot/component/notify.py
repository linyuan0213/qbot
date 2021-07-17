import logging
import sqlite3

from telegram import Update, BotCommand
from telegram.ext import CommandHandler, CallbackContext

from telebot.updater import updater
from telebot.qclient import qclient
from utils.bytes_utils import bytes_to_human

logger = logging.getLogger(__name__)


def alarm(context: CallbackContext) -> None:
    """发送提醒."""
    job = context.job

    tds = qclient.get_downloading_torrents()

    # 添加 sqlite3 连接
    conn = sqlite3.connect('qbot.db')
    cur = conn.cursor()

    for torrent in tds:

        # 添加正在下载记录
        cur.execute("INSERT OR IGNORE INTO torrent (id ,name) \
                    VALUES (?, ?)", (torrent.hash, torrent.name))
    conn.commit()

    tcs = qclient.get_completed_torrents()
    query = cur.execute("SELECT id, name FROM torrent")
    for td in query:
        for tc in tcs:
            if td[0] == tc.hash:
                size = bytes_to_human(tc.size)
                logger.info('%s: %s (%s)', tc.name, tc.state, size)
                torrent_info = f'{tc.name} 下载完成!'
                context.bot.send_message(job.context, text=torrent_info)

                # 删除已下载完成记录
                cur.execute("DELETE FROM torrent WHERE id = ?", (tc.hash,))
                conn.commit()


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_notify_timer(update: Update, context: CallbackContext) -> None:
    """添加任务到队列."""
    chat_id = update.message.chat_id

    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_repeating(alarm, 15, context=chat_id, name=str(chat_id))

    text = '下载完成提醒开启!'
    if job_removed:
        text += ' 老任务已经移除'
    update.message.reply_text(text)


def unset_notify(update: Update, context: CallbackContext) -> None:
    """移除任务."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = '提醒已经关闭' if job_removed else '你没有开启提醒'
    update.message.reply_text(text)


updater.add_handler(CommandHandler('startnotify', set_notify_timer),
                    bot_command=BotCommand("startnotify", "开启下载完成提醒"))
updater.add_handler(CommandHandler('stopnotify', unset_notify),
                    bot_command=BotCommand("stopnotify", "关闭下载完成提醒"))
