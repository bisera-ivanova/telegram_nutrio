import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv('Model/credentials.env')

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hello, {update.message.chat.username}! My name is NutrioBot and my role is to provide you with "
        f"nutritional information, give you healthy recipes and keep track of "
        f"food-related reminders!")


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hey there! Anything I can help with?"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    print(f"User {update.message.chat.id}")

    if message_type == "group":
        return "The nutrio bot is not yet available for group chats"
    response = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == '__main__':
    print("Starting bot")
    app = Application.builder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("start", start_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling bot")
    app.run_polling(poll_interval=3)
