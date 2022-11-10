# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view
from bot import bot


async def start(message: types.Message):
    await view.greetings(message)

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')

async def getNumber(message: types.Message):
    number = message.text
    if 0 < int(number) < 29:
        print(number)
    else:
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')