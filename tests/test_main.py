"""Unit tests for main.py with mocks."""

import base64
from datetime import datetime
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from telegram import Update, User, Chat

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import get_timestamp, is_allowed_chat


class TestGetTimestamp:
    """Tests for get_timestamp function."""

    def test_timestamp_format(self):
        """Test that timestamp returns correct format."""
        dt = datetime(2026, 1, 17, 7, 48, 38)
        result = get_timestamp(dt)
        assert result == "20260117_074838"

    def test_timestamp_with_different_time(self):
        """Test timestamp with different time."""
        dt = datetime(2025, 12, 31, 23, 59, 59)
        result = get_timestamp(dt)
        assert result == "20251231_235959"


class TestIsAllowedChat:
    """Tests for is_allowed_chat function."""

    @patch("main.TELEGRAM_CHANNEL", 123456)
    def test_allowed_chat(self):
        """Test that correct chat is allowed."""
        update = Mock(spec=Update)
        update.effective_chat.id = 123456
        assert is_allowed_chat(update) is True

    @patch("main.TELEGRAM_CHANNEL", 123456)
    def test_different_chat_not_allowed(self):
        """Test that different chat is not allowed."""
        update = Mock(spec=Update)
        update.effective_chat.id = 999999
        assert is_allowed_chat(update) is False


class TestDescribeImage:
    """Tests for describe_image function."""

    @patch("main.groq_client")
    def test_describe_image_success(self, mock_groq):
        """Test successful image description."""
        # Import here to avoid early import issues
        from main import describe_image

        # Create a temporary test image
        test_image = Path(__file__).parent.parent / "test_image.jpg"
        test_image_bytes = b"fake_image_data"
        test_image.write_bytes(test_image_bytes)

        try:
            # Mock Groq response
            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "Type: screenshot. Content: A test image."
            mock_groq.chat.completions.create.return_value = mock_response

            result = describe_image(test_image)
            assert result == "Type: screenshot. Content: A test image."

            # Verify Groq was called correctly
            mock_groq.chat.completions.create.assert_called_once()
            call_args = mock_groq.chat.completions.create.call_args
            assert call_args[1]["model"] == "meta-llama/llama-4-scout-17b-16e-instruct"
        finally:
            # Cleanup
            if test_image.exists():
                test_image.unlink()

    @patch("main.groq_client")
    def test_describe_image_cleans_whitespace(self, mock_groq):
        """Test that extra whitespace is cleaned from response."""
        from main import describe_image

        test_image = Path(__file__).parent.parent / "test_image_whitespace.jpg"
        test_image.write_bytes(b"fake_image_data")

        try:
            # Mock Groq response with extra whitespace - removes leading/trailing blank lines
            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "\n\n\n  Type: screenshot.  \n  Content: Test.  \n\n\n"
            mock_groq.chat.completions.create.return_value = mock_response

            result = describe_image(test_image)
            # Leading/trailing blank lines removed, trailing spaces on each line removed
            assert result == "Type: screenshot.\n  Content: Test."
        finally:
            if test_image.exists():
                test_image.unlink()


class TestClaudeRunner:
    """Tests for ClaudeRunner class."""

    def test_claude_event_properties(self):
        """Test ClaudeEvent property detection."""
        from claude_runner import ClaudeEvent

        # Test system init event
        event = ClaudeEvent({"type": "system", "subtype": "init", "model": "claude-4"})
        assert event.is_system_init is True
        assert event.is_assistant is False
        assert event.is_user is False

        # Test assistant event
        event = ClaudeEvent({"type": "assistant", "message": {"content": []}})
        assert event.is_system_init is False
        assert event.is_assistant is True
        assert event.is_user is False

        # Test user event
        event = ClaudeEvent({"type": "user", "tool_use_result": {}})
        assert event.is_system_init is False
        assert event.is_assistant is False
        assert event.is_user is True

    def test_claude_event_get_message(self):
        """Test ClaudeEvent.get_message method."""
        from claude_runner import ClaudeEvent

        event = ClaudeEvent({
            "type": "assistant",
            "message": {"role": "assistant", "content": "test"}
        })
        assert event.get_message() == {"role": "assistant", "content": "test"}

    def test_claude_event_get_tool_use_result(self):
        """Test ClaudeEvent.get_tool_use_result method."""
        from claude_runner import ClaudeEvent

        event = ClaudeEvent({
            "type": "user",
            "tool_use_result": {"type": "text", "content": "result"}
        })
        assert event.get_tool_use_result() == {"type": "text", "content": "result"}

    def test_format_tool_use_read(self):
        """Test formatting Read tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Read", {"file_path": "/path/to/file.py"})
        assert result == "📖 Reading: `file.py`"

    def test_format_tool_use_write(self):
        """Test formatting Write tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Write", {"file_path": "/path/to/file.py"})
        assert result == "✍️  Writing: `file.py`"

    def test_format_tool_use_edit(self):
        """Test formatting Edit tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Edit", {"file_path": "/path/to/file.py"})
        assert result == "✏️  Editing: `file.py`"

    def test_format_tool_use_bash(self):
        """Test formatting Bash tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Bash", {"command": "git status"})
        assert result == "💻 Running: `git status...`"

    def test_format_tool_use_todowrite(self):
        """Test formatting TodoWrite tool use."""
        from claude_runner import ClaudeProgressFormatter

        todos = [
            {"status": "pending", "content": "Task 1"},
            {"status": "in_progress", "content": "Task 2"},
            {"status": "pending", "content": "Task 3"},
        ]
        result = ClaudeProgressFormatter.format_tool_use("TodoWrite", {"todos": todos})
        assert result == "📋 Progress: 1/3 tasks active"

    def test_format_tool_use_glob(self):
        """Test formatting Glob tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Glob", {"pattern": "**/*.py"})
        assert result == "🔍 Finding: **/*.py"

    def test_format_tool_use_grep(self):
        """Test formatting Grep tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Grep", {"pattern": "import", "path": "."})
        assert result == "🔎 Searching: `import` in `.`"

    def test_format_tool_use_unknown(self):
        """Test formatting unknown tool use returns None."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("UnknownTool", {})
        assert result is None

    def test_format_tool_result_with_file(self):
        """Test formatting tool result with file info."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_result({
            "type": "text",
            "file": {"filePath": "/path/to/file.py", "numLines": 100}
        })
        assert result == "✅ Read: `file.py` (100 lines)"

    def test_format_tool_result_with_filenames(self):
        """Test formatting tool result with filenames."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_result({
            "filenames": ["file1.py", "file2.py"],
            "numFiles": 2
        })
        assert result == "✅ Found: 2 files"

    def test_format_tool_result_with_duration(self):
        """Test formatting tool result with duration."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_result({"durationMs": 1234})
        assert result == "✅ Done in 1234ms"

    def test_format_tool_result_unknown(self):
        """Test formatting unknown tool result returns None."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_result({"unknown": "value"})
        assert result is None

    def test_format_assistant_text(self):
        """Test formatting assistant text."""
        from claude_runner import ClaudeProgressFormatter

        text = "This is a long message that should be truncated because it exceeds two hundred characters in length. " * 3
        result = ClaudeProgressFormatter.format_assistant_text(text)
        assert result.startswith("💬")
        assert "..." in result
        assert len(result) < 250  # Should be truncated
