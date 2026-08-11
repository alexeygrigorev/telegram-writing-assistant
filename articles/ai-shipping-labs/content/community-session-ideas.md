---
title: "Community Session Ideas"
created: 2026-04-24
updated: 2026-07-03
tags: [ai-shipping-labs, community, ideas, activities, mastermind]
status: draft
---

# Community Session Ideas

Session ideas proposed by AI Shipping Labs community members, recorded so they do not get lost. These are not promises. The filter is whether an idea is useful to others. We also check whether we can run it without too much time investment[^4].

## Memory Layer for AI Agents in Production

A topic I want to bring to the community. I got a task from a startup to design the memory layer for an AI agent. I want to learn from people who have already built this in production[^7].

For those who avoided heavy frameworks and built custom memory systems:

- What kind of memory schema worked best for you?
- Do you store full conversations, per-turn summaries, extracted facts, key decisions, or something else?
- What looked smart initially but later became hard to scale or maintain?

Retrieval strategy questions:

- When a user asks something in a new session, how do you reconnect it with relevant past context?
- Do you handle it mostly through the system prompt?
- Or do you dynamically retrieve and inject relevant memory chunks based on the new query?
- How are you deciding what is worth remembering long term?

I want to focus on practical approaches that worked in production[^7].

The research on this lives in two places:

- [memory-layer](../../research/memory-layer.md) consolidates the production implementations and earlier broader research.

## Documenting and Refactoring Agent Output (Carlos Pumar)

Carlos Pumar shared two ideas for the next freestyle workshop after the Telepot session[^6]:

- Documenting "learnings" from agent-built projects so they can be reused. When working on a new project with agents, a lot of valuable insights are produced as the agent works. It is hard to decide what to keep and study in detail. A workshop showing how I document these learnings from one project to reuse them later would be useful[^6].
- Refactoring agent-generated code with named software principles. Look at code an agent has produced, walk through it using known software principles, and have the agent refactor it. The session would pick whatever code the agent has just produced and iterate on it live[^6].

## AI Engineer Job-Hunt Topics (Sai Kumar G)

Sai Kumar G is a member of my AI Engineering cohort on Maven.

He replied to Valeriia's outreach with the topics he would like to see covered[^5]:

- Recent AI Engineering interview questions
- Mock interviews and strategy for getting interview calls
- Building personal projects

He framed his own goal as needing a plan to build an AI project and get the AI Engineer role[^5].

## Mock interview and resume review sessions

Members in the community keep asking us to build mock interviews for them. Here is how I would run these[^8].

Resume review session: people come and share their resumes, I look at them and give feedback. We can fix resumes and work through them together. If you cannot attend live, you can send your resume in advance. I know a lot of people are interviewing right now, so we can go through their resumes[^8].

Mock interview session: find volunteers and run a two-hour session. Each person gets a 45-minute interview followed by a 15-minute debrief, then the next person gets another 45-minute interview and a 15-minute debrief. So I need to find two people and run it for them, or run several such sessions. I could run this kind of mock interview myself[^8].

## Interview prep topics requested by a member

A member suggested sessions for interview prep, mock sessions, and project walkthroughs. Alexey already has strong interview prep resources on the website that could be used, or members could bring their own[^9].

The skillsets and requirements for AI engineers and data scientists keep evolving constantly (most recently Forward Deployed Engineers), so such sessions could range across[^9]:

- Python coding - most companies still filter based on Leetcode DSA-style problems
- Technical deep dive - attention mechanisms, autoregressive models, deep learning algorithms in general
- Case studies - Gen AI systems, system design, scaling

The member noted this is based on what they observed for roles in the U.S. The suggestion is to discuss with Alexey and Valeriia to see if this is possible and figure out logistics[^9].

## Book-reading sprints

Another member proposed book-reading sprints alongside the technical sessions. There are several books and long-form resources many members want to read but struggle to finish consistently, for example[^10]:

- LLM Handbook
- AI Engineering by Chip Huyen
- Hamel Husain's work on evaluations (Evals)
- Other high-quality papers, blogs, and engineering handbooks

A sprint could work similarly to the coding sprints[^10]:

- Read a fixed number of chapters or pages each week
- Hold a weekly discussion or Q&A
- Share key takeaways, notes, and implementation ideas
- End with a small project or presentation applying what was learned

The goal is to help members build deeper understanding, stay accountable, and learn from one another rather than reading everything alone. It could become a great complement to the hands-on engineering curriculum[^10].

These interview and learning ideas were also discussed on a recent community call[^11].

## System design sessions with an AI interviewer

An idea for AI Shipping Labs: get together every so often and do system design together. It is all geared toward interview preparation. We take some project and do the system design for it - either a plain system or an AI system[^12].

The twist is that I want the AI to be my grader. The plan is to build an AI system that can give feedback and act as my interviewer. It would grill me hard and ask questions exactly like a real interviewer would[^12].

## Pitching ideas to different audiences

A community member proposed a Toastmasters-style session on how to pitch your idea and convey thoughts to different audiences[^1].

## Using the group learning format

Valeriia's suggestion is to run this through the existing group learning format. The person who requested the topic picks a source himself - a book or a blog post. He reads it and makes a presentation about it. Other members give him feedback and share their own experience[^2].

This pushes the format beyond hard and soft skills. A mastermind has one person's request at the centre. Other participants first ask clarifying questions to enter the context. Then they share their ideas - not just personal experience, but help solving the specific problem in front of them[^2].

## Mastermind moderation

Masterminds have defined rules for how the session should go. Valeriia has participated in one before but has never moderated. She is willing to read up on the format and run the session[^2].

## Cross-cultural note on feedback

A related point from the same conversation. When conveying ideas to different audiences, feedback styles differ sharply by culture. With Israelis and Germans the feedback is direct. They will simply say they did not like something and will not continue.

Americans often do not say this directly. They stay silent. You do not always know in advance what they thought. They might just need time, or they might have disliked something and not tell you[^3].

In practice, do what you can, wait, and ping them once more. If they do not want to, or are not ready, just wait. They may come back to us after some time[^3].

This is worth noting as real-world context for a session on pitching to different audiences.

## Filter for new ideas

We do not have to say yes to every idea and commit to running it. The right move is to record it and come back later. The recording is still useful to the person who proposed it.

If the topic is useful for others too, we can think about how to run it in a low-cost way. Mastermind-style group sessions are the main example of a format that fits that constraint[^4].

As a side note, the two people the original conversation was about are both from Sakhalin. An interesting coincidence that came up while discussing the idea[^2].

## Sources

[^1]: [20260424_104201_AlexeyDTC_msg3597.md](../../../inbox/used/20260424_104201_AlexeyDTC_msg3597.md)
[^2]: [20260424_104335_AlexeyDTC_msg3600_transcript.txt](../../../inbox/used/20260424_104335_AlexeyDTC_msg3600_transcript.txt)
[^3]: [20260424_104334_AlexeyDTC_msg3599_transcript.txt](../../../inbox/used/20260424_104334_AlexeyDTC_msg3599_transcript.txt)
[^4]: [20260424_104335_AlexeyDTC_msg3601_transcript.txt](../../../inbox/used/20260424_104335_AlexeyDTC_msg3601_transcript.txt)
[^5]: [20260429_104254_valeriia_kuka_msg3723.md](../../../inbox/used/20260429_104254_valeriia_kuka_msg3723.md)
[^6]: [20260506_090635_AlexeyDTC_msg3866.md](../../../inbox/used/20260506_090635_AlexeyDTC_msg3866.md)
[^7]: [20260515_063504_AlexeyDTC_msg4024.md](../../../inbox/used/20260515_063504_AlexeyDTC_msg4024.md)
[^8]: [20260703_132055_AlexeyDTC_msg4674_transcript.txt](../../../inbox/used/20260703_132055_AlexeyDTC_msg4674_transcript.txt)
[^9]: [20260703_132056_AlexeyDTC_msg4675.md](../../../inbox/used/20260703_132056_AlexeyDTC_msg4675.md)
[^10]: [20260703_132117_AlexeyDTC_msg4678.md](../../../inbox/used/20260703_132117_AlexeyDTC_msg4678.md)
[^11]: [20260703_132200_AlexeyDTC_msg4680.md](../../../inbox/used/20260703_132200_AlexeyDTC_msg4680.md)
[^12]: [20260703_160455_AlexeyDTC_msg4688_transcript.txt](../../../inbox/used/20260703_160455_AlexeyDTC_msg4688_transcript.txt)
