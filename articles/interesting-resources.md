---
title: "Interesting Resources"
created: 2026-01-31
updated: 2026-01-31
tags: [resources, tools, ai, development]
status: draft
---

# Interesting Resources

A collection of interesting resources curated for the "Alexey On Data" newsletter and beyond.

<figure>
  <img src="../assets/images/interesting-resources/substack-resources-section.jpg" alt="Interesting Resources section in the newsletter">
  <figcaption>The Interesting Resources section as it appears in the Alexey On Data newsletter on Substack</figcaption>
  <!-- This shows the format and presentation of resources in the newsletter -->
</figure>

## AI Development Tools

### Claude Code and Large-Context Reasoning

Materials from a hands-on O'Reilly Live Learning course by Tim Warner. Teaches how to build production-ready AI-assisted development workflows with Claude Code. Covers large-context reasoning, MCP-based persistent memory, agents, and custom skills, with practical examples for code review, automation, and CI/CD[^1].

### awesome-slash

A curated GitHub list of tools, patterns, and projects built around slash-command interfaces. A practical reference for anyone designing command-driven workflows, bots, or developer tools that rely on concise, action-oriented commands instead of complex UIs[^1].

## CLI Tools

### Codex

An AI-powered CLI tool by antirez for complex debugging, code analysis, and technical questions. Useful when encountering difficult problems that would benefit from a second perspective or deep analysis[^2].

Key features:
- File-based input/output pattern for complex questions
- Debugging subtle bugs (bitstream alignment, off-by-one errors)
- Analyzing complex algorithms against specifications
- Getting detailed code reviews with specific bug identification

Usage pattern:
```bash
cat /tmp/question.txt | codex exec -o /tmp/reply.txt --full-auto
```

## How This Article Works

This article collects resources shared via Telegram. When a link is sent with the "resource" marker, it gets added here. Orphaned links (links without context) that don't relate to ongoing conversations are also collected here[^3][^4].

## Sources

[^1]: [20260131_191039_AlexeyDTC_msg741_photo.md](../inbox/raw/20260131_191039_AlexeyDTC_msg741_photo.md)
[^2]: [https://gist.github.com/antirez/2e07727fb37e7301247e568b6634beff](https://gist.github.com/antirez/2e07727fb37e7301247e568b6634beff)
[^3]: [20260131_191025_AlexeyDTC_msg739_transcript.txt](../inbox/raw/20260131_191025_AlexeyDTC_msg739_transcript.txt)
[^4]: [20260131_191153_AlexeyDTC_msg745_transcript.txt](../inbox/raw/20260131_191153_AlexeyDTC_msg745_transcript.txt)
