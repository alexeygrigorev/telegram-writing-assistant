"""Mock Claude that replays a real log file for testing."""

import json
import sys
import time
from pathlib import Path


def replay_log(log_path: Path, speed_multiplier: float = 1.0):
    """Replay events from a real Claude run log.

    Args:
        speed_multiplier: 1.0 = normal speed (10 second duration), 0.5 = slower, 2.0 = faster
    """
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Target ~10 second duration with ~50 events = ~0.2s per event
    # At speed_multiplier=1.0, each event takes 0.2s
    base_delay = 0.2 / speed_multiplier

    for line in lines:
        if not line.strip():
            continue

        try:
            event = json.loads(line)
            print(json.dumps(event))
            sys.stdout.flush()

            # Delay between events to simulate real Claude processing
            time.sleep(base_delay)

        except json.JSONDecodeError:
            pass


def main():
    # Use a real log file from tests_integration/logs
    log_file = Path(__file__).parent / "logs" / "run_20260117_090703.json"

    if not log_file.exists():
        print(f"[MOCK CLAUDE] Log file not found: {log_file}", file=sys.stderr)
        # Generate simple mock events as fallback
        for i in range(10):
            print(json.dumps({
                "type": "assistant",
                "message": {
                    "id": f"msg_{i}",
                    "role": "assistant",
                    "content": [{
                        "type": "tool_use",
                        "name": "Read",
                        "input": {"file_path": f"file{i}.md"}
                    }]
                }
            }))
            sys.stdout.flush()
        return

    speed = float(sys.argv[1]) if len(sys.argv) > 1 else 100.0

    print(f"[MOCK CLAUDE] Replaying {log_file.name} at {speed}x speed", file=sys.stderr)

    replay_log(log_file, speed_multiplier=speed)

    print(f"[MOCK CLAUDE] Finished", file=sys.stderr)


if __name__ == "__main__":
    main()
