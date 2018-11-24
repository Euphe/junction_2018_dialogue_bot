import logging
from confi import BaseEnvironConfig, IntConfig, ConfigField


class Configuration(BaseEnvironConfig):
    LOG_LEVEL = IntConfig(default=logging.DEBUG)

    API_KEY = ConfigField(required=True)

    TARGET_QUERY = ConfigField(default='presentation')
    TARGET_QUERY_RESPONSE = ConfigField(default='Presentations are happening at main stage')
