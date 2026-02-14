---
title: "YC Guide to Vibe Coding and AI Workflow Optimization"
created: 2026-02-10
updated: 2026-02-10
tags: [research, yc, vibe-coding, claude-code, workflow, ai-tools]
status: draft
---

# YC Guide to Vibe Coding and AI Workflow Optimization

Practical patterns from Y Combinator founders on working effectively with AI coding tools like Claude Code, Cursor, and Windsurf.

## What I Want to Understand

The proven workflows that founders use to build products with AI assistance. These aren't theoretical - they're battle-tested patterns from YC companies shipping real software.

## Planning Process

- Create a comprehensive plan: Start by working with the AI to write a detailed implementation plan in a markdown file
- Review and refine: Delete unnecessary items, mark features as won't do if too complex
- Maintain scope control: Keep a separate section for ideas for later to stay focused
- Implement incrementally: Work section by section rather than attempting to build everything at once
- Track progress: Have the AI mark sections as complete after successful implementation
- Commit regularly: Ensure each working section is committed to Git before moving to the next

## Version Control Strategies

- Use Git religiously: Don't rely solely on the AI tools' revert functionality
- Start clean: Begin each new feature with a clean Git slate
- Reset when stuck: Use git reset --hard HEAD if the AI goes on a vision quest
- Avoid cumulative problems: Multiple failed attempts create layers of bad code
- Clean implementation: When you finally find a solution, reset and implement it cleanly

## Testing Framework

- Prioritize high-level tests: Focus on end-to-end integration tests over unit tests
- Simulate user behavior: Test features by simulating someone clicking through the site/app
- Catch regressions: LLMs often make unnecessary changes to unrelated logic
- Test before proceeding: Ensure tests pass before moving to the next feature
- Use tests as guardrails: Some founders recommend starting with test cases to provide clear boundaries

## Effective Bug Fixing

- Leverage error messages: Simply copy-pasting error messages is often enough for the AI
- Analyze before coding: Ask the AI to consider multiple possible causes
- Reset after failures: Start with a clean slate after each unsuccessful fix attempt
- Implement logging: Add strategic logging to better understand what's happening
- Switch models: Try different AI models when one gets stuck
- Clean implementation: Once you identify the fix, reset and implement it on a clean codebase

## AI Tool Optimization

- Create instruction files: Write detailed instructions for your AI in appropriate files (cursor.rules, windsurf.rules, claude.md)
- Local documentation: Download API documentation to your project folder for accuracy
- Use multiple tools: Some founders run both Cursor and Windsurf simultaneously on the same project
- Tool specialization: Cursor is faster for frontend work, while Windsurf thinks longer
- Compare outputs: Generate multiple solutions and pick the best one

## Complex Feature Development

- Create standalone prototypes: Build complex features in a clean codebase first
- Use reference implementations: Point the AI to working examples to follow
- Clear boundaries: Maintain consistent external APIs while allowing internal changes
- Modular architecture: Service-based architectures with clear boundaries work better than monorepos

## Tech Stack Considerations

- Established frameworks excel: Ruby on Rails works well due to 20 years of consistent conventions
- Training data matters: Newer languages like Rust or Elixir may have less training data
- Modularity is key: Small, modular files are easier for both humans and AIs to work with
- Avoid large files: Don't have files that are thousands of lines long

## Beyond Coding

- DevOps automation: Use AI for configuring servers, DNS, and hosting
- Design assistance: Generate favicons and other design elements
- Content creation: Draft documentation and marketing materials
- Educational tool: Ask the AI to explain implementations line by line
- Use screenshots: Share UI bugs or design inspiration visually
- Voice input: Tools like Aqua enable 140 words per minute input

## Continuous Improvement

- Regular refactoring: Once tests are in place, refactor frequently
- Identify opportunities: Ask the AI to find refactoring candidates
- Stay current: Try every new model release
- Recognize strengths: Different models excel at different tasks

## Claude Code Workflow Patterns

### Give It Memory

- At the start of every session, read your memory file before responding to the first message
- Save preferences as they're learned. When corrected, persist the correction immediately
- Without this, every session starts from zero - re-explaining stack, style, and rules

### Build a System That Scales

- Keep the memory index under 60 lines. If a topic needs more than 2 lines, create a linked file: lessons.md, preferences.md, [project].md
- When told to save memory, categorize each item and route it to the right file automatically
- Every 10 sessions, deduplicate and condense all memory files. Prune anything outdated

### Build Multi-Agent Teams

- The coordinator plans, delegates, and reviews. It never writes code directly
- Use Codex for code tasks and a research model for writing. Write a plan file before launching any worker
- One model doing everything sequentially is slow. Two workers in parallel, split by domain, is fast

### Show Work

- Never go silent for more than 60 seconds. Print what phase you're in before and after every step
- If something fails, show the exact error. Long tasks fail silently
- Phase markers before and after each step. When it dies, you know exactly where

### Automate Workflows

- Save prompts as slash commands. Run the full sequence end to end without stopping for approval
- If you type the same 5-step prompt more than twice, it should be a single command
- Compound workflows turn 20 minutes of prompting into one line

### Let Claude Maintain Itself

- Run memory maintenance every X days. Deduplicate entries, prune stale references, keep all files under their line limits
- Scheduled cleanup means your workspace stays organized without manual intervention
- Without maintenance, memory files bloat, old context piles up, and quality degrades

## Notes

The common theme: structure over improvisation. The most effective workflows have systems for memory, version control, testing, and automation. The AI is powerful, but it needs guardrails to work consistently at scale.

Key insight: complexity in the system, simplicity in the workflow. Spend time upfront building these patterns, then they become invisible during daily use.

## Sources

[^1]: [20260209_183721_AlexeyDTC_msg1251_photo.md](../../inbox/used/20260209_183721_AlexeyDTC_msg1251_photo.md)
[^2]: [20260209_183728_AlexeyDTC_msg1252_photo.md](../../inbox/used/20260209_183728_AlexeyDTC_msg1252_photo.md)
[^3]: [20260209_183733_AlexeyDTC_msg1253.md](../../inbox/used/20260209_183733_AlexeyDTC_msg1253.md)
[^4]: [20260209_183752_AlexeyDTC_msg1254_transcript.txt](../../inbox/used/20260209_183752_AlexeyDTC_msg1254_transcript.txt)
[^5]: [20260209_183811_AlexeyDTC_msg1255_transcript.txt](../../inbox/used/20260209_183811_AlexeyDTC_msg1255_transcript.txt)
[^6]: [20260210_082618_AlexeyDTC_msg1262_photo.md](../../inbox/used/20260210_082618_AlexeyDTC_msg1262_photo.md)
