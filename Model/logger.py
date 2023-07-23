import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name):
        self.logger = self.get_logger(name)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )
        logging.getLogger("httpx").setLevel(logging.WARNING)

        handler = self.create_handler()
        self.logger.addHandler(handler)

    def create_handler(self):
        handler = RotatingFileHandler("Model/logs/app.log", maxBytes=20000, backupCount=5)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        return handler

    def get_logger(self, name):
        return logging.getLogger(name)

    def log_user_message(self, update):
        self.logger.info(f"{update.effective_user} - {update.effective_message}")
