import logging

from telebot.updater import updater

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)

    updater.import_handlers(r'telebot/component')

    updater.init(drop_pending_updates=True)