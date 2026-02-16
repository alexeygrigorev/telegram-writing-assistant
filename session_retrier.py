"""Session Retrier - handles auto-resume when Claude session crashes.

When a Claude session is interrupted (non-zero exit code), this class:
1. Detects the crash via exit code
2. Reads the saved session_id
3. Automatically retries with --resume and a continuation prompt
4. Sends user feedback via Telegram about the retry
"""

import subprocess
from pathlib import Path
from typing import Callable, Optional

from claude_runner import ClaudeRunner


class SessionRetrier:
    """Handles automatic retry of crashed Claude sessions."""

    MAX_RETRIES = 3

    def __init__(self, repo_path: Path, logs_dir: Path):
        self.repo_path = repo_path
        self.logs_dir = logs_dir

    def get_commit_hash(self) -> str:
        """Get current git commit hash."""
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo_path,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()

    def get_session_id(self) -> Optional[str]:
        """Get saved session ID if it exists."""
        session_file = self.repo_path / ".tmp" / "claude_session_id.txt"
        if session_file.exists():
            try:
                return session_file.read_text().strip()
            except:
                pass
        return None

    async def run_with_auto_retry(
        self,
        chat_id: int,
        bot,
        on_progress: Callable[[str], None],
        session_id: Optional[str] = None
    ) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Run Claude with automatic retry on session crash.

        Only retries when Claude crashes (non-zero exit code).
        A successful exit (code 0) with no commit is treated as
        "nothing to process" - not a failure.

        Returns:
            (success, commit_hash, error_message)
        """
        commit_before = self.get_commit_hash()
        print(f"[SessionRetrier] Commit before: {commit_before[:8]}", flush=True)

        # First attempt (or resume if session_id provided)
        runner = ClaudeRunner(self.repo_path, self.logs_dir, session_id=session_id)

        import asyncio
        returncode, stdout, stderr = await asyncio.to_thread(
            runner.run_process_command,
            on_progress=on_progress
        )

        if returncode == 0:
            commit_after = self.get_commit_hash()
            print(f"[SessionRetrier] Commit after: {commit_after[:8]}", flush=True)
            if commit_after != commit_before:
                return True, commit_after, None
            print(f"[SessionRetrier] Session completed successfully with no new commit (nothing to process)", flush=True)
            return True, None, None

        # Session crashed - enter retry loop
        print(f"[SessionRetrier] Session crashed (exit code {returncode}), will attempt resume", flush=True)
        return await self._retry_loop(
            chat_id, bot, on_progress, commit_before, returncode
        )

    async def _retry_loop(
        self,
        chat_id: int,
        bot,
        on_progress: Callable[[str], None],
        commit_before: str,
        last_returncode: int,
    ) -> tuple[bool, Optional[str], Optional[str]]:
        """Retry loop for crashed sessions."""
        for attempt in range(1, self.MAX_RETRIES + 1):
            session_id = self.get_session_id()
            if not session_id:
                return False, None, f"Session crashed (exit code {last_returncode}) and no session ID saved to resume"

            print(f"[SessionRetrier] Auto-resume attempt {attempt}/{self.MAX_RETRIES}...", flush=True)
            await bot.send_message(
                chat_id=chat_id,
                text=f"Session crashed. Resuming... (attempt {attempt}/{self.MAX_RETRIES})",
                parse_mode=None
            )

            runner = ClaudeRunner(
                self.repo_path,
                self.logs_dir,
                session_id=session_id,
                continuation_prompt="Please continue with the task. You were interrupted before completing it."
            )

            import asyncio
            returncode, stdout, stderr = await asyncio.to_thread(
                runner.run_process_command,
                on_progress=on_progress
            )

            if returncode == 0:
                commit_after = self.get_commit_hash()
                print(f"[SessionRetrier] Commit after retry {attempt}: {commit_after[:8]}", flush=True)
                if commit_after != commit_before:
                    print(f"[SessionRetrier] Success after {attempt} retries!", flush=True)
                    return True, commit_after, None
                print(f"[SessionRetrier] Session completed with no new commit after retry {attempt}", flush=True)
                return True, None, None

            last_returncode = returncode
            print(f"[SessionRetrier] Retry {attempt} also crashed (exit code {returncode})", flush=True)

        return False, None, f"Session crashed {self.MAX_RETRIES + 1} times (last exit code {last_returncode})"
