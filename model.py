# юда все функции отправляющие сообщения


from aiogram import types

from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки')