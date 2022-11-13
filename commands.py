# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view,controller
from bot import bot
import model
from random import randint as rI


async def start(message: types.Message):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1=types.KeyboardButton(text= model.rules)
    btn2=types.KeyboardButton(text=model.game)
    kb.add(btn1,btn2) 
    model.player1_name = message.from_user.first_name
    await bot.send_message(message.chat.id,f'{message.from_user.first_name}, {view.game()}',reply_markup=kb)
   
    
async def game(message: types.Message):
    if message.text=='Правила игры':
        message.text=view.view_rules_game()
   
        await bot.send_message(message.chat.id,f'{message.text}')
    if message.text=='Поиграем в конфетки':

        await bot.send_message(message.chat.id,f'{message.from_user.first_name}, {view.lets_go()}')
        whosStep=controller.random_step()
        if whosStep==0:
            await bot.send_message(message.chat.id,f'{message.from_user.first_name}, {model.ans_first}')
            await bot.send_message(message.chat.id,model.ans_your_step)
            
            
        else:
            await bot.send_message(message.chat.id,f'{model.ans_bot_first} {model.player2_name}')
            step=controller.bot_step(1)
            await bot.send_message(message.chat.id,f'{step} {model.ans_bot_step}. {model.ans_sweet_on_table} {model.sweetsOnTable}.')
            await bot.send_message(message.chat.id,model.ans_your_step)

    if message.text.isdigit():
        step=int(message.text)
        if model.sweetsOnTable>0:
            
            if  controller.is_valid_sweet(step):#model.sweetsOnTable>0:
                controller.play_user(step)
                await bot.send_message(message.chat.id,f'{model.ans_step} {step}. {model.ans_sweet_on_table} {model.sweetsOnTable}.')
                
                if model.sweetsOnTable>0:
                        step=controller.bot_step(2)
                        if model.sweetsOnTable>0:
                            await bot.send_message(message.chat.id,f'{step} {model.ans_bot_step}. {model.ans_sweet_on_table} {model.sweetsOnTable}. {model.ans_your_step} {message.from_user.first_name}? ')
                        else:
                            model.sweetsOnTable=0
                            await bot.send_message(message.chat.id,f'{model.ans_bot_win} {model.player2_name}')
                else:
                    await bot.send_message(message.chat.id,f'{message.from_user.first_name}{model.ans_win_player}')
            else:
                message_error=view.error_input()
                await bot.send_message(message.chat.id,message_error)
               
        else:
           await bot.send_message(message.chat.id,view.game_false())
           
