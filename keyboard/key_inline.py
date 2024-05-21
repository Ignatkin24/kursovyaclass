from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://kalashnikovgroup.ru/')
    but_inline2 = InlineKeyboardButton('Посмотреть2', url='https://kalashnikovgroup.ru/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline

