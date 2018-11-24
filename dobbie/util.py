import logging


def get_logger(name=__name__, log_level=logging.INFO):
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        '[%(asctime)s] - %(module)s - %(levelname)s: %(message)s')
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    handler.setFormatter(formatter)
    return logger
