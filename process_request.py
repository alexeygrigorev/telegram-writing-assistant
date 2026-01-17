import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

REPO_PATH = Path.cwd()

def format_tool_use(content):
    """Format a tool_use event for display."""
    tool_name = content.get("name", "unknown")
    tool_input = content.get("input", {})

    if tool_name == "Read":
        return f"📖 Reading: {tool_input.get('file_path', '?')}"
    elif tool_name == "Write":
        return f"✍️  Writing: {tool_input.get('file_path', '?')}"
    elif tool_name == "Edit":
        return f"✏️  Editing: {tool_input.get('file_path', '?')}"
    elif tool_name == "Glob":
        return f"🔍 Finding: {tool_input.get('pattern', '?')}"
    elif tool_name == "Grep":
        return f"🔎 Searching: {tool_input.get('pattern', '?')} in {tool_input.get('path', '?')}"
    elif tool_name == "Bash":
        cmd = tool_input.get('command', '?')
        return f"💻 Running: {cmd[:80]}{'...' if len(cmd) > 80 else ''}"
    elif tool_name == "TodoWrite":
        todos = tool_input.get('todos', [])
        in_progress = sum(1 for t in todos if t.get('status') == 'in_progress')
        return f"📋 Todos: {len(todos)} total, {in_progress} in progress"
    elif tool_name == "Task":
        return f"🤖 Starting agent: {tool_input.get('subagent_type', '?')}"
    else:
        return f"🔧 Tool: {tool_name}"

def format_tool_result(content):
    """Format a tool_result event for display."""
    tool_use_id = content.get("tool_use_id", "")
    result_content = content.get("content", "")

    if isinstance(result_content, str) and len(result_content) > 100:
        preview = result_content[:100] + "..."
    else:
        preview = str(result_content)[:100]

    return f"✅ Result: {preview}"

def process_event(line):
    """Process a single JSON event line."""
    try:
        event = json.loads(line)

        # System init
        if event.get("type") == "system":
            subtype = event.get("subtype", "")
            if subtype == "init":
                model = event.get("model", "unknown")
                print(f"[SYSTEM] Session started - Model: {model}", flush=True)
            return

        # Assistant message (tool use)
        if event.get("type") == "assistant":
            message = event.get("message", {})
            content_list = message.get("content", [])

            for content in content_list:
                if content.get("type") == "tool_use":
                    formatted = format_tool_use(content)
                    print(f"[CLAUDE] {formatted}", flush=True)
                elif content.get("type") == "text":
                    text = content.get("text", "")
                    if text:
                        print(f"[CLAUDE] 💬 {text}", flush=True)
            return

        # User message (tool result)
        if event.get("type") == "user":
            tool_use_result = event.get("tool_use_result", {})

            # Check for detailed tool result info
            if tool_use_result:
                result_type = tool_use_result.get("type", "")

                if result_type == "text":
                    file_info = tool_use_result.get("file", {})
                    if file_info:
                        file_path = file_info.get("filePath", "")
                        num_lines = file_info.get("numLines", 0)
                        print(f"[RESULT] ✅ Read: {Path(file_path).name} ({num_lines} lines)", flush=True)
                        return

                if tool_use_result.get("filenames"):
                    filenames = tool_use_result.get("filenames", [])
                    num_files = tool_use_result.get("numFiles", len(filenames))
                    print(f"[RESULT] ✅ Found: {num_files} files", flush=True)
                    return

                if tool_use_result.get("durationMs"):
                    duration = tool_use_result.get("durationMs", 0)
                    print(f"[RESULT] ✅ Done in {duration}ms)", flush=True)
                    return

            # Fallback: generic result
            message = event.get("message", {})
            content_list = message.get("content", [])
            for content in content_list:
                if content.get("type") == "tool_result":
                    result_content = content.get("content", "")
                    if isinstance(result_content, str) and len(result_content) > 0:
                        if len(result_content) <= 100:
                            preview = result_content[:100]
                        else:
                            preview = f"{len(result_content)} chars"
                        print(f"[RESULT] ✅ {preview}", flush=True)
                    elif result_content:
                        print(f"[RESULT] ✅ Completed", flush=True)
            return

    except json.JSONDecodeError:
        pass

def run_claude_with_prompt(prompt: str):
    """Run Claude with a custom prompt and stream output."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = REPO_PATH / "claude_runs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"run_{timestamp}.json"

    cmd = f'claude -p "{prompt}" --allowedTools "Read,Edit,Bash,Write" --output-format stream-json --verbose'

    print(f"=== Claude Process Runner ===", flush=True)
    print(f"Prompt: {prompt}", flush=True)
    print(f"Log: {log_file}", flush=True)
    print(f"Running...", flush=True)
    print("=" * 60, flush=True)

    process = subprocess.Popen(
        cmd,
        cwd=REPO_PATH,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='replace',
        shell=True,
        bufsize=1
    )

    # Stream output line by line
    with open(log_file, "w", encoding="utf-8") as logf:
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue

            # Write raw line to log
            logf.write(line + "\n")
            logf.flush()

            # Process and display event
            process_event(line)

    process.wait()

    print("=" * 60, flush=True)
    print(f"Return code: {process.returncode}", flush=True)

    # Get stderr
    stderr = process.stderr.read()
    if stderr:
        print(f"Stderr:\n{stderr}", flush=True)

    return process.returncode

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = "analyze content in inbox/raw"

    run_claude_with_prompt(prompt)
