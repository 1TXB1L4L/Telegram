import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Telegram Bot API token
TOKEN = "6526952850:AAH4HpT8gzbxQXGrb4Jl14rRO33FvHQ-6vs"

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_html(f"Hello, {user.mention_html()}!")

# Define a function to handle incoming messages
def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == "/start":
        start(update, context)  # Handle the /start command
    elif text.lower() == "how are you?":
        update.message.reply_text("I'm fine.")
    elif text.lower() == "exit":
        update.message.reply_text("Goodbye!")
        updater.stop()  # Gracefully stop the bot
    else:
        update.message.reply_text("Script is outdated")

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler to respond to incoming messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C to exit
    updater.idle()

if __name__ == "__main__":
    main()
