from config import token
import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands = 'hi')
def hello(msg):
    bot.send_message(msg.chat.id, 'Привет Господин!')

# @bot.message_handler(commands = ['start', 'hi', 'dog'])
# def hello(msg):
#     bot.send_message(msg.chat.id, 'Привет! Я твой бот! Я буду передразнивать тебя')

# @bot.message_handler(content_types = 'text')
# def echo(msg):
#     bot.send_message(msg.chat.id, msg.text)

if __name__ == '__main__':
    # print('Go')
    bot.infinity_polling()
    # print('End')