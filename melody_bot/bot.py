import sys
sys.path.append(r"C:\Users\Mi\Desktop\telegram-python")

import config
import telebot
import time
import os

# print(config.TOKEN)

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["test"])
def send_voices(msg):
	for file in os.listdir('./music/'):
		if (file.split('.')[-1] == 'ogg'):
			# print(msg)
			file = open(f'./music/{file}', 'rb')
			msgAudio = bot.send_audio(msg.chat.id, file)

			bot.send_message(msg.chat.id, msgAudio.voice.file_id, reply_to_message_id=msgAudio.message_id)
			print(msgAudio)

		time.sleep(1)

if __name__ == '__main__':
	print('Start')
	bot.infinity_polling()
	print('Finish')