# Импортируем все необходимое
from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN, message_ids, admin, users
from aiogram.filters import Command, Text, or_f, and_f
from Data.lexica import START, HELP
from funcs import GetCat


# Объявляем необходимые переменные
bot = Bot(TOKEN)
dp = Dispatcher()
get_a_catt = GetCat()


@dp.message(Command(commands=['start']))  # Реагирует на комманду старт
async def start_react(message: types.Message):
    await message.reply(START)
    if message.from_user.id != admin and message.from_user.id not in users:
        users.append(message.from_user.id)


@dp.message(Command(commands=['help']))  # Реагирует на комманду помощь
async def help_func(message: types.Message):
    await message.reply(HELP)


# Прототип. Работает и отправляет фото!!! Через API
@dp.message(or_f(Command(commands=['photo']), Text(startswith=['Хочу котика', 'Давай кота'], ignore_case=True)))
async def kittens(message: types.Message):
    get_a_catt.get_a_cat(message_from_user_id=message.from_user.id)


# По плану, должно добавлять фото в избранные.
@dp.message(Command(commands='like'))
async def like(message: types.Message):
    idd = get_a_catt.photo_id()
    message_ids[message.from_user.id] = {}
    message_ids[message.from_user.id][1] = idd
    await message.reply('Фото добавлено!')
    print(message_ids[message.from_user.id])


# Отправляет понравившиеся фото
@dp.message(Command(commands='watchlike'))
async def watch_like(message: types.Message):
    await bot.forward_message(message.from_user.id, message.from_user.id, message_ids[message.from_user.id][1])


'''# По идее, должно выключать бот
@dp.message(and_f(lambda msg: msg.from_user.id == admin), Command(commands='stop'))
async def stop_work(message: types.Message):
    pass
'''

# Показывает кол-во пользователей админу.
@dp.message(and_f(lambda msg: msg.from_user.id == admin), Command(commands='stat'))
async def get_stat(message: types.Message):
    await message.reply(str(len(users)))


if __name__ == '__main__':
    dp.run_polling(bot)
