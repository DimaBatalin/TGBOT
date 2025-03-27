import telebot
import config
import random

bot = telebot.TeleBot(config.TG_API_CONFIG)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['getinfouser'])
def get_info(message:telebot.types.Message):
	bot.reply_to(message, message.from_user)

@bot.message_handler(commands=['about'])
def get_about(message:telebot.types.Message):
	bot.reply_to(message, "Я D1M0N, и я сделал этого бота с помощью telebot")

@bot.message_handler(commands=['getrarandom'])
def send_random(message):
	bot.reply_to(message, random.randint(1, 3))
	
@bot.message_handler(commands=['math'])
def get_math(message: telebot.types.Message):
	N1 = random.randint(1, 100)
	N2 = random.randint(1, 100)
	X = N2 / N1
	bot.send_message(message.chat.id, f"{N1} * X = {N2} \n X = || {X:.2f} ||", parse_mode='MarkdownV2')
	
@bot.message_handler(func=lambda message: True)
def get_none(message):
	match message.text:
		case "Привет":
			bot.reply_to(message, "Привет мой новый друг!")
		case "Пока":
			bot.reply_to(message, "Пока(")
		case "Ты работаешь?":
			bot.reply_to(message, "Да, я работаю")
		case _:
			bot.reply_to(message, "Неизвестная команда")
	


	
	
bot.infinity_polling()