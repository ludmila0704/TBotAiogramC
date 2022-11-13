# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start','help'])
    dp.register_message_handler(commands.game)
    
