"""Integration test for fetch-youtube command.

Tests that a Claude session can fetch a YouTube transcript end-to-end:
1. Claude discovers the youtube script by reading project files
2. Invokes scripts/youtube.py
3. The Oxylabs proxy routes the request successfully
4. A valid timestamped transcript is returned and cached

Run: uv run pytest tests/test_fetch_youtube.py -v -s --timeout=300
"""

import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from claude_runner import ClaudeRunner

# Short video (< 1 min) with known transcript
TEST_VIDEO_URL = "https://www.youtube.com/watch?v=AdDPmR6P6Bg"
TEST_VIDEO_ID = "AdDPmR6P6Bg"


@pytest.mark.timeout(300)
def test_fetch_youtube_via_claude():
    """Test that Claude can fetch a YouTube transcript via proxy."""

    repo_path = Path.cwd()
    logs_dir = repo_path / "claude_runs"

    # Clear cache so we test the actual proxy fetch (not a cached result)
    cache_file = Path.home() / ".cache" / "youtube_transcripts" / f"{TEST_VIDEO_ID}.txt"
    if cache_file.exists():
        cache_file.unlink()
        print(f"[TEST] Cleared cached transcript: {cache_file}")

    # Clear stale session file so ClaudeRunner starts a fresh session
    session_file = repo_path / ".tmp" / "claude_session_id.txt"
    if session_file.exists():
        session_file.unlink()

    # Unset CLAUDECODE so nested Claude invocation works when run from within Claude
    os.environ.pop("CLAUDECODE", None)

    # Claude discovers the youtube script by reading process.md,
    # which has a "Handling YouTube URLs" section
    prompt = (
        f"Fetch the YouTube transcript for {TEST_VIDEO_URL}. "
        f"Check .claude/commands/process.md for instructions on how to do this."
    )

    runner = ClaudeRunner(repo_path, logs_dir)

    progress_messages = []

    def on_progress(msg: str):
        progress_messages.append(msg)
        print(f"[PROGRESS] {msg}")

    returncode, stdout, stderr = runner.run_custom_prompt(
        prompt,
        on_progress=on_progress,
    )

    print(f"\n[TEST] Return code: {returncode}")
    print(f"[TEST] Progress messages: {len(progress_messages)}")
    if stderr:
        print(f"[TEST] Stderr: {stderr[:500]}")

    # Verify Claude session completed successfully
    assert returncode == 0, f"Claude exited with code {returncode}. Stderr: {stderr[:500]}"

    # Verify the transcript was cached (proves the script ran and proxy worked)
    assert cache_file.exists(), (
        f"Cache file {cache_file} not found - script likely failed to fetch transcript"
    )

    cached_content = cache_file.read_text(encoding="utf-8")
    lines = cached_content.splitlines()
    print(f"[TEST] Cached transcript: {len(cached_content)} chars, {len(lines)} lines")

    # Verify content looks like a transcript (has timestamps)
    assert len(lines) > 3, f"Transcript too short: {len(lines)} lines"

    first_line = lines[0]
    assert ":" in first_line.split(" ")[0], (
        f"First line doesn't start with timestamp: {first_line[:50]}"
    )

    print(f"\n[TEST] PASSED - Claude fetched YouTube transcript via proxy!")
    print(f"[TEST] First 3 lines:")
    for line in lines[:3]:
        print(f"[TEST]   {line}")
