from loguru import logger

def get_logger():
    logger.add("logs/agrisense.log", rotation="1 MB", retention="7 days", level="INFO")
    return logger

