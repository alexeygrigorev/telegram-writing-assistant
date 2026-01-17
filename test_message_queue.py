"""Test script to simulate message queue behavior with batched sending."""

import asyncio
import time
from datetime import datetime

# Configuration
RUN_DURATION = 15  # seconds
SEND_INTERVAL = 3.0  # seconds
MESSAGE_INTERVAL = 0.5  # seconds between generating messages


class MessageQueue:
    """Queues messages and sends them in batches periodically."""

    def __init__(self, send_interval: float = 5.0):
        self.queue: asyncio.Queue[str] = asyncio.Queue()
        self._task = None
        self._stop_event = asyncio.Event()
        self._last_send_time = 0
        self._send_interval = send_interval
        self._total_queued = 0
        self._total_sent = 0

    async def _worker(self):
        """Background worker that sends messages in batches periodically."""
        print(f"[POSTER] Started, interval: {self._send_interval}s", flush=True)

        while not self._stop_event.is_set() or not self.queue.empty():
            try:
                # Wait for send interval or stop event
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
                    print(f"[POSTER] Sending batch of {len(batch)} messages (queue: {queue_size} remaining):", flush=True)
                    for msg in batch:
                        print(f"  - {msg}", flush=True)
                    self._total_sent += len(batch)
                    self._last_send_time = asyncio.get_event_loop().time()

            except Exception as e:
                print(f"[POSTER] Worker error: {e}", flush=True)

        print(f"[POSTER] Stopped. Total sent: {self._total_sent}", flush=True)

    async def start(self):
        """Start the background worker."""
        if self._task is None or self._task.done():
            self._stop_event.clear()
            self._task = asyncio.create_task(self._worker())

    async def stop(self):
        """Stop the worker and wait for all messages to be sent."""
        self._stop_event.set()
        if self._task and not self._task.done():
            await asyncio.wait_for(self._task, timeout=30.0)

        # Wait for queue to be fully drained
        await self.queue.join()

        assert self.queue.empty(), f"Queue should be empty! Size: {self.queue.qsize()}"
        print(f"[POSTER] Queue confirmed empty.", flush=True)

    async def put(self, message: str):
        """Add a message to the queue."""
        self._total_queued += 1
        queue_size = self.queue.qsize()
        print(f"[GENERATOR] Generated: {message} (total: {self._total_queued}, queue: {queue_size})", flush=True)
        await self.queue.put(message)


async def generate_messages(queue: MessageQueue):
    """Simulate message generation."""
    count = 0
    start_time = time.time()

    while time.time() - start_time < RUN_DURATION:
        count += 1
        await queue.put(f"Message {count}")
        await asyncio.sleep(MESSAGE_INTERVAL)

    print(f"\n[GENERATOR] Finished generating {count} messages", flush=True)


async def main():
    print(f"=== Test: Message Queue for {RUN_DURATION}s ===", flush=True)
    print(f"Settings: send_interval={SEND_INTERVAL}s, message_interval={MESSAGE_INTERVAL}s\n", flush=True)

    queue = MessageQueue(send_interval=SEND_INTERVAL)
    await queue.start()

    # Run generator and wait for it to finish
    await generate_messages(queue)

    # Stop queue and show results
    await queue.stop()

    print(f"\n=== RESULTS ===", flush=True)
    print(f"Total generated: {queue._total_queued}", flush=True)
    print(f"Total sent: {queue._total_sent}", flush=True)

    # Assert all messages were sent
    assert queue._total_queued == queue._total_sent, f"Expected {queue._total_queued} sent, got {queue._total_sent}!"
    print(f"\n=== TEST PASSED ===", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
