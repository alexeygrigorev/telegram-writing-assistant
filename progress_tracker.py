"""Progress tracker for displaying Claude operations in Telegram."""

import asyncio
import re
from collections import defaultdict


def _safe_print(msg: str):
    """Print that handles encoding errors on Windows."""
    try:
        print(msg, flush=True)
    except (UnicodeEncodeError, ValueError):
        safe_msg = msg.encode('ascii', errors='replace').decode('ascii')
        print(safe_msg, flush=True)


class ProgressTracker:
    """Tracks and displays progress in a single editable Telegram message.

    This class parses Claude progress messages and formats them into a clean,
    collapsible display.
    """

    # Maximum visible commands before collapsing
    MAX_VISIBLE = 7

    # Emojis for different operations
    EMOJI_READ = "📖"
    EMOJI_FOUND = "🔍"
    EMOJI_EDIT = "✏️"
    EMOJI_WRITE = "✍️"
    EMOJI_RUNNING = "💻"
    EMOJI_ERROR = "❌"

    def __init__(self, bot, chat_id: int):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = None
        self.commands = []  # List of (emoji, text) tuples
        self.counters = defaultdict(int)  # Track operation counts
        self._dedup_cache = {}  # For consolidating consecutive similar operations
        self._loop: asyncio.AbstractEventLoop | None = None

    async def start(self):
        """Create initial progress message and store event loop."""
        self._loop = asyncio.get_event_loop()
        message = await self.bot.send_message(
            chat_id=self.chat_id,
            text="⏳ Processing...",
            parse_mode="Markdown"
        )
        if message:
            self.message_id = message.message_id
            _safe_print("[ProgressTracker] Started")
        return self.message_id is not None

    def add_message(self, message: str):
        """Add a progress message (thread-safe).

        This can be called from any thread (e.g., via asyncio.to_thread).
        """
        emoji, text, category = self._parse_message(message)
        if self._loop is not None:
            asyncio.run_coroutine_threadsafe(
                self.add_command(emoji, text, category),
                self._loop
            )

    async def add_command(self, emoji: str, text: str, category: str = None):
        """Add a command and update the message."""
        # Update counters
        if category:
            self.counters[category] += 1

        # Deduplication: skip consecutive operations on the same target
        if category in ("read", "edit", "write"):
            # Extract filename pattern for deduplication
            match = re.search(r'`([^`]+\.\w+)`', text)
            if match:
                key = (category, match.group(1))
                # Skip if we just did this same operation on this file
                if key in self._dedup_cache:
                    return
                self._dedup_cache[key] = True
        else:
            # Clear cache for non-file operations
            self._dedup_cache.clear()

        # Store command
        self.commands.append((emoji, text))

        # Update message
        await self._update_message()

    async def finish(self):
        """Mark as complete and do final update."""
        if self.message_id:
            await self._update_message(done=True)
            _safe_print(f"[ProgressTracker] Finished ({len(self.commands)} commands)")

    def _parse_message(self, message: str) -> tuple[str, str, str | None]:
        """Parse a progress message into emoji, text, and category.

        Returns:
            (emoji, text_without_emoji, category)
        """
        # Common patterns from ClaudeProgressFormatter
        patterns = [
            (r"📖 Read: (.*)", self.EMOJI_READ, "read"),
            (r"✅ Read: (.*)", self.EMOJI_READ, "read"),
            (r"🔍 Finding: (.*)", self.EMOJI_FOUND, "found"),
            (r"🔍 Found: (.*)", self.EMOJI_FOUND, "found"),
            (r"✏️  Editing: (.*)", self.EMOJI_EDIT, "edit"),
            (r"✍️  Writing: (.*)", self.EMOJI_WRITE, "write"),
            (r"💻 Running: (.*)", self.EMOJI_RUNNING, None),
            (r"⚠️ (.*)", self.EMOJI_ERROR, "error"),
        ]

        for pattern, emoji, category in patterns:
            match = re.match(pattern, message)
            if match:
                return emoji, match.group(1), category

        # Unknown pattern - try to extract emoji
        emoji = ""
        text = message
        if message and message[0] in ("📖", "🔍", "✏️", "✍️", "💻", "❌"):
            emoji = message[0] + message[1] if len(message) > 1 and ord(message[1]) > 127 else message[0]
            text = message[len(emoji):].strip()

        return emoji, text, None

    def _format_message(self, done: bool = False) -> str:
        """Format the progress message with collapsed history."""
        status = "✅ Done" if done else "⏳ Processing..."

        # Calculate what to show vs collapse
        total = len(self.commands)
        if total > self.MAX_VISIBLE:
            hidden = total - self.MAX_VISIBLE
            visible_commands = self.commands[-self.MAX_VISIBLE:]
            collapse_text = f"\n_({hidden} earlier commands hidden)_\n"
        else:
            visible_commands = self.commands
            collapse_text = ""

        # Format visible commands
        command_lines = []
        for emoji, text in visible_commands:
            # Escape special markdown chars for inline code
            text = self._escape_markdown(text)
            command_lines.append(f"{emoji} {text}")

        # Add counters summary at top
        counter_lines = []
        if self.counters.get("read", 0) > 1:
            counter_lines.append(f"{self.EMOJI_READ} Read {self.counters['read']} files")
        if self.counters.get("edit", 0) > 1:
            counter_lines.append(f"{self.EMOJI_EDIT} Edited {self.counters['edit']} files")
        if self.counters.get("found", 0) > 1:
            counter_lines.append(f"{self.EMOJI_FOUND} Found {self.counters['found']} items")

        summary = "\n".join(counter_lines)
        if summary:
            summary += "\n\n"

        return f"{status}\n\n{summary}{collapse_text}" + "\n".join(command_lines)

    @staticmethod
    def _escape_markdown(text: str) -> str:
        """Escape special markdown characters, but not inside backticks."""
        # Characters that need escaping in Telegram Markdown
        to_escape = ['*', '_', '[']

        result = []
        i = 0
        while i < len(text):
            # Check if we're inside backticks (code span)
            if text[i] == '`':
                # Find the closing backtick
                j = text.find('`', i + 1)
                if j == -1:
                    # No closing backtick, treat rest as literal
                    result.append(text[i:])
                    break
                # Don't escape anything inside backticks
                result.append(text[i:j+1])
                i = j + 1
            else:
                # Escape special characters outside backticks
                if text[i] in to_escape:
                    result.append('\\' + text[i])
                else:
                    result.append(text[i])
                i += 1

        return ''.join(result)

    async def _update_message(self, done: bool = False):
        """Update the progress message."""
        if not self.message_id:
            return

        formatted = self._format_message(done)

        # Telegram limit is 4096 chars
        if len(formatted) > 4000:
            formatted = formatted[:4000] + "\n... (truncated)"

        try:
            await self.bot.edit_message_text(
                chat_id=self.chat_id,
                message_id=self.message_id,
                text=formatted,
                parse_mode="Markdown"
            )
        except Exception as e:
            # Silently fail on edit errors (e.g., message not modified)
            _safe_print(f"[ProgressTracker] Edit error: {e}")
