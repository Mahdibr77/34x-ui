from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import subprocess

# Function to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من ربات مدیریت V2Ray 3x-ui هستم. از من بپرسید!")

# Function for help command
def help_command(update: Update, context: CallbackContext):
    help_text = (
        "دستورات موجود:
"
        "/start - شروع گفتگو
"
        "/help - لیست دستورات
"
        "/status - بررسی وضعیت V2Ray
"
        "/restart - راه‌اندازی مجدد V2Ray
"
        "/add_user - اضافه کردن کاربر
"
        "/remove_user - حذف کاربر"
    )
    update.message.reply_text(help_text)

# Function to check the status of V2Ray
def status(update: Update, context: CallbackContext):
    try:
        result = subprocess.run(["systemctl", "is-active", "v2ray"], capture_output=True, text=True)
        if result.stdout.strip() == "active":
            update.message.reply_text("V2Ray در حال کار است.")
        else:
            update.message.reply_text("V2Ray متوقف است.")
    except Exception as e:
        update.message.reply_text(f"خطا در بررسی وضعیت: {str(e)}")

# Function to restart V2Ray
def restart(update: Update, context: CallbackContext):
    try:
        subprocess.run(["systemctl", "restart", "v2ray"], check=True)
        update.message.reply_text("V2Ray در حال راه‌اندازی مجدد است...")
    except Exception as e:
        update.message.reply_text(f"خطا در راه‌اندازی مجدد: {str(e)}")

# Function to add a user
def add_user(update: Update, context: CallbackContext):
    if context.args:
        user_id = context.args[0]
        # Add code to add user to V2Ray here
        update.message.reply_text(f"کاربر با ID {user_id} اضافه شد.")
    else:
        update.message.reply_text("لطفاً ID کاربر را وارد کنید.")

# Function to remove a user
def remove_user(update: Update, context: CallbackContext):
    if context.args:
        user_id = context.args[0]
        # Add code to remove user from V2Ray here
        update.message.reply_text(f"کاربر با ID {user_id} حذف شد.")
    else:
        update.message.reply_text("لطفاً ID کاربر را وارد کنید.")

def main():
    # Place your API token here
    updater = Updater("YOUR_API_TOKEN")

    # Adding commands
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(CommandHandler("status", status))
    updater.dispatcher.add_handler(CommandHandler("restart", restart))
    updater.dispatcher.add_handler(CommandHandler("add_user", add_user))
    updater.dispatcher.add_handler(CommandHandler("remove_user", remove_user))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
