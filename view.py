# юда все функции отправляющие сообщения


from aiogram import types

from bot import bot


def get_button():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton(text='Правила игры')
    btn2=types.KeyboardButton(text='Поиграем в конфетки')
    kb.add(btn1,btn2)

def view_rules_game():
    message_rules='Игра с конфетами\nПравила: На столе лежит 150 конфет.\n'\
        'Играют два игрока: бот и вы, делая ход друг после друга.\n'\
        'Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.\n\n'\
        'Все конфеты оппонента достаются сделавшему последний ход.\n'\
            
    return message_rules
            

def game():
    message="привет. Предлагаю поиграть в игру 'Конфетки'"
    return message
def lets_go():
    message='сыграем в "Конфетки"\n''Первый ход определяем жеребьевкой.\n'
    return message

def print_sweet_on_table(sweetsOnTable):
    message=(f'На столе {sweetsOnTable} конфет(ы)')
    return message

def error_input():
    message='За один ход можно забрать не более чем 28 конфет или не больше, чем осталось на столе \nПопробуй еще раз'
    return message
def game_false():
    message="Конфеток не осталось. Игра окончена!!!\nЗапустите игру заново"
    return message

