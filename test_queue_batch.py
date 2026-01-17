"""Test message queue batching with stdout only (no Telegram)."""

import asyncio
import queue as thread_queue
import sys
import time

# Fix Windows console encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', newline='\n')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace', newline='\n')


class MockBot:
    """Mock bot for testing."""
    async def send_message(self, chat_id, text, parse_mode=None):
        print(f"\n{'='*60}")
        print(f"[TELEGRAM MESSAGE to {chat_id}]")
        print(f"{'='*60}")
        print(text)
        print(f"{'='*60}\n")


class MessageQueue:
    """Queues messages and sends them in batches periodically."""

    def __init__(self, chat_id: int, bot, send_interval: float = 3.0):
        self.chat_id = chat_id
        self.bot = bot
        self.queue = thread_queue.Queue()
        self._task = None
        self._stop_event = False
        self._last_send_time = time.time()
        self._send_interval = send_interval
        self._total_queued = 0
        self._total_sent = 0

    async def _send_message(self, msg: str):
        """Send a single message."""
        await self.bot.send_message(self.chat_id, msg)
        return True

    async def _worker(self):
        """Background worker that sends messages in batches periodically."""
        print(f"[POSTER] Started, interval: {self._send_interval}s", flush=True)

        while not self._stop_event:
            try:
                # Wait for send interval
                current_time = time.time()
                time_since_last_send = current_time - self._last_send_time
                wait_time = max(0, self._send_interval - time_since_last_send)

                if wait_time > 0:
                    # Sleep in small increments to check for new messages
                    while wait_time > 0 and not self._stop_event:
                        sleep_time = min(0.5, wait_time)
                        await asyncio.sleep(sleep_time)
                        wait_time -= sleep_time

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
                    print(f"[POSTER] Sending batch of {len(batch)} messages as ONE (queue: {queue_size} remaining)", flush=True)

                    # Join all messages into one
                    combined_message = "\n".join(batch)

                    # Send as ONE message
                    await self._send_message(combined_message)
                    self._total_sent += len(batch)
                    self._last_send_time = time.time()

            except Exception as e:
                print(f"[POSTER] Worker error: {e}", flush=True)

        # Send any remaining messages
        remaining = []
        while not self.queue.empty():
            try:
                remaining.append(self.queue.get_nowait())
            except thread_queue.Empty:
                break

        if remaining:
            print(f"[POSTER] Sending {len(remaining)} final messages...", flush=True)
            combined_message = "\n".join(remaining)
            await self._send_message(combined_message)
            self._total_sent += len(remaining)

        print(f"[POSTER] Stopped. Total sent: {self._total_sent}", flush=True)

    async def start(self):
        """Start the background worker."""
        if self._task is None or self._task.done():
            self._task = asyncio.create_task(self._worker())

    async def stop(self):
        """Stop the worker and wait for all messages to be sent."""
        self._stop_event = True
        if self._task and not self._task.done():
            await asyncio.wait_for(self._task, timeout=30.0)

    def put_sync(self, message: str):
        """Add a message from synchronous context."""
        self._total_queued += 1
        queue_size = self.queue.qsize()
        print(f"[GENERATOR] {message} (queue: {queue_size})", flush=True)
        self.queue.put(message)


async def simulate_claude_progress(queue: MessageQueue):
    """Simulate Claude generating progress messages."""
    messages = [
        "📖 Reading: `raw/message1.md`",
        "📖 Reading: `raw/message2.md`",
        "📖 Reading: `raw/message3.md`",
        "✅ Read: `message1.md` (15 lines)",
        "✅ Read: `message2.md` (20 lines)",
        "✅ Read: `message3.md` (18 lines)",
        "✏️  Editing: `summary.md`",
        "💻 Running: `git add .`",
        "✅ Done in 50ms",
        "✍️  Writing: `summary_20250117.md`",
        "💬 Creating summary of incoming messages...",
        "📋 Progress: 1/3 tasks active",
    ]

    for msg in messages:
        queue.put_sync(msg)
        await asyncio.sleep(0.3)  # Simulate time between messages

    print(f"\n[GENERATOR] Finished ({len(messages)} messages)", flush=True)


async def main():
    print("="*60)
    print("Testing Message Queue Batching")
    print("="*60)

    bot = MockBot()
    chat_id = 12345
    queue = MessageQueue(chat_id, bot, send_interval=3.0)

    await queue.start()

    # Simulate Claude progress
    await simulate_claude_progress(queue)

    # Stop and wait for all to be sent
    await queue.stop()

    print(f"\nRESULTS: {queue._total_sent} messages sent")


if __name__ == "__main__":
    asyncio.run(main())
