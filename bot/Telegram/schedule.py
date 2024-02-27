from environs import Env

import schedule
import telebot
import time

from bot.Telegram.auto_bot import AnswerBot


env = Env()
env.read_env()

bot = telebot.TeleBot(env.str('Token_bot'))


def job_with_argument(name):

    return AnswerBot(name)

schedule.every(1).seconds.do(job_with_argument, name=4)

while True:
    schedule.run_pending()
    time.sleep(1)


