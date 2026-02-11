"""Session Retrier - handles auto-resume when Claude session fails.

When a Claude session is interrupted (no commit made), this class:
1. Detects the failure by comparing git commit hashes
2. Reads the saved session_id
3. Automatically retries with --resume and a continuation prompt
4. Sends user feedback via Telegram about the retry
"""

import subprocess
from pathlib import Path
from typing import Callable, Optional

from claude_runner import ClaudeRunner


class SessionRetrier:
    """Handles automatic retry of interrupted Claude sessions."""

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
        Run Claude with automatic retry on session failure.

        Args:
            chat_id: Telegram chat ID for sending messages
            bot: Telegram bot instance
            on_progress: Callback for progress updates
            session_id: Optional session ID to resume from the start

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

        if returncode != 0:
            return False, None, f"Claude session failed (exit code {returncode})"

        # Check if a commit was made
        commit_after = self.get_commit_hash()
        print(f"[SessionRetrier] Commit after: {commit_after[:8]}", flush=True)

        # If commit was made, success!
        if commit_after != commit_before:
            return True, commit_after, None

        # No commit made - enter retry loop
        return await self._retry_loop(
            chat_id,
            bot,
            on_progress,
            commit_before,
            commit_after,
            initial_session_id=session_id
        )

    async def _retry_loop(
        self,
        chat_id: int,
        bot,
        on_progress: Callable[[str], None],
        commit_before: str,
        commit_after: str,
        initial_session_id: Optional[str] = None
    ) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Retry loop for interrupted sessions.

        Returns:
            (success, commit_hash, error_message)
        """
        retry_count = 0
        commit_hash = commit_after

        while commit_hash == commit_before and retry_count < self.MAX_RETRIES:
            if retry_count == 0:
                print(f"[SessionRetrier] WARNING: No new commit was made!", flush=True)
            else:
                print(f"[SessionRetrier] WARNING: Retry {retry_count} also failed!", flush=True)

            session_id = self.get_session_id()
            if not session_id:
                return False, None, "No session to resume and no commit was made"

            # Attempt resume with continuation prompt
            retry_count += 1
            print(f"[SessionRetrier] Auto-resume attempt {retry_count}/{self.MAX_RETRIES}...", flush=True)
            await bot.send_message(
                chat_id=chat_id,
                text=f"Session was interrupted. Resuming... (attempt {retry_count}/{self.MAX_RETRIES})",
                parse_mode=None
            )

            # Run with resume and continuation prompt
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

            if returncode != 0:
                return False, None, f"Resume failed (exit code {returncode})"

            # Check commit after retry
            commit_hash = self.get_commit_hash()
            print(f"[SessionRetrier] Commit after retry {retry_count}: {commit_hash[:8]}", flush=True)

        # After all retries
        if commit_hash == commit_before:
            return False, None, f"Resume attempted {self.MAX_RETRIES} times but no commit was made"

        print(f"[SessionRetrier] Success after {retry_count} retries!", flush=True)
        return True, commit_hash, None
