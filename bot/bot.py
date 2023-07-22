import logging
import os

from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes, \
    CallbackContext

from controller import Controller

# Credentials
load_dotenv('../Model/credentials.env')
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Instantiate the Controller
controller = Controller()

FOOD = 0


# Command handler to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(controller.handle_start_command(update, context))


async def nutritional_information_request(update: Update, context: CallbackContext):
    user_response = update.message.text
    await update.message.reply_text(controller.handle_request_nutritional_information(update, context))


async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        'Bye', reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


# Error handler
async def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    print("Starting bot")
    app = Application.builder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("start", start))
    nutritional_information_conversation_handler = ConversationHandler(
        entry_points=[(CommandHandler("request_nutritional_info", nutritional_information_request))],
        states={
            FOOD: [MessageHandler(filters.TEXT, nutritional_information_request)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]

    )

    logger.info("Bot started. Press Ctrl+C to stop.")
    app.add_handler(nutritional_information_conversation_handler)
    app.add_error_handler(error)
    print("Polling bot")
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()
