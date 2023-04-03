# Импортируем все необходимое
from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN
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


@dp.message(Command(commands=['help']))  # Реагирует на комманду помощь
async def help_func(message: types.Message):
    await message.reply(HELP)


# Прототип. Работает и отправляет фото!!! Через API
@dp.message(or_f(Command(commands=['photo']), Text(startswith=['Хочу котика', 'Давай кота'], ignore_case=True)))
async def kittens(message: types.Message):
    get_a_cat(message_from_user_id=message.from_user.id)



if __name__ == '__main__':
    dp.run_polling(bot)
