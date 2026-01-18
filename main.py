import asyncio
import base64
import os
import subprocess
import textwrap
import time
from datetime import datetime
from pathlib import Path

import httpx
from dotenv import load_dotenv
from groq import Groq
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from claude_runner import ClaudeRunner
from message_queue import MessageQueue

# Load environment variables
load_dotenv()



# Configuration
TELEGRAM_BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
TELEGRAM_CHANNEL = int(os.getenv("TELEGRAM_CHANNEL"))
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
REPO_PATH = Path.cwd()
INBOX_RAW = REPO_PATH / "inbox" / "raw"
INBOX_USED = REPO_PATH / "inbox" / "used"
ASSETS_IMAGES = REPO_PATH / "assets" / "images"
ARTICLES_DIR = REPO_PATH / "articles"
LOGS_DIR = REPO_PATH / "claude_runs"

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


def describe_image(image_path: Path) -> str:
    """Describe an image using Groq vision."""
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    prompt = textwrap.dedent("""\
        I'm building a personal knowledge base from screenshots and images sent to Telegram.
        Please analyze this image and provide:

        1. Type: screenshot, photo, terminal, code, diagram, document, etc.
        2. Main content: what is shown
        3. Visible text: any text you can read (put in a code block for readability)
        4. Potential use: what kind of article or note this might support

        Format clearly with sections. Put any OCR text in triple-backtick code blocks.
    """)

    response = groq_client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}},
                ],
            }
        ],
    )
    content = response.choices[0].message.content
    # Strip leading/trailing whitespace and clean up multiple blank lines
    lines = [line.rstrip() for line in content.strip().split('\n')]
    # Remove empty lines from start/end but keep structure
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return '\n'.join(lines)


def get_timestamp(message_date: datetime) -> str:
    """Get timestamp from message for filenames."""
    return message_date.strftime("%Y%m%d_%H%M%S")


def get_filename(message_date: datetime, message_id: int, username: str = None) -> str:
    """Get unique filename using message_id to prevent collisions."""
    timestamp = message_date.strftime("%Y%m%d_%H%M%S")
    user_tag = username or "unknown"
    return f"{timestamp}_{user_tag}_msg{message_id}"


def is_allowed_chat(update: Update) -> bool:
    """Check if message is from the allowed chat."""
    return update.effective_chat.id == TELEGRAM_CHANNEL


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command."""
    if not is_allowed_chat(update):
        return
    await update.message.reply_text(
        "Hello! I'm your writing assistant.\n\n"
        "Send me:\n"
        "• Text messages → saved as markdown\n"
        "• Voice messages → transcribed and saved\n"
        "• Photos → saved to assets/images\n\n"
        "Use /process to analyze accumulated materials and update articles."
    )


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /status command - show inbox count."""
    if not is_allowed_chat(update):
        return
    raw_files = list(INBOX_RAW.glob("*"))
    await update.message.reply_text(
        f"Inbox status:\n"
        f"📥 Raw items: {len([f for f in raw_files if not f.name.startswith('.')])}\n"
        f"📝 Articles: {len(list(ARTICLES_DIR.glob('*.md')))}"
    )


async def save_text_message(content: str, user_id: int, username: str = None, message_date: datetime = None, message_id: int = None) -> Path:
    """Save text message as markdown file."""
    msg_date = message_date or datetime.now()
    if message_id:
        base_name = get_filename(msg_date, message_id, username)
    else:
        base_name = f"{get_timestamp(msg_date)}_{username or f'user_{user_id}'}"
    filename = INBOX_RAW / f"{base_name}.md"

    # Build content without textwrap.dedent
    metadata = "\n".join([
        "---",
        "source: telegram",
        f"date: {msg_date.isoformat()}",
        f"user_id: {user_id}",
        f"username: {username or 'unknown'}",
        "---",
        "",
        ""
    ])

    with open(filename, "w", encoding="utf-8") as f:
        f.write(metadata + content)

    return filename


async def save_voice_message(file_path: str, user_id: int, username: str = None, message_date: datetime = None, message_id: int = None) -> tuple[Path, Path, str]:
    """Save voice message file and transcribe it."""
    msg_date = message_date or datetime.now()
    user_tag = username or f"user_{user_id}"

    if message_id:
        base_name = get_filename(msg_date, message_id, username)
    else:
        base_name = f"{get_timestamp(msg_date)}_{user_tag}"

    # Download and save the audio file
    audio_filename = INBOX_RAW / f"{base_name}.ogg"
    transcription_filename = INBOX_RAW / f"{base_name}_transcript.txt"

    # Download voice file
    async with httpx.AsyncClient() as client:
        response = await client.get(file_path)
        with open(audio_filename, "wb") as f:
            f.write(response.content)

    # Transcribe with Groq Whisper
    with open(audio_filename, "rb") as audio_file:
        transcription = groq_client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="text"
        )
        transcript_text = transcription.strip()

    # Build metadata without textwrap.dedent
    metadata = "\n".join([
        "---",
        "source: telegram_voice",
        f"date: {msg_date.isoformat()}",
        f"user_id: {user_id}",
        f"username: {username or 'unknown'}",
        f"audio_file: {audio_filename.name}",
        "---",
        "",
        ""
    ])
    # Wrap transcript text at 100 chars for readability
    wrapped_transcript = textwrap.fill(transcript_text, width=100)
    with open(transcription_filename, "w", encoding="utf-8") as f:
        f.write(metadata + wrapped_transcript)

    # Delete the .ogg file - we only need the transcript
    audio_filename.unlink()

    return audio_filename, transcription_filename, transcript_text


async def save_photo(file_path: str, user_id: int, username: str = None, caption: str = None, message_date: datetime = None, message_id: int = None) -> tuple[Path, str]:
    """Save photo to inbox/raw and return (filename, description)."""
    msg_date = message_date or datetime.now()
    user_tag = username or f"user_{user_id}"

    if message_id:
        base_name = get_filename(msg_date, message_id, username)
    else:
        base_name = f"{get_timestamp(msg_date)}_{user_tag}"

    # Save image in inbox/raw alongside its markdown description
    filename = INBOX_RAW / f"{base_name}.jpg"

    async with httpx.AsyncClient() as client:
        response = await client.get(file_path)
        with open(filename, "wb") as f:
            f.write(response.content)

    # Generate image description
    description = describe_image(filename)

    # Create markdown with description (image is in the same folder)
    md_filename = INBOX_RAW / f"{base_name}_photo.md"
    # Build content without textwrap.dedent to avoid indentation issues
    content_lines = [
        "---",
        f"source: telegram_photo",
        f"date: {msg_date.isoformat()}",
        f"user_id: {user_id}",
        f"username: {username or 'unknown'}",
        f"image_file: {filename.name}",
        "---",
        "",
        description,
    ]
    content = "\n".join(content_lines)
    if caption:
        content += f"\n\nCaption: {caption}"

    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename, description


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming text messages."""
    if not is_allowed_chat(update):
        return
    try:
        user = update.effective_user
        text = update.message.text
        msg_date = update.message.date
        msg_id = update.message.message_id

        filename = await save_text_message(text, user.id, user.username, msg_date, msg_id)
        await update.message.reply_text(f"Saved as {filename.name}", parse_mode=None)
    except Exception as e:
        await update.message.reply_text(f"Error: {type(e).__name__}: {e}", parse_mode=None)


async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming voice messages."""
    if not is_allowed_chat(update):
        return
    try:
        user = update.effective_user
        voice = update.message.voice
        msg_date = update.message.date
        msg_id = update.message.message_id

        # Get the file path
        file = await voice.get_file()
        audio_file, transcript_file, transcript_text = await save_voice_message(file.file_path, user.id, user.username, msg_date, msg_id)

        # Send transcript to chat
        reply = f"Saved: {audio_file.name}\n\n{transcript_text}"
        await update.message.reply_text(reply, parse_mode=None)
    except Exception as e:
        await update.message.reply_text(f"Error: {type(e).__name__}: {e}", parse_mode=None)


async def handle_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming photo messages."""
    if not is_allowed_chat(update):
        return
    try:
        user = update.effective_user
        photo = update.message.photo[-1]  # Get largest photo
        caption = update.message.caption
        msg_date = update.message.date
        msg_id = update.message.message_id

        # Get the file path
        file = await photo.get_file()
        filename, description = await save_photo(file.file_path, user.id, user.username, caption, msg_date, msg_id)

        # Reply with description (no parse_mode to avoid "cannot parse entities" error)
        reply = f"Saved: {filename.name}\n\n{description[:500]}"  # Limit description length
        await update.message.reply_text(reply, parse_mode=None)
    except Exception as e:
        await update.message.reply_text(f"Error: {type(e).__name__}: {e}", parse_mode=None)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors and send details to chat."""
    import traceback
    error = context.error

    # Send error details to chat
    error_msg = f"Error: {type(error).__name__}: {error}"
    if update and update.effective_message:
        await update.effective_message.reply_text(error_msg)

    # Also print to console
    print(f"Error: {error}")
    traceback.print_exc()


async def process_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /process command - analyze inbox and update articles."""
    if not is_allowed_chat(update):
        return

    bot = context.bot
    chat_id = update.effective_chat.id

    await update.message.reply_text("Processing inbox with Claude... This may take a few minutes.")

    # Start timing
    start_time = time.time()

    # Create and start the message queue
    queue = MessageQueue(chat_id, bot, send_interval=20.0)
    await queue.start()

    try:
        # Start progress tracking mode - creates editable message
        await queue.start_progress()

        # Create Claude runner
        runner = ClaudeRunner(REPO_PATH, LOGS_DIR)

        # Progress callback - queues messages for periodic sending
        def queue_progress(msg: str):
            # Non-blocking queue put from synchronous context
            queue.put_sync(msg)

        # Run Claude in a thread so it doesn't block the event loop
        # This allows the queue worker to send messages during processing
        returncode, stdout, stderr = await asyncio.to_thread(
            runner.run_process_command,
            on_progress=queue_progress
        )

        # Finish progress tracking mode
        await queue.finish_progress()

        # Git push (with timeout to avoid hanging)
        print(f"[process_command] Starting git push...", flush=True)
        try:
            push_result = subprocess.run(
                ["git", "push"],
                cwd=REPO_PATH,
                capture_output=True,
                text=True,
                timeout=30  # 30 second timeout
            )
            print(f"[process_command] Git push return code: {push_result.returncode}")
            if push_result.stderr:
                print(f"[process_command] Git push stderr: {push_result.stderr}")
        except subprocess.TimeoutExpired:
            print(f"[process_command] Git push timed out after 30 seconds", flush=True)
            push_result = None
        except Exception as e:
            print(f"[process_command] Git push error: {e}", flush=True)
            push_result = None

        # Get GitHub commit URL
        print(f"[process_command] Getting commit hash...", flush=True)
        hash_result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_PATH,
            capture_output=True,
            text=True,
            timeout=5
        )
        commit_hash = hash_result.stdout.strip()
        print(f"[process_command] Commit hash: {commit_hash[:8]}", flush=True)

        # Get remote URL to construct GitHub link
        print(f"[process_command] Getting remote URL...", flush=True)
        remote_result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=REPO_PATH,
            capture_output=True,
            text=True,
            timeout=5
        )
        remote_url = remote_result.stdout.strip()

        # Convert git@github.com:user/repo.git to https://github.com/user/repo
        if remote_url.startswith("git@github.com:"):
            repo_url = remote_url[15:].removesuffix(".git")
            github_url = f"https://github.com/{repo_url}/commit/{commit_hash}"
        elif remote_url.startswith("https://github.com/"):
            repo_url = remote_url[19:].removesuffix(".git")
            github_url = f"https://github.com/{repo_url}/commit/{commit_hash}"
        else:
            github_url = None

        # First: stop queue and wait for all progress messages to be sent
        await queue.stop()
        print(f"[process_command] Queue stopped, now sending summary...", flush=True)

        # Now send the summary as a SEPARATE message
        if returncode == 0:
            # Calculate duration
            duration = time.time() - start_time
            duration_str = f"{int(duration // 60)}m {int(duration % 60)}s"

            msg = f"✅ Processing complete! Duration: {duration_str}\n\n"
            if github_url:
                msg += f"📦 Commit: {github_url}\n"
            else:
                msg += f"📦 Commit: `{commit_hash[:8]}`\n"

            # Add summary content
            summaries_dir = REPO_PATH / "inbox" / "summaries"
            print(f"[process_command] Checking summaries dir: {summaries_dir}", flush=True)
            summaries = sorted(summaries_dir.glob("summary_*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
            print(f"[process_command] Found {len(summaries)} summary files", flush=True)
            if summaries:
                latest_summary = summaries[0]
                print(f"[process_command] Reading summary: {latest_summary.name}", flush=True)
                with open(latest_summary, "r", encoding="utf-8") as f:
                    summary_content = f.read()
                # Truncate if too long (Telegram limit is 4096 chars)
                if len(summary_content) > 3800:
                    summary_content = summary_content[:3800] + "\n... (truncated)"
                msg += f"\n📊 Summary:\n\n{summary_content}"

            print(f"[process_command] Sending summary message ({len(msg)} chars)", flush=True)
            # Send summary as direct message (not through queue)
            await bot.send_message(chat_id=chat_id, text=msg, parse_mode=None)
            print(f"[process_command] Summary sent successfully", flush=True)
        else:
            print(f"[process_command] Claude failed with returncode {returncode}", flush=True)
            await bot.send_message(chat_id=chat_id, text=f"⚠️ Claude exited with code {returncode}", parse_mode=None)

        if stderr:
            await bot.send_message(chat_id=chat_id, text=f"Stderr: `{stderr[:1000]}`", parse_mode=None)

    except Exception as e:
        print(f"[process_command] Error: {type(e).__name__}: {e}")
        # Try to send error message
        try:
            await bot.send_message(chat_id=chat_id, text=f"Error: {type(e).__name__}: {e}", parse_mode=None)
        except:
            pass


def main() -> None:
    """Start the bot."""
    if not TELEGRAM_BOT_API_KEY:
        print("Error: TELEGRAM_BOT_API_KEY not found in .env")
        return

    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_API_KEY).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("process", process_command))

    # Register message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice_message))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo_message))

    # Register error handler
    application.add_error_handler(error_handler)

    # Start the bot (run_polling creates its own event loop)
    print(f"Bot running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
