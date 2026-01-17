"""Mock Claude process that simulates the real Claude runner output.

This script mimics the behavior of claude_runner.py but with controllable timing
and output for testing purposes.
"""

import json
import sys
import time
from pathlib import Path


def emit(event: dict):
    """Emit a JSON event to stdout."""
    print(json.dumps(event))
    sys.stdout.flush()


def main():
    """Run mock Claude process."""
    speed = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0

    # Emit init event
    emit({
        "type": "system",
        "subtype": "init",
        "model": "claude-opus-mock",
        "cwd": str(Path.cwd())
    })

    base_delay = 0.5 / speed

    # Simulate reading files
    files_to_read = [
        "inbox/raw/message1.md",
        "inbox/raw/message2.md",
        "inbox/raw/message3.md",
    ]

    for filepath in files_to_read:
        emit({
            "type": "assistant",
            "message": {
                "id": f"msg_{int(time.time()*1000)}",
                "role": "assistant",
                "content": [{
                    "type": "tool_use",
                    "id": f"call_{int(time.time()*1000)}",
                    "name": "Read",
                    "input": {"file_path": filepath}
                }]
            }
        })
        time.sleep(base_delay)

        # Emit result
        emit({
            "type": "user",
            "message": {
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": f"call_{int(time.time()*1000)}",
                    "content": f"Content of {filepath}"
                }]
            }
        })
        time.sleep(base_delay)

    # Simulate editing a file
    emit({
        "type": "assistant",
        "message": {
            "id": f"msg_{int(time.time()*1000)}",
            "role": "assistant",
            "content": [{
                "type": "tool_use",
                "id": f"call_{int(time.time()*1000)}",
                "name": "Edit",
                "input": {
                    "file_path": "inbox/summary.md",
                    "old_string": "old content",
                    "new_string": "new content"
                }
            }]
        }
    })
    time.sleep(base_delay)

    emit({
        "type": "user",
        "message": {
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": f"call_{int(time.time()*1000)}",
                "content": "File edited successfully"
            }]
        }
    })
    time.sleep(base_delay)

    # Simulate git operations
    git_commands = [
        (["git", "add", "."], "Adding files to git"),
        (["git", "commit", "-m", "Update articles"], "Committing changes"),
    ]

    for cmd, desc in git_commands:
        emit({
            "type": "assistant",
            "message": {
                "id": f"msg_{int(time.time()*1000)}",
                "role": "assistant",
                "content": [{
                    "type": "tool_use",
                    "id": f"call_{int(time.time()*1000)}",
                    "name": "Bash",
                    "input": {"command": " ".join(cmd), "description": desc}
                }]
            }
        })
        time.sleep(base_delay)

        emit({
            "type": "user",
            "message": {
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": f"call_{int(time.time()*1000)}",
                    "content": f"Ran: {' '.join(cmd)}\nExit code: 0"
                }]
            }
        })
        time.sleep(base_delay)

    # Simulate writing summary
    emit({
        "type": "assistant",
        "message": {
            "id": f"msg_{int(time.time()*1000)}",
            "role": "assistant",
            "content": [{
                "type": "tool_use",
                "id": f"call_{int(time.time()*1000)}",
                "name": "Write",
                "input": {
                    "file_path": "inbox/summaries/summary_test.md",
                    "content": "# Summary\n\nProcessed 3 messages."
                }
            }]
        }
    })
    time.sleep(base_delay)

    emit({
        "type": "user",
        "message": {
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": f"call_{int(time.time()*1000)}",
                "content": "File written: inbox/summaries/summary_test.md"
            }]
        }
    })

    # Final message
    emit({
        "type": "system",
        "subtype": "complete",
        "exit_code": 0
    })

    print(f"\n[MOCK CLAUDE] Finished generating {len(files_to_read) * 2 + 6} events", file=sys.stderr)


if __name__ == "__main__":
    main()
