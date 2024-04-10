# Лабораторная работа №2 - Назаров

import telebot
from bucks import dollar

bot = telebot.TeleBot('6317281027:AAEkPON7DcUXbC4-hRT1Q94Y_1wa5PX9bEc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'{message.from_user.first_name}, здравствуйте!\nДавайте я помогу вам узнать курс доллара\nНапишите команду /dollar'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['dollar'])
def start(message):
    bot.send_message(message.chat.id, f'1$ = {dollar()}₽', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    bot.send_message(message.chat.id, 'Узнайте актуальный курс доллара\nПиши /dollar', parse_mode='html')


bot.polling(none_stop=True, interval=0)

