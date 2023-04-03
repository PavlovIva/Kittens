# Импортируем все необходимое
from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN, users, admin
from aiogram.filters import Command, Text, or_f
from Data.lexica import START, HELP
from funcs import get_a_cat


# Объявляем необходимые переменные
bot = Bot(TOKEN)
dp = Dispatcher()
n = 0

@dp.message(Command(commands=['start']))  # Реагирует на комманду старт
async def echo(message: types.Message):
    await message.reply(START)
    if message.from_user.id not in users: #and message.from_user.id != admin:
        users[f'id{int(n)}'] = [message.from_user.id]
        print(users)



@dp.message(Command(commands=['help']))  # Реагирует на комманду помощь
async def help_func(message: types.Message):
    await message.reply(HELP)


# Прототип. Работает и отправляет фото!!! Через API
@dp.message(or_f(Command(commands=['photo']), Text(startswith=['Хочу котика', 'Давай кота'], ignore_case=True)))
async def kittens(message):
    get_a_cat()


if __name__ == '__main__':
    dp.run_polling(bot)
