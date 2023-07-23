from Model.logger import Logger

import Model
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
import controller

# Credentials
load_dotenv("Model/credentials.env")
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

# Enable logging
logging = Logger("__name__")
logging.create_handler()

# Instantiating the variables used for the different states of the conversation
CHOOSING, TYPING_REPLY_NUTRITIONAL_INFORMATION, TYPING_REPLY_RECIPE = range(3)


class Bot:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        self.controller = controller.Controller()
        self.reply_keyboard = [["Nutritional information", "Recipes"]]
        self.markup = ReplyKeyboardMarkup(self.reply_keyboard, one_time_keyboard=True)
        if self.__initialized:
            return
        self.__initialized = True

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.controller.handle_start_command(update),
                                        reply_markup=self.markup), \
            logging.log_user_message(update)
        return CHOOSING

    async def handle_nutritional_information_request(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logging.log_user_message(update)
        await update.message.reply_text(self.controller.handle_request_nutritional_information_command()),
        return TYPING_REPLY_NUTRITIONAL_INFORMATION

    async def respond_to_nutritional_information_request(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logging.log_user_message(update)
        await update.message.reply_text(self.controller.handle_user_input_nutritional_information(update),
                                        reply_markup=self.markup),
        return CHOOSING

    async def handle_recipe_request(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logging.log_user_message(update)
        await update.message.reply_text(self.controller.handle_request_recipe_command()),
        return TYPING_REPLY_RECIPE

    async def respond_to_recipe_request(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logging.log_user_message(update)
        await update.message.reply_text(self.controller.handle_recipe_request(update),
                                        reply_markup=self.markup)
        return CHOOSING

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        logging.log_user_message(update)
        await update.message.reply_text(
            self.controller.handle_cancel_message(), reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END

    # Error handler
    async def error(self, update, context):
        logging.logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    bot = Bot()
    logging.logger.info("Starting bot")
    app = Application.builder().token(TELEGRAM_API_KEY).build()
    nutritional_information_conversation_handler = ConversationHandler(
        entry_points=[(CommandHandler("start", bot.start))],
        states={
            CHOOSING: [MessageHandler(filters.Regex("^(Nutritional information)$"),
                                      bot.handle_nutritional_information_request),
                       MessageHandler(filters.Regex("^(Recipes)$"),
                                      bot.handle_recipe_request)],

            TYPING_REPLY_NUTRITIONAL_INFORMATION: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    bot.respond_to_nutritional_information_request,
                )

            ],
            TYPING_REPLY_RECIPE: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    bot.respond_to_recipe_request,
                )

            ],

        },
        fallbacks=[CommandHandler("cancel", bot.cancel)]

    )

    logging.logger.info("Bot started. Press Ctrl+C to stop.")
    app.add_handler(nutritional_information_conversation_handler)
    app.add_error_handler(bot.error)
    logging.logger.info("Polling bot")
    app.run_polling(poll_interval=3)



