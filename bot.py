#Здесь создается бот и хранится его токен

from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(token='-----')
dp = Dispatcher(bot)