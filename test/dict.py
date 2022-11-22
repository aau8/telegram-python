# import EchoBotConfig
import telebot
import random
wordlist=[('mom','мама'), ('dad','папа'), ('cat','кошка')]


bot = telebot.TeleBot('5972429854:AAHJDUx2JH976ds2ehKTRQLfr8Wlj5xSP8E')

usranswer = ''

@bot.message_handler(commands=['start'])
def doStart(msg):
	bot.send_message(msg.chat.id, 'Привет! Я буду предлагать тебе слова, а ты переводи их')


@bot.message_handler(commands=['word'])
def getWord(message):
	word = wordlist[random.randint(0, len(wordlist) - 1)]
	last_msg = bot.send_message(message.chat.id, word[0])

	bot.register_next_step_handler(last_msg, handler_msg, word)


def handler_msg(message, word):
	if message.text != '/undo':
		text = "Молодец, ты ответил верно!" if word[1] == message.text else f"Ответ неверный. Правильный ответ: {word[1]}"

		bot.send_message(message.chat.id, text)
		getWord(message)


if __name__ == '__main__':
	print('Start')
	bot.infinity_polling()
	print('End')
