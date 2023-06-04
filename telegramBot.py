import random
import telebot
from telebot import types

bot = telebot.TeleBot("6129194736:AAFrw3Mh6t0YMtWoxSf_LYrHdGWI2V_WD5M")

moves = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    user = f"Hello {message.from_user.first_name} "
    bot.send_message(message.chat.id, user, parse_mode="html")
    start_markups = types.ReplyKeyboardMarkup()
    start_game_markup = types.KeyboardButton("/startgame")
    help_markup = types.KeyboardButton('/help')
    start_markups.add(start_game_markup, help_markup)
    bot.send_message(message.chat.id, f'Allll commands',
                     reply_markup=start_markups)


@bot.message_handler(commands=['help'])
def help_func(message):
    url_button = types.InlineKeyboardMarkup()
    url_button.add(types.InlineKeyboardButton("Жми сюда пупсик",
                   url='https://t.me/relaxrum'))
    bot.send_message(
        message.chat.id, f"Этим каналом автор дорожит если хочешь подпишись)", reply_markup=url_button)


# @bot.message_handler(commands=['exit'])
# def exit(message):
#     bot.send_message(message.chat.id, f'Goodbye! I hope you enjoyed the game.')
#     bot.stop_polling()


# @bot.message_handler(commands=['start'])
# def start_command(message):
#     start_message(message)


@bot.message_handler(commands=['startgame'])
def help_func(message):
    url_button = types.ReplyKeyboardMarkup()
    # websites = types.KeyboardButton('start game')
    quit = types.KeyboardButton("quit")
    rock = types.KeyboardButton('rock')
    scissors = types.KeyboardButton('scissors')
    paper = types.KeyboardButton('paper')

    url_button.add(rock, scissors, paper, quit)
    # url_button.add(websites)
    bot.send_message(message.chat.id, "Game is started",
                     reply_markup=url_button)


@bot.message_handler()
def handle_text(message):
    global user_score, computer_score

    if message.text.lower() == 'rock' or message.text.lower() == 'paper' or message.text.lower() == 'scissors':
        computer_move = random.choice(moves)
        bot.send_message(message.chat.id, f"Computer's move: {computer_move}")

        if message.text.lower() == computer_move:
            bot.send_message(message.chat.id, "It's a tie")
            bot.send_message(
                message.chat.id, f"{computer_score}:{user_score}")
        elif (message.text.lower() == 'rock' and computer_move == 'scissors') or (message.text.lower() == 'paper' and computer_move == 'rock') or (message.text.lower() == 'scissors' and computer_move == 'paper'):
            user_score += 1
            bot.send_message(message.chat.id, 'Score for human')
            bot.send_message(
                message.chat.id, f"{computer_score}:{user_score}")
        else:
            computer_score += 1
            bot.send_message(message.chat.id, 'Score for bot')
            bot.send_message(
                message.chat.id, f"{computer_score}:{user_score}")

        if user_score >= 3:
            bot.send_message(
                message.chat.id, f"Winner is human, computer is the loser. User score: {user_score}")
            bot.send_message(
                message.chat.id, f"Bot score: {computer_score}, Human score: {user_score}")
            user_score = 0
            computer_score = 0
        elif computer_score >= 3:
            bot.send_message(
                message.chat.id, f'Computer is the winner, human is the loser. Computer score: {computer_score}')
            bot.send_message(
                message.chat.id, f"Bot score: {computer_score}, Human score: {user_score}")
            user_score = 0
            computer_score = 0
    elif message.text == 'quit':
        start_markups = types.ReplyKeyboardMarkup()
        start_game_markup = types.KeyboardButton("/startgame")
        help_markup = types.KeyboardButton('/help')
        start_markups.add(start_game_markup, help_markup)
        bot.send_message(message.chat.id, f'Allll commands',
                         reply_markup=start_markups)
    else:
        bot.send_message(message.chat.id, 'Invalid move')
    # bot.send_message(
    #     message.chat.id, f"{computer_score}:{user_score}")


# Запускаем бота
bot.polling(non_stop=True)
