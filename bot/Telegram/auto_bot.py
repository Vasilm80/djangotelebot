import telebot
from environs import Env

import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotelebot.settings')
django.setup()
from bot.models import User, Message, Answers

env = Env()
env.read_env()

bot = telebot.TeleBot(env.str('Token_bot'))

def AnswerBot(id):
    ans = Answers.objects.get(id = id)
    bot.send_message(ans.Message_id.Chat_id, f'Вы справшивали <i>{ans.Message_id.Message_text}</i>\n Ответ - <b>{ans.Answer_text}</b>', parse_mode='html')
@bot.message_handler(commands=['help', 'start'])
def start_send(message):
    bot.send_message(message.chat.id,'Привет. Я бот, который все повторяет')
    us = User()
    us_all = User.objects.filter(User_id=message.chat.id)
    if not us_all:
        us.User_id = message.chat.id
        us.name = message.from_user.full_name
        us.save()
@bot.message_handler(commands=['send_all'])
def send_all(message):
    if message.from_user.id == 	6098608035:
        users = User.objects.all()
        for user in users:
            bot.send_message(user.User_id, f'С добрым утром, <b>{user.name}</b>', parse_mode='html')
    else: bot.send_message(message.from_user.id, f'К сожалению у вас нет прав доступа к данной команде, <b>{message.from_user.full_name}</b>', parse_mode='html')

@bot.message_handler(func=lambda message: True)
def echo(message):
    # print(message.id)
    # print(message.text)
    # print(message.from_user)
    # print(message.chat.id)
    # print(message.from_user.id)
    # print(message.from_user.first_name)
    # print(message.date)
    # print(message.chat)
    us = User.objects.get(User_id=message.chat.id)
    mes = Message()
    mes.Message_all = message
    mes.Chat_id = message.chat.id
    mes.Message_id = message.id
    mes.Message_text = message.text
    mes.User_id = us
    mes.save()
    bot.send_message(message.chat.id, f'Пользователь <b>{message.from_user.first_name}</b> написал: \n "<i>{message.text}</i>"', parse_mode="html")

# AnswerBot(4)
bot.infinity_polling()