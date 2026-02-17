---
title: "Writing Assistant Feedback"
created: 2026-02-17
updated: 2026-02-17
tags: [telegram-writing-assistant, feedback, improvements]
status: draft
---

# Writing Assistant Feedback

Collection of feedback and improvement ideas for the Telegram writing assistant bot. Saved here so nothing gets lost and can be acted upon later. There is already a GitHub issue for this work - just need to sit down and deal with all of it.[^5]

## Article Index Navigation

This was already mentioned in one of the GitHub issues. There are many articles now, and to understand what each article is about, you have to open each one individually and read what's inside.[^1]

For the beginning this is fine - it's even good because it allows giving feedback (e.g., content placed in the wrong article, content that should be in a different article). But overall, the navigation is not convenient.[^1]

What would help:[^1]
- An index sorted by "last updated," with the most recently updated articles at the top
- An indication of what event or context each article relates to. For example: "you say three articles can come from yesterday's webinar, I open the list, and honestly I can't tell which ones relate to the webinar"
- A chronology of processing: what messages were recorded, what files were changed or created as a result

When working together in a conversation, this chronology exists in the user's head. But when the bot is separate and there are many messages, it's hard to track what was recorded and what relates to what.[^1]

## Hard to Understand Article Purpose

For example, there are several articles about "AI Engineer" in the repository. Some were prepared to record ideas about the role. Some, like "AI Roles Now and Then," capture content about roles in a data team. It's sometimes hard to understand which article is meant for what purpose.[^2]

## Excessive Section Splitting

This is not critical, but if we're talking about optimizing to reduce the time spent on editing articles: the bot sometimes splits articles into too many sections. For example, in the SQLiteSearch article, there's a brief description (which is good), and then a separate section about the library's naming history. That naming detail doesn't need its own section - it's not a separate topic or critical information. It could just be mentioned inline.[^3]

Sometimes the section splitting is convenient because it helps understand what each part is about (e.g., "this part is about renaming, this part is about API design"). But overall, the splitting is often excessive compared to how a person would structure the article. Optimization would mean splitting less frequently.[^3]

## Alternative Processing Approach

One idea: have two separate processes.[^4]
1. The current process where the agent processes messages and creates articles
2. A second process where the user prepares the article structure (what sections should be included), and the agent fills that structure based on what's already on GitHub. If there's no information for a section, it should leave it empty.

The concern is that LLMs tend to want an answer for everything, which might lead to hallucination - filling in sections where there's no actual content. But it's worth trying.[^4]

The most useful improvement would be making it easier to understand what each article relates to.[^4]

## Sources

[^1]: [20260217_083630_AlexeyDTC_msg1867_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1867_transcript.txt)
[^2]: [20260217_083630_AlexeyDTC_msg1868_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1868_transcript.txt)
[^3]: [20260217_083630_AlexeyDTC_msg1869_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1869_transcript.txt)
[^4]: [20260217_083630_AlexeyDTC_msg1870_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1870_transcript.txt)
[^5]: [20260217_083710_AlexeyDTC_msg1871_transcript.txt](../inbox/used/20260217_083710_AlexeyDTC_msg1871_transcript.txt)
