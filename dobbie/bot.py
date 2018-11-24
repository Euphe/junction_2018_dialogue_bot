import re
from telegram.ext import Updater, RegexHandler, CommandHandler
from . import config
from .util import get_logger


logger = get_logger('bot', config.Configuration.LOG_LEVEL)

TEXT_REGEX = re.compile(r'^[^/](.|\n)+$', re.IGNORECASE | re.UNICODE)


class ManagerUser:
    def __init__(self, user_id, last_request_user):
        self.user_id = user_id
        self.last_request_user = last_request_user


manager_users = [ ]


DEFAULT_LOCATION = 'Dipoli'


USER_LOCATIONS = {
    389451119: 'Dipoli, floor 2, presentation area'
}


def manager_handler(bot, update):
    user_id = update.message.from_user.id
    if user_id in [m.user_id for m in manager_users]:
        update.message.reply_text('You are already a manager!')
    else:
        manager_users.append(ManagerUser(user_id, None))
        update.message.reply_text('Promoted to manager')


def handle_manager_message(bot, update, args=None, **kwargs):
    for manager in manager_users:
        manager_id = manager.user_id
        if manager_id == update.message.from_user.id and manager.last_request_user:
            bot.sendMessage(chat_id=manager.last_request_user, text=f'Manager reply: "{update.message.text}"')
            update.message.reply_text('Reply sent')
            break


def anything_handler(bot, update, args=None, **kwargs):
    user_id = update.message.from_user.id
    user_location = USER_LOCATIONS.get(user_id, DEFAULT_LOCATION)
    if user_id in [m.user_id for m in manager_users]:
        handle_manager_message(bot, update, args=None, **kwargs)
    update.message.reply_text(f'By my information you are at {user_location}')
    if config.Configuration.TARGET_QUERY in update.message.text:
        update.message.reply_text(config.Configuration.TARGET_QUERY_RESPONSE)
    else:
        update.message.reply_text('I can\'t help with that, but I will notify a manager to assist you')
        for manager in manager_users:
            manager_id = manager.user_id
            manager.last_request_user = user_id
            bot.sendMessage(chat_id=manager_id, text=f'Person needs help: "{update.message.text}"\n'
                                                     f'Location: {user_location}')


class Bot:
    api_key = None
    channel_id = None

    def __init__(self, api_key):
        self.__class__.api_key = api_key

        self.updater = Updater(api_key)
        self.updater.dispatcher.add_error_handler(self.error_handler)

    def start(self):
        self.updater.start_polling()
        self.updater.idle()

    @staticmethod
    def error_handler(bot, update, error):
        """Log Errors caused by Updates."""
        logger.error('Update "%s" caused error "%s"', update, error)


def create_bot(api_key):
    bot = Bot(api_key)
    bot.updater.dispatcher.add_handler(CommandHandler('manager', manager_handler))
    bot.updater.dispatcher.add_handler(RegexHandler(TEXT_REGEX, anything_handler))
    return bot
