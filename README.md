# 🤖 Telegram Bot with LLM Integration

This project demonstrates a Telegram bot built with `pyTelegramBotAPI` that integrates with a Large Language Model (LLM) for interactive conversations.

## ✨ Features

- **Start Command**: Greet users with a welcome message. 👋
- **Text Message Handling**: Processes incoming text messages and responds using an integrated LLM. 💬
- **Environment Variable for API Key**: Securely manages the Telegram Bot API token. 🔑
- **Basic Media Handling**: Prompts users to send text messages for LLM interaction. 🖼️🔊

## 🚀 Getting Started

Follow these steps to set up and run your Telegram bot.

### Prerequisites

- Python 3.x installed.
- A Telegram Bot Token from BotFather.
- An API key for your chosen Large Language Model (LLM).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/TeleBot.git
   cd TeleBot
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: You might need to create a `requirements.txt` file first if it doesn't exist)*

### Configuration

1. **Set up environment variables:**
   Create a `.env` file in the root directory of your project and add your Telegram Bot API key and LLM API key:

   ```
   api_key=YOUR_TELEGRAM_BOT_API_KEY
   LLM_API_KEY=YOUR_LLM_API_KEY
   ```
   Replace `YOUR_TELEGRAM_BOT_API_KEY` with your actual Telegram bot token and `YOUR_LLM_API_KEY` with your LLM service API key.

### Running the Bot

1. **Start the bot:**
   ```bash
   python src/myBot.py
   ```

   Your bot should now be running and ready to receive messages on Telegram! 🎉

## 📂 Project Structure

```
.
├── src/
│   ├── myBot.py           # Main bot logic
│   ├── myllm.py           # LLM integration (assumed)
│   └── telbot.ipynb       # Jupyter notebook with basic examples
├── .env.example           # Example environment file
└── README.md              # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
