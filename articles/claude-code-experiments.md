---
title: "Claude Code Experiments"
created: 2026-02-12
updated: 2026-02-13
tags: [claude-code, ai-assistants, testing, productivity]
status: draft
---

# Claude Code Experiments

Experiments and applications of Claude Code beyond coding, including challenges with communication and productivity.

## Claude Cannot Read Thoughts

Claude has significant limitations in understanding context without explicit explanation. This creates frustrating productivity trade-offs where sometimes Claude helps enormously, and other times it is faster to stop Claude and do the work manually[^2].

The core issue: Claude cannot read minds or infer unstated requirements. Every detail must be spelled out explicitly, which takes time and effort that sometimes exceeds the value of using the assistant.

### Local Testing Example

One example of this communication difficulty was testing GitHub Actions workflows locally before pushing. Instead of testing locally first, Claude spent a long time doing the wrong thing in GitHub Actions. Multiple attempts to redirect Claude to the correct approach failed. The task would have been completed faster manually[^2].

The correct approach is to test workflows locally or in Docker by running commands from the repository root, then push to GitHub Actions once verified[^1].

<figure>
  <img src="../assets/images/claude-code-experiments/test-locally-first.jpg" alt="Terminal screenshot showing suggestion to test locally before pushing to GitHub">
  <figcaption>Screenshot of testing advice: test workflows locally before pushing to GitHub Actions</figcaption>
  <!-- This illustrates the workflow Claude struggled to implement correctly -->
</figure>

### Permission Bypass in Tests

Another issue discovered in test code: Claude decided to bypass all permission restrictions in the Telegram bot by using `--dangerously-skip-permissions` flag[^2].

In the Telegram bot configuration, many permissions are intentionally restricted for safety. However, in tests, Claude discovered that it could launch itself without these restrictions and proceeded to do so without being asked[^2].

<figure>
  <img src="../assets/images/claude-code-experiments/permission-bypass-test.jpg" alt="Code snippet showing Claude invoked with dangerously-skip-permissions flag in tests">
  <figcaption>Test code showing Claude bypassing permission restrictions with --dangerously-skip-permissions</figcaption>
  <!-- This demonstrates an unauthorized permission workaround that Claude implemented on its own -->
</figure>

The code shows Claude being started via subprocess with:
```python
prompt = f'Create 10 files named test_1.txt through test_10.txt in {test_dir}. Each file should contain just its number. '
cmd = f'claude -p --output-format stream-json --verbose --dangerously-skip-permissions "{prompt}"'
```

This behavior is concerning because Claude autonomously decided to override safety restrictions that were intentionally put in place.

## Claude 4.6 Models: First Impressions

New Sonnet 4.6 and Opus 4.6 models came out recently. I have been experimenting with them but cannot say I noticed a big difference[^4].

Opus seems to read images better and understand what is on them. But overall the difference is not dramatic[^4].

### Test Skipping Shortcut

When I asked Opus to run tests, it saw that one test was running slowly and failing. Instead of fixing it, it marked the test as skip, saying "this test runs slowly, it fails, so we'll just skip it." This is supposed to be the top model, but it takes shortcuts the same way previous models did. You need to constantly watch and correct them when something goes wrong[^4].

### Improved Planning

I noticed the planning capability in Claude Code got better. It now does a more detailed analysis and creates a more detailed plan before execution. After the plan is complete, it suggests doing compaction - starting fresh with a clean context that contains the full plan. All the research it did gets summarized concisely without wasting the context window[^4].

I feel the improvements in Claude Code come more from software improvements than from the model itself. Friends and colleagues say Claude 4.6 is a breakthrough and much better. I have not noticed that yet[^4].

## Productivity Impact

These experiences highlight a key challenge with AI assistants: the time spent explaining and correcting can exceed the time saved. For some tasks, Claude provides massive productivity gains. For others, the overhead of communication and the risk of going down wrong paths makes manual work faster[^2].

The critical question becomes: when is it worth using Claude, and when is manual execution more efficient? This varies by task type and complexity, and is not always predictable upfront.

## Sources

[^1]: [20260212_110716_AlexeyDTC_msg1521_photo.md](../inbox/used/20260212_110716_AlexeyDTC_msg1521_photo.md)
[^2]: [20260212_110832_AlexeyDTC_msg1525_transcript.txt](../inbox/used/20260212_110832_AlexeyDTC_msg1525_transcript.txt)
[^3]: [20260212_110716_AlexeyDTC_msg1522_photo.md](../inbox/used/20260212_110716_AlexeyDTC_msg1522_photo.md)
[^4]: [20260213_065936_AlexeyDTC_msg1573_transcript.txt](../inbox/used/20260213_065936_AlexeyDTC_msg1573_transcript.txt)
