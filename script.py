import telepot
from telepot.loop import MessageLoop

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6526952850:AAH4HpT8gzbxQXGrb4Jl14rRO33FvHQ-6vs'

# Dictionary to store user data
user_data = {}

def handle_start(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "Hello! What's your first name?")
    user_data[chat_id] = {'state': 'first_name'}

def handle_message(msg):
    chat_id = msg['chat']['id']
    user_id = msg['from']['id']

    if user_id in user_data:
        state = user_data[user_id]['state']

        if state == 'first_name':
            user_data[user_id]['first_name'] = msg['text']
            bot.sendMessage(chat_id, "Great! What's your last name?")
            user_data[user_id]['state'] = 'last_name'

        elif state == 'last_name':
            user_data[user_id]['last_name'] = msg['text']
            full_name = f"{user_data[user_id]['first_name']} {user_data[user_id]['last_name']}"
            bot.sendMessage(chat_id, f"Your full name is: {full_name}")
            del user_data[user_id]

bot = telepot.Bot(BOT_TOKEN)
MessageLoop(bot, {'chat': handle_start, 'text': handle_message}).run_as_thread()

while True:
    pass
