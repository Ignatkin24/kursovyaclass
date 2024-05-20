from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from  keyboard.keyboards import get_keyboard_1,get_keyboard_2

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Запуск бота'),
        types.BotCommand(command='/help', description='Помощь бота')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Привет. я твой первый ЭХО бот',reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text =='Отправь фото АК')
async  def button_1_click(message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://upload.wikimedia.org/wikipedia/commons/f/fa/Ak74l.jpg?20130919161751',caption='Результат')

@dp.message_handler(lambda message: message.text =='Перейти на следующую клавиатуру')
async  def button_2_click(message:types.Message):
    await message.answer('Перейти на следующую клавиатуру', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text =='Перейти на предыдущую клавиатуру')
async  def button_2_click(message:types.Message):
    await message.answer('Перейти на предыдущую клавиатуру', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text =='Отправь фото M4')
async  def button_3_click(message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://upload.wikimedia.org/wikipedia/commons/d/dc/M4A1_ACOG.png',caption='Результат')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с девушками')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ =='__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)