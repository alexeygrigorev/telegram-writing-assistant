"""Test to understand how to detect Claude session failure.

The key question: How do we know a session didn't finish?
Answer: Compare git commit hash before and after.

If commit hash is the same:
- Claude exited before making a commit (crashed, killed, error)
- We should detect this and auto-resume

If commit hash changed:
- Session completed successfully
- No resume needed
"""

import json
import subprocess
import time
from pathlib import Path


def test_detect_session_failure():
    """Test that we can detect when Claude session fails to complete."""

    repo_path = Path.cwd()
    test_dir = repo_path / ".tmp" / "failure_test"
    test_dir.mkdir(parents=True, exist_ok=True)

    # Clean up any previous test files
    for f in test_dir.glob("test_*.txt"):
        f.unlink()

    # Get commit hash BEFORE
    result_before = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    commit_before = result_before.stdout.strip()
    print(f"[TEST] Commit BEFORE: {commit_before[:8]}")

    # Start Claude with a task that creates files
    prompt = f'Create 10 files named test_1.txt through test_10.txt in {test_dir}. Each file should contain just its number.'
    cmd = f'claude -p --output-format stream-json --verbose --dangerously-skip-permissions "{prompt}"'

    print(f"[TEST] Starting Claude...")
    process = subprocess.Popen(
        cmd,
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
    )

    # Extract session_id and wait for some files
    session_id = None
    file_count = 0

    start_time = time.time()
    while time.time() - start_time < 60:
        line = process.stdout.readline()
        if not line:
            if process.poll() is not None:
                break
            time.sleep(0.1)
            continue

        line = line.strip()
        if not line:
            continue

        # Extract session_id from first line
        if session_id is None:
            try:
                data = json.loads(line)
                if data.get("type") == "system" and data.get("subtype") == "init":
                    session_id = data.get("session_id")
                    print(f"[TEST] Session ID: {session_id}")
            except:
                pass

        # Check for files being created
        current_files = list(test_dir.glob("test_*.txt"))
        if len(current_files) > file_count:
            file_count = len(current_files)
            print(f"[TEST] Files created: {file_count}/10")

            # Kill after 3 files (SIMULATE CRASH)
            if file_count >= 3:
                print(f"[TEST] KILLING PROCESS (simulating crash)...")
                process.kill()
                process.wait(timeout=5)
                break

    # Get commit hash AFTER (no commit should have been made)
    result_after = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    commit_after = result_after.stdout.strip()
    print(f"[TEST] Commit AFTER:  {commit_after[:8]}")

    # DETECTION: Compare commits
    print(f"\n[TEST] === FAILURE DETECTION ===")
    if commit_before == commit_after:
        print(f"[TEST] DETECTED: No new commit made!")
        print(f"[TEST] Session crashed or was interrupted")
        print(f"[TEST] Session ID: {session_id}")

        # This is the signal to AUTO-RESUME
        print(f"\n[TEST] === AUTO-RESUME ===")
        print(f"[TEST] Sending message to Telegram: 'Session interrupted, resuming...'")

        resume_cmd = f'claude -p --output-format stream-json --verbose --dangerously-skip-permissions --resume {session_id} "Please continue creating the remaining files."'

        resumed_process = subprocess.Popen(
            resume_cmd,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            bufsize=1
        )

        # Wait for completion
        last_count = file_count
        while time.time() - start_time < 60:
            line = resumed_process.stdout.readline()
            if not line:
                if resumed_process.poll() is not None:
                    break
                time.sleep(0.1)
                continue

            current_files = list(test_dir.glob("test_*.txt"))
            if len(current_files) > last_count:
                last_count = len(current_files)
                print(f"[TEST] Files created: {last_count}/10")

                if last_count >= 10:
                    time.sleep(0.5)
                    break

        if last_count >= 10:
            # Now MAKE A COMMIT to verify it worked
            subprocess.run(
                ["git", "add", "-A"],
                cwd=repo_path,
                capture_output=True
            )
            subprocess.run(
                ["git", "commit", "-m", "Test: Resume completed task"],
                cwd=repo_path,
                capture_output=True
            )

            # Get commit hash AFTER resume
            result_final = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=repo_path,
                capture_output=True,
                text=True
            )
            commit_final = result_final.stdout.strip()
            print(f"\n[TEST] Commit FINAL:  {commit_final[:8]}")

            # Verify commit changed
            assert commit_final != commit_before, "Commit should have changed after resume"
            print(f"[TEST] SUCCESS: Commit changed after resume!")

    else:
        print(f"[TEST] ERROR: Commit changed unexpectedly!")
        assert False, "Test setup error - commit should not have changed"

    # Verify all files exist
    final_files = list(test_dir.glob("test_*.txt"))
    print(f"\n[TEST] Final file count: {len(final_files)}")
    assert len(final_files) == 10, f"Expected 10 files, got {len(final_files)}"

    # Clean up
    import shutil
    shutil.rmtree(test_dir)

    print(f"\n[TEST] PASSED")


if __name__ == "__main__":
    test_detect_session_failure()
