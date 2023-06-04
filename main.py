# import random
# import telebot
# from telebot import types
# import random


# bot = telebot.TeleBot("6129194736:AAFrw3Mh6t0YMtWoxSf_LYrHdGWI2V_WD5M")

# # Определяем обработчик команды /start


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     user = f"Hello {message.from_user.first_name} "
#     bot.send_message(message.chat.id, user, parse_mode="html")


# @bot.message_handler(commands=['help'])
# def help_func(message):
#     url_button = types.InlineKeyboardMarkup()
#     url_button.add(types.InlineKeyboardButton(
#         "Жми сюда пупсик", url='https://pypi.org/project/pyTelegramBotAPI/'))
#     bot.send_message(
#         message.chat.id, f"Перейдите на сайт и узнавайте все побробно", reply_markup=url_button)


# @bot.message_handler(commands=['buttons'])
# def help_func(message):
#     url_button = types.ReplyKeyboardMarkup()
#     website = types.KeyboardButton('Start game')

#     url_button.add(website)
#     bot.send_message(
#         message.chat.id, f"Перейдите на сайт и узнавайте все побробно", reply_markup=url_button)


# # moves = ['rock', 'paper', 'scissors']
# # user_score = 0
# # computer_score = 0


# # @bot.message_handler()
# # def just_text(message):

# #     if message.text == "Начать игру":
# #         bot.send_message(message.chat.id, f'Welcome to Rock, Paper, Scissors!')

# #         while True:
# #             computer_move = random.choice(['rock', 'paper', 'scissors'])
# #             bot.send_message(message.chat_id, f'computers move{computer_move}')
# #             bot.send_message(message.chat_id, f"enter your move ")

# #             if message.text not in moves:
# #                 bot.send_message(message.chat_id, 'Try again, invalid move')
# #                 continue
# #             if message.text == computer_move:
# #                 bot.send_message(message.chat_id, "it's tie")
# #             elif message.texts == 'rock' and computer_move == 'paper':
# #                 computer_score += 1
# #                 bot.send_message(message.chat_id, 'score for bot')
# #             elif message.texts == 'paper' and computer_move == 'scissors':
# #                 computer_score += 1
# #                 bot.send_message(message.chat_id, 'score for bot')
# #             elif message.texts == 'scissors' and computer_move == 'rock':
# #                 computer_score += 1
# #                 bot.send_message(message.chat_id, 'score for bot')
# #             else:
# #                 user_score += 1
# #                 bot.send_message(message.chat_id, 'score for human')
# #             if user_score == 3:
# #                 bot.send_message(message.chat.id,
# #                                  f"Winner is human, computer loser user score is:{user_score} ")
# #                 bot.send_message(message.chat.id,
# #                                  f"bot score:{computer_score} human score:{user_score}")
# #                 break
# #             elif computer_score == 3:
# #                 bot.send_message(message.chat.id,
# #                                  f'computer is winner , human is loser compueter score is: {computer_score} ')
# #                 bot.send_message(message.chat.id,
# #                                  f"bot score:{computer_score} human score:{user_score}")
# #                 break

# #     bot.send_message(message.chat.id, f'{user_score}:{computer_score}')


# moves = ['rock', 'paper', 'scissors']
# user_score = 0
# computer_score = 0


# @bot.message_handler()
# def just_text(message):
#     global user_score, computer_score

#     if message.text == "Начать игру":
#         bot.send_message(message.chat.id, 'Welcome to Rock, Paper, Scissors!')

#         while True:
#             computer_move = random.choice(['rock', 'paper', 'scissors'])
#             bot.send_message(
#                 message.chat.id, f'Computer\'s move: {computer_move}')
#             bot.send_message(message.chat.id, 'Enter your move:')

#             if message.text not in moves:
#                 bot.send_message(message.chat.id, 'Try again, invalid move')
#                 continue
#             if message.text == computer_move:
#                 bot.send_message(message.chat.id, "It's a tie")
#             elif message.text == 'rock' and computer_move == 'paper':
#                 computer_score += 1
#                 bot.send_message(message.chat.id, 'Score for bot')
#             elif message.text == 'paper' and computer_move == 'scissors':
#                 computer_score += 1
#                 bot.send_message(message.chat.id, 'Score for bot')
#             elif message.text == 'scissors' and computer_move == 'rock':
#                 computer_score += 1
#                 bot.send_message(message.chat.id, 'Score for bot')
#             else:
#                 user_score += 1
#                 bot.send_message(message.chat.id, 'Score for human')

#             if user_score == 3:
#                 bot.send_message(
#                     message.chat.id, f"Winner is human, computer is the loser. User score: {user_score}")
#                 bot.send_message(
#                     message.chat.id, f"Bot score: {computer_score}, Human score: {user_score}")
#                 break
#             elif computer_score == 3:
#                 bot.send_message(
#                     message.chat.id, f'Computer is the winner, human is the loser. Computer score: {computer_score}')
#                 bot.send_message(
#                     message.chat.id, f"Bot score: {computer_score}, Human score: {user_score}")
#                 break

#         bot.send_message(
#             message.chat.id, f'Scores: {user_score}:{computer_score}')


# # Определяем обработчик сообщений с текстом
# # @bot.message_handler(func=lambda message: True)
# # def echo_message(message):
# #     bot.reply_to(message, message.text)
# # Запускаем бота
# bot.polling(non_stop=True)
