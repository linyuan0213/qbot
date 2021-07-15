import yaml
import logging
import os
import copy

logger = logging.getLogger(__name__)


class Config:

    def __init__(self) -> None:

        self.__config = {}
        self.__old_config = {}

        try:
            QB_CONF = os.environ['QB_CONF']
        except Exception:
            raise ValueError

        try:
            with open(QB_CONF) as f:
                self.__config = yaml.safe_load(f)
                self.__old_config = copy.deepcopy(self.__config)
        except FileNotFoundError:
            logger.debug('Config file <%s> not found', os.path.normpath(QB_CONF))
            return

    def get_conf(self):
        return self.__config

    def set_save_path(self, save_path=None):

        if save_path is None:
            return

        if not save_path.startswith('/'):
            save_path = f'/{save_path}'
        logger.debug('save_path: %s', save_path)

        self.__config['qbittorrent']['save_path'] = save_path

    def set_category(self, category=None):
        if category is None:
            return

        logger.debug('save_path: %s', category)

        self.__config['qbittorrent']['category'] = category

    def reset(self):
        self.__config = copy.deepcopy(self.__old_config)


conf = Config()
