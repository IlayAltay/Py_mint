import telebot

bot = telebot.TeleBot('1023899509:AAEX4KXDYer8DW8ZGxOxFQ4fStWwgTJrAeA')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'aaaaaaaaaa /start')

bot.polling()