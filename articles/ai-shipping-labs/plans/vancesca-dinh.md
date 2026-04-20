---
title: "Plan: Vancesca Dinh"
created: 2026-04-20
updated: 2026-04-20
tags: [ai-shipping-labs, plan, community]
status: draft
---

# Plan: Vancesca Dinh

## AI Shipping Labs Personal Plan Intake

### 1) Your Initial Input

Thanks so much for reaching out. My son is home for Easter, so my focus has been a bit scattered these past few weeks. I really appreciate your persistence and kindness in letting me know about this program.

This is definitely something I'm interested in being a part of.

As for what I'm working on or hoping to get out of this:

- I'm currently searching for an AI role, and for me, building a strong portfolio. I completed one project as part of the AI Buildcamp. I'd like to add another. I've been feeling stuck about coming up with an idea has been tough lately.
- One thing I want to mention is that I'd like to contribute to the DataTalks community, especially on projects involving LLM/agents. I'd love to hear about potential projects I can work on to support the DTC community.
- I'd really like to deploy applications on AWS.
- I'm especially interested in evaluating agents.
- To maintain motivation, I'd like to have a coffee chat with the community where anyone can join and we talk about AI, our projects, things we're working on, etc. - kind of a peer learning thing. I wouldn't mind hosting it if it's something we can build.

### 2) Questions

#### If you build one more project now, what do you want it to prove to employers about you?

I want to show that I can set up API endpoints and host on AWS.

#### Would you want the next project to be mainly for your portfolio, or mainly to support DataTalks.Club, or ideally both?

Ideally both. I want to be exposed to problems and figure out how to solve them. Defining the problem is my bottleneck - once I build the moment by having a clear idea of what the problem is then getting started and doing the work comes easy.

#### What do you hope to achieve with this plan in the next 6 to 8 weeks?

- Add another end-to-end project to my portfolio
- Experiment with adding a cron job or some sort of scheduling feature

#### How much time can you realistically commit each week over the next 6 to 8 weeks?

About 20 hours.

#### From your experience with building previous projects, what have you learned about the most effective ways you work when tackling technical tasks?

- Defining the end result. The how reveals itself once I figure out what result is expected. This also means breaking the larger idea into smaller tasks.
- Building schemas and being organized
- Pushing to GitHub regularly

#### Where do you typically encounter challenges when working on projects? For instance: scoping, getting started, maintaining momentum, technical obstacles, or finishing tasks.

The start and the end, so coming up with ideas and maintaining the project once it's "finished".

## Alexey's Recommendations

For Vancesca, it would be great to find a project for the DataTalks.Club that she wants to work on[^3].

For the DTC project side, Alexey wants to minimize his own involvement, because one community member is already working on a project and he is the bottleneck for her. So ideally Vancesca's project should run without constant feedback from Alexey's side. Participating in the community sync-ups would be enough structure.

Her task is to pick a project. On the DataTalks.Club organization website there are open GitHub issues with hackathon projects. Extract all of them, put them together, and ask her to choose one. We can help her pick and sketch out roughly how to implement it.

The DTC hackathon projects (open issues in `DataTalksClub/datatalksclub.github.io` labeled "AI Bootcamp Hackathon"):

- [#97 Build a Unified Search Interface for Topics, Subtopics & Timestamp Segments](https://github.com/DataTalksClub/datatalksclub.github.io/issues/97) - Semantic search across all podcast episodes that returns episode-level and timestamp-level hits with deep links.
- [#96 Build a Chatbot That Answers Questions About Any Podcast Episode](https://github.com/DataTalksClub/datatalksclub.github.io/issues/96) - RAG chatbot over podcast transcripts (minsearch + Groq/OpenAI) that returns timestamped answers with jump-links.
- [#95 Add a List of Mentioned Resources to Each Podcast Page](https://github.com/DataTalksClub/datatalksclub.github.io/issues/95) - AI extracts tools/books/people/papers from transcripts and injects a "Resources Mentioned" section into each episode page.
- [#94 Assign Topics & Subtopics to Each Podcast Episode (Episode + Timestamp)](https://github.com/DataTalksClub/datatalksclub.github.io/issues/94) - Design a topic taxonomy and auto-classify episodes and individual clips to feed future `/insights/<topic>/` hub pages.
- [#93 Create Dedicated Workshop and Webinar Pages](https://github.com/DataTalksClub/datatalksclub.github.io/issues/93) - Generate per-item pages (like podcast pages) from YouTube workshop/webinar playlists with video embed, description, resources, transcript.
- [#92 Build a Full Tools Catalog + Connections Graph](https://github.com/DataTalksClub/datatalksclub.github.io/issues/92) - Extract every tool mentioned across podcasts/Zoomcamps/workshops, build a catalog page, optionally use Cognee for a tool-to-video connections graph.
- [#91 Build a Catalog of Open-Source Demos from YouTube](https://github.com/DataTalksClub/datatalksclub.github.io/issues/91) - Turn the open-source-demos YouTube playlist into a structured, searchable catalog page on the site.
- [#90 Automate Slack Discussions to Website FAQ Sync](https://github.com/DataTalksClub/datatalksclub.github.io/issues/90) - Daily pipeline (GitHub Actions) that pulls Q&A from Slack zoomcamp channels and updates FAQ markdown via PR. Prototype agent exists.
- [#87 Podcast: Key Takeaways Section](https://github.com/DataTalksClub/datatalksclub.github.io/issues/87) - Generate concise, timestamped key-takeaways summaries for every podcast page.

On the hosting side, the community will have a webinar soon about Codex, Claude Code, and AWS Lambda. After that the plan is to move on to more complex deployment setups. So let's try to pick a project where she can use AWS Lambda to talk to OpenAI or something similar. She should be able to develop and test locally, then deploy the project to AWS Lambda. Everything in Python.

Pick a concrete project from the list above that fits these criteria.

For the portfolio, Alexey recommends she look at the [AI Engineering Field Guide](../../ai-engineering-field-guide.md) to see what kinds of roles and projects are relevant.

Also share with her the same step-by-step gist with prompts for finding an interesting project that we already shared with other members. Based on that we can put together a more detailed plan.

Alexey wants her to be involved in the planning too - to think about what is realistic for her and what is not. The plan we propose is just a draft; she can use it as a starting point and adjust.

So her first task is to pick a project and decide whether she likes it or not.

## Sources

[^1]: [Google Doc](https://docs.google.com/document/d/1fJT6wQMA_bK9nwYXmfeGuXiA0k8a8fheZB9NyVbCZCQ/edit?usp=sharing)
[^2]: [20260420_083739_AlexeyDTC_msg3443.md](../../../inbox/used/20260420_083739_AlexeyDTC_msg3443.md)
[^3]: [20260420_102138_AlexeyDTC_msg3471_transcript.txt](../../../inbox/used/20260420_102138_AlexeyDTC_msg3471_transcript.txt)
