import os

from dotenv import load_dotenv

from app.bot.telegram import create_bot


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN is missing"
    )

bot = create_bot(TOKEN)

print("Atlas AI Bot Started...")

bot.run_polling()