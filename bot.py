import config
import telebot
from telebot import types
import os

client = telebot.TeleBot(config.TOKEN)

@client.message_handler(content_types=['text'])

def welcome(message):
    msg = client.send_message(message.chat.id, 'Введите пароль доступа')
    client.register_next_step_handler(msg, password)

def password(message):
        if message.text == '123':
            rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rmk.add(types.KeyboardButton('Игровое открыть'), types.KeyboardButton('Полный интернет'), types.KeyboardButton('Выключить позже'), types.KeyboardButton('Игровое закрыть'), types.KeyboardButton('Ограничить интернет'), types.KeyboardButton('Выключить сейчас'))
            msg = client.send_message(message.chat.id, 'Переход к управлению', reply_markup=rmk)
            client.register_next_step_handler(msg, user_answer)

        else:
            msg = client.send_message(message.chat.id, 'Неверно. Введите правильный пароль')
            client.register_next_step_handler(msg, password)

def user_answer(message):
    if message.text == 'Игровое открыть':
        msg = client.send_message(message.chat.id, 'Игровое пространство Открыто')
        client.register_next_step_handler(msg, user_answer)
        os.system('net user Матвей ""')
    elif message.text == 'Игровое закрыть':
        msg = client.send_message(message.chat.id, 'Игровое пространство Закрыто')
        client.register_next_step_handler(msg, user_answer)
        os.system('net user Матвей 17031948')
        #os.system('shutdown /r /f /t 600')
    elif message.text == 'Выключить сейчас':
        msg = client.send_message(message.chat.id, 'Компьютер будет выключен через 1 минуту')
        client.register_next_step_handler(msg, user_answer)
        os.system('shutdown /a')
        #os.system('shutdown /s /f /t 600')
    elif message.text == 'Ограничить интернет':
        msg = client.send_message(message.chat.id, 'Сейчас разрешены только сайты для учёбы')
        client.register_next_step_handler(msg, user_answer)
        os.system(r'runas /savecred /user:scool "C:\Users\proxyon.bat"')
    elif message.text == 'Полный интернет':
        msg = client.send_message(message.chat.id, 'Сейчас разрешены все сайты')
        client.register_next_step_handler(msg, user_answer)
        os.system(r'runas /savecred /user:scool "C:\Users\proxyoff.bat"')

    else:
        msg=client.send_message(message.chat.id, 'Функция в разработке')
        client.register_next_step_handler(msg, user_answer)

def user_reg(message):
    msg=client.send_message(message.chat.id, f'Команда {message.text} выполнена. Что-нибудь ещё?')
    client.register_next_step_handler(msg, user_reg)

client.polling(none_stop=True)