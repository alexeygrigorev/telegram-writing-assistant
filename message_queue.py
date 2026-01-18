"""Message queue for sending Telegram updates in batches to avoid rate limits."""

import asyncio
import re
import sys
from collections import defaultdict


def _safe_print(msg: str):
    """Print that handles encoding errors on Windows."""
    try:
        print(msg, flush=True)
    except (UnicodeEncodeError, ValueError):
        # Fallback for Windows console encoding issues
        safe_msg = msg.encode('ascii', errors='replace').decode('ascii')
        print(safe_msg, flush=True)


class ProgressTracker:
    """Tracks and displays progress in a single editable Telegram message."""

    # Maximum visible commands before collapsing
    MAX_VISIBLE = 15

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

    async def start(self):
        """Create initial progress message."""
        message = await self.bot.send_message(
            chat_id=self.chat_id,
            text="⏳ Working...",
            parse_mode="Markdown"
        )
        if message:
            # python-telegram-bot v20+ returns a Message object
            self.message_id = message.message_id
            _safe_print("[progress tracker] Started")
        return self.message_id is not None

    async def add_command(self, emoji: str, text: str, category: str = None):
        """Add a command and update the message."""
        # Update counters
        if category:
            self.counters[category] += 1

        # Deduplication: consolidate consecutive reads of files
        if category == "read":
            # Extract filename pattern for deduplication
            match = re.search(r'(\S+\.\w+)', text)
            if match:
                key = ("read", match.group(1))
                # Skip if we just read this same file
                if key in self._dedup_cache:
                    return
                self._dedup_cache[key] = True
        else:
            # Clear cache for non-read operations
            self._dedup_cache.clear()

        # Store command
        self.commands.append((emoji, text))

        # Update message
        await self._update_message()

    async def finish(self):
        """Mark as complete and do final update."""
        if self.message_id:
            await self._update_message(done=True)
            _safe_print(f"[progress tracker] Finished ({len(self.commands)} commands)")

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
        """Escape special markdown characters."""
        # Only escape characters that would break markdown
        # Don't escape backticks so code formatting works
        to_escape = ['*', '_', '[']
        for char in to_escape:
            text = text.replace(char, '\\' + char)
        return text

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
            _safe_print(f"[progress tracker] Edit error: {e}")


class MessageQueue:
    """Queues messages and sends them in batches periodically to avoid rate limits."""

    def __init__(self, chat_id: int, bot, send_interval: float = 5.0):
        self.chat_id = chat_id
        self.bot = bot
        # Use simple list with asyncio lock instead of queue.Queue
        # queue.Queue has mutex issues in async contexts on Windows
        self._messages = []
        self._lock = asyncio.Lock()
        self._task = None
        self._stop_event = asyncio.Event()
        # Will be set to loop time when worker starts
        # We can't use loop.time() here because we don't have a running event loop
        self._last_send_time = None
        self._send_interval = send_interval
        self._total_queued = 0
        self._total_sent = 0
        # Progress tracker mode
        self._progress_tracker: ProgressTracker | None = None

    async def _worker(self):
        """Background worker that sends messages in batches periodically."""
        _safe_print(f"[telegram poster] Started, interval: {self._send_interval}s")

        # Get the event loop and use its time consistently
        loop = asyncio.get_event_loop()
        # Initialize to current loop time so first send happens after send_interval
        self._last_send_time = loop.time()

        while not self._stop_event.is_set():
            try:
                # Use loop.time() consistently (same time source)
                current_time = loop.time()
                time_since_last_send = current_time - self._last_send_time
                wait_time = max(0, self._send_interval - time_since_last_send)

                if wait_time > 0:
                    # Sleep in small increments to check for new messages
                    while wait_time > 0 and not self._stop_event.is_set():
                        sleep_time = min(0.5, wait_time)
                        await asyncio.sleep(sleep_time)
                        wait_time -= sleep_time

                # Check if we should stop
                if self._stop_event.is_set():
                    async with self._lock:
                        if not self._messages:
                            break
                        # Process remaining messages and exit
                        batch = list(self._messages)
                        self._messages.clear()
                else:
                    # Collect all currently queued messages into a batch
                    async with self._lock:
                        batch = list(self._messages)
                        self._messages.clear()

                if batch:
                    # Join all messages into one, separated by newlines
                    combined_message = "\n".join(batch)

                    # Telegram limit is 4096 chars, truncate if needed
                    if len(combined_message) > 4000:
                        combined_message = combined_message[:4000] + "\n... (truncated)"

                    # Send as ONE message
                    success = await self.bot.send_message(
                        chat_id=self.chat_id,
                        text=combined_message,
                        parse_mode=None
                    )
                    if success:
                        self._total_sent += len(batch)
                        _safe_print(f"[telegram poster] Sent batch of {len(batch)} messages ({len(combined_message)} chars)")

                    # Use loop.time() consistently
                    self._last_send_time = loop.time()
                else:
                    # No messages to send - sleep a bit to avoid tight loop
                    # This is critical for stop() to get a chance to run
                    await asyncio.sleep(0.1)

            except Exception as e:
                _safe_print(f"[telegram poster] Worker error: {e}")

        _safe_print(f"[telegram poster] Worker loop ended. Total sent: {self._total_sent}")

        # Send any remaining messages before exiting
        async with self._lock:
            remaining = list(self._messages)
            self._messages.clear()

        if remaining:
            combined_message = "\n".join(remaining)
            if len(combined_message) > 4000:
                combined_message = combined_message[:4000] + "\n... (truncated)"
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=combined_message,
                parse_mode=None
            )
            self._total_sent += len(remaining)
            _safe_print(f"[telegram poster] Sent {len(remaining)} final messages ({len(combined_message)} chars)")

        _safe_print(f"[telegram poster] Stopped. Total sent: {self._total_sent}")

    async def start(self):
        """Start the background worker."""
        if self._task is None or self._task.done():
            self._stop_event.clear()
            self._task = asyncio.create_task(self._worker())

    async def stop(self):
        """Stop the worker and wait for all messages to be sent."""
        self._stop_event.set()
        if self._task and not self._task.done():
            try:
                await asyncio.wait_for(self._task, timeout=30.0)
            except asyncio.TimeoutError:
                _safe_print("[telegram poster] Worker timeout")
        # Worker handles sending remaining messages before exiting

    async def start_progress(self):
        """Start progress tracking mode."""
        if self._progress_tracker is None:
            self._progress_tracker = ProgressTracker(self.bot, self.chat_id)
            return await self._progress_tracker.start()
        return True

    async def finish_progress(self):
        """Finish progress tracking mode."""
        if self._progress_tracker:
            await self._progress_tracker.finish()
            self._progress_tracker = None

    def _parse_progress_message(self, message: str) -> tuple[str, str, str | None]:
        """Parse a progress message into emoji, text, and category.

        Returns:
            (emoji, text_without_emoji, category)
        """
        # Common patterns from ClaudeProgressFormatter
        patterns = [
            (r"📖 Read: (.*)", ProgressTracker.EMOJI_READ, "read"),
            (r"✅ Read: (.*)", ProgressTracker.EMOJI_READ, "read"),  # Old pattern for compatibility
            (r"🔍 Finding: (.*)", ProgressTracker.EMOJI_FOUND, "found"),
            (r"🔍 Found: (.*)", ProgressTracker.EMOJI_FOUND, "found"),
            (r"✏️  Editing: (.*)", ProgressTracker.EMOJI_EDIT, "edit"),
            (r"✍️  Writing: (.*)", ProgressTracker.EMOJI_WRITE, "write"),
            (r"💻 Running: (.*)", ProgressTracker.EMOJI_RUNNING, None),
            (r"⚠️ (.*)", ProgressTracker.EMOJI_ERROR, "error"),
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

    async def put(self, message: str):
        """Add a message to the queue (async)."""
        self._total_queued += 1

        # If progress tracker is active, route through it
        if self._progress_tracker:
            emoji, text, category = self._parse_progress_message(message)
            await self._progress_tracker.add_command(emoji, text, category)
            return

        async with self._lock:
            self._messages.append(message)

    def put_sync(self, message: str):
        """Add a message to the queue from synchronous context."""
        self._total_queued += 1

        # If progress tracker is active, route through it (create task)
        if self._progress_tracker:
            emoji, text, category = self._parse_progress_message(message)
            # Schedule async call on the running loop
            loop = asyncio.get_event_loop()
            asyncio.create_task(self._progress_tracker.add_command(emoji, text, category))
            return

        # Simple list append is atomic in CPython for simple appends
        # We rely on the GIL (Global Interpreter Lock) for thread safety here
        self._messages.append(message)
