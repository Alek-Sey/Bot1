import telebot
import config
import random
from telebot import types
import  os


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Здравствуй, <b>{0.first_name}</b>, здравствуй,\n друг прекрасный".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton ("Случайное число")
item2 = types.KeyboardButton ("Как дела?")
item3 = types.KeyboardButton ("Выключить ПК")
markup.add(item1, item2, item3)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Случайное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id, 'Пока не родила ))')
        elif message.text == 'Выключить ПК':
            bot.send_message(message.chat.id, 'Выключаю ПК ))')
            os.system('shutdown /a')
            os.system('shutdown /s /f /t 600')
        else:
            bot.send_message(message.chat.id, 'Хз')

#@bot.message_handler(content_types=['text'])
#def lalala(message):
#    bot.send_message(message.chat.id, message.text)

# run
bot.polling(none_stop=True)