from os import read
from re import T
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMAdmin(StatesGroup):
    document = State()
    name = State()

#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


#@dp.message_handler(commands='Добавить_бонус', state=None)
async def bonus_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.document.set()
        await message.reply('Загрузите файл')

#@dp.message_handler(state="*", commands='отмена')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

#@dp.message_handler(content_types=['document'], state=FSMAdmin.document)
async def load_document(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['document'] = message.document.file_id
        await FSMAdmin.next()
        await message.reply('Теперь небольшой коментарий')

#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text

        await sqlite_db.sql_add_command(state)
        await state.finish()

#@dp.callback_query_handler(lambda x: x.data and x.data.startswitch('del '))
#async def del_callback_run(callback_query: types.CallbackQuery):
#    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
#    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)

#@dp.message_handler(commands='Удалить')
#async def delete_item(message: types.Message):
#    if message.from_user.id == ID:
#        read = await sqlite_db.sql_read2()
#        for ret in read:
#            await bot.send_document(message.from_user.id, ret[0], f'/n{ret[1]}')
#            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
#                add(InlineKeyboardButton(f'Удалить {ret[1]}')))


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(bonus_start, commands='Бонус', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_document, content_types=['document'], state=FSMAdmin.document)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
#    dp.register_message_handler(del_callback_run, lambda x: x.data and x.data.startswitch('del '))
#    dp.register_message_handler(delete_item, commands='Удалить')