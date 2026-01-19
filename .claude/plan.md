# Interactive Progress Messaging Implementation Plan

## Goal
Replace multiple progress message posts with a single editable message that updates incrementally, reducing clutter during long-running Claude processes.

## Requirements from Voice Transcripts

1. **Single editable message** - Create one message and edit it instead of posting multiple updates
2. **Show only last 15 commands** - Earlier commands should be collapsed/hidden with summary text
3. **Consolidated counters** - "Read 23 files" instead of individual "Read: file1.md" entries
4. **Fix emoji collisions** - "Read" and "Found" currently use same emoji
5. **Markdown parsing** - Use `parse_mode="Markdown"` for inline code rendering

## Implementation Design

### 1. New Class: `ProgressTracker` (in `message_queue.py`)

```python
class ProgressTracker:
    """Tracks and displays progress in a single editable Telegram message."""

    def __init__(self, bot, chat_id: str):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = None
        self.commands = []  # List of (emoji, text) tuples
        self.counters = defaultdict(int)  # Track operation counts
        self.max_visible = 15

    async def start(self):
        """Create initial progress message."""
        self.message_id = await self.bot.send_message(
            chat_id=self.chat_id,
            text="⏳ Working...",
            parse_mode="Markdown"
        )

    async def add_command(self, emoji: str, text: str, category: str = None):
        """Add a command and update the message."""
        if category:
            self.counters[category] += 1

        # Store command (with deduplication for reads)
        self.commands.append((emoji, text))

        # Update message
        await self._update_message()

    async def finish(self):
        """Mark as complete and do final update."""
        await self._update_message(done=True)

    def _format_message(self, done: bool = False) -> str:
        """Format the progress message with collapsed history."""
        status = "✅ Done" if done else "⏳ Processing..."

        # Calculate what to show vs collapse
        total = len(self.commands)
        if total > self.max_visible:
            hidden = total - self.max_visible
            visible_commands = self.commands[-self.max_visible:]
            collapse_text = f"\n_({hidden} earlier commands collapsed_)\n"
        else:
            visible_commands = self.commands
            collapse_text = ""

        # Format visible commands
        command_lines = []
        for emoji, text in visible_commands:
            command_lines.append(f"{emoji} {text}")

        # Add counters summary at top
        counter_lines = []
        if self.counters.get("read", 0) > 0:
            counter_lines.append(f"📖 Read {self.counters['read']} files")
        if self.counters.get("edit", 0) > 0:
            counter_lines.append(f"✏️ Edited {self.counters['edit']} files")
        if self.counters.get("found", 0) > 0:
            counter_lines.append(f"🔍 Found {self.counters['found']} items")

        summary = "\n".join(counter_lines)
        if summary:
            summary += "\n\n"

        return f"{status}\n\n{summary}{collapse_text}" + "\n".join(command_lines)
```

### 2. Modify `ClaudeProgressFormatter` (in `claude_runner.py`)

**Current emojis to fix:**
- Read: ✅ → Change to 📖
- Found: 🔍 (keep)
- Edit: ✏️ (keep)
- Write: ✍️ (keep)
- Running: 💻 (keep)

**Add consolidation logic:**
- Detect consecutive "Read" operations with same pattern
- Emit single consolidated command instead of individual ones

### 3. Modify `MessageQueue.put()` to use ProgressTracker

```python
async def put(self, message: str):
    if self._progress_tracker:
        # Parse message to extract emoji and content
        emoji, text, category = self._parse_progress_message(message)
        await self._progress_tracker.add_command(emoji, text, category)
    else:
        # Fall back to regular batching
        ...
```

### 4. Add signal handlers to `run Claude` in `main.py`

- Send `/progress:start` when Claude starts processing
- Send `/progress:finish` when Claude completes
- This signals when to create/destroy the ProgressTracker

## Files to Modify

1. **`message_queue.py`**
   - Add `ProgressTracker` class
   - Modify `put()` to optionally use ProgressTracker
   - Add `start_progress()` and `finish_progress()` methods

2. **`claude_runner.py`**
   - Fix emoji collisions in `ClaudeProgressFormatter`
   - Add consolidation logic for consecutive reads
   - Extract category from command patterns

3. **`main.py`**
   - Add `/progress:start` and `/progress:finish` command handlers
   - Signal MessageQueue when to use ProgressTracker mode

## Implementation Steps

1. **Add ProgressTracker class** to message_queue.py
2. **Fix emoji collisions** in ClaudeProgressFormatter
3. **Add command consolidation** - detect consecutive "Read" operations
4. **Wire up start/finish signals** in main.py
5. **Test with a long-running /process** command

## Wording for Collapsed Section

User preference: "say 10 previous commands collapsed or hidden - choose the wording"

Proposed wording (using Markdown italics for subtle appearance):
- `_10 earlier commands collapsed_`
- `_(10 previous commands hidden)_`
- `_... 10 more commands hidden_`

Recommendation: `_(10 earlier commands hidden)_` - clear and compact.

## Testing Plan

1. Run `/process` with multiple input files
2. Verify single message created at start
3. Verify message edits instead of new posts
4. Verify only last 15 commands shown
5. Verify collapse text appears when >15 commands
6. Verify counters work (e.g., "📖 Read 23 files")
7. Verify status changes from "⏳ Processing..." to "✅ Done"
