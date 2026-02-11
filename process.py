"""Process command logic - handles running Claude and auto-resume on failure."""

import subprocess
import time
from pathlib import Path
from typing import Callable, Optional

from claude_runner import ClaudeRunner
from progress_tracker import ProgressTracker


class ProcessRunner:
    """Handles running Claude with auto-retry on session failure."""

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
        progress: ProgressTracker,
        on_progress: Callable[[str], None],
        start_time: float
    ) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Run Claude with automatic retry on session failure.

        Returns:
            (success, commit_hash, error_message)
        """
        commit_before = self.get_commit_hash()
        print(f"[ProcessRunner] Commit before: {commit_before[:8]}", flush=True)

        # First attempt
        runner = ClaudeRunner(self.repo_path, self.logs_dir)
        returncode, stdout, stderr = await self._run_in_thread(
            runner.run_process_command,
            on_progress
        )

        if returncode != 0:
            return False, None, f"Claude session failed (exit code {returncode})"

        # Check if a commit was made
        commit_after = self.get_commit_hash()
        print(f"[ProcessRunner] Commit after: {commit_after[:8]}", flush=True)

        # If commit was made, success!
        if commit_after != commit_before:
            return True, commit_after, None

        # No commit made - enter retry loop
        return await self._retry_loop(
            chat_id,
            bot,
            progress,
            on_progress,
            commit_before,
            commit_after
        )

    async def _run_in_thread(self, func, on_progress):
        """Run a function in asyncio thread pool."""
        import asyncio
        return await asyncio.to_thread(func, on_progress=on_progress)

    async def _retry_loop(
        self,
        chat_id: int,
        bot,
        progress: ProgressTracker,
        on_progress: Callable[[str], None],
        commit_before: str,
        commit_after: str
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
                print(f"[ProcessRunner] WARNING: No new commit was made!", flush=True)
            else:
                print(f"[ProcessRunner] WARNING: Retry {retry_count} also failed!", flush=True)

            session_id = self.get_session_id()
            if not session_id:
                return False, None, "No session to resume and no commit was made"

            # Attempt resume
            retry_count += 1
            print(f"[ProcessRunner] Auto-resume attempt {retry_count}/{self.MAX_RETRIES}...", flush=True)
            await bot.send_message(
                chat_id=chat_id,
                text=f"Session was interrupted. Resuming... (attempt {retry_count}/{self.MAX_RETRIES})",
                parse_mode=None
            )

            # Run with resume
            runner = ClaudeRunner(self.repo_path, self.logs_dir)
            runner.session_id = session_id

            returncode, stdout, stderr = await self._run_in_thread(
                runner.run_process_command,
                on_progress
            )

            if returncode != 0:
                return False, None, f"Resume failed (exit code {returncode})"

            # Check commit after retry
            commit_hash = self.get_commit_hash()
            print(f"[ProcessRunner] Commit after retry {retry_count}: {commit_hash[:8]}", flush=True)

        # After all retries
        if commit_hash == commit_before:
            return False, None, f"Resume attempted {self.MAX_RETRIES} times but no commit was made"

        print(f"[ProcessRunner] Success after {retry_count} retries!", flush=True)
        return True, commit_hash, None
