import logging
from . import config
from .bot import create_bot


def main():
    bot = create_bot(config.Configuration.API_KEY)
    logging.info(f'Starting with config:\n{config.Configuration.as_text()}')
    bot.start()


if __name__ == '__main__':
    main()