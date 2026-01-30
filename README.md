# Telegram Writing Assistant

![17698041000364903691004859085197](https://github.com/user-attachments/assets/a5c0f75b-dd1c-4ad1-965a-e1296edcb237)


A drafting system for writers, developers, and creators who regularly publish articles or newsletters. It gets you from scattered thoughts to publishable articles.

You send thoughts to a telegram bot that saves everything locally, processes it with Claude, and organizes it into articles.

## How It Works

1. Send materials to Telegram bot (text, voice, images)
2. Bot saves everything locally to `inbox/raw/`
3. Run `/process` command to organize materials
4. Claude analyzes accumulated materials
5. Updates existing articles or creates new ones
6. Commits to GitHub
7. Sends commit link back to Telegram

## Workflow Philosophy

Brain dump → Draft → Publish → Delete

### 1. Brain Dump Phase

When you're working on something, having ideas, or want to capture thoughts:

- Send voice notes with ideas, thoughts, random bits of information
- Drop links (they'll be fetched and summarized during processing)
- Send screenshots or photos
- Don't worry about organization - just get it out of your head

Think of this as your "working memory" - a place to dump raw thoughts.

### 2. Article Formation Phase

Run `/process` - Claude automatically groups related materials into articles:

- Articles form organically from your scattered inputs
- Source citations included, so you know where each idea came from
- Messages sent within ~1-2 minutes are analyzed together

Over time, articles take shape from your accumulated brain dumps.

### 3. Draft Phase

When an article feels "ready":

- The article is already structured (headings, sections, sources)
- Edit it: polish the content, fix structure, add your voice

### 4. Publish and Delete Phase

- Publish wherever you want: blog, newsletter, documentation site
- Once published, delete the article from this repo
- Use the `/delete` command (planned) to remove article + all references (images, assets)


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
