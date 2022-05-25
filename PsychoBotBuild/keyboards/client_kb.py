from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Инстаграм')
b2 = KeyboardButton('/Вконтакте')
b3 = KeyboardButton('/Телеграм')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b2).add(b3).insert(b1)