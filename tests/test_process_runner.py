"""Test SessionRetrier logic.

Unit tests using mocks to verify retry behavior without needing Claude CLI.
"""

import asyncio
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
