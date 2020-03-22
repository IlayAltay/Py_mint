import telebot

#bot = telebot.TeleBot('1023899509:AAEX4KXDYer8DW8ZGxOxFQ4fStWwgTJrAeA')


bot = telebot.TeleBot('1023899509:AAHSDEZaop4490O84oFiOuvMHdprM8uVs-g')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'You write mi _  /start')

bot.polling()
