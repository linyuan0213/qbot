import yaml
import logging
import os

logger = logging.getLogger(__name__)


class Config:

    def __init__(self) -> None:

        try:
            QB_CONF = os.environ['QB_CONF']
        except Exception:
            raise ValueError

        self.config_file = QB_CONF

    def get_conf(self):

        try:
            with open(self.config_file) as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            logger.debug('Config file <%s> not found', os.path.normpath(self.config_file))
            return

        return config


conf = Config()