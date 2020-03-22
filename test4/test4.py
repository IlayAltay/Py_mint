
# -*- coding: utf-8 -*-
import telebot

#bot = telebot.TeleBot('1023899509:AAEX4KXDYer8DW8ZGxOxFQ4fStWwgTJrAeA')


bot = telebot.TeleBot('1023899509:AAHSDEZaop4490O84oFiOuvMHdprM8uVs-g')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ты написал _  /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    slovar={
        u'привет':'дароф',
        u'хай':'йоу',
        u'день добрый':'Здравствуйте',
        u'здравствуйте':'Приветствую',
        u'хелоу': 'Борев брат',
        u'рахмет': 'Хай',
        u'хой': 'Доброго',
        u'abc': 'yyyaaa',
        u'хай пипл': 'Салам Дорогой'
    }
    key =message.text.lower()
    if key in slovar:
        bot.send_message(message.chat.id,slovar[key] )
    else:
        bot.send_message(message.chat.id, 'Сие выражение мне не ведомо сир!')
        bot.send_message(message.chat.id, '... но я быстро учусь...')
    if message.text.lower() == u'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == u'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()