import logging
from logging.handlers import RotatingFileHandler


class Logger:
    """The Logger class provides logging capabilities to record bot interactions and messages."""

    def __init__(self, name):
        """Initialize the Logger.

        Args:
            name (str): The name of the logger.
        """
        self.logger = self.get_logger(name)
        self.setup_logging()

    def setup_logging(self):
        """Set up the logging configuration with a rotating file handler."""
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )
        logging.getLogger("httpx").setLevel(logging.WARNING)

        handler = self.create_handler()
        self.logger.addHandler(handler)

    def create_handler(self):
        """Create a rotating file handler to log messages to the 'app.log' file.

        Returns:
            RotatingFileHandler: The rotating file handler for logging messages.
        """
        handler = RotatingFileHandler("Model/logs/app.log", maxBytes=20000, backupCount=5)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        return handler

    def get_logger(self, name):
        """Get a logger with the specified name.

        Args:
            name (str): The name of the logger.

        Returns:
            logging.Logger: The logger with the specified name.
        """
        return logging.getLogger(name)

    def log_user_message(self, update):
        """Log the user message.
        Args:
        Update (object): Update object containing the user message information.
        """
        self.logger.info(f"{update.effective_user} - {update.effective_message}")
