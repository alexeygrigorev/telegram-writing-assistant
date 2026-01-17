import asyncio
import base64
import os
import subprocess
import textwrap
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

# Load environment variables
load_dotenv()


class MessageQueue:
    """Queues messages and sends them periodically to avoid rate limits."""

    def __init__(self, chat_id: int, bot):
        self.chat_id = chat_id
        self.bot = bot
        self.queue: asyncio.Queue = asyncio.Queue()
        self._task = None
        self._stop_event = asyncio.Event()
        self._last_send_time = 0
        self._send_interval = 3.0  # Minimum seconds between sends

    async def _worker(self):
        """Background worker that sends messages periodically."""
        while not self._stop_event.is_set():
            try:
                # Wait for a message or the stop event
                msg = await asyncio.wait_for(
                    self.queue.get(),
                    timeout=1.0
                )

                # Calculate remaining wait time
                current_time = asyncio.get_event_loop().time()
                time_since_last_send = current_time - self._last_send_time
                wait_time = max(0, self._send_interval - time_since_last_send)

                if wait_time > 0:
                    await asyncio.sleep(wait_time)

                # Check if we were stopped while waiting
                if self._stop_event.is_set():
                    # Put message back and exit
                    self.queue.put_nowait(msg)
                    break

                # Send the message
                try:
                    await self.bot.send_message(
                        chat_id=self.chat_id,
                        text=msg,
                        parse_mode="Markdown"
                    )
                    self._last_send_time = asyncio.get_event_loop().time()
                except Exception as e:
                    print(f"[MessageQueue] Failed to send: {e}", flush=True)
                    # Re-queue for retry
                    self.queue.put_nowait(msg)

                self.queue.task_done()
            except asyncio.TimeoutError:
                # No message, continue loop
                continue
            except Exception as e:
                print(f"[MessageQueue] Worker error: {e}", flush=True)

    async def start(self):
        """Start the background worker."""
        if self._task is None or self._task.done():
            self._stop_event.clear()
            self._task = asyncio.create_task(self._worker())

    async def stop(self):
        """Stop the worker and drain the queue."""
        self._stop_event.set()
        if self._task and not self._task.done():
            await asyncio.wait_for(self._task, timeout=5.0)

        # Send any remaining messages
        while not self.queue.empty():
            msg = self.queue.get_nowait()
            try:
                await self.bot.send_message(
                    chat_id=self.chat_id,
                    text=msg,
                    parse_mode="Markdown"
                )
                await asyncio.sleep(self._send_interval)
            except Exception as e:
                print(f"[MessageQueue] Failed to send final message: {e}", flush=True)
            self.queue.task_done()

    async def put(self, message: str):
        """Add a message to the queue."""
        await self.queue.put(message)


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


async def save_text_message(content: str, user_id: int, username: str = None, message_date: datetime = None) -> Path:
    """Save text message as markdown file."""
    msg_date = message_date or datetime.now()
    timestamp = get_timestamp(msg_date)
    user_tag = username or f"user_{user_id}"
    filename = INBOX_RAW / f"{timestamp}_{user_tag}.md"

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


async def save_voice_message(file_path: str, user_id: int, username: str = None, message_date: datetime = None) -> tuple[Path, Path, str]:
    """Save voice message file and transcribe it."""
    msg_date = message_date or datetime.now()
    timestamp = get_timestamp(msg_date)
    user_tag = username or f"user_{user_id}"

    # Download and save the audio file
    audio_filename = INBOX_RAW / f"{timestamp}_{user_tag}.ogg"
    transcription_filename = INBOX_RAW / f"{timestamp}_{user_tag}_transcript.txt"

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


async def save_photo(file_path: str, user_id: int, username: str = None, caption: str = None, message_date: datetime = None) -> tuple[Path, str]:
    """Save photo to inbox/raw and return (filename, description)."""
    msg_date = message_date or datetime.now()
    timestamp = get_timestamp(msg_date)
    user_tag = username or f"user_{user_id}"
    # Save image in inbox/raw alongside its markdown description
    filename = INBOX_RAW / f"{timestamp}_{user_tag}.jpg"

    async with httpx.AsyncClient() as client:
        response = await client.get(file_path)
        with open(filename, "wb") as f:
            f.write(response.content)

    # Generate image description
    description = describe_image(filename)

    # Create markdown with description (image is in the same folder)
    md_filename = INBOX_RAW / f"{timestamp}_{user_tag}_photo.md"
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

        filename = await save_text_message(text, user.id, user.username, msg_date)
        await update.message.reply_text(f"Saved as `{filename.name}`", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"Error: {type(e).__name__}: {e}", parse_mode="Markdown")


async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming voice messages."""
    if not is_allowed_chat(update):
        return
    try:
        user = update.effective_user
        voice = update.message.voice
        msg_date = update.message.date

        # Get the file path
        file = await voice.get_file()
        audio_file, transcript_file, transcript_text = await save_voice_message(file.file_path, user.id, user.username, msg_date)

        # Send transcript to chat
        reply = f"Saved: `{audio_file.name}`\n\n{transcript_text}"
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"Error: {type(e).__name__}: {e}", parse_mode="Markdown")


async def handle_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming photo messages."""
    if not is_allowed_chat(update):
        return
    try:
        user = update.effective_user
        photo = update.message.photo[-1]  # Get largest photo
        caption = update.message.caption
        msg_date = update.message.date

        # Get the file path
        file = await photo.get_file()
        filename, description = await save_photo(file.file_path, user.id, user.username, caption, msg_date)

        # Reply with description
        reply = f"Saved: `{filename.name}`\n\n{description}"
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"Error: {type(e).__name__}: {e}", parse_mode="Markdown")


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

    # Create and start the message queue
    queue = MessageQueue(chat_id, bot)
    await queue.start()

    try:
        # Create Claude runner
        runner = ClaudeRunner(REPO_PATH, LOGS_DIR)

        # Progress callback - queues messages for periodic sending
        def queue_progress(msg: str):
            # Non-blocking queue put from synchronous context
            asyncio.create_task(queue.put(msg))

        # Run Claude with progress streaming
        returncode, stdout, stderr = runner.run_process_command(
            on_progress=queue_progress
        )

        # Git push
        push_result = subprocess.run(
            ["git", "push"],
            cwd=REPO_PATH,
            capture_output=True,
            text=True
        )
        print(f"[process_command] Git push return code: {push_result.returncode}")
        if push_result.stderr:
            print(f"[process_command] Git push stderr: {push_result.stderr}")

        # Get GitHub commit URL
        hash_result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_PATH,
            capture_output=True,
            text=True
        )
        commit_hash = hash_result.stdout.strip()

        # Get remote URL to construct GitHub link
        remote_result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=REPO_PATH,
            capture_output=True,
            text=True
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

        # Send results to chat
        if returncode == 0:
            msg = f"✅ Processing complete!\n\n"
            if github_url:
                msg += f"📦 Commit: {github_url}\n"
            else:
                msg += f"📦 Commit: `{commit_hash[:8]}`\n"
            await queue.put(msg)

            # Send summary content
            summaries_dir = REPO_PATH / "inbox" / "summaries"
            summaries = sorted(summaries_dir.glob("summary_*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
            if summaries:
                latest_summary = summaries[0]
                with open(latest_summary, "r", encoding="utf-8") as f:
                    summary_content = f.read()
                # Truncate if too long (Telegram limit is 4096 chars)
                if len(summary_content) > 4000:
                    summary_content = summary_content[:4000] + "\n... (truncated)"
                await queue.put(f"📊 Summary:\n\n{summary_content}")
        else:
            await queue.put(f"⚠️ Claude exited with code {returncode}")

        if stderr:
            await queue.put(f"Stderr: `{stderr[:1000]}`")

    except Exception as e:
        print(f"[process_command] Error: {type(e).__name__}: {e}")
        await queue.put(f"Error during processing: {type(e).__name__}: {e}")

    finally:
        # Stop queue and drain remaining messages
        await queue.stop()


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
