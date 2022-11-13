# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view
from bot import bot
import model
from random import randint as rI



def random_step():
    model.sweetsOnTable = 150
    if rI(1, 3) == 1:
        whosStep = 0

    else:

        whosStep = 1

    return whosStep

def bot_step(hod):
    if hod == 1:  # bot

        step = int(model.sweetsOnTable % 29)
        model.sweetsOnTable -= step
    if hod > 1:  # bot

        if model.sweetsOnTable > 100:
            step = rI(1, 29)
        elif model.sweetsOnTable > 90:
            step = int(model.sweetsOnTable % 29)
        elif model.sweetsOnTable > 28:

            step = 29-model.sweetPlayer
        else:
            step = model.sweetsOnTable
        model.sweetsOnTable -= step

    return step

def is_valid_sweet(step):

    if 0 < step <= model.maxCountSweet and step <= model.sweetsOnTable:
        return True

def play_user(step):

    model.sweetPlayer = step
    model.sweetsOnTable -= step

