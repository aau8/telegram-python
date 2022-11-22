import sys
sys.path.append(r"C:\Users\Mi\Desktop\telegram-python")

from config import TOKEN
from pydub import AudioSegment
import telebot
import os

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start', 'help'])
def doStart(msg):
	text = '''
		Привет, я твой супербот! Я умею:
		/audio_to_voice - генерировать из музыки голосовые сообщения
	'''
	bot.send_message(msg.chat.id, text)


@bot.message_handler(commands=['audio_to_voice'])
def getAudio(msg):

	audio_obs = bot.send_message(msg.chat.id, 'Отправь файл с музыкой в любом формате')
	bot.register_next_step_handler(audio_obs, audio_proccess)


def audio_proccess(msg):
	global date = []
	date = date + msg

	audio_per = msg.audio.performer
	audio_title = msg.audio.title

	msg_info_1 = bot.send_message(msg.chat.id, 'Аудио обрабатывается...')

	audio_info = bot.get_file(msg.audio.file_id)
	audio_dl = bot.download_file(audio_info.file_path)
	audio_name = audio_info.file_path.split('/')[-1]
	audio_ext = audio_name.split('.')[-1]
	audio_ogg_name = audio_name.replace(f".{audio_ext}", '.ogg')

	with open(f"./music/{audio_name}", 'wb') as audio_file:
		audio_file.write(audio_dl)
		audio_parse = AudioSegment.from_file(f"./music/{audio_name}", audio_ext)
		bot.delete_message(msg.chat.id, msg_info_1.message_id)
		msg_info_2 = bot.send_message(msg.chat.id, 'Аудио загружается...')
		audio_ogg = audio_parse.export(f"./music/{audio_ogg_name}", format='ogg')

		bot.delete_message(msg.chat.id, msg_info_2.message_id)
		msg_audio = bot.send_voice(msg.chat.id, audio_ogg)
		msg_audio_text = f"<b>Автор: </b> {audio_per if audio_per is not None else 'Неизвестно'}\n\r<b>Название: </b> {audio_title if audio_title is not None else 'Неизвестно'}"
		bot.send_message(msg.chat.id, msg_audio_text, parse_mode='HTML', reply_to_message_id=msg_audio.message_id)

		audio_file.close()

	# Удалить все созданные файлы
	# os.remove(f"./music/{audio_ogg_name}")
	os.remove(f"./music/{audio_name}")


if __name__ == '__main__':
	print('Start')
	bot.infinity_polling()
	print('End')