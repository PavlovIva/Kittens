# Импортируем все необходимое
from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN, message_ids
from aiogram.filters import Command, Text, or_f
from Data.lexica import START, HELP
from funcs import GetCat


# Объявляем необходимые переменные
bot = Bot(TOKEN)
dp = Dispatcher()



@dp.message(Command(commands=['start']))  # Реагирует на комманду старт
async def echo(message: types.Message):
    await message.reply(START)


@dp.message(Command(commands=['help']))  # Реагирует на комманду помощь
async def help_func(message: types.Message):
    await message.reply(HELP)


# Прототип. Работает и отправляет фото!!! Через API
@dp.message(or_f(Command(commands=['photo']), Text(startswith=['Хочу котика', 'Давай кота'], ignore_case=True)))
async def kittens(message: types.Message):
    get_a_catt = GetCat()
    get_a_catt.get_a_cat(message_from_user_id=message.from_user.id)
    idd = get_a_catt.photo_id()
    message_ids.append(idd)


# По плану, должно добавлять фото в избранные.
@dp.message(Command(commands='like'))
async def like(message: types.message.Message):
    pass


# Отправляет понравившиеся фото
@dp.message(Command(commands='watchlike'))
async def watchlike(message: types.Message):
    await bot.forward_message(message.from_user.id, message.from_user.id, message_ids[0])


if __name__ == '__main__':
    dp.run_polling(bot)
