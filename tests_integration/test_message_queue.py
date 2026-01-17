"""Integration tests for the MessageQueue batching behavior."""

import asyncio
import json
import sys
import time
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from claude_runner import ClaudeProgressFormatter
from message_queue import MessageQueue


class TestMessageQueue:
    """Integration tests for MessageQueue batching behavior."""

    @pytest.mark.asyncio
    async def test_message_queue_batches_messages(self):
        """Test that messages are batched and sent together."""
        sent_messages = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                return True

        bot = MockBot()
        # Use shorter interval for faster tests
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=0.3)

        # Start first so worker is running
        await queue.start()

        # Give worker time to start its loop
        await asyncio.sleep(0.1)

        # Add 5 messages quickly (simulating rapid progress updates)
        queue.put_sync("Message 1")
        queue.put_sync("Message 2")
        queue.put_sync("Message 3")
        queue.put_sync("Message 4")
        queue.put_sync("Message 5")

        # Wait for batch to be sent (0.3s interval + buffer)
        await asyncio.sleep(0.6)

        await queue.stop()

        # Should have sent at least one combined message
        assert len(sent_messages) >= 1

        # Find the message with our content
        combined = "\n".join(sent_messages)
        assert "Message 1" in combined
        assert "Message 2" in combined
        assert "Message 3" in combined
        assert "Message 4" in combined
        assert "Message 5" in combined

    @pytest.mark.asyncio
    async def test_message_queue_send_on_stop(self):
        """Test that messages are sent when queue is stopped."""
        sent_messages = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=10.0)

        await queue.start()
        await asyncio.sleep(0.1)

        # Add messages
        queue.put_sync("Message 1")
        queue.put_sync("Message 2")
        queue.put_sync("Message 3")

        # Stop immediately - should send remaining
        await queue.stop()

        # Messages should be sent as final batch
        assert len(sent_messages) >= 1

        combined = "\n".join(sent_messages)
        assert "Message 1" in combined
        assert "Message 2" in combined
        assert "Message 3" in combined

    @pytest.mark.asyncio
    async def test_message_queue_sync_callback_context(self):
        """Test that put_sync works from synchronous callback context."""
        sent_messages = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=0.3)

        await queue.start()
        await asyncio.sleep(0.1)

        # Simulate synchronous callback (like from subprocess runner)
        def sync_callback(msg):
            queue.put_sync(msg)  # This should work from sync context

        # Call from sync context
        sync_callback("Sync message 1")
        sync_callback("Sync message 2")
        sync_callback("Sync message 3")

        # Wait for batch
        await asyncio.sleep(0.6)

        await queue.stop()

        # All messages should be sent
        combined = "\n".join(sent_messages)
        assert "Sync message 1" in combined
        assert "Sync message 2" in combined
        assert "Sync message 3" in combined

    @pytest.mark.asyncio
    async def test_message_queue_truncates_long_messages(self):
        """Test that messages longer than 4000 chars are truncated."""
        sent_messages = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=0.3)

        await queue.start()
        await asyncio.sleep(0.1)

        # Create very long messages
        long_msg = "A" * 2000
        queue.put_sync(long_msg)
        queue.put_sync(long_msg)  # Total 4000 chars
        queue.put_sync("Extra")   # Should trigger truncation

        await asyncio.sleep(0.6)
        await queue.stop()

        # Message should be truncated
        assert len(sent_messages) >= 1
        for msg in sent_messages:
            assert len(msg) <= 4020  # 4000 + "... (truncated)"
            if "Extra" in msg:
                assert "truncated" in msg

    @pytest.mark.asyncio
    async def test_message_queue_empty_after_stop(self):
        """Test that queue is empty after stop."""
        sent_messages = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=0.3)

        await queue.start()
        await asyncio.sleep(0.1)

        # Add and send messages
        queue.put_sync("Message 1")
        queue.put_sync("Message 2")
        await asyncio.sleep(0.6)

        # Stop should send any remaining
        await queue.stop()

        # Queue should be empty
        assert queue.queue.empty()

    @pytest.mark.asyncio
    async def test_message_queue_with_asyncio_to_thread(self):
        """Test that messages are sent when put_sync is called from asyncio.to_thread context.

        This reproduces the actual scenario in process_command where runner.run_process_command
        is executed via asyncio.to_thread() and calls put_sync() from a thread pool.
        """
        sent_messages = []
        send_times = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                send_times.append(time.time())
                return True

        bot = MockBot()
        # Short interval for faster test
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=0.5)

        await queue.start()
        await asyncio.sleep(0.1)

        start_time = time.time()

        # Simulate the actual scenario: run a function in a thread pool that calls put_sync
        def worker_function(queue_ref):
            """This simulates the ClaudeRunner calling progress callbacks."""
            import time
            # These calls happen from a thread pool thread
            queue_ref.put_sync("Thread Message 1")
            time.sleep(0.2)
            queue_ref.put_sync("Thread Message 2")
            time.sleep(0.2)
            queue_ref.put_sync("Thread Message 3")
            return "done"

        # Run in thread pool like process_command does
        result = await asyncio.to_thread(worker_function, queue)

        # Give the worker time to send batches
        await asyncio.sleep(0.8)

        # Stop queue
        await queue.stop()

        total_time = time.time() - start_time

        # Verify the worker completed
        assert result == "done"

        # Messages should have been sent
        assert len(sent_messages) >= 1, f"Expected at least 1 sent message, got {len(sent_messages)}"

        # All messages should be in sent messages
        combined = "\n".join(sent_messages)
        assert "Thread Message 1" in combined
        assert "Thread Message 2" in combined
        assert "Thread Message 3" in combined

        # Messages should have been sent DURING processing, not just at the end
        # If messages were only sent after stop(), there would be only 1 message at the end
        # With proper batching, we should see sends distributed over time
        if len(send_times) > 1:
            # Verify messages were sent at different times (not all at once at end)
            time_span = max(send_times) - min(send_times)
            assert time_span > 0.1, "Messages should be sent over time, not all at once"

    @pytest.mark.asyncio
    async def test_message_queue_cross_thread_stop_signal(self):
        """Test that stop() works correctly when called from different async context.

        This reproduces the issue where asyncio.Event may not work correctly
        across thread boundaries when using asyncio.to_thread().
        """
        sent_messages = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=10.0)

        await queue.start()
        await asyncio.sleep(0.1)

        # Add messages
        queue.put_sync("Before thread")

        # Run some work in thread that adds more messages
        def add_more_messages(q):
            q.put_sync("From thread 1")
            q.put_sync("From thread 2")

        await asyncio.to_thread(add_more_messages, queue)

        # Stop should be reliable regardless of thread context
        await queue.stop()

        # All messages should be sent (either in batch during worker or final send)
        combined = "\n".join(sent_messages)
        assert "Before thread" in combined
        assert "From thread 1" in combined
        assert "From thread 2" in combined

    @pytest.mark.asyncio
    async def test_message_queue_time_mismatch_bug(self):
        """Test for the time.time() vs loop.time() mismatch bug.

        In __init__, _last_send_time is set using time.time() (wall clock).
        In _worker, current_time uses asyncio.get_event_loop().time() (monotonic).
        These have different offsets, which can cause the wait_time calculation to be wrong.
        """
        sent_messages = []
        send_times = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                send_times.append(time.time())
                return True

        bot = MockBot()
        # Use same interval as production
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=5.0)

        start_time = time.time()
        await queue.start()

        # Immediately queue messages - worker should wait 5 seconds before sending
        queue.put_sync("Immediate message 1")
        queue.put_sync("Immediate message 2")

        # Wait 6 seconds - worker should have sent by now
        await asyncio.sleep(6.0)

        # Add more messages
        queue.put_sync("Delayed message 1")
        queue.put_sync("Delayed message 2")

        # Wait another 6 seconds for second batch
        await asyncio.sleep(6.0)

        await queue.stop()
        total_time = time.time() - start_time

        # Should have received at least the first batch before stop() final send
        # First batch should have been sent around 5 seconds after start
        assert len(sent_messages) >= 1, f"Expected messages to be sent during execution, got {len(sent_messages)}"

        # Check that first send happened during execution, not at the very end
        if send_times:
            first_send_time = send_times[0] - start_time
            # First send should be ~5 seconds after start, not at the end (12+ seconds)
            assert first_send_time < 8.0, f"First send happened too late: {first_send_time}s after start (expected ~5s)"

        # All messages should be present
        combined = "\n".join(sent_messages)
        assert "Immediate message 1" in combined
        assert "Immediate message 2" in combined
        assert "Delayed message 1" in combined
        assert "Delayed message 2" in combined

    @pytest.mark.asyncio
    async def test_message_queue_worker_loop_time_source(self):
        """Test to verify that the worker loop is actually running and checking messages.

        This test adds messages continuously and checks that they're being sent
        periodically, not just accumulating until the end.
        """
        sent_messages = []
        send_count = 0

        class MockBot:
            def __init__(self):
                self.send_count = 0

            async def send_message(self, chat_id, text, parse_mode=None):
                nonlocal send_count
                sent_messages.append(text)
                send_count += 1
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=1.0)

        await queue.start()
        await asyncio.sleep(0.2)  # Let worker start

        # Simulate a long-running process that adds messages
        async def long_running_process():
            for i in range(10):
                queue.put_sync(f"Progress message {i}")
                await asyncio.sleep(0.3)  # Add message every 300ms

        # Run for about 3 seconds - should get ~3 batches
        await long_running_process()

        # Wait for any pending sends
        await asyncio.sleep(1.5)

        await queue.stop()

        # With 1 second interval and 3 seconds of runtime,
        # we should have multiple sends, not just one at the end
        assert send_count >= 2, f"Expected at least 2 sends over 3+ seconds, got {send_count}"

        # All messages should be in sent messages
        combined = "\n".join(sent_messages)
        for i in range(10):
            assert f"Progress message {i}" in combined

    @pytest.mark.asyncio
    async def test_message_queue_with_mock_claude_subprocess(self):
        """Test message queue with a mock Claude subprocess.

        This reproduces the exact production scenario:
        1. Queue is started
        2. A subprocess is run via asyncio.to_thread()
        3. The subprocess outputs JSON events to stdout
        4. Progress callbacks queue messages via put_sync()
        5. Worker should send batches DURING subprocess execution, not just at the end
        """
        import subprocess

        sent_messages = []
        send_times = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                send_times.append(time.time())
                return True

        bot = MockBot()
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=2.0)

        await queue.start()
        await asyncio.sleep(0.1)  # Let worker start

        start_time = time.time()

        # Function that runs the subprocess and processes its output
        # This mimics what ClaudeRunner.run_process_command() does
        def run_subprocess_with_progress(on_progress):
            mock_claude_path = Path(__file__).parent.parent / "mock_claude.py"

            # Run the mock Claude process
            proc = subprocess.run(
                ["uv", "run", "python", str(mock_claude_path), "5"],  # speed=5x
                cwd=Path(__file__).parent.parent,
                capture_output=True,
                text=True,
            )

            # Process the JSON output
            for line in proc.stdout.split('\n'):
                if not line.strip():
                    continue
                try:
                    event = json.loads(line)
                    # Format progress for tool_use events
                    if event.get('type') == 'assistant':
                        message = event.get('message', {})
                        content = message.get('content', [])
                        for item in content:
                            if item.get('type') == 'tool_use':
                                tool_name = item.get('name')
                                tool_input = item.get('input')
                                progress = ClaudeProgressFormatter.format_tool_use(tool_name, tool_input)
                                if progress:
                                    on_progress(progress)
                except json.JSONDecodeError:
                    pass

            return proc.returncode, proc.stdout, proc.stderr

        # Progress callback
        def queue_progress(msg: str):
            queue.put_sync(msg)

        # Run in thread pool exactly like production
        returncode, stdout, stderr = await asyncio.to_thread(
            run_subprocess_with_progress,
            queue_progress
        )

        # Wait for any pending sends
        await asyncio.sleep(3.0)

        await queue.stop()

        total_time = time.time() - start_time

        # Verify subprocess completed
        assert returncode == 0

        # Messages should have been sent
        assert len(sent_messages) >= 1, f"Expected at least 1 message, got {len(sent_messages)}"

        # Check that first send happened during processing, not at the very end
        if send_times:
            first_send_time = send_times[0] - start_time
            # First send should be around 2 seconds after start (send_interval)
            # NOT at the very end (which would be total_time)
            assert first_send_time < total_time * 0.7, \
                f"First send happened too late: {first_send_time:.2f}s after start (total: {total_time:.2f}s)"

        # All message types should be present
        combined = "\n".join(sent_messages)
        assert "Reading" in combined or "Read:" in combined
        assert "Editing" in combined or "Edit:" in combined
