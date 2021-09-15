import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def first (message):
    bot.send_message(message.chat.id,'Введите пароль', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def password (message):
#    if message.chat.type == 'private':
        if message.text == '123':
            bot.send_message(message.chat.id, 'Верно. Выберите пункт меню', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Пароль неверный, введите пароль')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton ('Случайное число')
item2 = types.KeyboardButton ('Как дела?')

markup.add(item1, item2)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Случайное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Прекрасно', callback_data='good')
            item2 = types.InlineKeyboardButton('Так себе', callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Не знаю, что ответить')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отлично!')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как дела?', reply_markup=None)
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Пичалька (')
    # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как дела?', reply_markup=None)




  #          @bot.message_handler(commands = ['start'])
   #         def welcome(message):
    #        sti = open('static/welcome.webp', 'rb')
     #       bot.send_sticker(message.chat.id, sti)
     #       bot.send_message(message.chat.id, 'Здравствуй, <b>{0.first_name}</b>, здравствуй,\n друг прекрасный'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

#keyboard



                
    except Exception as e:
            print(repr(e))

# run
bot.polling(none_stop=True)
