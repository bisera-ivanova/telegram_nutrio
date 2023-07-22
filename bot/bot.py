import logging
import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from controller import Controller

# Credentials
load_dotenv('../Model/credentials.env')
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

# Instantiate the Controller
controller = Controller()

reply_keyboard = [["Nutritional information", "Recipes"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


# Command handler to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(controller.handle_start_command(update, context),
                                    reply_markup=markup)
    return CHOOSING


async def handle_nutritional_information_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(controller.handle_request_nutritional_information_command(update, context))
    return TYPING_REPLY


async def respond_to_nutritional_information_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(controller.handle_user_input_nutritional_information(update, context),
                                    reply_markup=markup)
    return CHOOSING


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
    nutritional_information_conversation_handler = ConversationHandler(
        entry_points=[(CommandHandler("start", start))],
        states={
            CHOOSING: [MessageHandler(filters.Regex("^(Nutritional information)$"),
                                      handle_nutritional_information_request)],
            TYPING_REPLY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    respond_to_nutritional_information_request,
                )
            ],

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
