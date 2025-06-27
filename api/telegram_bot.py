import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import TelegramUser

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    if not username:
        await update.message.reply_text("Please set a Telegram username in your Telegram settings.")
        return

    user, created = TelegramUser.objects.get_or_create(telegram_username=username)
    if created:
        await update.message.reply_text(f"Hi {username}, you've been registered!")
    else:
        await update.message.reply_text(f"Welcome back, {username}!")

def run_bot():
    token = config("TG_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
