import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing from .env"
    )

client = genai.Client(
    api_key=api_key
)


def ask_ai(user_message, conversation_history=""):

    prompt = f"""
You are Atlas, an AI financial assistant.

You help users with:
- Companies
- Stock markets
- Financial research
- Earnings
- Business news
- Financial documents

User message:
{user_message}

Conversation history:
{conversation_history}

Rules:
- Be concise and useful.
- Explain important information clearly.
- Never invent financial data.
- Do not pretend to have live stock prices unless
  live financial data has actually been retrieved.
- Ask a clarification question when the request is ambiguous.
- Explain why important information matters.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text