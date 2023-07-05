import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from controller import Controller

# Credentials
load_dotenv('../Model/credentials.env')
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Instantiate the Controller
controller = Controller()


# Command handler to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(controller.handle_start_command(update, context))


# Error handler
async def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    print("Starting bot")
    app = Application.builder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("Bot started. Press Ctrl+C to stop.")
    app.add_error_handler(error)
    print("Polling bot")
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()
