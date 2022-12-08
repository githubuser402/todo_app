import logging 
from pathlib import Path

def get_logger() -> logging.RootLogger:
    """instance of logger module, will be used for logging operations"""
    
    # logger config
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # log format
    lg_format = "%(levelname)s|%(filename)s:%(lineno)d|%(asctime)s|%(message)s"
    log_format = logging.Formatter(lg_format)

    # file handler
    file_handler = logging.FileHandler(Path(__name__).parent / "logs/debug.log")
    file_handler.setFormatter(log_format)

    logger.handlers.clear()
    logger.addHandler(file_handler)
    return logger

logger = get_logger()