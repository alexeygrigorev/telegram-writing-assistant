"""Integration tests for SessionRetrier with real Claude CLI.

Unlike tests/test_process_runner.py (which fully mocks ClaudeRunner),
these tests spawn real Claude through SessionRetrier -> ClaudeRunner
in a throwaway git repo. Verifies the full stack actually works.
"""

import subprocess
import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from session_retrier import SessionRetrier


def _init_repo(repo: Path) -> None:
    """Create a minimal git repo with an initial commit."""
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@test.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "commit.gpgsign", "false"], cwd=repo, check=True)
    (repo / "README.md").write_text("init\n")
    subprocess.run(["git", "add", "README.md"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)


def _write_process_command(repo: Path, instructions: str) -> None:
    """Create a .claude/commands/process.md file with the given instructions."""
    cmds = repo / ".claude" / "commands"
    cmds.mkdir(parents=True)
    (cmds / "process.md").write_text(instructions)


def _write_settings(repo: Path) -> None:
    """Allow Claude to use Bash, Edit, Write without prompting."""
    settings = repo / ".claude" / "settings.local.json"
    settings.parent.mkdir(parents=True, exist_ok=True)
    settings.write_text(
        '{"permissions": {"allow": ["Bash", "Edit", "Write"]}}\n'
    )


@pytest.mark.asyncio
async def test_retrier_happy_path_real_claude(tmp_path):
    """SessionRetrier + ClaudeRunner + real claude: commit detected, returns success."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _init_repo(repo)
    _write_settings(repo)
    _write_process_command(
        repo,
        "Run this bash command exactly (do not modify): "
        "`echo done > done.txt && git add done.txt && git commit -q -m 'test commit'`. "
        "Do not do anything else. After the command succeeds, respond with 'ok'.",
    )

    retrier = SessionRetrier(repo, tmp_path / "logs")
    bot = AsyncMock()
    on_progress = Mock()

    success, commit_hash, error = await retrier.run_with_auto_retry(
        chat_id=1, bot=bot, on_progress=on_progress
    )

    assert success is True, f"Expected success, got error: {error}"
    assert commit_hash is not None, "Expected a new commit hash"
    assert error is None

    # Verify the commit hash actually points to a real commit with the expected file
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True
    ).stdout.strip()
    assert commit_hash == head
    assert (repo / "done.txt").exists()


@pytest.mark.asyncio
async def test_retrier_no_commit_with_pending_inbox_fails(tmp_path):
    """When inbox/raw has files but Claude makes no commit, retrier must return failure."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _init_repo(repo)
    _write_settings(repo)
    _write_process_command(
        repo,
        "Do not make any edits, do not run any tools, do not commit anything. "
        "Just respond with the single word 'skipped'.",
    )

    # Put a file in inbox/raw so raw_before is non-empty
    (repo / "inbox" / "raw").mkdir(parents=True)
    (repo / "inbox" / "raw" / "pending.txt").write_text("pending work\n")

    retrier = SessionRetrier(repo, tmp_path / "logs")
    bot = AsyncMock()
    on_progress = Mock()

    success, commit_hash, error = await retrier.run_with_auto_retry(
        chat_id=1, bot=bot, on_progress=on_progress
    )

    assert success is False, "Should have failed: no commit but inbox had files"
    assert commit_hash is None
    assert error is not None
    assert "no commit" in error.lower() or "unprocessed" in error.lower()
