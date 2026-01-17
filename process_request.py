#!/usr/bin/env python
"""Simple script to run Claude with a custom prompt. Useful for testing."""

import sys
from pathlib import Path

from claude_runner import ClaudeRunner

def main():
    if len(sys.argv) < 2:
        print("Usage: python process_request.py <prompt>")
        print("Example: python process_request.py 'analyze raw messages'")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

    REPO_PATH = Path.cwd()
    LOGS_DIR = REPO_PATH / "claude_runs"

    runner = ClaudeRunner(REPO_PATH, LOGS_DIR)

    # Run with stdout only (no Telegram delays)
    returncode, stdout, stderr = runner.run_custom_prompt(prompt, on_progress=None)

    if returncode == 0:
        print(f"\nSuccess!")
    else:
        print(f"\nFailed with code {returncode}")
        if stderr:
            print(f"Stderr: {stderr}")

if __name__ == "__main__":
    main()
