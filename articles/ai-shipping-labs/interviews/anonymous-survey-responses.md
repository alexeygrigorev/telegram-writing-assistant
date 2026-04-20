---
title: "Interview: Anonymous Survey Responses"
person: Multiple anonymous respondents
persona: Undetermined
created: 2026-04-10
updated: 2026-04-10
tags: [ai-shipping-labs, interview, community]
status: draft
---

# Interview: Anonymous Survey Responses

Responses to the community survey where the respondent is not named. Each section is a separate person.

## Persona

Undetermined for all responses in this file - the survey did not capture enough background about each respondent to map them to a specific persona.

See [personas.md](../personas.md) for full persona definitions.

## Response 1: OpenClaw topics

One member said the hottest topic at the moment is OpenClaw, so anything related to that is interesting[^13].

## Response 2: Inference and local models

Another member is curious about inference and how to run models locally on cheaper machines. They recommended starting with the Baseten inference engineering book (https://www.baseten.co/inference-engineering/) and an interview with Scott Hanselman (https://www.youtube.com/watch?v=lcC1rtHjDrw). They are also interested in hearing from someone who has taken an AI product to production as a side income - their learnings, gotchas, and starting points[^14].

## Response 3: Keeping up with the buzz

One member wants to discuss relevant topics but also the challenges people face with the constant buzz of new tools, frameworks, and paradigms. Despite trying to keep up, they feel constantly behind, and it can be overwhelming[^15].

## Response 4: MCP and multi-agent workflows

One member wants to learn about writing custom MCP (Model Context Protocol) servers, particularly for long-term memory and context storage. They see the biggest bottleneck in AI-assisted coding as managing context without blowing out the context window with bloated .md files[^16].

Specific topics they want tutorials or deep dives on[^16]:

- Building a persistent memory bridge - how to write a local MCP server (using SQLite, pgvector, etc.) to store state across sessions
- Multi-agent workflows - how to use shared memory to set up a "Worker/Supervisor" dynamic, for example showing how Gemini can act as the executor writing drafts to the MCP context while another model like Codex or Claude reads that same memory space to act as a reviewer

They haven't built this themselves yet, but learning how to construct a shared brain so multiple models can collaborate and iterate on the same project is what they hope to get from the community[^16].

## Sources

[^13]: [20260410_184334_AlexeyDTC_msg3359.md](../../../inbox/used/20260410_184334_AlexeyDTC_msg3359.md)
[^14]: [20260410_184350_AlexeyDTC_msg3361.md](../../../inbox/used/20260410_184350_AlexeyDTC_msg3361.md)
[^15]: [20260410_184358_AlexeyDTC_msg3363.md](../../../inbox/used/20260410_184358_AlexeyDTC_msg3363.md)
[^16]: [20260410_184425_AlexeyDTC_msg3365.md](../../../inbox/used/20260410_184425_AlexeyDTC_msg3365.md)
