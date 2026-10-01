# Aplexer messaging capture

Source: https://github.com/PocketShell-io/aplexer/blob/main/src/bin/aplexer/message_commands.rs

Run outcome: real local CLI output from aplexer 0.1.9, rendered as a PNG with Pillow. The exact transcript is in `message-inbox.txt`.

Two Bash sessions, tagged `builder` and `review`, were started in a temporary workspace. `APLEXER_RUNTIME_DIR`, `APLEXER_STATE_DIR`, and `APLEXER_CONFIG` all pointed to temporary locations. Inherited `APLEXER_*` variables were removed before starting the demo. No existing sessions or mailboxes were used.

Commands:

```bash
a start --tag builder --json -- bash --norc
a start --tag review --json -- bash --norc
a message send --from builder --to review 'Implementation is ready. Please review the diff.'
a message inbox --from review
a message ack --from review <message-id>
a message inbox --from review
```

The message ID came from the real inbox output. Both sessions were killed after capture, and the temporary directories were removed.

`message-inbox.png` shows the send, inbox, acknowledgement, and empty inbox outputs. The image wraps long lines for readability. It demonstrates mailbox behavior with shell sessions; no model or external service was invoked, and it does not demonstrate automatic agent wake-up or review execution.
