---
title: "AI Agent Project Ideas"
created: 2026-02-26
updated: 2026-02-26
tags: [ai-buildcamp, projects, agents, ideas]
status: draft
---

# AI Agent Project Ideas

A student from AI Buildcamp asked for a project idea suggestion. They wanted to work on something with a specific customer or business requirement rather than something they define themselves[^1].

The best customer for these kinds of projects is yourself. If you have a problem and want to solve it, you will be the user and the most interested person in making it work. You will be your own customer - that is the ideal scenario[^1].

Not everyone has ideas readily available though. This article collects project ideas that people can use for implementing agents or upskilling in core AI engineering skills. Some of these projects will be implemented during AI Buildcamp - this is also a promotion for the course because students are going to implement many of them[^3].

This could also become a category on the website where people can see what others implemented and find project ideas[^5].

## GitHub Issue Creator Bot

A project for someone who has many different GitHub projects and sometimes gets ideas while on the go, away from the computer. Currently, opening GitHub on the phone, selecting the right project, choosing an issue template, and manually describing everything is tedious[^2].

Instead, a Telegram bot can create issues automatically. Here is how it would work[^2]:

1. Setup: define a specific set of repositories (or all repositories) that the agent should be interested in
2. Interaction: send a voice note to a Telegram bot
3. Processing: the bot transcribes the voice note, and based on the command, the agent performs an action like creating or editing an issue
4. Categorization: if the agent cannot categorize an issue, it records it in a "not categorized" list for review later. You can then correct the agent by telling it which repository the issue actually belongs to

This is just a suggestion to run with or use as inspiration[^2].

## Project Idea Generator Agent

An agent that helps people identify projects they can do[^4]. Similar to the "kid-parent" Claude slash commands described in a previous Substack article[^4].

This could be a conversational agent - not really an agent, more like a chatbot - that helps people come up with original project ideas[^4].

This is a nice project idea in itself, but it is also a useful project for the community. People can try playing with it. It could be a good lead magnet for the community - they would have to sign up to interact with the agent, and then the agent can suggest different ideas[^4].

## Problem Discovery Framework

A framework for helping people discover problems that need solving. The goal is to help them think about what kinds of things require automation in what they do right now[^6].

This means coming up with a list of questions you can ask in order to identify problems that can be solved with AI, automation, and agents. These could be opportunities for automation, opportunities for being more effective, but also nice portfolio projects[^6].

The best customer is yourself. If you have a problem and want to solve it, you will be your own customer. That is the ideal scenario[^6].

## Job Market Analytics Agent

An agent that scrapes new jobs from different locations. You set it up and it sends you different trends about these jobs - new positions, different trends. You can talk about the trends in the data with your agent[^7].

You can also personalize it. If you have your own profile, it can quickly highlight jobs that you are a good match for. It can also highlight areas for improvement - you say what you already know, and it tells you what else you need to know. It can help you select things based on data, do some sort of research[^7].

It can cluster different jobs into different clusters, help you select a domain, help you select project ideas for these jobs[^7].

Based on existing data, you can continue collecting this data. Another angle: given all this dataset, what can you do with it to help upskill yourself. Include a link to the recent AI engineering field guide where the data is, so people can actually build a RAG on top of that to help them. If they also specify their profile, this becomes a really cool project[^7].

This is a pretty interesting project and something that could also be implemented for AI Buildcamp[^7].

## Knowledge Management Bot

Something like the Telegram Writing Assistant, but simpler. You send a voice message or share an article, and instead of Claude, you have an agent that determines the right place to put it[^8].

This is very similar to the FAQ Assistant in the DataTalks.Club. You make a request and the agent determines whether this is something new that needs a new entry, or something that should be added to an existing one, plus it creates the right category[^8].

There can be two types of interactions: adding information and asking questions. You can share a link, and the agent describes what is in that link and adds it to the knowledge base. If you share a YouTube video, it makes a summary and puts it somewhere. It is a knowledge management or idea management system[^8].

Similar to the Telegram Writing Assistant but simpler - you have a bot with a small agent, and you do not need to figure out how to hook up the code yourself[^8].

For storage, the simplest approach is just files. Then you can commit everything to Git. Something like a real Obsidian - not the custom system, but actual Obsidian. You could make an Obsidian client, that is also an idea. You can just organize the structure, or you can take actual Obsidian and build on top of it. Other platforms like Notion are more complicated. But Obsidian is a good fit[^9].

## Journaling Agent

A journaling (diary) agent. Every day you record things - this can be a Telegram bot, a website, whatever. Standard journaling: you talk about events that happened in your life, you list three things you are proud of today, and so on[^10].

Then you can look at your entries. You can also color-code each day. A cron job can collect entries or remind you if you have not journaled today[^10].

All of this gets saved in whatever format you want. A full journaling experience with all the standard attributes[^10].

Every day you record your results. Then when it is time for a performance review, you can show your manager: look at all these achievements, give me a raise. This is a very useful and convenient thing, and why not use AI for it[^10].

This is something that can be done manually too. When working at a company, having a weekly one-on-one with a manager and preparing a document for it is a common practice. That document then becomes useful for preparing for the performance review. There is a well-known article about this concept called the [brag document](https://jvns.ca/blog/brag-documents/)[^10].

As for the agent tools: you can ask questions about past entries, add new entries, correct entries if something is wrong. The format can be anything[^11].

## Sources

[^1]: [20260226_112322_AlexeyDTC_msg2498_transcript.txt](../inbox/used/20260226_112322_AlexeyDTC_msg2498_transcript.txt)
[^2]: [20260226_112325_AlexeyDTC_msg2500.md](../inbox/used/20260226_112325_AlexeyDTC_msg2500.md)
[^3]: [20260226_112412_AlexeyDTC_msg2502_transcript.txt](../inbox/used/20260226_112412_AlexeyDTC_msg2502_transcript.txt)
[^4]: [20260226_112618_AlexeyDTC_msg2504_transcript.txt](../inbox/used/20260226_112618_AlexeyDTC_msg2504_transcript.txt)
[^5]: [20260226_112730_AlexeyDTC_msg2506_transcript.txt](../inbox/used/20260226_112730_AlexeyDTC_msg2506_transcript.txt)
[^6]: [20260226_112909_AlexeyDTC_msg2508_transcript.txt](../inbox/used/20260226_112909_AlexeyDTC_msg2508_transcript.txt)
[^7]: [20260226_113217_AlexeyDTC_msg2510_transcript.txt](../inbox/used/20260226_113217_AlexeyDTC_msg2510_transcript.txt)
[^8]: [20260226_114053_AlexeyDTC_msg2522_transcript.txt](../inbox/used/20260226_114053_AlexeyDTC_msg2522_transcript.txt)
[^9]: [20260226_114141_AlexeyDTC_msg2524_transcript.txt](../inbox/used/20260226_114141_AlexeyDTC_msg2524_transcript.txt)
[^10]: [20260226_114348_AlexeyDTC_msg2526_transcript.txt](../inbox/used/20260226_114348_AlexeyDTC_msg2526_transcript.txt)
[^11]: [20260226_114428_AlexeyDTC_msg2528_transcript.txt](../inbox/used/20260226_114428_AlexeyDTC_msg2528_transcript.txt)
