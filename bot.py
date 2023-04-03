from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN, url_for_kittens, data, admin
from aiogram.filters import Command, Text, or_f
from Data.lexica import START, HELP
import requests
import random

bot = Bot(TOKEN)
dp = Dispatcher()

def get_a_cat():
    response = requests.get('https://api.telegram.org/bot5873257022:AAHCkfdP4bJAV3oQhB9FRNqnbZoiRtpUdKc/sendPhoto?chat_id=867978028&photo=https://cataas.com/cat')
    response.raise_for_status()
    #return response.json()['file']


def get_a_cat1():
    url = 'https://cataas.com/cat?json=true'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['file']



@dp.message(Command(commands=['start']))  # Реагирует на комманду старт
async def echo(message: types.Message):
    await message.reply(START)


@dp.message(Command(commands=['help']))  # Реагирует на комманду помощь
async def help_func(message: types.Message):
    await message.reply(HELP)


@dp.message(or_f(Command(commands=['photo']), Text(startswith=['Хочу котика', 'Давай кота'], ignore_case=True)))
async def kittens(message: types.Message):
    get_a_cat()








if __name__ == '__main__':
    dp.run_polling(bot)