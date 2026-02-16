"""Test SessionRetrier logic.

Unit tests using mocks to verify retry behavior without needing Claude CLI,
plus integration tests for CLI --resume functionality.
"""

import asyncio
import json
import shutil
import subprocess
import time
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch, MagicMock

import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from session_retrier import SessionRetrier


class TestSessionRetrier:
    """Unit tests for SessionRetrier helpers."""

    def test_get_commit_hash(self, tmp_path):
        """Test getting commit hash."""
        runner = SessionRetrier(tmp_path, tmp_path / "logs")

        with patch("subprocess.run") as mock_run:
            mock_result = Mock()
            mock_result.stdout = "abc123def456\n"
            mock_run.return_value = mock_result

            result = runner.get_commit_hash()
            assert result == "abc123def456"

    def test_get_session_id_exists(self, tmp_path):
        """Test getting session ID when file exists."""
        runner = SessionRetrier(tmp_path, tmp_path / "logs")
        session_file = tmp_path / ".tmp" / "claude_session_id.txt"
        session_file.parent.mkdir(parents=True, exist_ok=True)
        session_file.write_text("test-session-id-12345")

        result = runner.get_session_id()
        assert result == "test-session-id-12345"

    def test_get_session_id_missing(self, tmp_path):
        """Test getting session ID when file doesn't exist."""
        runner = SessionRetrier(tmp_path, tmp_path / "logs")

        result = runner.get_session_id()
        assert result is None


class TestAutoRetry:
    """Test run_with_auto_retry logic."""

    def _make_retrier(self, tmp_path):
        retrier = SessionRetrier(tmp_path, tmp_path / "logs")
        bot = AsyncMock()
        progress = Mock()
        return retrier, bot, progress

    @pytest.mark.asyncio
    async def test_success_with_commit(self, tmp_path):
        """returncode 0 + new commit = success with commit hash."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        with patch.object(retrier, "get_commit_hash", side_effect=["aaa", "bbb"]), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.return_value = (0, "", "")

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is True
        assert commit == "bbb"
        assert error is None

    @pytest.mark.asyncio
    async def test_success_no_commit(self, tmp_path):
        """returncode 0 + same commit = success with no commit (nothing to process)."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        with patch.object(retrier, "get_commit_hash", return_value="aaa"), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.return_value = (0, "", "")

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is True
        assert commit is None
        assert error is None
        # Should NOT have sent any retry messages
        bot.send_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_crash_then_retry_succeeds_with_commit(self, tmp_path):
        """Crash on first run, retry succeeds with a commit."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        # Write session ID file so retry can find it
        session_file = tmp_path / ".tmp" / "claude_session_id.txt"
        session_file.parent.mkdir(parents=True, exist_ok=True)
        session_file.write_text("sess-123")

        call_count = 0
        def mock_run_process(**kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return (1, "", "crash")  # First run crashes
            return (0, "", "")  # Retry succeeds

        with patch.object(retrier, "get_commit_hash", side_effect=["aaa", "bbb"]), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.side_effect = mock_run_process

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is True
        assert commit == "bbb"
        assert error is None
        bot.send_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_crash_then_retry_succeeds_no_commit(self, tmp_path):
        """Crash on first run, retry succeeds but nothing to commit."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        session_file = tmp_path / ".tmp" / "claude_session_id.txt"
        session_file.parent.mkdir(parents=True, exist_ok=True)
        session_file.write_text("sess-123")

        call_count = 0
        def mock_run_process(**kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return (1, "", "crash")
            return (0, "", "")

        with patch.object(retrier, "get_commit_hash", return_value="aaa"), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.side_effect = mock_run_process

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is True
        assert commit is None
        assert error is None

    @pytest.mark.asyncio
    async def test_crash_no_session_id(self, tmp_path):
        """Crash with no session ID saved = failure, no retry."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        with patch.object(retrier, "get_commit_hash", return_value="aaa"), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.return_value = (1, "", "crash")

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is False
        assert commit is None
        assert "no session ID" in error
        bot.send_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_all_retries_crash(self, tmp_path):
        """All retries crash = failure after MAX_RETRIES."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        session_file = tmp_path / ".tmp" / "claude_session_id.txt"
        session_file.parent.mkdir(parents=True, exist_ok=True)
        session_file.write_text("sess-123")

        with patch.object(retrier, "get_commit_hash", return_value="aaa"), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.return_value = (1, "", "crash")

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is False
        assert commit is None
        assert "crashed" in error
        # Should have sent MAX_RETRIES retry messages
        assert bot.send_message.call_count == retrier.MAX_RETRIES

    @pytest.mark.asyncio
    async def test_crash_twice_then_succeed(self, tmp_path):
        """Two crashes then success on third retry."""
        retrier, bot, progress = self._make_retrier(tmp_path)

        session_file = tmp_path / ".tmp" / "claude_session_id.txt"
        session_file.parent.mkdir(parents=True, exist_ok=True)
        session_file.write_text("sess-123")

        call_count = 0
        def mock_run_process(**kwargs):
            nonlocal call_count
            call_count += 1
            if call_count <= 3:  # First run + 2 retries crash
                return (1, "", "crash")
            return (0, "", "")  # 3rd retry succeeds

        with patch.object(retrier, "get_commit_hash", side_effect=["aaa", "bbb"]), \
             patch("session_retrier.ClaudeRunner") as MockRunner:
            MockRunner.return_value.run_process_command.side_effect = mock_run_process

            success, commit, error = await retrier.run_with_auto_retry(
                chat_id=1, bot=bot, on_progress=progress
            )

        assert success is True
        assert commit == "bbb"
        assert error is None
        assert bot.send_message.call_count == 3


class TestMultipleInterruptions:
    """Integration test: multiple interruptions with real Claude CLI."""

    def test_resume_multiple_times(self):
        """Test simulating Claude being interrupted 2 times, then succeeding."""
        repo_path = Path.cwd()
        test_dir = repo_path / ".tmp" / "multi_interrupt_test"
        test_dir.mkdir(parents=True, exist_ok=True)

        # Clean up any previous test files
        for f in test_dir.glob("test_*.txt"):
            f.unlink()

        # Get commit hash BEFORE
        result_before = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        commit_before = result_before.stdout.strip()
        print(f"\n[TEST] Commit BEFORE: {commit_before[:8]}")

        # Start with sleep to give us time to interrupt
        # Create a marker file first, then sleep, then create result files
        prompt = f'Run this: cd {test_dir} && echo "start" > status.txt && sleep 60 && for i in {{1..20}}; do echo $i > test_$i.txt; sleep 0.5; done'

        cmd = f'claude -p --allowedTools "Read,Edit" --output-format stream-json --verbose "{prompt}"'

        print(f"\n[TEST] Starting Claude (will interrupt multiple times)...")
        process = subprocess.Popen(
            cmd,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            bufsize=1
        )

        session_id = None
        interrupt_count = 0
        MAX_INTERRUPTS = 2
        file_count = 0
        start_time = time.time()

        while time.time() - start_time < 90:
            line = process.stdout.readline()
            if not line:
                if process.poll() is not None:
                    break
                time.sleep(0.1)
                continue

            line = line.strip()
            if not line:
                continue

            # Extract session_id from first line
            if session_id is None:
                try:
                    data = json.loads(line)
                    if data.get("type") == "system" and data.get("subtype") == "init":
                        session_id = data.get("session_id")
                        print(f"[TEST] Session ID: {session_id}")
                except:
                    pass

            # Wait for status.txt to appear (bash started sleeping)
            if (test_dir / "status.txt").exists() and interrupt_count == 0:
                time.sleep(1)  # Give it a moment in the sleep
                interrupt_count += 1
                print(f"[TEST] INTERRUPTION #{interrupt_count}: Killing during sleep phase...")
                process.kill()
                process.wait(timeout=5)
                break

        # First interruption done
        assert interrupt_count == 1, "Should have interrupted once"

        # Resume - interrupt again
        print(f"\n[TEST] === Resume 1 ===")
        cmd = f'claude -p --allowedTools "Read,Edit" --output-format stream-json --verbose --resume {session_id} "Please continue creating the remaining files."'

        process = subprocess.Popen(
            cmd,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            bufsize=1
        )

        # Check for existing files
        existing_files = list(test_dir.glob("test_*.txt"))
        file_count = len(existing_files)
        print(f"[TEST] Found {file_count} existing files")

        start_time = time.time()
        while time.time() - start_time < 90:
            line = process.stdout.readline()
            if not line:
                if process.poll() is not None:
                    break
                time.sleep(0.1)
                continue

            # Check for new files
            current_files = list(test_dir.glob("test_*.txt"))
            if len(current_files) > file_count:
                file_count = len(current_files)
                print(f"[TEST] Files created: {file_count}/20")

                # Interrupt after we have at least 5 more files
                if file_count >= 5:
                    interrupt_count += 1
                    print(f"[TEST] INTERRUPTION #{interrupt_count}: Killing during file creation...")
                    process.kill()
                    process.wait(timeout=5)
                    break

        # Second interruption done
        assert interrupt_count == 2, "Should have interrupted twice"

        # Final resume - let it complete
        print(f"\n[TEST] === Final Resume ===")
        cmd = f'claude -p --allowedTools "Read,Edit" --output-format stream-json --verbose --resume {session_id} "Please continue creating the remaining test files."'

        process = subprocess.Popen(
            cmd,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            bufsize=1
        )

        # Wait for completion or timeout
        start_time = time.time()
        while time.time() - start_time < 90:
            line = process.stdout.readline()
            if not line:
                if process.poll() is not None:
                    break
                time.sleep(0.1)
                continue

            # Check for files
            current_files = list(test_dir.glob("test_*.txt"))
            if len(current_files) > file_count:
                file_count = len(current_files)
                print(f"[TEST] Files created: {file_count}/20")

                if file_count >= 20:
                    time.sleep(1)
                    break

        process.wait(timeout=5)

        # Verify all 20 files exist (since the bash loop creates 20, not 10)
        final_files = list(test_dir.glob("test_*.txt"))
        final_files.sort(key=lambda x: int(x.stem.split("_")[1]))

        print(f"\n[TEST] Final file count: {len(final_files)}")
        assert len(final_files) >= 20, f"Expected at least 20 files, got {len(final_files)}"

        # Clean up
        shutil.rmtree(test_dir)

        print(f"\n[TEST] PASSED - Handled {MAX_INTERRUPTS} interruptions successfully!")


def test_multiple_interruptions_integration():
    """Run the multiple interruptions test."""
    TestMultipleInterruptions().test_resume_multiple_times()
