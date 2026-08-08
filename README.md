# 🤖 Atlas AI — Financial Assistant

**Atlas AI** is an AI-powered financial assistant built with **Python, Telegram, and Google Gemini AI**.

It is designed to help users research companies, understand financial information, and interact with an AI financial assistant through natural conversation.

> 🚧 **Project Status:** Working MVP / Hackathon Project

---

## ✨ Features

### ✅ Currently Implemented

- 🤖 AI-powered financial assistant
- 📱 Telegram Bot integration
- 💬 Natural-language conversation
- 🧠 Google Gemini AI integration
- 🐍 Python-based application
- 🔐 Environment-variable API key configuration
- 💰 Finance-focused AI assistant prompt
- ⚠️ Basic API error handling

### 🚀 Planned Features

- 🧠 Conversation memory
- 🗄️ SQLite database
- 📈 Live stock prices
- 📰 Financial news
- 🏢 Company research
- ⚖️ Company comparison
- ⭐ Personalized watchlists
- 🔔 Price and news alerts
- 🌅 Daily market briefing
- 📄 Financial PDF analysis
- 🎙️ Voice-message support
- 📑 SEC filing research

---

## 🎯 Project Goal

The goal of **Atlas AI** is to build more than a simple chatbot.

Atlas AI is designed to become a personal financial assistant that helps users:

- Research companies faster
- Understand financial concepts
- Analyze financial information
- Follow companies and markets
- Reduce repetitive research
- Receive useful financial information
- Interact naturally through Telegram

The long-term goal is to create a **proactive financial assistant** that can understand, remember, research, analyze, monitor, and assist.

---

# 🏗️ Architecture

```text
                         👤 USER
                           │
                           ▼
                    📱 TELEGRAM
                           │
                           ▼
                   🤖 TELEGRAM BOT
                           │
                           ▼
                     🐍 PYTHON
                           │
                           ▼
                      🧠 AI AGENT
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
          📈 FINANCE     📰 NEWS     📄 DOCUMENTS
             TOOLS        TOOLS         TOOLS
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                     🧠 AI ANALYSIS
                           │
                           ▼
                    💬 FINAL RESPONSE
                           │
                           ▼
                       📱 TELEGRAM
