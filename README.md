🤖 Atlas AI --- Financial Assistant

Atlas AI is an AI-powered financial assistant designed to work insideTelegram. It helps users research companies, understand financialtopics, and interact with an AI assistant through natural conversation.

The project is being developed as an MVP for the Atlas AI FinancialAssistant Hackathon.

🚀 Current Status

The current prototype includes:

✅ Telegram bot integration

✅ Python backend

✅ Gemini AI integration

✅ Natural-language conversation

✅ Finance-focused AI system prompt

✅ Environment-variable based API key configuration

Planned features include:

⏳ Conversation memory

⏳ SQLite/PostgreSQL database

⏳ Live stock prices

⏳ Company and market news

⏳ Company comparison

⏳ Personalized watchlists

⏳ Price/news alerts

⏳ Daily market briefing

⏳ Financial PDF/document analysis

⏳ Voice-message support

⏳ SEC and other trusted financial data sources

🎯 Project Goal

The goal of Atlas AI is to create more than a normal chatbot.

The assistant is designed to help finance professionals:

Research companies faster

Understand financial information

Stay informed about important market developments

Remember user interests and preferences

Reduce repetitive research

Receive useful information proactively

The hackathon emphasizes usefulness, proactivity, product thinking,conversational quality, finance depth, and engineering quality.

🏗️ Architecture

                    Telegram User
                         │
                         ▼
                  Telegram Bot API
                         │
                         ▼
                    Python Bot
                         │
                         ▼
                    AI Assistant
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Finance          News         Documents
        Tools           Tools           Tools
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                    AI Reasoning
                         │
                         ▼
                  Personalized Answer
                         │
                         ▼
                      Telegram

🛠️ Technology Stack

Component               Technology

Programming Language    PythonBot Platform            TelegramAI                      Google Gemini APIBackend                 PythonDatabase                SQLite initiallyHTTP/API Client         HTTPXPDF Processing          PyMuPDFScheduling              APSchedulerEnvironment Variables   python-dotenvVersion Control         Git / GitHub

📁 Project Structure

atlas-ai/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   └── agent.py
│   │
│   ├── bot/
│   │   ├── __init__.py
│   │   └── telegram.py
│   │
│   ├── alerts/
│   ├── database/
│   ├── documents/
│   └── finance/
│
├── uploads/
│
└── .venv/

⚙️ Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/atlas-ai.git
cd atlas-ai

2. Create a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\activate

macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

If requirements.txt has not been generated yet, install the currentcore dependencies:

pip install python-telegram-bot google-genai python-dotenv fastapi uvicorn sqlalchemy httpx apscheduler pymupdf

4. Configure environment variables

Create a .env file in the project root:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key

Never commit .env or API keys to GitHub.

5. Run the bot

python -m app.main

Expected output:

Atlas AI Bot Started...

Open the Telegram bot and send:

/start

Then try:

Hello

💬 Example Prompts

General Finance

What is a stock?

Explain P/E ratio in simple words.

What is the difference between revenue and profit?

Company Research

Tell me about Microsoft.

Give me an overview of Nvidia.

What are the main risks of investing in technology companies?

Company Comparison

Compare Apple and Microsoft from an investment perspective.

Compare Nvidia and AMD based on their business models.

🔐 Security

API keys and bot tokens must never be committed to GitHub.

The following files should remain private:

.env
.venv/
__pycache__/

Recommended .gitignore:

.env
.venv/
venv/
__pycache__/
*.pyc
*.db
uploads/

If an API key or Telegram bot token is accidentally published, revoke itand generate a replacement immediately.

🧠 Planned AI Workflow

Atlas AI will eventually use an agent-style architecture:

User Request
     │
     ▼
AI Agent
     │
     ├── Stock Tool
     ├── News Tool
     ├── Financial Data Tool
     ├── SEC Tool
     ├── Document Tool
     ├── Watchlist Tool
     └── Alert Tool
     │
     ▼
AI Reasoning
     │
     ▼
Concise Financial Response

The assistant should use external financial tools when currentinformation is required instead of inventing financial data.

📊 Planned Personalization

Atlas AI will gradually learn useful user context such as:

Companies the user follows

Preferred industries

Topics of interest

Watchlists

Notification preferences

Previous conversations

Research interests

This information will be stored in the database and used to improvefuture responses.

🔔 Planned Proactive Features

Morning Briefing

☀️ Morning Market Brief

Markets
S&P 500: ...
NASDAQ: ...

Your Watchlist
NVDA: ...
AAPL: ...
TSLA: ...

Important News
• ...
• ...

Why It Matters
...

Price Alert

Example:

User:
Alert me if Nvidia moves more than 5%.

Atlas will monitor the configured condition and send a Telegramnotification when it is triggered.

📄 Financial Document Intelligence

A planned feature allows users to upload financial documents such as:

Annual reports

Quarterly reports

Earnings presentations

Financial statements

SEC filings

Investment decks

Users will be able to ask questions naturally, for example:

What are the biggest risks in this report?

Summarize the financial performance.

What changed compared with the previous report?

🏆 Hackathon Focus

Atlas AI is being developed around five major evaluation areas:

Criterion                                             Weight

Usefulness, proactivity, and overall user value          30%Product thinking, judgment, and feature selection        25%AI experience and conversational quality                 20%Depth of the finance vertical                            15%Engineering quality and implementation                   10%

The project prioritizes a polished, useful experience over implementinga large number of disconnected features.

🗺️ Roadmap

[✓] Telegram Bot
[✓] Gemini AI
[✓] Basic Conversation
[ ] Conversation Memory
[ ] Database
[ ] Live Stock Data
[ ] Financial News
[ ] Company Research Tools
[ ] Company Comparison
[ ] Watchlist
[ ] Price Alerts
[ ] Daily Briefing
[ ] PDF Analysis
[ ] Voice Input
[ ] SEC Research
[ ] Production Deployment

👨‍💻 Development

This project is intended as an AI-assisted development project. Thearchitecture is kept modular so new financial tools, integrations, andworkflows can be added without rewriting the entire application.

📜 License

This project is currently developed as a hackathon prototype.

Add an appropriate open-source license if you decide to publish theproject for general use.
