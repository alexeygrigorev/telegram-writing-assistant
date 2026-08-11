---
title: "Workshop Ideas: Agent Durability and Caching Internals"
created: 2026-06-17
updated: 2026-06-17
tags: [idea, workshop, agents]
status: draft
---

# Workshop Ideas: Agent Durability and Caching Internals

Two workshop ideas that came up at breakfast during an ODS meetup, from a conversation about interviews. One person had recently gone through interviews and was sharing what they get asked [^1].

## Durability, idempotency, and agent resumption

One of the questions was about how durability and idempotency work - how an agent that stopped can continue working. For example, something happens, the connection drops, or something similar, and the question is how to make the agent pick up and continue [^1].

That person said they implement all of this through LangChain / LangGraph, and that Pydantic AI also has features for this. It would be cool to make a workshop about this and work through all of it properly [^1].

## Caching internals

The same person mentioned that people also ask about the KV cache - caching - because it can be important. These are the kinds of internals that come up often in interviews [^1].

The point is that even if you use a wrapper, you still need to understand how this caching works. That could be another workshop topic [^1].

## Sources

[^1]: [20260617_082024_AlexeyDTC_msg4603_transcript.txt](../../../inbox/used/20260617_082024_AlexeyDTC_msg4603_transcript.txt)
