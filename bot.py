from aiogram import Bot, Dispatcher, types
from Data.config import TOKEN
from aiogram.filters import Command
from Data.lexica import START

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def echo(message: types.Message):
    await message.reply(START)



if __name__ == '__main__':
    dp.run_polling(bot)