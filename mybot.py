import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# توکن رباتی که از BotFather گرفتی
TOKEN = "8435156609:AAHZP0Hh1Dvbz9l49mcgqwdQkTuzmUXPG6w"

# آیدی کانال (با -100 شروع میشه)
CHANNEL_ID =  -1003090077793  # اینو با کدی که از RAW BOT گرفتی عوض کن

# فعال کردن لاگ برای خطاها
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# هندلر پیام
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # ارسال پیام به کانال
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"📩 پیام ناشناس جدید:\n\n{text}\n\n👤 شناسه کاربر: {user_id}"
    )

    # ارسال پاسخ به کاربر
    await update.message.reply_text("✅ پیام شما ناشناس ارسال شد.")


def main():
    # ساخت اپلیکیشن
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلر
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # اجرا
    application.run_polling()


if __name__ == "__main__":
    main()
