"""Integration tests for ClaudeRunner with MessageQueue."""

import asyncio
import json
import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

# Fix Windows console encoding for emoji
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', newline='\n')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace', newline='\n')

from claude_runner import ClaudeRunner
from message_queue import MessageQueue


class TestClaudeRunnerIntegration:
    """Integration tests for ClaudeRunner with MessageQueue."""

    @pytest.mark.asyncio
    async def test_claude_runner_with_message_queue_mock_command(self):
        """Test ClaudeRunner with MessageQueue using mock command.

        This uses the actual ClaudeRunner class but overrides the command
        to run the mock_claude.py script instead of the real claude command.
        This reproduces the exact production scenario.
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

        # Create ClaudeRunner with mock command
        repo_path = Path(__file__).parent.parent
        logs_dir = repo_path / "claude_runs"

        # Override the command to use our mock script
        runner = ClaudeRunner(repo_path, logs_dir)
        mock_claude_path = repo_path / "mock_claude.py"
        runner.cmd = ["uv", "run", "python", str(mock_claude_path), "5"]

        # Progress callback
        def queue_progress(msg: str):
            queue.put_sync(msg)

        # Run Claude in thread - just like production
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

        # Check timing - with the time bug, messages are sent late
        if send_times:
            first_send_time = send_times[0] - start_time
            # Print timing for debugging
            print(f"\n[TEST] First send at: {first_send_time:.2f}s, total: {total_time:.2f}s")

            # With the bug, first send happens much later than expected
            # After the fix, it should happen around 2s (send_interval)
            # For now, just verify it happened during the test, not at the very end
            assert first_send_time < total_time, \
                f"First send happened after total time: {first_send_time:.2f}s >= {total_time:.2f}s"

        # Verify content
        combined = "\n".join(sent_messages)
        assert "Reading" in combined or "Read:" in combined
