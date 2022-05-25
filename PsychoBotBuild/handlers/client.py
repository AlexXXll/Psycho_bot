from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import kb_client

#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Psychoengineers_Psychobot')
#@dp.message_handler(commands=['Инстаграм'])
async def commands_inst(message : types.Message):
    await bot.send_message(message.from_user.id, 'https://instagram.com/olga.zolotareva.gh?igshid=YmMyMTA2M2Y=')

#@dp.message_handler(commands=['Вконтакте'])
async def commands_vk(message : types.Message):
    await bot.send_message(message.from_user.id, 'https://vk.com/club121185049')

#@dp.message_handler(commands=['Телеграм'])
async def commands_tg(message : types.Message):
    await bot.send_message(message.from_user.id, 'https://t.me/psychotechnics_ot_psychoengineer')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_inst, commands=['Инстаграмм'])
    dp.register_message_handler(commands_vk, commands=['Вконтакте'])
    dp.register_message_handler(commands_tg, commands=['Телеграм'])