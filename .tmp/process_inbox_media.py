import base64
import os
import textwrap
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Configuration
REPO_PATH = Path.cwd()
INBOX_RAW = REPO_PATH / "inbox" / "raw"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)


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


def transcribe_audio(audio_path: Path) -> str:
    """Transcribe audio using Groq Whisper."""
    with open(audio_path, "rb") as audio_file:
        transcription = groq_client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="text"
        )
        return transcription.strip()


def process_image(image_path: Path) -> None:
    """Process an image file and generate description."""
    if image_path.name.startswith('.'):
        return

    # Check if photo.md already exists
    md_path = image_path.with_suffix('').with_name(f"{image_path.stem}_photo.md")
    if md_path.exists():
        print(f"  Skipping {image_path.name} - description already exists")
        return

    print(f"  Processing {image_path.name}...")

    try:
        # Generate description
        description = describe_image(image_path)

        # Parse filename to get metadata
        # Format: YYYYMMDD_HHMMSS_USERNAME_msg###.jpg
        parts = image_path.stem.split('_')
        if len(parts) >= 3:
            date_str = parts[0]
            time_str = parts[1]
            username = parts[2]
            msg_id = parts[3] if len(parts) > 3 else ""

            try:
                msg_date = datetime.strptime(f"{date_str}{time_str}", "%Y%m%d%H%M%S")
            except:
                msg_date = datetime.now()

            # Create markdown description file
            content_lines = [
                "---",
                f"source: telegram_photo",
                f"date: {msg_date.isoformat()}",
                f"user_id: unknown",
                f"username: {username}",
                f"image_file: {image_path.name}",
                "---",
                "",
                description,
            ]
            content = "\n".join(content_lines)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"    Created {md_path.name}")
        else:
            print(f"  Could not parse filename: {image_path.name}")
    except Exception as e:
        print(f"  Error processing {image_path.name}: {e}")


def process_audio(audio_path: Path) -> None:
    """Process an audio file and transcribe it."""
    if audio_path.name.startswith('.'):
        return

    # Check if transcript already exists
    transcript_path = audio_path.with_suffix('').with_name(f"{audio_path.stem}_transcript.txt")
    if transcript_path.exists():
        print(f"  Skipping {audio_path.name} - transcript already exists")
        return

    print(f"  Processing {audio_path.name}...")

    try:
        # Transcribe
        transcript = transcribe_audio(audio_path)

        # Parse filename to get metadata
        # Format: YYYYMMDD_HHMMSS_USERNAME_msg###.ogg
        parts = audio_path.stem.split('_')
        if len(parts) >= 3:
            date_str = parts[0]
            time_str = parts[1]
            username = parts[2]

            try:
                msg_date = datetime.strptime(f"{date_str}{time_str}", "%Y%m%d%H%M%S")
            except:
                msg_date = datetime.now()

            # Create metadata
            metadata = "\n".join([
                "---",
                "source: telegram_voice",
                f"date: {msg_date.isoformat()}",
                f"user_id: unknown",
                f"username: {username}",
                f"audio_file: {audio_path.name}",
                "---",
                "",
                ""
            ])

            # Wrap transcript text at 100 chars for readability
            wrapped_transcript = textwrap.fill(transcript, width=100)

            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(metadata + wrapped_transcript)

            # Delete the .ogg file
            audio_path.unlink()
            print(f"    Created {transcript_path.name}, deleted {audio_path.name}")
        else:
            print(f"  Could not parse filename: {audio_path.name}")
    except Exception as e:
        print(f"  Error processing {audio_path.name}: {e}")


def main():
    """Process all images and audio files in inbox/raw."""
    print("Processing media files in inbox/raw...")

    # Process images
    print("\n=== Processing Images ===")
    images = sorted(INBOX_RAW.glob("*.jpg"))
    print(f"Found {len(images)} image(s)")
    for img in images:
        process_image(img)

    # Process audio
    print("\n=== Processing Audio ===")
    audio_files = sorted(INBOX_RAW.glob("*.ogg"))
    print(f"Found {len(audio_files)} audio file(s)")
    for audio in audio_files:
        process_audio(audio)

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
