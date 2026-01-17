# Telegram Writing Assistant

A personal knowledge management system where you send thoughts to Telegram (text, voice, images) and a bot saves everything locally, processes it with Claude, and organizes it into articles.

## How It Works

1. Send materials to Telegram bot (text, voice, images)
2. Bot saves everything locally to `inbox/raw/`
3. Run `/process` command to organize materials
4. Claude analyzes accumulated materials
5. Updates existing articles or creates new ones
6. Commits to GitHub
7. Sends commit link back to Telegram

## Setup

1. Clone the repo
2. Install dependencies:

```bash
uv add python-telegram-bot groq python-dotenv httpx
```

3. Create `.env` file:

```env
TELEGRAM_BOT_API_KEY=your_bot_token
TELEGRAM_CHANNEL=your_chat_id
GROQ_API_KEY=your_groq_key
```

4. Run the bot:

```bash
uv run python main.py
```

## Bot Commands

- `/start` - Start the bot
- `/status` - Show inbox status
- `/process` - Process accumulated materials with Claude

## Project Structure

```
telegram-writing-assistant/
├── articles/           # Generated articles
├── inbox/
│   ├── raw/           # New materials (text, transcripts, photos)
│   ├── used/          # Processed materials
│   └── summaries/     # Processing summaries (not pushed to git)
├── assets/
│   └── images/        # Organized by article name
├── claude_runs/       # Claude run logs (not pushed to git)
├── .claude/
│   └── commands/
│       └── process.md # Claude processing instructions
├── main.py            # Telegram bot
└── .env               # API keys (not pushed to git)
```

## Voice Transcription

Voice messages are transcribed using Groq's Whisper API. The `.ogg` files are deleted after transcription - only the text transcript is kept.

## Image Processing

Images are analyzed using Groq Vision to generate descriptions. When placed in articles:
- Images are renamed to descriptive names based on content
- Placed in `assets/images/{article_name}/`
- Unused images go to `assets/images/_unused/`

## License

MIT
