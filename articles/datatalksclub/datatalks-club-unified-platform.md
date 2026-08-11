---
title: "DataTalks.Club Unified Platform"
created: 2026-07-07
updated: 2026-08-11
tags: [datatalks-club, platform, vision, community, planning, ux]
status: draft
---

# DataTalks.Club Unified Platform

This is a starting document for rethinking how everything at DataTalks.Club fits together. The goal is the same as the document we made for AI Shipping Labs: describe the problem clearly, capture the vision, and lay out what exists today so we can start iterating on a direction. It is a work in progress - Alexey and Valeriia will keep adding notes here until there is a shared understanding of what we want to build[^7].

The idea in one line: everything we do at DataTalks.Club should live within one platform, convenient for people and with a unified design[^7].

## The problem

Right now the same student-facing information is spread across several surfaces, and it is not clear which one is the single source of truth. There is a bit of confusion between the docs and the repository[^4].

For each course there is:

- The course GitHub repository - the notes themselves, links to videos, and navigation between modules[^3].
- The DataTalks.Club Docs site - prerequisites, getting started, curriculum, and rules like how to write in Slack or information about workshops[^1][^3].
- A separate FAQ - a place to check whether a question has already been answered[^2][^3].
- The course management platform - where people register and submit homework and the project[^3].

Prerequisites, getting started, and curriculum partially duplicate what is on GitHub. If I put myself in the position of someone taking the course, this can create confusion. And from a content standpoint the question is simply: why do we have the same thing in two places[^1]?

### How this grew

The docs were not a mistake - they solved a real problem. They were made from the launch streams so I would not have to repeat the same things cohort after cohort. I got tired of making the same slides every time, so I started sending people to the docs. Naturally that created repetition with the rest of the material[^5][^7].

The FAQ grew the same way. People contribute to it, and on top of that I pull in messages from Slack and from streams and stuff them all into the FAQ. So there is repetition there too[^7].

### The student's perspective

The deeper issue is that there is no single complete source. As a student, I come to GitHub and try to understand where my main source of information is - the place I return to day to day, module to module, to find everything I need. Instead, the prerequisites and rules are in the docs, the notes and video links and navigation are on GitHub, and there is a FAQ to check as well. That fragmentation makes it hard to know where to go[^3].

It is not only a student problem. Even for me, navigating between the content is hard, because things repeat. When I need to point someone to information about a course, I have to decide: do I send them to the docs, to the FAQ, to the course management platform, or to GitHub? Having all of this mixed together adds unnecessary navigation complexity[^1][^2].

And it is not purely a question of whether the information is available. People ask the same questions over and over even when the answer is written down. Part of that is that people are lazy to read, even if you write it ten times in different places. But it still feels like everything should be centralized in one place[^2].

One thing I did try in that direction: I made a pinned navigation message in AI Dev Tools Zoomcamp with the basic rules, written to anticipate and answer the common questions up front so people ask fewer repeated ones. That helps, but it is one more surface on top of the docs, FAQ, and repo[^1].

## The vision

We have talked before about a potential redesign for DataTalks.Club. The vision is not just to change the design. It is to think about what should live where, so that there is one portal that has everything - courses, articles, all of it in one place, with a unified design[^7].

How to get there and how to implement it, I do not know yet. But the end state is clear enough to start moving toward: everything in one place, unified. We can start iterating in that direction now[^7].

### Directions considered

A few different shapes for this came up while thinking out loud. They are not decisions, just options to weigh:

- Make the docs site the nice interface. The docs would become a clean interface where everything is visible in a convenient form, and you could click between the previous and next topic. Course notes would live there too. Not every course has notes, but for the courses that do not, we would at least have the video links plus a mention of community notes at the bottom[^1].
- Move the docs content onto GitHub. The opposite direction - take what is in the docs and add it to GitHub as well, so that a student arriving at the repo finds their single main source there[^2].
- Put everything on the course management platform. Since people already register, submit homework, and submit the project there, we could add all of this information into it with convenient navigation. Design the student's path from the moment they join the course[^3].

The course management platform option is the most ambitious. The idea is to add a Zoomcamp Logistics part at the start of the course, then a repeating structure of homework and workshop, homework and workshop - organizational files alongside the material files (notes, or community notes plus links to the videos), then the FAQ for that specific module, and the homework itself. The homework text would live right there, and you would be able to select your answers inside it. Today the answers are submitted in one place that does not contain the full homework, while the homework conditions live on GitHub. I am not sure how hard this is to build with the course management platform, but if it is possible it would be great[^3].

### Course notes format

There was already an idea to move the course notes out of the repos and into this unified format. In LLM Zoomcamp I tried making separate notes for each lesson, and that experiment went well. In ML Zoomcamp, Vancesca is doing something similar that we can build on. We can fit all the courses to this format, which means we do not have to keep everything on GitHub - we can use GitHub to store less information than we do now[^8].

### On technology

I would not think about the technology yet - what matters first is what it should look like and what should be in it. But to give a sense of the scope: in principle the current course management platform could be replaced with a single site written in Django, for roughly the same cost. Right now I pay for the course management platform; that way I would pay for the site instead. Or we could look at doing it on GitHub Pages. Technology is an open question for later[^7].

## How to approach the redesign

I am listening to the book Lean Product Design, and there is a part in it about UX. I want to analyze it and apply it to the DataTalks.Club website redesign right now[^10].

### User research with students

The book says it is a good idea to run user interviews and do user research. That is a good idea here. Once I make the first version, I should contact some students and tell them I want to show them the new version of the site, so I can get feedback from them[^11].

### Personas for DataTalks.Club

The book also talks about personas. For AI Shipping Labs we defined personas, but for DataTalks.Club we never did this. I think we need to do it. I still need to think about how[^12].

The AI Shipping Labs personas are in [personas.md](../ai-shipping-labs/personas.md).

## Current DataTalks.Club surfaces

To ground the redesign, here is a map of what already exists across the DataTalks.Club GitHub organization - the public site, the courses, and the supporting apps. This is the output of analyzing the org repositories at [github.com/orgs/DataTalksClub/repositories](https://github.com/orgs/DataTalksClub/repositories) [^9].

### The public website

The main site at datatalks.club (repo datatalksclub.github.io) is a content-first static site built with Rustkyll, a Jekyll-compatible static generator. Content is modeled as collections that each emit their own pages: podcast (about 206 episodes), books (about 99), people (about 438 author and guest pages), posts (about 54 articles), plus small tools and conferences collections. Navigation surfaces Articles, Slack, Events, Podcast, Wiki, Books, and Courses.

Courses are the biggest gap on the site. The Courses nav item does not point to a real course listing - it links to a single blog post. The courses collection holds one stale 2021 file, and the courses page says "Nothing here, come back later." So course content is effectively not hosted on the website; it lives in the external per-course repos, and the site only links out.

podwiki is an LLM-maintained exploration wiki layered over the podcast archive (also Rustkyll, deployed under datatalks.club/podwiki). It adds topic hubs, roadmaps, comparisons, a graph view, and search, while deliberately not re-publishing the canonical episode, people, and book pages - it links back to the main site instead. This is a good model for the unified platform: add layers on top of a single canonical source rather than duplicate it.

Several content islands are not linked from the site navigation at all: data-paths (six role learning paths - data analyst, data engineer, data scientist, ML engineer, MLOps, product manager), project-of-the-week (DIY project study groups), reading-club-nlp and reading-club-books, and awesome-data-podcasts. These are valuable learning and community materials that currently reach people only through Slack or direct GitHub links.

### The courses

The main courses are Machine Learning Zoomcamp, Data Engineering Zoomcamp, LLM Zoomcamp, MLOps Zoomcamp, AI Dev Tools Zoomcamp, plus Stock Markets Analytics Zoomcamp and the Open-Source LLM mini-course. Each lives in its own repo, and the way material and navigation are organized differs a lot between them.

The canonical structure is defined in the zoomcamp-template repo (a STRUCTURE.md spec, README templates, conventions, a new-course checklist, and shared scripts). It prescribes a fixed root README layout (banner, quick links, about, who should join, prerequisites, how to take the course, syllabus, projects, certificate, community and support), a module folder convention (NN-kebab-name folders each with a README, homework, and a standard community-notes section), and a cohort folder with a schedule and deadlines. The template itself notes the camps drifted apart over the years and exists to pull them back into line. A separate playbooks repo covers launch and marketing structure (cohort brief, launch checklist, campaign calendar, per-course course.yaml metadata, announcement templates, and a proof library of testimonials and stats).

How each course handles per-lesson notes varies widely:

- LLM Zoomcamp is running the per-lesson notes experiment and is the most developed version. Each module has a lessons/ folder with genuinely written prose tutorials (full explanations, inline code, a video link at the top), and the module README acts as a structured index. This is a step beyond what the template currently prescribes.
- ML Zoomcamp has older community-written conspectus notes wrapped around a YouTube link and a slides link.
- Data Engineering, MLOps, and AI Dev Tools organize modules around code and notebook subfolders with a README hub, and no per-lesson written notes.
- Stock Markets and Open-Source LLM do not follow the canonical README at all - different heading names, no live-versus-self-paced table, cohorts embedded in the root README, and Google Doc FAQs instead of the hosted FAQ. These are the partner-run and mini-course repos.

### The supporting apps

- docs (datatalks.club/docs) is a Jekyll site built from the launch streams. It is organized as shared zoomcamp-logistics pages (start here, joining, communication, Slack, homework, workshops, peer review, leaderboard, certification, and so on) plus a per-course folder for each zoomcamp carrying the same page set (prerequisites, getting started, curriculum, environment setup, project, resources), and a section documenting the course management platform UI.
- faq (datatalks.club/faq) is a custom static site generated from per-course question folders, with an AI automation module that triages community-submitted proposals. It is community-contributed and organized per course and per module.
- faq-assistant is a Slack bot (single AWS Lambda) that answers questions in-thread using the FAQ content via zerosearch and OpenAI. It is a fourth consumer of the same FAQ knowledge, reached through Slack.
- course-management-platform (courses.datatalks.club) is a Django app handling registration, homework and project submission, peer review, scoring, and leaderboards. Important detail for the source-of-truth question: the homework text does not live here - the platform stores the submission form (graded questions and answers) and links out to the instructions in the course repo. The Course record is full of outbound pointers (github_repo_url, faq_document_url, registration_url).
- Back-office repos that are not student-facing: dataops and dtc-operations (internal operations portals, the former superseding the latter), zoomcamp-scoring (certificate generation from final scores), and zoomcamp-analytics (public course analytics notebooks).

### Where the same information is duplicated

The analysis confirmed the fragmentation the voice notes describe. The same student-facing information is maintained independently in several places:

- Prerequisites exist both in docs/courses/<course>/prerequisites.md and in the course repo README.
- How the course works (live versus self-paced, homework, leaderboard, certificate) is in both the repo README and the shared zoomcamp-logistics docs pages.
- Getting started and onboarding (star the repo, join Slack and Telegram) is split across the docs getting-started page, the docs joining page, and the repo README community section.
- Homework is the sharpest case: the question text lives in the course repo, the deadline and policy live in two cross-referencing docs pages, and the graded submission form lives in the Django platform - four places for one assignment.
- FAQ content is reachable through four doors: the FAQ site, a docs pointer, the platform link, and the Slack bot. Some docs logistics pages (environment setup, asking questions, certification) overlap heavily with FAQ entries.
- Curriculum and syllabus are kept in sync by hand in both the repo README and the docs curriculum page.
- Registration links and cohort dates are scattered across the docs landing table, each repo README, and the platform.

## Possible next steps

These are directions to discuss, drawn from the analysis - not decisions[^9].

- Own the course metadata once. The platform's Course record already points out to the repo, FAQ, and registration links. Invert this: keep the canonical course metadata (dates, registration, prerequisites, curriculum, links) in one place and render it into the repo README, docs, and platform pages instead of maintaining each by hand.
- Make courses a first-class citizen on the website. Turn the dead Courses placeholder into a real, sourced course listing so the main site becomes the single front door, the same way podcast, books, and articles already are.
- Separate shared logistics from per-course specifics. The zoomcamp-logistics layer is genuinely reusable and should be written once and transcluded everywhere, so course READMEs stop re-stating it.
- Single-source the homework. Pick one home for the assignment definition (the repo homework file or the platform questions) and generate the other view, instead of maintaining prose in the repo and answers in the database separately.
- Keep the FAQ as the one canonical Q&A store. Have docs link into FAQ anchors instead of duplicating FAQ-style content, keeping the FAQ, website, platform, and Slack bot all reading from the same source.
- Decide whether per-lesson written notes become the standard. The LLM Zoomcamp lessons model is ahead of the template spec. If it becomes the norm, update the template and roll it out across courses, which also lets us store less on GitHub and move notes into the unified format.
- Pull the orphaned content islands (learning paths, project-of-the-week, reading clubs) into the website as browsable sections so they stop being reachable only through Slack.
- Converge the two outlier courses (Stock Markets, Open-Source LLM) onto the template, and keep the back-office repos (operations, scoring, analytics) out of the student-facing consolidation.
- Define which surface owns each content type, so new repos do not re-fragment the picture. The org has a pattern of accreting parallel apps (dataops superseding dtc-operations is one example).

## Sources

[^1]: [20260707_100803_AlexeyDTC_msg4690_transcript.txt](../../inbox/used/20260707_100803_AlexeyDTC_msg4690_transcript.txt)
[^2]: [20260707_100803_AlexeyDTC_msg4691_transcript.txt](../../inbox/used/20260707_100803_AlexeyDTC_msg4691_transcript.txt)
[^3]: [20260707_100803_AlexeyDTC_msg4692_transcript.txt](../../inbox/used/20260707_100803_AlexeyDTC_msg4692_transcript.txt), [20260707_100803_AlexeyDTC_msg4693_transcript.txt](../../inbox/used/20260707_100803_AlexeyDTC_msg4693_transcript.txt)
[^4]: [20260707_100803_AlexeyDTC_msg4694.md](../../inbox/used/20260707_100803_AlexeyDTC_msg4694.md)
[^5]: [20260707_100803_AlexeyDTC_msg4695.md](../../inbox/used/20260707_100803_AlexeyDTC_msg4695.md)
[^7]: [20260707_100803_AlexeyDTC_msg4697_transcript.txt](../../inbox/used/20260707_100803_AlexeyDTC_msg4697_transcript.txt), [20260707_100928_AlexeyDTC_msg4708_transcript.txt](../../inbox/used/20260707_100928_AlexeyDTC_msg4708_transcript.txt)
[^8]: [20260707_100803_AlexeyDTC_msg4698_transcript.txt](../../inbox/used/20260707_100803_AlexeyDTC_msg4698_transcript.txt)
[^9]: [20260707_101107_AlexeyDTC_msg4710.md](../../inbox/used/20260707_101107_AlexeyDTC_msg4710.md)
[^10]: [20260809_081254_AlexeyDTC_msg4853_transcript.txt](../../inbox/used/20260809_081254_AlexeyDTC_msg4853_transcript.txt)
[^11]: [20260809_081820_AlexeyDTC_msg4855_transcript.txt](../../inbox/used/20260809_081820_AlexeyDTC_msg4855_transcript.txt)
[^12]: [20260809_082043_AlexeyDTC_msg4857_transcript.txt](../../inbox/used/20260809_082043_AlexeyDTC_msg4857_transcript.txt)
