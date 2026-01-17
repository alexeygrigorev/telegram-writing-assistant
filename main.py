import asyncio
import base64
import os
import subprocess
import textwrap
from datetime import datetime
from pathlib import Path
from uuid import uuid4

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
        Analyze this image and provide:
        1. Type: screenshot, photo, terminal, code, diagram, document, etc.
        2. Main content: what is shown
        3. Text: any visible text (OCR if present)
        4. Context: what this might be useful for

        Be concise. Format as: "Type: [type]. Content: [description]."")
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
    return response.choices[0].message.content.strip()


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

    metadata = textwrap.dedent(f"""\
        ---
        source: telegram
        date: {msg_date.isoformat()}
        user_id: {user_id}
        username: {username or "unknown"}
        ---

        """)
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

    metadata = textwrap.dedent(f"""\
        ---
        source: telegram_voice
        date: {msg_date.isoformat()}
        user_id: {user_id}
        username: {username or "unknown"}
        audio_file: {audio_filename.name}
        ---

        """)
    with open(transcription_filename, "w", encoding="utf-8") as f:
        f.write(metadata + transcript_text)

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
    content = textwrap.dedent(f"""\
        ---
        source: telegram_photo
        date: {msg_date.isoformat()}
        user_id: {user_id}
        username: {username or "unknown"}
        image_file: {filename.name}
        ---

        {description}
        """)
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
    await update.message.reply_text("Processing inbox with Claude... This may take a few minutes.")

    try:
        # Create log file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = LOGS_DIR / f"run_{timestamp}.json"
        LOGS_DIR.mkdir(parents=True, exist_ok=True)

        # Run Claude Code with the custom process command in non-interactive mode
        cmd = "claude -p \"read and execute instructions in .claude/commands/process.md\" --allowedTools \"Read,Edit,Bash,Write\" --output-format stream-json --verbose"
        print(f"[process_command] Running: {cmd}", flush=True)

        # Import for JSON parsing
        import json
        import io

        process = subprocess.Popen(
            cmd,
            cwd=REPO_PATH,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace',
            shell=True,
            bufsize=1
        )

        # Collect output for log file
        output_buffer = io.StringIO()

        # Track last progress message to avoid spam
        last_progress_time = None
        progress_messages = []

        # Stream stdout line by line
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue

            # Write to log
            output_buffer.write(line + "\n")

            # Try to parse as JSON event
            try:
                event = json.loads(line)

                # Format and send progress updates
                progress_msg = None

                if event.get("type") == "system":
                    subtype = event.get("subtype", "")
                    if subtype == "init":
                        model = event.get("model", "unknown")
                        print(f"[SYSTEM] Session started - Model: {model}", flush=True)

                elif event.get("type") == "assistant":
                    message = event.get("message", {})
                    content_list = message.get("content", [])

                    for content in content_list:
                        if content.get("type") == "tool_use":
                            tool_name = content.get("name", "unknown")
                            tool_input = content.get("input", {})

                            if tool_name == "Read":
                                file_path = tool_input.get("file_path", "?")
                                progress_msg = f"📖 Reading: `{Path(file_path).name}`"
                                print(f"[CLAUDE] {progress_msg}", flush=True)
                            elif tool_name == "Write":
                                file_path = tool_input.get("file_path", "?")
                                progress_msg = f"✍️  Writing: `{Path(file_path).name}`"
                                print(f"[CLAUDE] {progress_msg}", flush=True)
                            elif tool_name == "Edit":
                                file_path = tool_input.get("file_path", "?")
                                progress_msg = f"✏️  Editing: `{Path(file_path).name}`"
                                print(f"[CLAUDE] {progress_msg}", flush=True)
                            elif tool_name == "Bash":
                                cmd_text = tool_input.get("command", "")[:60]
                                progress_msg = f"💻 Running: `{cmd_text}...`"
                                print(f"[CLAUDE] {progress_msg}", flush=True)
                            elif tool_name == "TodoWrite":
                                todos = tool_input.get("todos", [])
                                in_progress = sum(1 for t in todos if t.get("status") == "in_progress")
                                progress_msg = f"📋 Progress: {in_progress}/{len(todos)} tasks active"
                                print(f"[CLAUDE] {progress_msg}", flush=True)
                            elif tool_name == "Glob":
                                pattern = tool_input.get("pattern", "?")
                                print(f"[CLAUDE] 🔍 Finding: {pattern}", flush=True)

                        elif content.get("type") == "text":
                            text = content.get("text", "")
                            if text:
                                print(f"[CLAUDE] 💬 {text[:200]}...", flush=True)

                elif event.get("type") == "user":
                    tool_use_result = event.get("tool_use_result", {})

                    if tool_use_result:
                        result_type = tool_use_result.get("type", "")

                        if result_type == "text":
                            file_info = tool_use_result.get("file", {})
                            if file_info:
                                file_path = file_info.get("filePath", "")
                                num_lines = file_info.get("numLines", 0)
                                progress_msg = f"✅ Read: `{Path(file_path).name}` ({num_lines} lines)"
                                print(f"[RESULT] {progress_msg}", flush=True)

                        elif tool_use_result.get("filenames"):
                            filenames = tool_use_result.get("filenames", [])
                            num_files = tool_use_result.get("numFiles", len(filenames))
                            progress_msg = f"✅ Found: {num_files} files"
                            print(f"[RESULT] {progress_msg}", flush=True)

                # Send progress to Telegram (with rate limiting - max 1 message per 2 seconds)
                if progress_msg:
                    import time
                    current_time = time.time()
                    if last_progress_time is None or (current_time - last_progress_time) > 2:
                        try:
                            await update.message.reply_text(progress_msg, parse_mode="Markdown")
                            last_progress_time = current_time
                            progress_messages.append(progress_msg)
                        except Exception as e:
                            print(f"[process_command] Failed to send progress: {e}", flush=True)

            except json.JSONDecodeError:
                # Not JSON, just print raw line
                print(f"[RAW] {line[:100]}", flush=True)

        # Wait for process to complete
        process.wait()
        returncode = process.returncode

        # Get any stderr
        stderr_output = process.stderr.read()

        print(f"\n[process_command] Return code: {returncode}", flush=True)
        print(f"[process_command] Log saved to: {log_file}", flush=True)
        if stderr_output:
            print(f"[process_command] Stderr:\n{stderr_output}", flush=True)

        # Save output to log file
        full_output = output_buffer.getvalue()
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(full_output)

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
            await update.message.reply_text(msg, parse_mode="Markdown")

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
                await update.message.reply_text(f"📊 Summary:\n\n{summary_content}", parse_mode="Markdown")
        else:
            await update.message.reply_text(f"⚠️ Claude exited with code {returncode}", parse_mode="Markdown")

        if stderr_output:
            await update.message.reply_text(f"Stderr: `{stderr_output[:1000]}`", parse_mode="Markdown")

    except Exception as e:
        print(f"[process_command] Error: {type(e).__name__}: {e}")
        await update.message.reply_text(f"Error during processing: {type(e).__name__}: {e}")


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
