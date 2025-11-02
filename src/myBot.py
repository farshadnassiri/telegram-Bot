import telebot
import os

api_key=os.getenv("api_key")

bot = telebot.TeleBot(api_key, parse_mode="MARKDOWN")

@bot.message_handler(commands=["start"])
def send_welcome(message):  
    bot.reply_to(message, "Welcome to the Telegram bot!")

@bot.message_handler(content_types=["text", "photo", "audio", "voice", "video", "document"])
def handle_message(message):
    #chat_id = message.chat.id

    if message.content_type == 'text':
        bot.reply_to(message, f"📄 متن دریافت شد:\n{message.text}")
    else:
        bot.reply_to(message, "Please send a text message")
        
bot.infinity_polling()



