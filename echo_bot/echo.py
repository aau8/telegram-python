import sys
sys.path.append(r"C:\Users\Mi\Desktop\telegram-python")

from config import token
import telebot

userOne = 803056459
userTwo = 685679598

bot = telebot.TeleBot(token)


# @bot.message_handler(content_types=["photo"])
# def echo_messages(message):
# 	bot.send_message(message.chat.id, 'it\' photo')

@bot.message_handler(content_types=["text"])
def echo_messages(message):

	if message.from_user.id == userOne:
		bot.send_message(userTwo, message.text)
		bot.send_message(userOne, 'Message send')

	if message.from_user.id == userTwo:
		bot.send_message(userOne, message.text)
		bot.send_message(userTwo, 'Message send')

@bot.message_handler(content_types=['document'])
def msg(message):
	document = message.document
	if (document.mime_type == 'video/mp4'):

		if message.from_user.id == userOne:
			bot.send_document(userTwo, document.file_id)
			bot.send_message(userOne, 'Gif send')

		if message.from_user.id == userTwo:
			bot.send_document(userOne, document.file_id)
			bot.send_message(userTwo, 'Gif send')

# print('ok')

if __name__ == '__main__':
	print('Hello, Telegram Bot!!!')
	bot.infinity_polling()
	print('Goodbye, Telegram Bot!!!')