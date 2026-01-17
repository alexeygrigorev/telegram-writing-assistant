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
        """
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
        await asyncio.sleep(0.1)

        start_time = time.time()

        # Create ClaudeRunner with mock command that replays real log
        repo_path = Path(__file__).parent.parent
        logs_dir = repo_path / "claude_runs"
        mock_claude_path = Path(__file__).parent / "mock_claude.py"

        runner = ClaudeRunner(repo_path, logs_dir)
        # Override command to use our mock (replays real log)
        runner.cmd = f'uv run python {mock_claude_path} 100'  # 100x speed

        # Progress callback - queues messages
        def queue_progress(msg: str):
            queue.put_sync(msg)

        # Run Claude in thread - exactly like production
        returncode, stdout, stderr = await asyncio.to_thread(
            runner.run_process_command,
            on_progress=queue_progress
        )

        # Wait for pending sends
        await asyncio.sleep(3.0)

        await queue.stop()

        total_time = time.time() - start_time

        # Verify it completed
        assert returncode == 0, f"ClaudeRunner failed with code {returncode}"

        # Messages should have been sent
        assert len(sent_messages) >= 1, f"Expected at least 1 message, got {len(sent_messages)}"

        # Check timing
        if send_times:
            first_send_time = send_times[0] - start_time
            print(f"\n[TEST] First send at: {first_send_time:.2f}s, total: {total_time:.2f}s")

            # First send should happen well before total time (during processing)
            # With the time bug, it happens at the very end
            assert first_send_time < total_time * 0.8, \
                f"First send happened too late: {first_send_time:.2f}s >= {total_time * 0.8:.2f}s (total: {total_time:.2f}s)"

        # Verify content - should have real tool names from the log
        combined = "\n".join(sent_messages)
        assert any(word in combined for word in ["Reading", "Running", "Writing", "Found", "Done"])
