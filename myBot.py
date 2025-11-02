import telebot
import os

api_key=os.getenv("api_key")

bot = telebot.TeleBot(api_key, parse_mode="MARKDOWN")

@bot.message_handler(commands=["start"])
def send_welcome(message):  
    bot.reply_to(message, "Welcome to the Telegram bot!")

@bot.message_handler(content_types=['text', 'photo', 'audio', 'voice', 'video', 'document'])
def handle_message(message):
    chat_id = message.chat.id

    # 📝 اگر پیام متنی بود
    if message.content_type == 'text':
        bot.send_message(chat_id, f"📄 متن دریافت شد:\n{message.text}")
        text=message.text.lower()
        if "hello" in text:
           bot.reply_to(message, "Hello, how are you?")
        elif "bye" in text:
           bot.reply_to(message, "Bye, see you later!")
        else:
           bot.reply_to(message, "Have a nice day!")

    # 🖼 اگر عکس بود
    elif message.content_type == 'photo':
        bot.send_message(chat_id, f"🖼 عکس دریافت شد! کپشن: {message.caption or 'ندارد'}")

    # 🎧 اگر موزیک بود
    elif message.content_type == 'audio':
        bot.send_message(chat_id, f"🎵 آهنگ دریافت شد! عنوان: {message.audio.title or 'نامشخص'}")

    # 🎤 اگر ویس بود
    elif message.content_type == 'voice':
        bot.send_message(chat_id, "🎤 ویس دریافت شد!")

    # 🎬 اگر ویدیو بود
    elif message.content_type == 'video':
        bot.send_message(chat_id, f"🎬 ویدیو دریافت شد! کپشن: {message.caption or 'ندارد'}")

    # 📁 اگر فایل (مثلاً PDF یا ZIP) بود
    elif message.content_type == 'document':
        bot.send_message(chat_id, f"📁 فایل دریافت شد: {message.document.file_name}")

bot.infinity_polling()



