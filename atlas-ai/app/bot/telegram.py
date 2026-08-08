from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from app.ai.agent import ask_ai


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Hello! I'm Atlas, your AI financial assistant.\n\n"
        "Ask me anything about companies, markets or finance."
    )


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_message = update.message.text

    try:

        response = ask_ai(user_message)

        await update.message.reply_text(response)

    except Exception as e:

        print("ERROR:", repr(e))

        await update.message.reply_text(
            f"AI Error: {e}"
        )


def create_bot(token):

    app = Application.builder().token(token).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    return app