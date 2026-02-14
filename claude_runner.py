"""Claude Code runner with real-time event streaming."""

import json
import subprocess
import time
import io
import sys
from pathlib import Path
from datetime import datetime
from typing import Callable, Optional


def _safe_print(msg: str):
    """Print that handles encoding errors on Windows."""
    try:
        print(msg, flush=True)
    except (UnicodeEncodeError, ValueError):
        # Fallback for Windows console encoding issues - replace emojis
        # Use ASCII encoding with replacement to remove problematic characters
        safe_msg = msg.encode('ascii', errors='replace').decode('ascii')
        print(safe_msg, flush=True)


class ClaudeEvent:
    """Represents a single Claude event."""

    def __init__(self, event_data: dict):
        self.data = event_data
        self.type = event_data.get("type", "")
        self.subtype = event_data.get("subtype", "")

    @property
    def is_system_init(self) -> bool:
        return self.type == "system" and self.subtype == "init"

    @property
    def is_assistant(self) -> bool:
        return self.type == "assistant"

    @property
    def is_user(self) -> bool:
        return self.type == "user"

    def get_message(self) -> dict:
        return self.data.get("message", {})

    def get_tool_use_result(self) -> dict:
        return self.data.get("tool_use_result", {})


class ClaudeProgressFormatter:
    """Formats Claude events into human-readable progress messages."""

    @staticmethod
    def format_tool_use(tool_name: str, tool_input: dict) -> Optional[str]:
        """Format a tool_use event."""
        # Safety check: ensure tool_input is a dict
        if not isinstance(tool_input, dict):
            return f"🔧 Tool: {tool_name}"

        # Skip "Reading..." messages - only show "Read..." when done
        if tool_name == "Read":
            return None
        elif tool_name == "TodoWrite":
            return ClaudeProgressFormatter._format_todo_write(tool_input)
        elif tool_name == "Task":
            return ClaudeProgressFormatter._format_task(tool_input)
        elif tool_name == "Write":
            file_path = tool_input.get("file_path", "?")
            return f"✍️  Writing: `{Path(file_path).name}`"
        elif tool_name == "Edit":
            file_path = tool_input.get("file_path", "?")
            return f"✏️  Editing: `{Path(file_path).name}`"
        elif tool_name == "Bash":
            cmd_text = tool_input.get("command", "")[:60]
            return f"💻 Running: `{cmd_text}...`"
        elif tool_name == "Glob":
            pattern = tool_input.get("pattern", "?")
            return f"🔍 Finding: {pattern}"
        elif tool_name == "Grep":
            pattern = tool_input.get("pattern", "?")
            path = tool_input.get("path", "?")
            return f"🔎 Searching: `{pattern}` in `{path}`"
        return None

    @staticmethod
    def _format_task(tool_input: dict) -> Optional[str]:
        """Format a Task (subagent) tool use."""
        description = tool_input.get("description", "")
        if not description:
            return None
        bg = " (bg)" if tool_input.get("run_in_background") else ""
        return f"🤖 Agent{bg}: {description}"

    @staticmethod
    def _format_todo_write(tool_input: dict) -> Optional[str]:
        """Format a TodoWrite tool use showing current task progress."""
        todos = tool_input.get("todos", [])
        if not todos:
            return None
        completed = sum(1 for t in todos if t.get("status") == "completed")
        total = len(todos)
        # Find the in_progress task
        in_progress = next(
            (t.get("content", "") for t in todos if t.get("status") == "in_progress"),
            None
        )
        if in_progress:
            return f"📋 Tasks [{completed}/{total}]: {in_progress}"
        return f"📋 Tasks [{completed}/{total}]"

    @staticmethod
    def format_tool_result(tool_result: dict) -> Optional[str]:
        """Format a tool_result event."""
        result_type = tool_result.get("type", "")

        if result_type == "text":
            file_info = tool_result.get("file", {})
            if file_info:
                file_path = file_info.get("filePath", "")
                num_lines = file_info.get("numLines", 0)
                return f"📖 Read: `{Path(file_path).name}` ({num_lines} lines)"

        elif tool_result.get("filenames"):
            filenames = tool_result.get("filenames", [])
            num_files = tool_result.get("numFiles", len(filenames))
            return f"🔍 Found: {num_files} files"

        elif tool_result.get("durationMs"):
            duration = tool_result.get("durationMs", 0)
            return f"✅ Done in {duration}ms"

        return None

    @staticmethod
    def format_assistant_text(text: str) -> str:
        """Format assistant text output."""
        return f"💬 {text[:200]}..."


class ClaudeRunner:
    """Runs Claude Code and streams events in real-time."""

    # Session tracking (stored in .tmp to avoid accidental commits)
    SESSION_FILE = ".tmp/claude_session_id.txt"

    def __init__(self, repo_path: Path, logs_dir: Path, session_id: Optional[str] = None, continuation_prompt: Optional[str] = None):
        self.repo_path = repo_path
        self.logs_dir = logs_dir
        self.formatter = ClaudeProgressFormatter()
        # Allow overriding the command for testing
        self.cmd: Optional[str] = None
        # Track the session ID from the current run
        self.session_id: Optional[str] = None
        # Optional session to resume from (overrides file)
        self.resume_session_id: Optional[str] = session_id
        # Optional continuation prompt when resuming
        self.continuation_prompt: Optional[str] = continuation_prompt

    def _run_command(
        self,
        prompt: str,
        on_event: Optional[Callable] = None,
        on_progress: Optional[Callable[[str], None]] = None,
        allowed_tools: str = "Read,Edit,Bash,Write"
    ) -> tuple[int, str, str]:
        """Run Claude with given prompt and stream events."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.logs_dir / f"run_{timestamp}.json"
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        # Determine which session to resume (explicit parameter takes precedence)
        tmp_dir = self.repo_path / ".tmp"
        tmp_dir.mkdir(exist_ok=True)
        session_file_path = tmp_dir / "claude_session_id.txt"

        resume_session_id = self.resume_session_id
        if not resume_session_id and session_file_path.exists():
            try:
                resume_session_id = session_file_path.read_text().strip()
            except:
                pass

        # Build command
        if self.cmd:
            cmd = self.cmd
        elif resume_session_id:
            # Use continuation prompt if provided, otherwise use default prompt
            effective_prompt = self.continuation_prompt if self.continuation_prompt else prompt
            _safe_print(f"[ClaudeRunner] Resuming session: {resume_session_id[:8]}...")
            cmd = f'claude -p "{effective_prompt}" --allowedTools "{allowed_tools}" --output-format stream-json --verbose --resume {resume_session_id}'
        else:
            # New session
            cmd = f'claude -p "{prompt}" --allowedTools "{allowed_tools}" --output-format stream-json --verbose'

        _safe_print(f"[ClaudeRunner] Running: {prompt[:60]}...")
        _safe_print(f"[ClaudeRunner] Log: {log_file}")

        process = subprocess.Popen(
            cmd,
            cwd=self.repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace',
            shell=True,
            bufsize=1
        )

        output_buffer = io.StringIO()

        for line in process.stdout:
            line = line.strip()
            if not line:
                continue

            output_buffer.write(line + "\n")

            # Try to parse as JSON event
            try:
                event = ClaudeEvent(json.loads(line))

                # Call event handler if provided
                if on_event:
                    on_event(event)

                # Generate progress message
                progress_msg = None

                if event.is_system_init:
                    model = event.data.get("model", "unknown")
                    self.session_id = event.data.get("session_id", "")
                    _safe_print(f"[SYSTEM] Session started - Model: {model}, ID: {self.session_id[:8] if self.session_id else 'unknown'}...")

                    # Save session_id for potential resume
                    if self.session_id:
                        try:
                            session_file_path.write_text(self.session_id)
                        except:
                            pass

                elif event.is_assistant:
                    message = event.get_message()
                    content_list = message.get("content", [])

                    for content in content_list:
                        if content.get("type") == "tool_use":
                            tool_name = content.get("name", "unknown")
                            tool_input = content.get("input", {})
                            try:
                                progress_msg = self.formatter.format_tool_use(tool_name, tool_input)
                                if progress_msg:
                                    _safe_print(f"[CLAUDE] {progress_msg}")
                            except Exception as e:
                                _safe_print(f"[CLAUDE] 🔧 Tool: {tool_name}")

                        elif content.get("type") == "text":
                            text = content.get("text", "")
                            if text:
                                _safe_print(f"[CLAUDE] {self.formatter.format_assistant_text(text)}")

                elif event.is_user:
                    tool_result = event.get_tool_use_result()
                    if tool_result:
                        try:
                            progress_msg = self.formatter.format_tool_result(tool_result)
                            if progress_msg:
                                _safe_print(f"[RESULT] {progress_msg}")
                        except Exception as e:
                            _safe_print(f"[RESULT] ✅ Completed")

                # Send progress (rate limiting handled by callback if needed)
                if progress_msg and on_progress:
                    try:
                        on_progress(progress_msg)
                    except Exception as e:
                        _safe_print(f"[ClaudeRunner] Failed to send progress: {e}")

            except json.JSONDecodeError:
                _safe_print(f"[RAW] {line[:100]}")

        process.wait()
        returncode = process.returncode
        stdout = output_buffer.getvalue()
        stderr = process.stderr.read()

        # Save to log file
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(stdout)

        _safe_print(f"[ClaudeRunner] Return code: {returncode}")

        # Clear session file on success (task completed)
        if returncode == 0 and session_file_path.exists():
            try:
                session_file_path.unlink()
                _safe_print(f"[ClaudeRunner] Session completed - cleared session file")
            except:
                pass

        return returncode, stdout, stderr

    def run_process_command(self, on_progress: Optional[Callable[[str], None]] = None) -> tuple[int, str, str]:
        """Run the /process command with optional progress callback."""
        prompt = "read and execute instructions in .claude/commands/process.md"
        return self._run_command(prompt, on_progress=on_progress)

    def run_custom_prompt(self, prompt: str, on_progress: Optional[Callable[[str], None]] = None) -> tuple[int, str, str]:
        """Run Claude with a custom prompt."""
        return self._run_command(prompt, on_progress=on_progress)
