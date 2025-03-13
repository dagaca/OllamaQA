"""
This module sets up logging for the application. It configures a rotating
file handler using environment variables.
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

def setup_logging():
    """
    Set up logging configuration for the application.
    
    Returns:
        logger (logging.Logger): The configured logger.
    """
    log_dir = os.getenv("LOG_DIR", "logs")
    log_file = os.getenv("LOG_FILE", "app.log")
    log_path = os.path.join(log_dir, log_file)
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("qa_app")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = RotatingFileHandler(
            log_path, maxBytes=2 * 1024 * 1024, backupCount=5
        )
        fmt = (
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
