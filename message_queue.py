"""Message queue for sending Telegram updates in batches to avoid rate limits."""

import asyncio
import sys


def _safe_print(msg: str):
    """Print that handles encoding errors on Windows."""
    try:
        print(msg, flush=True)
    except (UnicodeEncodeError, ValueError):
        # Fallback for Windows console encoding issues
        safe_msg = msg.encode('ascii', errors='replace').decode('ascii')
        print(safe_msg, flush=True)


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

    async def _send_message(self, msg: str) -> bool:
        """Send a single message, return True if successful."""
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=msg,
                parse_mode=None
            )
            _safe_print(f"[telegram poster] Sent batch ({len(msg)} chars)")
            return True
        except Exception as e:
            _safe_print(f"[telegram poster] Send error: {e}")
            return False

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
                    _safe_print(f"[telegram poster] Sending batch of {len(batch)} messages as ONE")

                    # Join all messages into one, separated by newlines
                    combined_message = "\n".join(batch)

                    # Telegram limit is 4096 chars, truncate if needed
                    if len(combined_message) > 4000:
                        combined_message = combined_message[:4000] + "\n... (truncated)"

                    # Send as ONE message
                    success = await self._send_message(combined_message)
                    if success:
                        self._total_sent += len(batch)

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
            _safe_print(f"[telegram poster] Sending {len(remaining)} final messages...")
            combined_message = "\n".join(remaining)
            if len(combined_message) > 4000:
                combined_message = combined_message[:4000] + "\n... (truncated)"
            await self._send_message(combined_message)
            self._total_sent += len(remaining)

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

    async def put(self, message: str):
        """Add a message to the queue (async)."""
        self._total_queued += 1
        async with self._lock:
            queue_size = len(self._messages)
            self._messages.append(message)
        _safe_print(f"[telegram poster] Queued (total: {self._total_queued}, queue: {queue_size}): {message[:50]}...")

    def put_sync(self, message: str):
        """Add a message to the queue from synchronous context."""
        self._total_queued += 1
        # Simple list append is atomic in CPython for simple appends
        # We rely on the GIL (Global Interpreter Lock) for thread safety here
        self._messages.append(message)
        queue_size = len(self._messages)
        _safe_print(f"[telegram poster] Queued (queue: {queue_size}): {message[:50]}...")
