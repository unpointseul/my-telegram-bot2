import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters, CommandHandler

# توکن رباتی که از BotFather گرفتی
TOKEN = "8435156609:AAHZP0Hh1Dvbz9l49mcgqwdQkTuzmUXPG6w"

# آیدی کانال (با -100 شروع میشه)
CHANNEL_ID = -1003090077793  # جایگزین کن با آیدی کانالت

# فعال کردن لاگ برای خطاها
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# 📩 هندل پیام کاربر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = update.effective_user.full_name
    username = update.effective_user.username
    text = update.message.text

    # ارسال پیام به کانال
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=(
            f"📩 پیام ناشناس جدید:\n\n"
            f"{text}\n\n"
            f"👤 نام: {user_name}\n"
            f"🔗 یوزرنیم: @{username if username else '---'}\n"
            f"🆔 شناسه: {user_id}"
        )
    )

    # ارسال پاسخ به کاربر
    await update.message.reply_text("✅ پیام شما ناشناس ارسال شد.")


# 🔁 هندل دستور /reply برای جواب دادن
async def reply_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # فرمت: /reply user_id متن
    if len(context.args) < 2:
        await update.message.reply_text("❌ فرمت درست: /reply user_id متن")
        return
    
    try:
        user_id = int(context.args[0])
        reply_text = " ".join(context.args[1:])
        
        # ارسال پاسخ به کاربر
        await context.bot.send_message(chat_id=user_id, text=f"📩 پاسخ مدیر:\n\n{reply_text}")
        await update.message.reply_text("✅ پیام ارسال شد.")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا: {e}")


def main():
    # ساخت اپلیکیشن
    application = Application.builder().token(TOKEN).build()

    # هندلر پیام‌ها
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # هندلر دستور /reply
    application.add_handler(CommandHandler("reply", reply_command))

    # اجرا
    application.run_polling()


if __name__ == "__main__":
    main()


