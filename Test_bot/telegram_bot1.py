
# -*- coding: utf-8 -*-
import telebot
import datetime
from time import sleep
#bot = telebot.TeleBot('1023899509:AAEX4KXDYer8DW8ZGxOxFQ4fStWwgTJrAeA')


bot = telebot.TeleBot('1023899509:AAHSDEZaop4490O84oFiOuvMHdprM8uVs-g')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ты написал _  /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    slovar_privet={
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
    slovar_poka={
        u'пока':'счастливо',
        u'покед':'Будь!',
        u'досвидания':'Адиос!',
        u'бай':'Бай бай',
        u'прощай':'Досвиданиья',
        u'счастливо':'Пока',
        u'адиос':'пока пока'
    }
    slovar_stopprogram={
        u'стоп':'Выключаюсь',
        u'stop':'отключение',
        u'выключись':'остановка_питания',
        u'power_off':'отключен'        
    }
    key =message.text.lower()
    if key in slovar_privet:
        bot.send_message(message.chat.id,slovar_privet[key] )
    else:
        if key in slovar_poka:
            bot.send_message(message.chat.id,slovar_poka[key])    
        else:
            if key in slovar_stopprogram:
                bot.send_message(message.chat.id,slovar_stopprogramm[key])
                sleep(5)
                exit(0)
            else:    
                bot.send_message(message.chat.id, 'Сие выражение мне не ведомо сир!')
                bot.send_message(message.chat.id, '... но я быстро учусь...')
    


bot.polling()
