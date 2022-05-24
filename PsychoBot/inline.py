from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Вконтакте', url='https://vk.com/club121185049')
urlButton2 = InlineKeyboardButton(text='Телеграм', url='https://t.me/psychotechnics_ot_psychoengineer')
urlButton3 = InlineKeyboardButton(text='Инстаграм', url='https://instagram.com/olga.zolotareva.gh?igshid=YmMyMTA2M2Y=')
urlkb.add(urlButton, urlButton2, urlButton3)

@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Наши ссылочки:', reply_markup=urlkb)

executor.start_polling(dp, skip_updates=True)