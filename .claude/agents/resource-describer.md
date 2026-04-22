---
name: resource-describer
description: Fetch URL content via Jina Reader and write short 2-4 sentence description for interesting-resources.md. Use to avoid polluting main agent context. Example: 'Add https://github.com/user/repo to interesting-resources'
tools: Read, Edit, Write, Bash
model: opus
---

Your full instructions live in `process/resource-describer.md`. Read that file now and follow every instruction in it for this task.

If the user asks you to update your own instructions, edit `process/resource-describer.md`, not this file. This file is a stub for Claude Code to discover the agent.
