import telebot

bot = telebot.TeleBot("6129194736:AAFrw3Mh6t0YMtWoxSf_LYrHdGWI2V_WD5M")


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.chat.id
    username = message.from_user.username
    print(f"Новый пользователь: {username} (ID: {user_id})")
    bot.send_message(user_id, 'Привет! Добро пожаловать!')


@bot.message_handler(commands=['exit'])
def exit_message(message):
    user_id = message.chat.id
    username = message.from_user.username
    print(f"Пользователь вышел: {username} (ID: {user_id})")
    bot.send_message(user_id, 'До свидания!')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    username = message.from_user.username
    text = message.text
    print(
        f"Пользователь {username} (ID: {user_id}) отправил сообщение: {text}")


bot.polling()
