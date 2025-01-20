import asyncio
from loader import dp, bot, db
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.message(CommandStart())
async def start_cmd(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text='Получить данные по товару', callback_data='get_data')
    await message.answer('Хотите получить данные по товару?', reply_markup=kb.as_markup())


@dp.callback_query(F.data == 'get_data')
async def get_data(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Введите артикул товара *(число)*', parse_mode='Markdown')


@dp.message(F.text)
async def text_message(message: Message):
    if not (message.text).isdigit():
        return await message.answer('Принимаются только числа')\
    
    product_info = await db.select_product_info(int(message.text))
    if not product_info:
        return await message.answer('По этому товару нет информации') 
    #В тз, написано, что данные берутся из БД, так что даю такой ответ. Можно было бы напрямую у ВБ брать, в случае, если в бд нет инфы

    return await message.answer(
f'''
Артикул: *{message.text}*
Название товара: *{product_info.name}*
Цена: *{product_info.price}*
Рейтинг: *{product_info.rating}*
Количество товара: *{product_info.total_quantity}*
''', parse_mode='Markdown')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())