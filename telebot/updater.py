from telegram.ext import Defaults

from .telebot import TeleBot
from config.config import Config

conf = Config()
token = conf.get_conf()['telegram']['token']
timeout = conf.get_conf()['telegram']['timeout']
workers = conf.get_conf()['telegram']['workers']

updater = TeleBot(
    token=token,
    defaults=Defaults(timeout=timeout, disable_web_page_preview=True),
    workers=workers
)