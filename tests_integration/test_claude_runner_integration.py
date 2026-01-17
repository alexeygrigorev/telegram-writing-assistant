"""Integration tests for ClaudeRunner with MessageQueue."""

import asyncio
import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from claude_runner import ClaudeRunner
from message_queue import MessageQueue


class TestClaudeRunnerIntegration:
    """Integration tests for ClaudeRunner with MessageQueue."""

    @pytest.mark.asyncio
    async def test_claude_runner_with_message_queue_real_log(self):
        """Test ClaudeRunner with MessageQueue using real log replay.

        This uses the actual ClaudeRunner class with a mock command that
        replays a real Claude log file, reproducing the exact production scenario.

        Test runs for ~10 seconds with messages sent every 2 seconds.
        """
        sent_messages = []
        send_times = []

        class MockBot:
            async def send_message(self, chat_id, text, parse_mode=None):
                sent_messages.append(text)
                send_times.append(time.time())
                return True

        bot = MockBot()
        # Send every 2 seconds
        queue = MessageQueue(chat_id=12345, bot=bot, send_interval=2.0)

        await queue.start()
        await asyncio.sleep(0.1)

        start_time = time.time()

        # Create ClaudeRunner with mock command that replays real log
        repo_path = Path(__file__).parent.parent
        logs_dir = repo_path / "claude_runs"
        mock_claude_path = Path(__file__).parent / "mock_claude.py"

        runner = ClaudeRunner(repo_path, logs_dir)
        # Use default speed (1.0 = ~10 seconds)
        runner.cmd = f'uv run python {mock_claude_path}'

        # Progress callback - queues messages
        def queue_progress(msg: str):
            queue.put_sync(msg)

        # Run Claude in thread - exactly like production
        returncode, stdout, stderr = await asyncio.to_thread(
            runner.run_process_command,
            on_progress=queue_progress
        )

        # Wait for pending sends (2 more seconds for final batch)
        await asyncio.sleep(2.5)

        await queue.stop()

        total_time = time.time() - start_time

        # Verify it completed
        assert returncode == 0, f"ClaudeRunner failed with code {returncode}"

        # Messages should have been sent
        assert len(sent_messages) >= 1, f"Expected at least 1 message, got {len(sent_messages)}"

        # Check timing - should have sent multiple batches
        print(f"\n[TEST] Total time: {total_time:.2f}s")
        print(f"[TEST] Batches sent: {len(sent_messages)}")
        if send_times:
            for i, t in enumerate(send_times):
                print(f"[TEST] Batch {i+1} sent at: {t - start_time:.2f}s")

            first_send_time = send_times[0] - start_time
            # First send should happen around 2 seconds after start
            assert 1.5 < first_send_time < 3.0, \
                f"First send should be ~2s after start, was: {first_send_time:.2f}s"

        # Verify content - should have real tool names from the log
        combined = "\n".join(sent_messages)
        assert any(word in combined for word in ["Reading", "Running", "Writing", "Found", "Done"])
