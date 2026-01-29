---
title: "Streaming JSON Parsing with jaxn"
created: 2026-01-23
updated: 2026-01-29
tags: [json, streaming, python, llm, structured-output, state-machines]
status: draft
---

# Streaming JSON Parsing with jaxn

jaxn is a streaming JSON parser that makes it possible to parse JSON while it's being streamed, particularly useful for LLM applications. The parser was rewritten using a state machine approach for better maintainability and bug fixing[^1].

## The Problem

When you ask an LLM to generate content (like a scary story) without structured output, streaming is straightforward. The tokens arrive one by one and you can display them immediately[^2].

However, when using structured output, the model returns JSON. You can't easily stream JSON directly to users because:
- JSON isn't human-readable until fully parsed
- Users don't want to see raw JSON tokens
- The structure isn't complete until the end[^3]

## The Solution

jaxn allows you to parse JSON on-the-fly while it's streaming and show only the parts the user needs to see. This bridges the gap between LLM structured output and user-friendly streaming responses[^4].

## Why a Custom Parser

The parser was created because existing solutions found online didn't meet the requirements. Since it's used in course materials, reliability is important - students shouldn't encounter broken code when trying to run examples[^5].

## State Machine Rewrite

During course recording, a bug was discovered in the parser. Initial attempts to fix it with GitHub Copilot failed repeatedly - Copilot claimed to fix the issue but the problem persisted. This revealed that the code had become difficult to understand and debug[^6].

The decision was made to rewrite the parser using a state machine approach. Knowledge from a Coursera Automata Theory course (created in 2012-2013) finally proved practically useful after all these years[^7].

The rewrite involved:
- Collaborating with Claude to design the state machine structure
- Creating clearer abstractions within the parser
- Making state transitions more explicit and understandable
- Reducing code complexity through modular design[^8]

While not every design decision was perfect, the result is code that is easier to maintain and debug. Future bugs should be simpler to fix because the state transitions are more transparent[^8].

## Resources

- jaxn repository: [https://github.com/alexeygrigorev/jaxn](https://github.com/alexeygrigorev/jaxn)
- State machine documentation: [https://github.com/alexeygrigorev/jaxn/blob/main/states.md](https://github.com/alexeygrigorev/jaxn/blob/main/states.md)
- Automata Theory course: [https://online.stanford.edu/courses/soe-ycsautomata-automata-theory](https://online.stanford.edu/courses/soe-ycsautomata-automata-theory)

## Sources

- [20260123_121522_valeriia_kuka_msg459.md](../inbox/raw/20260123_121522_valeriia_kuka_msg459.md)
- [20260123_121522_valeriia_kuka_msg460_file.md](../inbox/raw/20260123_121522_valeriia_kuka_msg460_file.md)
- [20260123_121522_valeriia_kuka_msg461_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg461_transcript.txt)
- [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
- [20260123_121522_valeriia_kuka_msg463_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg463_transcript.txt)
- [20260129_171834_AlexeyDTC_msg643_transcript.txt](../inbox/raw/20260129_171834_AlexeyDTC_msg643_transcript.txt)
- [20260129_172109_AlexeyDTC_msg644_transcript.txt](../inbox/raw/20260129_172109_AlexeyDTC_msg644_transcript.txt)
- [20260129_172305_AlexeyDTC_msg645_transcript.txt](../inbox/raw/20260129_172305_AlexeyDTC_msg645_transcript.txt)
- [20260129_172432_AlexeyDTC_msg646.md](../inbox/raw/20260129_172432_AlexeyDTC_msg646.md)
- [20260129_172533_AlexeyDTC_msg647_transcript.txt](../inbox/raw/20260129_172533_AlexeyDTC_msg647_transcript.txt)

[^1]: [20260129_172432_AlexeyDTC_msg646.md](../inbox/raw/20260129_172432_AlexeyDTC_msg646.md)
[^2]: [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
[^3]: [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
[^4]: [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
[^5]: [20260129_172305_AlexeyDTC_msg645_transcript.txt](../inbox/raw/20260129_172305_AlexeyDTC_msg645_transcript.txt)
[^6]: [20260129_171834_AlexeyDTC_msg643_transcript.txt](../inbox/raw/20260129_171834_AlexeyDTC_msg643_transcript.txt)
[^7]: [20260129_172533_AlexeyDTC_msg647_transcript.txt](../inbox/raw/20260129_172533_AlexeyDTC_msg647_transcript.txt)
[^8]: [20260129_172109_AlexeyDTC_msg644_transcript.txt](../inbox/raw/20260129_172109_AlexeyDTC_msg644_transcript.txt)
