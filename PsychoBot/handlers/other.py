from aiogram import types, Dispatcher
from create_bot import dp
from data_base import sqlite_db

#@dp.message_handler(content_types=['text'])
async def document_bonus(message : types.Message):
    if message.text == 'бонус':
        await sqlite_db.sql_read(message)

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(document_bonus, content_types=['text'])