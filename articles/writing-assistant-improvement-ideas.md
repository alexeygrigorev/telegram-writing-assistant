---
title: "Writing Assistant Improvement Ideas"
created: 2026-02-17
updated: 2026-02-20
tags: [telegram-writing-assistant, feedback, improvements]
status: draft
---

# Writing Assistant Improvement Ideas

Collection of feedback and improvement ideas for the Telegram writing assistant bot. Saved here so nothing gets lost and can be acted upon later. There is already a [GitHub issue](https://github.com/alexeygrigorev/telegram-writing-assistant/issues/1) tracking this work - just need to sit down and deal with all of it.[^5][^6]

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

## Content Routing and Categorization (GitHub Issue #1)

The agent processes voice messages from Telegram, transcribes them, and writes output into the articles/ folder. It also attempts to categorize content into articles, update existing articles if a new message is related, and create new articles if no related one exists.[^6]

### Current issues

1. Feedback and meta-comments are treated as articles. Messages containing feedback on how the agent behaves, instructions on how it should work, or comments about system behavior get written into articles/, even though they are not content.[^6]

2. Raw ideas are indistinguishable from active work. Some messages are early, unstructured ideas, notes not connected to any existing article, or thoughts that should be stored for later and not developed immediately. These end up as new articles or merged into existing ones, which is misleading.[^6]

3. The articles/ folder is overloaded. It currently contains drafts meant for newsletters or social media, meta feedback, and raw idea dumps. This makes it harder to reason about what content is production-bound vs exploratory vs meta.[^6]

### Desired behavior

Separate content by intent:[^6]

1. articles/ - Only content related to active ideas or processes already being worked on. Content that will be edited further and used primarily for the newsletter, and possibly for social media. New messages should update an existing article only if they clearly relate to an ongoing article. New articles should be created only if the content represents a concrete idea or process, not meta discussion or raw brainstorming.

2. feedback/ - Store all feedback, comments, and instructions directed at the agent. Includes comments about how the agent works or should work, requests to change behavior or logic, and meta discussion about the system. These messages should never be merged into articles. They should be stored as standalone notes for later review.

3. ideas/ (or ideas marker inside articles/) - Store raw, undeveloped ideas that are not yet part of any active article. Includes brain dumps, early thoughts, and standalone ideas without a clear process or structure. These should not automatically become full articles. They should be stored for future reference. If kept inside articles/, they must be clearly marked as "idea" or similar.

### Examples of mixed content

The articles folder currently has content that arguably belongs elsewhere. For example, [task-management-app-idea.md](task-management-app-idea.md) and [telegram-bot-server-migration.md](telegram-bot-server-migration.md) - these are internal ideas and implementation stories that sit alongside articles meant for the newsletter. They won't be shared publicly, and there won't be newsletter issues about them. Currently, embryonic ideas and ready articles live in the same place, mixed with ideas that will probably never be published - like detailed marketing plans for the paid community.[^10][^11][^12]

On the other hand, some of these internal ideas might eventually become published articles, so the line isn't always clear-cut. There are feedback and articles categories but no ideas category. It works as is for now.[^13][^14]

These issues were previously recorded as GitHub issues. If they don't make sense to implement, they can just be closed.[^14]

### Proposed folder restructuring

Alexey agrees that separating internal and external content makes sense. The research folder already exists as a first step. The broader vision for the structure:[^15]

- A resources folder with its own index
- A folder for external/public articles with its own index
- A folder for internal articles with its own index
- The existing research folder

The bot would need to categorize content as internal or external, and then look at the right index. It would need to keep multiple indexes in mind. Each index would describe what belongs in that folder so the bot doesn't get confused.[^15]

This separation makes sense. The understanding of what the structure should look like is now more concrete. Will get back to implementing this after the current focus on the course is done.[^15]

## Resource Index Table

This has been hanging as a pending item. The question was: what exactly needs to be done and what's the workflow for implementing it? Where should it live - in the bot or somewhere else?[^7]

Inside the articles folder there is an index - a table showing when an article was added, when it was last updated, and a short description. The idea is to do the same thing for all resources shared via the bot. Right now resources are just a list with short descriptions. The proposed format is a table with:[^8]
- Resource name
- Category
- Short description
- Date when the resource was added
- Status: backlog or published

This way the table preserves a record of resources, making it clear what has been shared and what hasn't. This is what the issue is about.[^8]

How to use this afterwards: automatic updates from Substack won't work because Substack has no API. The workflow would be manual - updating the table to mark what was already published, or sending the bot a list (just copy from the newsletter) and saying "these resources were already published, mark as published."[^9]

Where to use it: on the website, in the resources section where there's a grid of resources. New published resources would get added there.[^9]

## Keyword-Based Input Categorization

An idea for helping the bot categorize content: when sending a message, include a keyword like "idea", "research", or "article" to tell the bot how to classify the input.[^16][^17]

This would replace the current approach where the bot tries to infer the intent from the content alone.

## Sources

[^1]: [20260217_083630_AlexeyDTC_msg1867_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1867_transcript.txt)
[^2]: [20260217_083630_AlexeyDTC_msg1868_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1868_transcript.txt)
[^3]: [20260217_083630_AlexeyDTC_msg1869_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1869_transcript.txt)
[^4]: [20260217_083630_AlexeyDTC_msg1870_transcript.txt](../inbox/used/20260217_083630_AlexeyDTC_msg1870_transcript.txt)
[^5]: [20260217_083710_AlexeyDTC_msg1871_transcript.txt](../inbox/used/20260217_083710_AlexeyDTC_msg1871_transcript.txt)
[^6]: [20260219_145821_AlexeyDTC_msg2083.md](../inbox/used/20260219_145821_AlexeyDTC_msg2083.md) / [GitHub Issue #1](https://github.com/alexeygrigorev/telegram-writing-assistant/issues/1)
[^7]: [20260220_071344_AlexeyDTC_msg2111_transcript.txt](../inbox/used/20260220_071344_AlexeyDTC_msg2111_transcript.txt)
[^8]: [20260220_071344_AlexeyDTC_msg2112_transcript.txt](../inbox/used/20260220_071344_AlexeyDTC_msg2112_transcript.txt)
[^9]: [20260220_071344_AlexeyDTC_msg2113_transcript.txt](../inbox/used/20260220_071344_AlexeyDTC_msg2113_transcript.txt)
[^10]: [20260220_071345_AlexeyDTC_msg2114_transcript.txt](../inbox/used/20260220_071345_AlexeyDTC_msg2114_transcript.txt)
[^11]: [20260220_071345_AlexeyDTC_msg2115.md](../inbox/used/20260220_071345_AlexeyDTC_msg2115.md)
[^12]: [20260220_071345_AlexeyDTC_msg2116.md](../inbox/used/20260220_071345_AlexeyDTC_msg2116.md)
[^13]: [20260220_071345_AlexeyDTC_msg2117_transcript.txt](../inbox/used/20260220_071345_AlexeyDTC_msg2117_transcript.txt)
[^14]: [20260220_071345_AlexeyDTC_msg2118_transcript.txt](../inbox/used/20260220_071345_AlexeyDTC_msg2118_transcript.txt)
[^15]: [20260220_071345_AlexeyDTC_msg2119_transcript.txt](../inbox/used/20260220_071345_AlexeyDTC_msg2119_transcript.txt)
[^16]: [20260220_073330_AlexeyDTC_msg2132.md](../inbox/used/20260220_073330_AlexeyDTC_msg2132.md)
[^17]: [20260220_073330_AlexeyDTC_msg2133.md](../inbox/used/20260220_073330_AlexeyDTC_msg2133.md)
