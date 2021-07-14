import logging

from telegram import Update
from telegram.ext import CallbackContext


logger = logging.getLogger(__name__)


def list_torrents(update: Update, context: CallbackContext):
    logger.info('torrents list menu button from %s: %s', update.message.from_user.first_name, context.match[0])

    command = context.match[0]
    if command.startswith('/'):
        command = command.replace('/', '')

    logger.info('torrents status: %s', command)