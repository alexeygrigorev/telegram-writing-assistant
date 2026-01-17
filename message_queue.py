"""Message queue for sending Telegram updates in batches to avoid rate limits."""

import asyncio


class MessageQueue:
    """Queues messages and sends them in batches periodically to avoid rate limits."""

    def __init__(self, chat_id: int, bot, send_interval: float = 5.0):
        self.chat_id = chat_id
        self.bot = bot
        self.queue: asyncio.Queue[str] = asyncio.Queue()
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
        # Try with markdown first
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=msg,
                parse_mode="Markdown"
            )
            print(f"[telegram poster] >>> SENT OK", flush=True)
            return True
        except Exception as e:
            error_str = str(e)
            print(f"[telegram poster] >>> SEND ERROR: {e}", flush=True)
            # If it's a parse error, try without markdown
            if "parse" in error_str.lower() or "entity" in error_str.lower():
                try:
                    await self.bot.send_message(
                        chat_id=self.chat_id,
                        text=msg,
                        parse_mode=None
                    )
                    print(f"[telegram poster] >>> SENT OK (no markdown)", flush=True)
                    return True
                except Exception as e2:
                    print(f"[telegram poster] Failed (no markdown): {e2}", flush=True)
                    return False
            else:
                print(f"[telegram poster] Failed: {e}", flush=True)
                return False

    async def _worker(self):
        """Background worker that sends messages in batches periodically."""
        print(f"[telegram poster] Started, interval: {self._send_interval}s", flush=True)

        while not self._stop_event.is_set() or not self.queue.empty():
            try:
                # Wait for send interval
                current_time = asyncio.get_event_loop().time()
                time_since_last_send = current_time - self._last_send_time
                wait_time = max(0, self._send_interval - time_since_last_send)

                if wait_time > 0:
                    await asyncio.sleep(wait_time)

                # Check if we should stop (only if queue is empty)
                if self._stop_event.is_set() and self.queue.empty():
                    break

                # Collect all currently queued messages into a batch
                batch = []
                while not self.queue.empty():
                    msg = self.queue.get_nowait()
                    batch.append(msg)
                    self.queue.task_done()

                if batch:
                    queue_size = self.queue.qsize()
                    print(f"[telegram poster] Sending batch of {len(batch)} messages (queue: {queue_size} remaining)", flush=True)

                    # Send each message in the batch
                    for msg in batch:
                        success = await self._send_message(msg)
                        if success:
                            self._total_sent += 1
                        # Small delay between messages in a batch
                        await asyncio.sleep(0.3)

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

        # Wait for queue to be fully drained
        try:
            await asyncio.wait_for(self.queue.join(), timeout=10.0)
        except asyncio.TimeoutError:
            print(f"[telegram poster] WARNING: Queue not empty after timeout", flush=True)

    async def put(self, message: str):
        """Add a message to the queue."""
        self._total_queued += 1
        queue_size = self.queue.qsize()
        print(f"[telegram poster] Queued (total: {self._total_queued}, queue: {queue_size}): {message[:50]}...", flush=True)
        await self.queue.put(message)
