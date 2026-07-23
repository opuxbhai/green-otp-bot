import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["📩 Get Number"],
        ["💰 Balance", "📊 Status"],
        ["ℹ️ Help"],
    ],
    resize_keyboard=True,
)

SERVICE_MENU = ReplyKeyboardMarkup(
    [
        ["📘 Facebook", "📸 Instagram"],
        ["💬 Telegram", "📱 WhatsApp"],
        ["🔙 Back"],
    ],
    resize_keyboard=True,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\nChoose an option:",
        reply_markup=MAIN_MENU,
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📩 Get Number":
        await update.message.reply_text(
            "📱 Select a service:",
            reply_markup=SERVICE_MENU
        )

    elif text == "🔙 Back":
        await update.message.reply_text(
            "🏠 Main Menu",
            reply_markup=MAIN_MENU
        )

    elif text == "💰 Balance":
        await update.message.reply_text("💰 Your Balance: 0.00$")

    elif text == "📊 Status":
        await update.message.reply_text("🟢 Bot Status: Online")

    elif text == "ℹ️ Help":
        await update.message.reply_text(
            "Use the buttons below to access the bot."
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Text buttons
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            button_handler
        )
    )

    print("🤖 Bot is running...")

    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
