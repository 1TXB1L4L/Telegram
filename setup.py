from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Conversation states
START, HOW_ARE_YOU = range(2)

# Define a dictionary to store user data (in this case, we don't need it)
user_data = {}

def start(update: Update, context: CallbackContext) -> int:
    user_data.clear()  # Clear any previous user data
    update.message.reply_text("Hello! How are you?")
    return HOW_ARE_YOU

def how_are_you(update: Update, context: CallbackContext) -> int:
    user_response = update.message.text.lower()
    
    if 'fine' in user_response or 'great' in user_response:
        update.message.reply_text("I'm glad to hear that!")
    else:
        update.message.reply_text("I'm just a bot, but I'm here to help!")

    return ConversationHandler.END

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            HOW_ARE_YOU: [MessageHandler(Filters.text & ~Filters.command, how_are_you)],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
