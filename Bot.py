from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.BOT_TOKEN) # Удобно
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка курса', 'Покупка куроса itProgger', 'invoice', config.PAYMENT_TOKEN, 'USD', [types.LabeledPrice('Покупка курса', 5 * 100)]) 
    # Там в конце типо 5 монет умножить на 100 = 5 долларов. 2 - название товара. 3 - описание товара, 4 - тип товара, 5 - ключ для подключения, 6 - валюта.
    # 7 - список, составляющий из себя название товара, и его цену. А так эта функция принимает очень много параметров, а мы передали только обязательные
    # Как же трахаться порой приходиться из-за Гошиных видео...

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT) # Этот прикол будет работать при успешной оплате
async def succesful_payment(message: types.Message):
    await message.answer(f'success: {message.successful_payment.order_info}') # Капец прикол, оч много инфы есть после оплаты.

executor.start_polling(dp)