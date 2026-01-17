"""Replay a Claude run log to test message queue behavior."""

import asyncio
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from claude_runner import ClaudeProgressFormatter
from message_queue import MessageQueue


class MockBot:
    """Mock bot that tracks sent messages."""
    def __init__(self):
        self.sent_messages = []
        self.send_times = []

    async def send_message(self, chat_id, text, parse_mode=None):
        self.sent_messages.append(text)
        self.send_times.append(time.time())
        print(f"\n{'='*60}")
        print(f"[TELEGRAM] Message sent ({len(text)} chars)")
        print(f"{'='*60}\n")
        return True


async def replay_log(log_path: Path, queue: MessageQueue, speed_multiplier: float = 10.0):
    """Replay a Claude run log, queueing progress messages.

    Args:
        log_path: Path to the JSON log file
        queue: MessageQueue to send progress to
        speed_multiplier: Speed up replay by this factor (10 = 10x faster)
    """
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"[REPLAY] Replaying {len(lines)} events from {log_path.name}")
    print(f"[REPLAY] Speed multiplier: {speed_multiplier}x")

    start_time = time.time()
    first_timestamp = None

    for line in lines:
        if not line.strip():
            continue

        try:
            event = json.loads(line)
            event_type = event.get('type')

            # Get timestamp from event (if available)
            # For now, we'll use actual time delays based on event processing
            current_time = time.time()

            # Process assistant events (tool use)
            if event_type == 'assistant':
                message = event.get('message', {})
                content = message.get('content', [])

                for item in content:
                    if item.get('type') == 'tool_use':
                        tool_name = item.get('name')
                        tool_input = item.get('input')

                        # Format and queue progress
                        progress = ClaudeProgressFormatter.format_tool_use(tool_name, tool_input)
                        if progress:
                            queue.put_sync(progress)

                            # Small delay to simulate real-time processing
                            await asyncio.sleep(0.01 / speed_multiplier)

            # Process user events (tool results)
            elif event_type == 'user':
                message = event.get('message', {})
                content = message.get('content', [])

                for item in content:
                    if item.get('type') == 'tool_result':
                        result = item.get('content', '')

                        # Format and queue progress for results
                        progress = ClaudeProgressFormatter.format_tool_result(result)
                        if progress:
                            queue.put_sync(progress)
                            await asyncio.sleep(0.01 / speed_multiplier)

        except json.JSONDecodeError as e:
            print(f"[REPLAY] JSON decode error: {e}")
        except Exception as e:
            print(f"[REPLAY] Error processing event: {e}")

    elapsed = time.time() - start_time
    print(f"[REPLAY] Finished replaying {len(lines)} events in {elapsed:.2f}s")


async def test_replay_with_queue():
    """Test replaying a log file with the message queue."""
    log_file = Path(__file__).parent.parent / "claude_runs" / "run_20260117_090703.json"

    if not log_file.exists():
        print(f"Log file not found: {log_file}")
        return

    bot = MockBot()
    chat_id = 12345

    # Use same interval as production
    queue = MessageQueue(chat_id, bot, send_interval=5.0)

    await queue.start()
    print(f"\n[TEST] Queue started, replaying log...\n")

    start_time = time.time()

    # Replay the log
    await replay_log(log_file, queue, speed_multiplier=5.0)

    # Wait for any pending sends
    print(f"\n[TEST] Log replayed, waiting for queue to send...")
    await asyncio.sleep(6.0)

    await queue.stop()

    total_time = time.time() - start_time

    # Results
    print(f"\n{'='*60}")
    print(f"RESULTS")
    print(f"{'='*60}")
    print(f"Total time: {total_time:.2f}s")
    print(f"Messages sent: {len(bot.sent_messages)}")
    print(f"Messages per batch: {[len(m.split('\\n')) for m in bot.sent_messages]}")

    if bot.send_times:
        first_send = bot.send_times[0] - start_time
        print(f"First send at: {first_send:.2f}s after start")

        if len(bot.send_times) > 1:
            for i, t in enumerate(bot.send_times):
                print(f"  Send {i+1}: {t - start_time:.2f}s")

    # Check if messages were sent during replay (not just at the end)
    if bot.send_times:
        first_send_time = bot.send_times[0] - start_time
        if first_send_time < total_time * 0.5:
            print(f"\n✅ Messages were sent DURING replay (first at {first_send_time:.2f}s)")
        else:
            print(f"\n❌ Messages were only sent at the END (first at {first_send_time:.2f}s)")

    return bot.sent_messages, bot.send_times


if __name__ == "__main__":
    asyncio.run(test_replay_with_queue())
