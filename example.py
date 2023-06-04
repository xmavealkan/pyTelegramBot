import telebot
from telebot import types

bot = telebot.TeleBot("6129194736:AAFrw3Mh6t0YMtWoxSf_LYrHdGWI2V_WD5M")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Вот команды:',
                     reply_markup=get_commands_keyboard())


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Команда 1":
        # Действия, связанные с выполнением команды 1
        bot.send_message(message.chat.id, 'Вы выполнили Команду 1')
    elif message.text == "Команда 2":
        # Действия, связанные с выполнением команды 2
        bot.send_message(message.chat.id, 'Вы выполнили Команду 2')
    else:
        pass


def get_commands_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(types.KeyboardButton("Команда 1"),
                 types.KeyboardButton("Команда 2"))
    return keyboard


bot.polling()
