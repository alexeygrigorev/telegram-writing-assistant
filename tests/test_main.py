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

    @patch("main.TELEGRAM_CHAT_ID", 123456)
    def test_allowed_chat(self):
        """Test that correct chat is allowed."""
        update = Mock(spec=Update)
        update.effective_chat.id = 123456
        assert is_allowed_chat(update) is True

    @patch("main.TELEGRAM_CHAT_ID", 123456)
    def test_different_chat_not_allowed(self):
        """Test that different chat is not allowed."""
        update = Mock(spec=Update)
        update.effective_chat.id = 999999
        assert is_allowed_chat(update) is False


class TestCreateCollapsibleMessage:
    """Tests for create_collapsible_message function."""

    def test_create_collapsible_message_basic(self):
        """Test basic collapsible message creation."""
        from main import create_collapsible_message
        from telegram.constants import MessageEntityType

        prefix = "Saved: audio.ogg"
        content = "This is a transcript."
        text, entities = create_collapsible_message(prefix, content)

        # Check text structure
        assert text == "Saved: audio.ogg\n\nThis is a transcript."

        # Check entities
        assert len(entities) == 1
        entity = entities[0]
        assert entity.type == MessageEntityType.EXPANDABLE_BLOCKQUOTE
        # Offset should be after prefix and newlines (len(prefix) + 2)
        assert entity.offset == len(prefix) + 2
        assert entity.length == len(content)

    def test_create_collapsible_message_with_long_content(self):
        """Test that long content is truncated."""
        from main import create_collapsible_message
        from telegram.constants import MessageEntityType

        prefix = "Saved: audio.ogg"
        content = "x" * 1500  # Longer than default max_length
        text, entities = create_collapsible_message(prefix, content, max_length=1000)

        # Content should be truncated
        assert "... (truncated)" in text
        assert len(entities) == 1
        # The entity should cover the truncated content
        entity = entities[0]
        assert entity.type == MessageEntityType.EXPANDABLE_BLOCKQUOTE

    def test_create_collapsible_message_with_unicode(self):
        """Test collapsible message with Unicode characters."""
        from main import create_collapsible_message
        from telegram.constants import MessageEntityType

        prefix = "Saved: аудио.ogg"
        content = "Это транскрипция на русском языке"
        text, entities = create_collapsible_message(prefix, content)

        assert "аудио.ogg" in text
        assert len(entities) == 1
        assert entities[0].type == MessageEntityType.EXPANDABLE_BLOCKQUOTE

    def test_create_collapsible_message_empty_content(self):
        """Test collapsible message with empty content."""
        from main import create_collapsible_message
        from telegram.constants import MessageEntityType

        prefix = "Saved: audio.ogg"
        content = ""
        text, entities = create_collapsible_message(prefix, content)

        assert text == "Saved: audio.ogg\n\n"
        assert len(entities) == 1
        # Entity with zero length for empty content
        assert entities[0].length == 0

    def test_create_collapsible_message_multiline_content(self):
        """Test collapsible message with multiline content."""
        from main import create_collapsible_message
        from telegram.constants import MessageEntityType

        prefix = "Saved: audio.ogg"
        content = "Line 1\nLine 2\nLine 3"
        text, entities = create_collapsible_message(prefix, content)

        assert "Line 1" in text
        assert "Line 2" in text
        assert "Line 3" in text
        assert len(entities) == 1
        entity = entities[0]
        assert entity.type == MessageEntityType.EXPANDABLE_BLOCKQUOTE
        # Offset should be after prefix and newlines
        assert entity.offset == len(prefix) + 2


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
        """Test formatting Read tool use - returns None to avoid noise."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Read", {"file_path": "/path/to/file.py"})
        assert result is None  # Skip "Reading..." messages, only show when done

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

    def test_format_tool_use_todowrite_with_in_progress(self):
        """Test formatting TodoWrite shows current task progress."""
        from claude_runner import ClaudeProgressFormatter

        todos = [
            {"status": "completed", "content": "Task 1"},
            {"status": "in_progress", "content": "Process text content"},
            {"status": "pending", "content": "Task 3"},
        ]
        result = ClaudeProgressFormatter.format_tool_use("TodoWrite", {"todos": todos})
        assert result == "📋 Tasks [1/3]: Process text content"

    def test_format_tool_use_todowrite_all_completed(self):
        """Test formatting TodoWrite when all tasks are done."""
        from claude_runner import ClaudeProgressFormatter

        todos = [
            {"status": "completed", "content": "Task 1"},
            {"status": "completed", "content": "Task 2"},
        ]
        result = ClaudeProgressFormatter.format_tool_use("TodoWrite", {"todos": todos})
        assert result == "📋 Tasks [2/2]"

    def test_format_tool_use_todowrite_empty(self):
        """Test formatting TodoWrite with empty todos returns None."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("TodoWrite", {"todos": []})
        assert result is None

    def test_format_tool_use_task(self):
        """Test formatting Task (subagent) tool use."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Task", {
            "description": "Research claude-pilot repo",
            "subagent_type": "general-purpose",
            "prompt": "Fetch the content..."
        })
        assert result == "🤖 Agent: Research claude-pilot repo"

    def test_format_tool_use_task_background(self):
        """Test formatting background Task shows (bg) suffix."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Task", {
            "description": "Summarize article",
            "subagent_type": "general-purpose",
            "run_in_background": True,
            "prompt": "..."
        })
        assert result == "🤖 Agent (bg): Summarize article"

    def test_format_tool_use_task_no_description(self):
        """Test formatting Task with no description returns None."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_use("Task", {
            "subagent_type": "general-purpose",
            "prompt": "..."
        })
        assert result is None

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
        assert result == "📖 Read: `file.py` (100 lines)"

    def test_format_tool_result_with_filenames(self):
        """Test formatting tool result with filenames."""
        from claude_runner import ClaudeProgressFormatter

        result = ClaudeProgressFormatter.format_tool_result({
            "filenames": ["file1.py", "file2.py"],
            "numFiles": 2
        })
        assert result == "🔍 Found: 2 files"

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


class TestHandleVideoMessage:
    """Tests for handle_video_message function."""

    @patch("main.INBOX_RAW")
    @patch("main.TELEGRAM_CHAT_ID", -1001234567890)
    @pytest.mark.asyncio
    async def test_handle_video_basic(self, mock_inbox_raw):
        """Test basic video message handling creates markdown file with metadata."""
        from main import handle_video_message

        # Mock the inbox directory
        mock_inbox_path = MagicMock()
        mock_inbox_raw.__truediv__ = MagicMock(return_value=mock_inbox_path)

        # Create update with video
        update = Mock(spec=Update)
        update.effective_chat.id = -1001234567890
        update.effective_user.id = 12345
        update.effective_user.username = "testuser"
        update.message.message_id = 100
        update.message.date = datetime(2026, 2, 7, 12, 0, 0)

        # Mock video object
        video = MagicMock()
        video.duration = 90
        video.width = 1920
        video.height = 1080
        video.file_size = 5242880
        video.file_name = "demo.mp4"
        update.message.video = video
        update.message.caption = "Screen recording of feature"
        update.message.text = None

        # Mock file writing
        mock_file = MagicMock()
        mock_inbox_path.__truediv__.return_value = mock_file
        mock_file.__aenter__ = AsyncMock(return_value=mock_file)
        mock_file.__aexit__ = AsyncMock()

        # Mock reply
        update.message.reply_text = AsyncMock(return_value=MagicMock())

        await handle_video_message(update, MagicMock())

        # Verify reply was sent
        update.message.reply_text.assert_called_once()

    @patch("main.INBOX_RAW")
    @patch("main.TELEGRAM_CHAT_ID", -1003688590333)
    @pytest.mark.asyncio
    async def test_video_telegram_link_group_format(self, mock_inbox_raw):
        """Test that Telegram link uses correct group format."""
        from main import handle_video_message

        mock_inbox_path = MagicMock()
        mock_inbox_raw.__truediv__ = MagicMock(return_value=mock_inbox_path)
        mock_file = MagicMock()
        mock_inbox_path.__truediv__.return_value = mock_file

        # Track what was written
        written_content = []
        def mock_write(content):
            written_content.append(content)

        mock_open = MagicMock()
        mock_open.return_value.__enter__ = MagicMock(return_value=MagicMock(write=mock_write))
        mock_open.return_value.__exit__ = MagicMock(return_value=False)

        update = Mock(spec=Update)
        update.effective_chat.id = -1003688590333
        update.effective_user.id = 12345
        update.effective_user.username = "testuser"
        update.message.message_id = 1077
        update.message.date = datetime(2026, 2, 7, 12, 0, 0)

        video = MagicMock()
        video.duration = 45
        video.width = 1920
        video.height = 1080
        video.file_size = 3145728
        video.file_name = None
        update.message.video = video
        update.message.caption = None
        update.message.text = None

        update.message.reply_text = AsyncMock()

        with patch("builtins.open", mock_open):
            await handle_video_message(update, MagicMock())

        # Verify the content contains the correct Telegram link
        # For chat_id -1003688590333, link should be https://t.me/c/3688590333/1077
        content = written_content[0] if written_content else ""
        assert "https://t.me/c/3688590333/1077" in content

    @patch("main.INBOX_RAW")
    @patch("main.TELEGRAM_CHAT_ID", -1001234567890)
    @pytest.mark.asyncio
    async def test_video_with_caption(self, mock_inbox_raw):
        """Test video with caption includes caption in output."""
        from main import handle_video_message

        mock_inbox_path = MagicMock()
        mock_inbox_raw.__truediv__ = MagicMock(return_value=mock_inbox_path)
        mock_file = MagicMock()
        mock_inbox_path.__truediv__.return_value = mock_file

        written_content = []
        def mock_write(content):
            written_content.append(content)

        mock_open = MagicMock()
        mock_open.return_value.__enter__ = MagicMock(return_value=MagicMock(write=mock_write))
        mock_open.return_value.__exit__ = MagicMock(return_value=False)

        update = Mock(spec=Update)
        update.effective_chat.id = -1001234567890
        update.effective_user.id = 12345
        update.effective_user.username = "testuser"
        update.message.message_id = 100
        update.message.date = datetime(2026, 2, 7, 12, 0, 0)

        video = MagicMock()
        video.duration = 120
        video.width = None
        video.height = None
        video.file_size = 10485760
        video.file_name = "recording.mov"
        update.message.video = video
        update.message.caption = "This is a screen recording"
        update.message.text = None

        update.message.reply_text = AsyncMock()

        with patch("builtins.open", mock_open):
            await handle_video_message(update, MagicMock())

        content = written_content[0] if written_content else ""
        assert "Caption: This is a screen recording" in content

    @patch("main.INBOX_RAW")
    @patch("main.TELEGRAM_CHAT_ID", -1001234567890)
    @pytest.mark.asyncio
    async def test_video_with_message_text(self, mock_inbox_raw):
        """Test video with separate message text includes text in output."""
        from main import handle_video_message

        mock_inbox_path = MagicMock()
        mock_inbox_raw.__truediv__ = MagicMock(return_value=mock_inbox_path)
        mock_file = MagicMock()
        mock_inbox_path.__truediv__.return_value = mock_file

        written_content = []
        def mock_write(content):
            written_content.append(content)

        mock_open = MagicMock()
        mock_open.return_value.__enter__ = MagicMock(return_value=MagicMock(write=mock_write))
        mock_open.return_value.__exit__ = MagicMock(return_value=False)

        update = Mock(spec=Update)
        update.effective_chat.id = -1001234567890
        update.effective_user.id = 12345
        update.effective_user.username = "testuser"
        update.message.message_id = 100
        update.message.date = datetime(2026, 2, 7, 12, 0, 0)

        video = MagicMock()
        video.duration = 30
        video.width = 1280
        video.height = 720
        video.file_size = 2097152
        video.file_name = None
        update.message.video = video
        update.message.caption = None
        update.message.text = "Check this out"

        update.message.reply_text = AsyncMock()

        with patch("builtins.open", mock_open):
            await handle_video_message(update, MagicMock())

        content = written_content[0] if written_content else ""
        assert "Message text: Check this out" in content

    @patch("main.INBOX_RAW")
    @patch("main.TELEGRAM_CHAT_ID", -1001234567890)
    @pytest.mark.asyncio
    async def test_video_rejects_wrong_chat(self, mock_inbox_raw):
        """Test that video from wrong chat is rejected."""
        from main import handle_video_message

        update = Mock(spec=Update)
        update.effective_chat.id = -9999999999  # Wrong chat
        update.effective_user.id = 12345
        update.effective_user.username = "testuser"
        update.message.message_id = 100
        update.message.date = datetime(2026, 2, 7, 12, 0, 0)

        video = MagicMock()
        update.message.video = video
        update.message.caption = None
        update.message.text = None

        update.message.reply_text = AsyncMock()

        await handle_video_message(update, MagicMock())

        # Should not reply for wrong chat
        update.message.reply_text.assert_not_called()

    @patch("main.INBOX_RAW")
    @patch("main.TELEGRAM_CHAT_ID", -1001234567890)
    @pytest.mark.asyncio
    async def test_video_with_all_metadata(self, mock_inbox_raw):
        """Test video with all metadata fields populated."""
        from main import handle_video_message

        mock_inbox_path = MagicMock()
        mock_inbox_raw.__truediv__ = MagicMock(return_value=mock_inbox_path)
        mock_file = MagicMock()
        mock_inbox_path.__truediv__.return_value = mock_file

        written_content = []
        def mock_write(content):
            written_content.append(content)

        mock_open = MagicMock()
        mock_open.return_value.__enter__ = MagicMock(return_value=MagicMock(write=mock_write))
        mock_open.return_value.__exit__ = MagicMock(return_value=False)

        update = Mock(spec=Update)
        update.effective_chat.id = -1001234567890
        update.effective_user.id = 12345
        update.effective_user.username = "testuser"
        update.message.message_id = 100
        update.message.date = datetime(2026, 2, 7, 12, 0, 0)

        video = MagicMock()
        video.duration = 150  # 2m 30s
        video.width = 3840
        video.height = 2160
        video.file_size = 104857600  # 100 MB
        video.file_name = "4k-demo.mp4"
        update.message.video = video
        update.message.caption = "4K demo video"
        update.message.text = None

        update.message.reply_text = AsyncMock()

        with patch("builtins.open", mock_open):
            await handle_video_message(update, MagicMock())

        content = written_content[0] if written_content else ""
        assert "duration_seconds: 150" in content
        assert "width: 3840" in content
        assert "height: 2160" in content
        assert "file_size_bytes: 104857600" in content
        assert "file_name: 4k-demo.mp4" in content
        assert "Duration: 2m 30s" in content
        assert "Resolution: 3840x2160" in content
        assert "Size: 100.0 MB" in content
