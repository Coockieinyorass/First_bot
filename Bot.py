from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo # Чтобы делать веб-приложения

bot = Bot("6093324846:AAFQWK-P-xkDmUOO8I-SysC14JFRqSfCeuE")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup() # Бтв прикол, данные пользователя будут подставляться, только при кнопке под сообщением. Через кнопку в клавиатуре не будут
    markup.add(types.InlineKeyboardButton("Открыть веб страницу", web_app=WebAppInfo(url="https://coockieinyorass.github.io/First_bot/"))) # Тут мы указали, что при нажатии на кнопку
    # будет открываться веб-приложение + url для него. Url надо указывать в качетве аргумента!

    await message.answer("Ку, жми на кнопку!", reply_markup=markup)
    # В результате открытия веб-приложения появился полноценные мини-браузер.
    # Ё-маё... Гоша предложил создать своё веб-приложение при помощи html-файла... Походу я знаю, что буду учить дальше... (Вот это нативность конечно получилась)

executor.start_polling(dp)