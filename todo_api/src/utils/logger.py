import logging 
from pathlib import Path
import os

def get_logger() -> logging.RootLogger:
    log_file_name = os.path.join(
        __name__, os.pardir, "logs/", "development.log")

    logger = logging.getLogger()

    log_formatter = logging.Formatter( "[%(levelname)-5.5s]  [%(filename)s]  %(message)s")

    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(log_formatter)

    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)
    return logger

logger = get_logger()