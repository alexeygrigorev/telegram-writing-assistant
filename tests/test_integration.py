"""Integration tests for the full message handling flow."""

import asyncio
import sys
import time
from datetime import datetime
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from telegram import Update, User, Chat, Message, PhotoSize, Voice

sys.path.insert(0, str(Path(__file__).parent.parent))

from main import (
    save_text_message,
    save_voice_message,
    save_photo,
    handle_text_message,
    handle_voice_message,
    handle_photo_message,
    INBOX_RAW,
)

from message_queue import MessageQueue


class TestSaveTextMessage:
    """Integration tests for saving text messages."""

    @pytest.mark.asyncio
    async def test_save_text_message_creates_file(self, tmp_path):
        """Test that save_text_message creates a markdown file."""
        with patch("main.INBOX_RAW", tmp_path):
            filename = await save_text_message(
                content="Test content",
                user_id=123456,
                username="testuser",
                message_date=datetime(2026, 1, 17, 12, 0, 0)
            )

            assert filename.exists()
            content = filename.read_text(encoding="utf-8")
            assert "---" in content
            assert "source: telegram" in content
            assert "user_id: 123456" in content
            assert "username: testuser" in content
            assert "Test content" in content

    @pytest.mark.asyncio
    async def test_save_text_message_no_username(self, tmp_path):
        """Test saving text message without username."""
        with patch("main.INBOX_RAW", tmp_path):
            filename = await save_text_message(
                content="Test content",
                user_id=123456,
                username=None,
                message_date=datetime(2026, 1, 17, 12, 0, 0)
            )

            content = filename.read_text(encoding="utf-8")
            assert "username: unknown" in content


class TestSaveVoiceMessage:
    """Integration tests for saving and transcribing voice messages."""

    @pytest.mark.asyncio
    @patch("main.groq_client")
    @patch("httpx.AsyncClient")
    async def test_save_voice_message_transcribes(self, mock_client_class, mock_groq, tmp_path):
        """Test that save_voice_message downloads and transcribes."""
        with patch("main.INBOX_RAW", tmp_path):
            # Mock HTTP client for downloading
            mock_response = MagicMock()
            mock_response.content = b"fake_ogg_data"
            mock_client = AsyncMock()
            mock_client.get = AsyncMock(return_value=mock_response)
            mock_client_class.return_value.__aenter__.return_value = mock_client

            # Mock Groq transcription
            mock_groq.audio.transcriptions.create.return_value = "Hello world"

            audio_file, transcript_file, transcript_text = await save_voice_message(
                file_path="https://api.telegram.org/file/bot123/voice.ogg",
                user_id=123456,
                username="testuser",
                message_date=datetime(2026, 1, 17, 12, 0, 0)
            )

            # Audio file should be deleted after transcription
            assert not audio_file.exists()

            # Transcript file should exist with content
            assert transcript_file.exists()
            content = transcript_file.read_text(encoding="utf-8")
            assert "Hello world" in content
            assert "source: telegram_voice" in content


class TestSavePhoto:
    """Integration tests for saving photos with descriptions."""

    @pytest.mark.asyncio
    @patch("main.describe_image")
    @patch("httpx.AsyncClient")
    async def test_save_photo_creates_markdown(self, mock_client_class, mock_describe, tmp_path):
        """Test that save_photo downloads image and creates markdown."""
        with patch("main.INBOX_RAW", tmp_path):
            # Mock HTTP client
            mock_response = MagicMock()
            mock_response.content = b"fake_jpg_data"
            mock_client = AsyncMock()
            mock_client.get = AsyncMock(return_value=mock_response)
            mock_client_class.return_value.__aenter__.return_value = mock_client

            # Mock image description
            mock_describe.return_value = "Type: screenshot\nContent: A test image"

            filename, description = await save_photo(
                file_path="https://api.telegram.org/file/bot123/photo.jpg",
                user_id=123456,
                username="testuser",
                caption="Test caption",
                message_date=datetime(2026, 1, 17, 12, 0, 0)
            )

            # Image file should exist
            assert filename.exists()

            # Markdown file should also exist
            md_file = tmp_path / f"{filename.stem}_photo.md"
            assert md_file.exists()

            content = md_file.read_text(encoding="utf-8")
            assert "Type: screenshot" in content
            assert "Test caption" in content


class TestHandleTextMessage:
    """Integration tests for handling incoming text messages via Telegram."""

    @pytest.mark.asyncio
    @patch("main.save_text_message")
    @patch("main.INBOX_RAW")
    async def test_handle_text_saves_and_replies(self, mock_inbox, mock_save, tmp_path):
        """Test that handle_text_message saves file and replies."""
        from main import handle_text_message

        mock_inbox.__truediv__ = Mock(return_value=tmp_path)

        # Mock save_text_message to return a path
        mock_save.return_value = Path("test_file.md")

        # Create mock update
        update = Mock(spec=Update)
        update.effective_chat.id = 123456

        user = Mock(spec=User)
        user.id = 123456
        user.username = "testuser"

        message = Mock(spec=Message)
        message.text = "Test message"
        message.date = datetime(2026, 1, 17, 12, 0, 0)
        message.reply_text = AsyncMock()

        update.effective_user = user
        update.message = message

        # Patch is_allowed_chat to return True
        with patch("main.is_allowed_chat", return_value=True):
            await handle_text_message(update, None)

        # Verify save was called
        mock_save.assert_called_once_with("Test message", 123456, "testuser", message.date)

        # Verify reply was sent
        message.reply_text.assert_called_once()


class TestStatusCommand:
    """Integration tests for /status command."""

    @pytest.mark.asyncio
    @patch("main.ARTICLES_DIR")
    @patch("main.INBOX_RAW")
    async def test_status_command_counts_files(self, mock_inbox, mock_articles, tmp_path):
        """Test that status command counts files correctly."""
        from main import status_command

        # Create some test files
        (tmp_path / "test1.md").write_text("test")
        (tmp_path / "test2.md").write_text("test")

        # Set up mock inbox glob to return test files
        mock_inbox.glob = Mock(return_value=[
            tmp_path / "test1.md",
            tmp_path / "test2.md",
            tmp_path / ".hidden"  # This should be filtered out
        ])

        # Create articles directory and mock it
        articles_dir = tmp_path / "articles"
        articles_dir.mkdir()
        (articles_dir / "article1.md").write_text("article")

        mock_articles.glob = Mock(return_value=[articles_dir / "article1.md"])

        # Create mock update - status_command uses update.message not update.effective_message
        update = Mock(spec=Update)
        update.effective_chat.id = 123456
        update.message = Mock(spec=Message)
        update.message.reply_text = AsyncMock()

        with patch("main.is_allowed_chat", return_value=True):
            await status_command(update, None)

        # Verify reply was sent
        update.message.reply_text.assert_called_once()
        args = update.message.reply_text.call_args[0][0]
        assert "Raw items: 2" in args  # Should exclude .hidden
        assert "Articles: 1" in args


class TestClaudeRunnerIntegration:
    """Integration tests for ClaudeRunner with event streaming."""

    def test_claude_runner_parses_events(self):
        """Test that ClaudeRunner correctly parses JSON events."""
        from claude_runner import ClaudeEvent, ClaudeProgressFormatter

        # Simulate a stream of JSON events
        events = [
            {"type": "system", "subtype": "init", "model": "claude-4"},
            {
                "type": "assistant",
                "message": {
                    "content": [
                        {
                            "type": "tool_use",
                            "name": "Read",
                            "input": {"file_path": "/path/to/file.py"}
                        }
                    ]
                }
            },
            {
                "type": "user",
                "tool_use_result": {
                    "type": "text",
                    "file": {"filePath": "/path/to/file.py", "numLines": 100}
                }
            },
        ]

        results = []
        for event_data in events:
            event = ClaudeEvent(event_data)
            if event.is_system_init:
                results.append("system_init")
            elif event.is_assistant:
                message = event.get_message()
                for content in message.get("content", []):
                    if content.get("type") == "tool_use":
                        progress = ClaudeProgressFormatter.format_tool_use(
                            content["name"],
                            content["input"]
                        )
                        if progress:
                            results.append(progress)
            elif event.is_user:
                result = event.get_tool_use_result()
                if result:
                    progress = ClaudeProgressFormatter.format_tool_result(result)
                    if progress:
                        results.append(progress)

        assert "system_init" in results
        assert any("Reading" in r for r in results)
        assert any("Read:" in r for r in results)


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
