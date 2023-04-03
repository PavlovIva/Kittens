# Импортируем все необходимое
from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN, users
from aiogram.filters import Command, Text, or_f
from Data.lexica import START, HELP, PHOTO
import random
import requests


# Объявляем необходимые переменные
bot = Bot(TOKEN)
dp = Dispatcher()
n = 0


@dp.message(Command(commands=['start']))  # Реагирует на комманду старт
async def echo(message: types.Message):
    await message.reply(START)
    if message.from_user.id not in users:
        users[f'id{int(n)}'] = [message.from_user.id]
        print(users)


@dp.message(Command(commands=['help']))  # Реагирует на комманду помощь
async def help_func(message: types.Message):
    await message.reply(HELP)


# Прототип. Работает и отправляет фото!!! Через API
@dp.message(or_f(Command(commands=['photo']), Text(startswith=['Хочу котика', 'Давай кота'], ignore_case=True)))
async def kittens(message: types.Message):
    caption = PHOTO[random.randint(0, (len(PHOTO) - 1))]
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={message.from_user.id}&caption={caption}&photo=http://random.cat/view/{str(random.randint(0, 1677))}')
    response.raise_for_status()


if __name__ == '__main__':
    dp.run_polling(bot)
