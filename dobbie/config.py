import logging
from confi import BaseEnvironConfig, IntConfig, ConfigField


class Configuration(BaseEnvironConfig):
    LOG_LEVEL = IntConfig(default=logging.DEBUG)

    API_KEY = ConfigField(required=True)

    TARGET_QUERY = ConfigField(default='dobbie')
    TARGET_QUERY_RESPONSE = ConfigField(default='Dobbie team is presenting in Dipoli, floor 2, near table K7')
