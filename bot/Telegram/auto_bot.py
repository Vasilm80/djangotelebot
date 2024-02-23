import telebot
from environs import Env

env = Env()
env.read_env()

bot = telebot.TeleBot(env.str('Token_bot'))

@bot.message_handler(commands=['help', 'start'])
def start_send(message):
    bot.send_message(message.chat.id,'Привет. Я бот, который все повторяет')


@bot.message_handler(func=lambda message: True)
def echo(message):
    print(message.id)
    print(message.text)
    print(message.from_user)
    print(message.from_user.first_name)
    print(message.date)
    print(message.chat)
    bot.send_message(message.chat.id, f'Пользователь <b>{message.from_user.first_name}</b> написал: \n "<i>{message.text}</i>"', parse_mode="html")

bot.infinity_polling()