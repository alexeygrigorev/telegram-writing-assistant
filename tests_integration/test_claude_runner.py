"""Integration tests for ClaudeRunner - runs actual Claude without mocking.

These tests are in a separate directory because they:
1. Require Claude Code CLI to be installed
2. Make actual API calls to Claude
3. Are slower than unit tests
4. May fail due to external factors

Run these with: uv run pytest tests_integration/ -v
"""

import io
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Fix Windows encoding for emojis
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, str(Path(__file__).parent.parent))

from claude_runner import ClaudeRunner, ClaudeEvent, ClaudeProgressFormatter


def test_claude_cli_installed():
    """Test that Claude CLI is available."""
    # Just check that 'claude' command exists by trying to get help
    # This is a simple sanity check
    import shutil
    claude_path = shutil.which("claude")
    assert claude_path is not None, "Claude CLI not found in PATH. Install with: npm install -g @anthropic-ai/claude-code"
    print(f"Claude CLI found at: {claude_path}")


class TestClaudeRunnerReal:
    """Integration tests with actual Claude execution."""

    def test_claude_runner_simple_prompt(self, tmp_path):
        """Test ClaudeRunner with a simple prompt."""
        logs_dir = tmp_path / "logs"
        runner = ClaudeRunner(Path.cwd(), logs_dir)

        progress_messages = []

        def capture_progress(msg):
            progress_messages.append(msg)

        returncode, stdout, stderr = runner.run_custom_prompt(
            "Say 'Hello, World!' and nothing else.",
            on_progress=capture_progress
        )

        print(f"\nReturn code: {returncode}")
        print(f"Stdout length: {len(stdout)}")
        print(f"Progress messages: {progress_messages}")

        assert returncode == 0, f"Claude failed: {stderr}"
        assert len(stdout) > 0
        # Progress messages depend on timing, so we don't assert them

        # Check that a log file was created
        log_files = list(logs_dir.glob("run_*.json"))
        assert len(log_files) > 0, "Log file should be created"

        # Verify "Hello" is in the output
        assert "Hello" in stdout or "World" in stdout

    def test_claude_runner_read_file(self, tmp_path):
        """Test ClaudeRunner reading a file."""
        # Create a test file to read
        test_file = tmp_path / "test.txt"
        test_file.write_text("The quick brown fox jumps over the lazy dog.")

        logs_dir = tmp_path / "logs"
        runner = ClaudeRunner(tmp_path, logs_dir)

        progress_messages = []

        def capture_progress(msg):
            progress_messages.append(msg)
            print(f"Progress: {msg}")

        returncode, stdout, stderr = runner.run_custom_prompt(
            f"Read the file test.txt and tell me what animal is mentioned.",
            on_progress=capture_progress
        )

        print(f"\nReturn code: {returncode}")
        print(f"Stdout: {stdout[:500]}...")

        assert returncode == 0, f"Claude failed: {stderr}"
        assert "dog" in stdout.lower() or "fox" in stdout.lower()

        # Check for Read result in progress messages (format is "Read: `filename` (N lines)")
        read_messages = [m for m in progress_messages if "Read:" in m]
        assert len(read_messages) > 0, "Should have seen a Read tool result"

    def test_claude_runner_event_streaming(self, tmp_path):
        """Test that ClaudeRunner correctly parses event stream."""
        logs_dir = tmp_path / "logs"
        runner = ClaudeRunner(tmp_path, logs_dir)

        events = []

        def capture_event(event: ClaudeEvent):
            events.append(event)

        returncode, stdout, stderr = runner._run_command(
            "Create a file named hello.txt with content 'Hello!'",
            on_event=capture_event,
            on_progress=None
        )

        print(f"\nTotal events captured: {len(events)}")
        event_types = [e.type for e in events]
        print(f"Event types: {set(event_types)}")

        # Should have system init event
        assert any(e.is_system_init for e in events), "Should have system init event"
        # Should have assistant events
        assert any(e.is_assistant for e in events), "Should have assistant events"
        # Should have user events (tool results)
        assert any(e.is_user for e in events), "Should have user/tool_result events"

        # Check that the file was created
        hello_file = tmp_path / "hello.txt"
        assert hello_file.exists(), "Claude should have created hello.txt"
        assert hello_file.read_text() == "Hello!", "File content should match"

    def test_claude_runner_progress_formatter(self, tmp_path):
        """Test the progress formatter with actual Claude output."""
        logs_dir = tmp_path / "logs"
        runner = ClaudeRunner(tmp_path, logs_dir)

        all_progress = []

        def capture_progress(msg):
            all_progress.append(msg)
            print(f"Progress: {msg}")

        # Create a task that uses multiple tools
        (tmp_path / "input.txt").write_text("Count the words in this file.")

        returncode, stdout, stderr = runner.run_custom_prompt(
            "Read input.txt, count the words, and write the count to output.txt",
            on_progress=capture_progress
        )

        print(f"\nAll progress messages: {all_progress}")

        assert returncode == 0
        # Progress messages are rate-limited, so we might get 0 or a few messages
        # The important thing is the command completed successfully

        # Check output file was created
        output_file = tmp_path / "output.txt"
        assert output_file.exists(), "Output file should be created"

        # Verify the output has correct content
        content = output_file.read_text()
        assert "6" in content, f"Expected word count 6, got: {content}"

    def test_claude_runner_multiple_operations(self, tmp_path):
        """Test ClaudeRunner with multiple file operations."""
        logs_dir = tmp_path / "logs"
        runner = ClaudeRunner(tmp_path, logs_dir)

        # Create multiple files and have Claude process them
        (tmp_path / "file1.txt").write_text("Apple")
        (tmp_path / "file2.txt").write_text("Banana")
        (tmp_path / "file3.txt").write_text("Cherry")

        returncode, stdout, stderr = runner.run_custom_prompt(
            "Read file1.txt, file2.txt, and file3.txt, then create summary.txt with all three words on separate lines"
        )

        print(f"\nReturn code: {returncode}")
        print(f"Stdout length: {len(stdout)}")

        assert returncode == 0, f"Claude failed: {stderr[:200] if stderr else 'No stderr'}"

        # Check that summary.txt was created
        summary_file = tmp_path / "summary.txt"
        assert summary_file.exists(), "summary.txt should be created"

        content = summary_file.read_text().lower()
        assert "apple" in content and "banana" in content and "cherry" in content, \
            f"Summary should contain all three fruits. Got: {content}"


class TestClaudeEventParsing:
    """Test event parsing with real Claude output."""

    def test_parse_real_claude_output(self, tmp_path):
        """Test parsing actual JSON events from Claude."""
        logs_dir = tmp_path / "logs"
        runner = ClaudeRunner(tmp_path, logs_dir)

        parsed_events = []

        def capture_and_parse(event: ClaudeEvent):
            parsed_events.append({
                "type": event.type,
                "subtype": event.subtype,
                "is_system_init": event.is_system_init,
                "is_assistant": event.is_assistant,
                "is_user": event.is_user,
            })

        runner._run_command(
            "Create a file named test.txt with content 'Test content'",
            on_event=capture_and_parse,
            on_progress=None
        )

        print(f"\nParsed {len(parsed_events)} events")
        for i, event in enumerate(parsed_events[:5]):
            print(f"  Event {i}: {event}")

        assert len(parsed_events) > 0
        assert any(e["is_system_init"] for e in parsed_events)

