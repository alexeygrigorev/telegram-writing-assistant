"""Test session resume functionality.

This test simulates a Claude session being interrupted and then resumed.

The test task: Create 10 numbered files.
We kill the process after 3-4 files exist, then resume and verify all 10 files are created.
"""

import json
import os
import shutil
import subprocess
import time
from pathlib import Path


def extract_session_id(json_line: str) -> str | None:
    """Extract session_id from a JSON line."""
    try:
        data = json.loads(json_line)
        return data.get("session_id")
    except:
        return None


def test_session_resume():
    """Test that a Claude session can be resumed after interruption."""

    test_dir = Path.cwd() / ".tmp" / "resume_test"
    test_dir.mkdir(parents=True, exist_ok=True)

    # Clean up any previous test files
    for f in test_dir.glob("test_*.txt"):
        f.unlink()

    # The prompt - create 10 files using Write tool (each file is a separate operation)
    # This lets us interrupt after some files are created, then resume to continue
    prompt = f'Create 10 files named test_1.txt through test_10.txt in directory {test_dir}. Each file should contain just its number. Use the Write tool to create each file.'

    print(f"[TEST] Starting Claude session...")
    print(f"[TEST] Test directory: {test_dir}")

    # Start Claude in stream-json mode
    cmd = f'claude -p --output-format stream-json --verbose --dangerously-skip-permissions "{prompt}"'

    process = subprocess.Popen(
        cmd,
        cwd=Path.cwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
    )

    session_id = None
    file_count = 0
    line_count = 0

    print(f"[TEST] Waiting for files to be created...")

    # Monitor output and wait for some files to be created, then kill
    start_time = time.time()
    timeout = 60  # 60 seconds max

    while time.time() - start_time < timeout:
        line = process.stdout.readline()
        if not line:
            if process.poll() is not None:
                print(f"[TEST] Process exited with code: {process.returncode}")
                _, stderr = process.communicate()
                if stderr:
                    print(f"[TEST] Stderr: {stderr[:500]}")
                break
            time.sleep(0.1)
            continue

        line = line.strip()
        if not line:
            continue

        line_count += 1

        # Log first few lines for debugging
        if line_count <= 5:
            print(f"[TEST] Line {line_count}: {line[:150]}...")

        # Extract session_id from first line with subtype="init"
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

            # Kill after 3-4 files are created
            if file_count >= 3:
                print(f"[TEST] Killing process after {file_count} files...")
                process.kill()
                process.wait(timeout=5)
                break

    # Verify we interrupted mid-task
    assert file_count >= 3, f"Expected at least 3 files created before interrupt, got {file_count}"
    assert file_count < 10, f"Expected less than 10 files (interrupted mid-task), got {file_count}"

    print(f"[TEST] Process killed. Files created: {file_count}/10")

    # Now RESUME the session
    print(f"[TEST] Resuming session {session_id}...")

    # When resuming, we need to provide a prompt to continue the task
    resume_cmd = f'claude -p --output-format stream-json --verbose --dangerously-skip-permissions --resume {session_id} "Please continue creating the remaining files."'

    resumed_process = subprocess.Popen(
        resume_cmd,
        cwd=Path.cwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
    )

    print(f"[TEST] Waiting for resumed session to complete...")

    # Wait for completion or timeout
    start_time = time.time()
    last_count = file_count
    resume_line_count = 0

    while time.time() - start_time < timeout:
        line = resumed_process.stdout.readline()
        if not line:
            if resumed_process.poll() is not None:
                print(f"[TEST] Resumed process exited with code: {resumed_process.returncode}")
                break
            time.sleep(0.1)
            continue

        resume_line_count += 1

        # Log first few lines for debugging
        if resume_line_count <= 5:
            print(f"[TEST] Resume Line {resume_line_count}: {line.strip()[:150]}...")

        # Log progress
        current_files = list(test_dir.glob("test_*.txt"))
        if len(current_files) > last_count:
            last_count = len(current_files)
            print(f"[TEST] Files created: {last_count}/10")

            # All files created - we can stop waiting
            if last_count >= 10:
                time.sleep(0.5)  # Give a moment for process to finish cleanly
                break

    print(f"[TEST] Resumed process exit code: {resumed_process.returncode}")
    # Don't wait too long - if we have all 10 files, the test passed
    if last_count >= 10:
        print(f"[TEST] All files created, terminating process...")
        resumed_process.terminate()
        try:
            resumed_process.wait(timeout=2)
        except:
            resumed_process.kill()
    else:
        resumed_process.wait(timeout=30)

    # Verify all 10 files were created
    final_files = list(test_dir.glob("test_*.txt"))
    final_files.sort(key=lambda x: int(x.stem.split("_")[1]))

    print(f"[TEST] Final file count: {len(final_files)}")
    for f in final_files:
        print(f"[TEST]   - {f.name}: {f.read_text().strip()}")

    assert len(final_files) == 10, f"Expected 10 files after resume, got {len(final_files)}"

    # Verify file contents
    for i in range(1, 11):
        expected_file = test_dir / f"test_{i}.txt"
        assert expected_file.exists(), f"File {expected_file} doesn't exist"
        content = expected_file.read_text().strip()
        assert content == str(i), f"File {expected_file} has wrong content: {content}"

    print(f"[TEST] SUCCESS! All 10 files created with correct content.")

    # Clean up
    shutil.rmtree(test_dir)

    return True


if __name__ == "__main__":
    try:
        test_session_resume()
        print("\n[TEST] PASSED")
    except AssertionError as e:
        print(f"\n[TEST] FAILED: {e}")
        exit(1)
    except Exception as e:
        print(f"\n[TEST] ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
