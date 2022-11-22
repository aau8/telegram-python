import telebot
import sqlite3
from db import write_chat_to_db, write_message_to_db, check_pass_to_db, add_user_to_blacklist, check_user_to_blacklist

TOKEN = '5017239893:AAGxLYhGZ7wH_zGtsPy3nGMnxQROpDsJC9o'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def go_start(msg):
	if msg.chat.type == 'private':
		# print()
		if check_user_to_blacklist(msg) is None:
			# print(msg)
			msg_pass = bot.send_message(msg.chat.id, "Введите пароль:")
			bot.register_next_step_handler(msg_pass, auth)

		# else:
		# 	bot.send_message(msg.chat.id, "Пошел нахуй отсюда, мудила ебанный!")

	# write_message_to_db(msg)

	# msg_hello = bot.send_message(msg.chat.id, 'Привет! Я буду записывать историю нашей переписки. С помощью команды /message <id_message> ты можешь узнать текст сообщения по его id')
	# write_message_to_db(msg_hello)

def auth(msg, attempt=0):
	# attempt = None

	# if attempt is None:
	# 	attempt = 0


	if msg.text != check_pass_to_db(msg):
		if attempt < 2:
			reply = bot.send_message(msg.chat.id, "Неправильно, попробуйте еще раз!")
			bot.register_next_step_handler(reply, auth, attempt=attempt + 1)

		else:
			bot.send_message(msg.chat.id, "Пошел нахуй отсюда, мудила ебанный!")
			add_user_to_blacklist(msg)

	else:
		bot.send_message(msg.chat.id, "👑👑👑 Добро пожаловать, мой Король! 👑👑👑")

@bot.message_handler(commands=['history'])
def do_history(msg):

	print('history')

	# message_id = msg.text.replace('/message', '').strip()

	# if message_id:
	# 	try:
	# 		message_id = int(message_id)
	# 	except:
	# 		msg_last = bot.send_message(msg.chat.id, 'id сообщения должно быть числом. Отправьте id еще раз')
	# 		write_message_to_db(msg_last)
	# 		bot.register_next_step_handler(msg_last, do_message)
	# 		return 0

	# else:
	# 	msg_last = bot.send_message(msg.chat.id, 'Отправьте id сообщения, которое хотите получить')
	# 	write_message_to_db(msg_last)
	# 	bot.register_next_step_handler(msg_last, do_message)
	# 	return 0


@bot.message_handler()
def getText(msg):
	write_chat_to_db(msg)
	write_message_to_db(msg)


if __name__ == '__main__':
    print('Start')
    bot.infinity_polling()
    print('End')
