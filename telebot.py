import telebot

bot = telebot.TeleBot("8482831224:AAGpust7xLA6FilDyc5HOEbNZhAM6Nx7J0o", parse_mode="MARKDOWN")

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id, "Hello, how are you?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
