---
title: "Community Session Ideas"
created: 2026-04-24
updated: 2026-05-15
tags: [ai-shipping-labs, community, ideas, activities, mastermind]
status: draft
---

# Community Session Ideas

Session ideas proposed by AI Shipping Labs community members, recorded so they do not get lost. These are not promises - the filter is whether an idea is useful to others and whether we can run it without too much time investment[^4].

## Memory Layer for AI Agents in Production

A topic to bring to the community: Alexey got a task from a startup to design the memory layer for an AI agent, and wants to learn from people who have already built this in production[^7].

For those who avoided heavy frameworks and built custom memory systems:

- What kind of memory schema worked best for you?
- Do you store full conversations, per-turn summaries, extracted facts, key decisions, or something else?
- What looked smart initially but later became hard to scale or maintain?

Retrieval strategy questions:

- When a user asks something in a new session, how do you reconnect it with relevant past context?
- Do you handle it mostly through the system prompt?
- Or do you dynamically retrieve and inject relevant memory chunks based on the new query?
- How are you deciding what is worth remembering long term?

The goal is practical approaches that actually worked in production[^7]. A research article on production memory implementations (ChatGPT, Claude Code, and 5 other open source systems) is in [memory-layer-implementations](../research/memory-layer-implementations.md). The earlier broader research lives in [agentic-memory](../research/agentic-memory.md).

## Documenting and Refactoring Agent Output (Carlos Pumar)

Carlos Pumar shared two ideas for the next freestyle workshop after the Telepot session[^6]:

- Documenting "learnings" from agent-built projects so they can be reused. When working on a new project with agents, a lot of valuable insights are produced as the agent works. It is hard to decide what to keep and study in greater detail so that next time you understand what the agent has done in the prior project and will probably do in a new one. A workshop showing how Alexey documents these learnings from one project in order to reuse them at a later stage would be useful[^6].
- Refactoring agent-generated code with named software principles. Look at code an agent has produced, walk through it using known software principles, and have the agent refactor it until the code reads as maintainable. The session would pick whatever code the agent has just produced and iterate on it live[^6].

## AI Engineer Job-Hunt Topics (Sai Kumar G)

Sai Kumar G - a member of Alexey's AI Engineering cohort on Maven - replied to Valeriia's outreach with the topics he would like to see covered in the community[^5]:

- Recent AI Engineering interview questions
- Mock interviews and strategy for getting interview calls
- Building personal projects

He framed his own goal as: "I need the plan to build AI project and get the AI Engineer role"[^5].

## How to Pitch Your Idea

A community member proposed a session on how to pitch your idea and how to convey thoughts to different audiences, in a Toastmasters style[^1].

## Using the group learning format

Valeriia's suggestion: run this through the existing group learning format. The person who requested the topic - "how to pitch his ideas" - picks a source himself (a book, a blog post), reads it, finds the information, and then makes a presentation about it. Other members give him feedback and share their own experience[^2].

This pushes the format beyond hard and soft skills. A mastermind has one person's request at the centre. Other participants first ask clarifying questions to enter the context of what has already been done, and only then share their ideas - not just to share personal experience, but to help solve the specific problem in front of them[^2].

## Mastermind moderation

Masterminds have defined rules for how the session should go. Valeriia has participated in one before but has never moderated. She is willing to read up on the format and run the session[^2].

## Cross-cultural note on feedback

A related point from the same conversation: when conveying ideas to different audiences, the feedback styles differ sharply by culture. With Israelis and Germans the feedback is direct - they will simply say they did not like something and will not continue. Americans often do not say this directly. They stay silent. So you do not always know in advance what they thought - they might just need time, or they might have disliked something and will not tell you[^3].

The practical handling: do what you could, wait, and you can ping them once more. If they do not want to, or are not ready, just wait. They may come back to us after some time[^3].

This is worth noting as real-world context for a session on pitching to different audiences.

## How We Handle Community Session Ideas

We do not have to say yes to every idea and commit to running it. The right move is to record the idea and come back to it, because it might still be useful to the person who proposed it. If it turns out to be useful for others too, we can think about how to do it in a way that does not require much of our time but is still valuable for the community. Mastermind-style group sessions are the main example of the kind of format that fits that constraint[^4].

Also relevant: the two people the original conversation was about are both from Sakhalin, which came up as an interesting coincidence while discussing the idea[^2].

## Sources

[^1]: [20260424_104201_AlexeyDTC_msg3597.md](../inbox/used/20260424_104201_AlexeyDTC_msg3597.md)
[^2]: [20260424_104335_AlexeyDTC_msg3600_transcript.txt](../inbox/used/20260424_104335_AlexeyDTC_msg3600_transcript.txt)
[^3]: [20260424_104334_AlexeyDTC_msg3599_transcript.txt](../inbox/used/20260424_104334_AlexeyDTC_msg3599_transcript.txt)
[^4]: [20260424_104335_AlexeyDTC_msg3601_transcript.txt](../inbox/used/20260424_104335_AlexeyDTC_msg3601_transcript.txt)
[^5]: [20260429_104254_valeriia_kuka_msg3723.md](../inbox/used/20260429_104254_valeriia_kuka_msg3723.md)
[^6]: [20260506_090635_AlexeyDTC_msg3866.md](../inbox/used/20260506_090635_AlexeyDTC_msg3866.md)
[^7]: [20260515_063504_AlexeyDTC_msg4024.md](../inbox/used/20260515_063504_AlexeyDTC_msg4024.md)
