---
title: "Streaming JSON Parsing with jaxn"
created: 2026-01-23
updated: 2026-01-23
tags: [json, streaming, python, llm, structured-output]
status: draft
---

# Streaming JSON Parsing with jaxn

jaxn is a streaming parser that makes it possible to parse JSON while it's being streamed, particularly useful for LLM applications.

## The Problem

When you ask an LLM to generate content (like a scary story) without structured output, streaming is straightforward. The tokens arrive one by one and you can display them immediately[^1].

However, when using structured output, the model returns JSON. You can't easily stream JSON directly to users because:
- JSON isn't human-readable until fully parsed
- Users don't want to see raw JSON tokens
- The structure isn't complete until the end[^2]

## The Solution

jaxn allows you to parse JSON on-the-fly while it's streaming and show only the parts the user needs to see. This bridges the gap between LLM structured output and user-friendly streaming responses[^3].

## Demo

A demonstration is available showing how to use jaxn for streaming JSON from LLM responses.

## Sources

- [20260123_121522_valeriia_kuka_msg459.md](../inbox/raw/20260123_121522_valeriia_kuka_msg459.md)
- [20260123_121522_valeriia_kuka_msg460_file.md](../inbox/raw/20260123_121522_valeriia_kuka_msg460_file.md)
- [20260123_121522_valeriia_kuka_msg461_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg461_transcript.txt)
- [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
- [20260123_121522_valeriia_kuka_msg463_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg463_transcript.txt)

[^1]: [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
[^2]: [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
[^3]: [20260123_121522_valeriia_kuka_msg462_transcript.txt](../inbox/raw/20260123_121522_valeriia_kuka_msg462_transcript.txt)
