"""Message queue for sending Telegram updates in batches to avoid rate limits."""

import asyncio
import queue as thread_queue


class MessageQueue:
    """Queues messages and sends them in batches periodically to avoid rate limits."""

    def __init__(self, chat_id: int, bot, send_interval: float = 5.0):
        self.chat_id = chat_id
        self.bot = bot
        # Use thread-safe queue so sync callbacks can add messages immediately
        self.queue: thread_queue.Queue[str] = thread_queue.Queue()
        self._task = None
        self._stop_event = asyncio.Event()
        # Initialize to current time to avoid long initial delay
        import time
        self._last_send_time = time.time()
        self._send_interval = send_interval
        self._total_queued = 0
        self._total_sent = 0

    async def _send_message(self, msg: str) -> bool:
        """Send a single message, return True if successful."""
        print(f"[telegram poster] >>> SENDING: {msg[:100]}...", flush=True)
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=msg,
                parse_mode=None
            )
            print(f"[telegram poster] >>> SENT OK ({len(msg)} chars)", flush=True)
            return True
        except Exception as e:
            print(f"[telegram poster] >>> SEND ERROR: {e}", flush=True)
            return False

    async def _worker(self):
        """Background worker that sends messages in batches periodically."""
        print(f"[telegram poster] Started, interval: {self._send_interval}s", flush=True)

        while not self._stop_event.is_set():
            try:
                # Wait for send interval
                current_time = asyncio.get_event_loop().time()
                time_since_last_send = current_time - self._last_send_time
                wait_time = max(0, self._send_interval - time_since_last_send)

                if wait_time > 0:
                    # Sleep in small increments to check for new messages
                    while wait_time > 0 and not self._stop_event.is_set():
                        sleep_time = min(0.5, wait_time)
                        await asyncio.sleep(sleep_time)
                        wait_time -= sleep_time

                # Check if we should stop
                if self._stop_event.is_set() and self.queue.empty():
                    break

                # Collect all currently queued messages into a batch
                batch = []
                while not self.queue.empty():
                    try:
                        msg = self.queue.get_nowait()
                        batch.append(msg)
                    except thread_queue.Empty:
                        break

                if batch:
                    queue_size = self.queue.qsize()
                    print(f"[telegram poster] Sending batch of {len(batch)} messages as ONE (queue: {queue_size} remaining)", flush=True)

                    # Join all messages into one, separated by newlines
                    combined_message = "\n".join(batch)

                    # Telegram limit is 4096 chars, truncate if needed
                    if len(combined_message) > 4000:
                        combined_message = combined_message[:4000] + "\n... (truncated)"

                    # Send as ONE message
                    success = await self._send_message(combined_message)
                    if success:
                        self._total_sent += len(batch)

                    self._last_send_time = asyncio.get_event_loop().time()

            except Exception as e:
                print(f"[telegram poster] Worker error: {e}", flush=True)

        print(f"[telegram poster] Stopped. Total sent: {self._total_sent}", flush=True)

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
                print(f"[telegram poster] Worker timeout", flush=True)

        # Send any remaining messages
        remaining = []
        while not self.queue.empty():
            try:
                remaining.append(self.queue.get_nowait())
            except thread_queue.Empty:
                break

        if remaining:
            print(f"[telegram poster] Sending {len(remaining)} final messages...", flush=True)
            combined_message = "\n".join(remaining)
            if len(combined_message) > 4000:
                combined_message = combined_message[:4000] + "\n... (truncated)"
            await self._send_message(combined_message)
            self._total_sent += len(remaining)

    async def put(self, message: str):
        """Add a message to the queue (async)."""
        self._total_queued += 1
        queue_size = self.queue.qsize()
        print(f"[telegram poster] Queued (total: {self._total_queued}, queue: {queue_size}): {message[:50]}...", flush=True)
        await asyncio.to_thread(self.queue.put, message)

    def put_sync(self, message: str):
        """Add a message to the queue from synchronous context."""
        self._total_queued += 1
        queue_size = self.queue.qsize()
        print(f"[telegram poster] Queued SYNC (total: {self._total_queued}, queue: {queue_size}): {message[:50]}...", flush=True)
        # Thread-safe put - works immediately from sync context!
        self.queue.put(message)
