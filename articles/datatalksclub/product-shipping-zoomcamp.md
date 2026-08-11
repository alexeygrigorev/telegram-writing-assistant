---
title: "Product Shipping Zoomcamp"
created: 2026-07-01
updated: 2026-07-01
tags: [course-idea, zoomcamp, product, build-in-public]
status: draft
---

# Product Shipping Zoomcamp

A concept for a new course about building and shipping a real product end to end. The working title is Product Shipping Zoomcamp[^1][^2].

Alternative names considered: Build & Ship Zoomcamp, Vibe Shipping Zoomcamp, Full-Stack Product Zoomcamp, Build in Public Zoomcamp, End-to-End Product Development Zoomcamp.

Product Shipping Zoomcamp is the recommended name. It is broad enough to include any product, while still making it clear that the goal is not only coding. The course is about building, deploying, improving, measuring, and launching a real product.

## 1. Course idea

Course promise. Students go from "I have an idea" to "I shipped a deployed product, got feedback, improved it, measured usage, launched it publicly, and reviewed other students' products."

The running example can be a small game, but the course itself is not a game-development course. The game is just the example used to demonstrate the full product-development lifecycle.

The broader goal is to teach students how to build an end-to-end product:

- problem discovery
- audience research
- MVP scoping
- full-stack implementation
- deployment
- polish and usability
- peer review
- feedback-driven iteration
- analytics
- build-in-public
- community participation
- launch and distribution
- final peer-reviewed capstone

This follows the same spirit as the Vibe Shipping idea: Product = Code + Marketing + Sales. Students should not treat marketing and users as something that happens only after development is finished.

## 2. Core philosophy

Main principle: a product is not finished when the code works. A product exists when other people can use it.

Students should learn that shipping means:

- making the product accessible
- making it understandable
- making it usable
- getting feedback
- improving based on feedback
- measuring what happens
- finding users
- launching in the right places

The course should avoid the common trap: "I spent six weeks coding, then I launched to nobody." Instead, students start building public presence and community context from the first module.

## 3. Course structure

The course has six modules, a midterm project, and a final capstone.

| Stage | Name | Main output |
|---|---|---|
| Module 1 | Problem Discovery, JTBD, Communities, and MVP Scope | Product idea, audience, community map, build-in-public plan |
| Module 2 | End-to-End MVP Deployment | Deployed full-stack MVP |
| Module 3 | MVP Polish and Peer-Test Readiness | Minimal usable version ready for review |
| Midterm Project | Deployed MVP Peer Review | Students review 3 deployed peer applications |
| Module 4 | Feedback-Driven Product Iteration | Improved product based on peer feedback |
| Module 5 | Product Analytics, Monitoring, and Readiness | Measurable product with feedback and error visibility |
| Module 6 | Launch, Distribution, and Build-in-Public Finale | Public launch and launch report |
| Final Project | End-to-End Product Capstone Review | Students review 3 final shipped products |

The structure mirrors the ML Zoomcamp style: students complete modules independently, they submit a project, they evaluate three peer projects, project submission and peer-evaluation windows are separate, and peer review is required for the project to count.

## 4. Course-wide build-in-public layer

Build-in-public should not be only Module 6. It starts in Module 1 and continues throughout the course.

Why build in public? By the time students launch, they should already have joined relevant communities, observed what people talk about, posted progress, asked questions, shared early lessons, found potential testers, and built some familiarity with the target audience. The launch should not be the first time anybody hears about the product.

Build-in-public activities across the course:

| Stage | Build-in-public activity |
|---|---|
| Module 1 | Find communities, observe discussions, collect problem language, post initial learning/progress |
| Module 2 | Share first deployed skeleton or technical milestone |
| Module 3 | Share the MVP and invite testers |
| Midterm | Get peer reviews and optionally external testers |
| Module 4 | Share what feedback was received and what changed |
| Module 5 | Share usage/analytics learnings, bugs fixed, and readiness progress |
| Module 6 | Launch to the communities and audiences developed during the course |
| Final | Share final write-up, metrics, lessons, and roadmap |

Students should choose channels based on their target audience: Reddit, Discord communities, Slack communities, LinkedIn, X/Twitter, Hacker News, Indie Hackers, Product Hunt, itch.io if relevant, GitHub Discussions, niche forums, newsletters, university or local communities, and direct outreach.

The important lesson: do not launch everywhere. Launch where your users already spend time.

Each student keeps a simple public or semi-public log:

```markdown
## Build-in-Public Log

### Week / Module
Date:

### What I built
-

### What I learned
-

### Where I shared
-

### Responses / comments / feedback
-

### What I will do next
-
```

This can live in the repo, a blog, LinkedIn posts, a GitHub Discussion, or another chosen public channel.

## 5. Module 1: Problem Discovery, JTBD, Communities, and MVP Scope

Goal: find a real problem, define a focused MVP, and start building public context around the idea. This module should be mostly about discovery, not coding.

Students should not start with "I want to build an app." They should start with "Who is this for, what job are they trying to do, where do they already talk about this, and what is the smallest product that can test the idea?"

Main question: what problem or job are we building for, and where do these people already hang out?

Topics:

1. Jobs To Be Done. Students learn to frame the product around a user job using this template:

```text
When I am ___,
I want to ___,
so I can ___.
```

Two examples of the JTBD template in use:

```text
When I have a short break between meetings,
I want a quick competitive game,
so I can relax and challenge a friend without installing anything.
```

Another example, this time for a learning context:

```text
When I am learning a new technical topic,
I want a small interactive challenge,
so I can practice without setting up a full environment.
```

2. Problem and idea discovery. Students research before building. Sources include Reddit threads, Discord conversations, forum posts, GitHub issues, product reviews, app store reviews, YouTube comments, blog comments, competitor communities, support forums, Slack groups, and niche newsletters.

They look for repeated complaints, repeated desires, workarounds, "I wish..." statements, "Does anyone know a tool for..." posts, confusing existing solutions, people paying for bad solutions, and communities where the problem appears often.

3. Community mapping. Students identify where their users already are. For each community:

```markdown
## Community Research

Community:
URL:
Who is there:
What they discuss:
Common problems:
Common language they use:
Can I post there? Rules:
Potential launch angle:
```

4. Build-in-public setup. Students choose one or more channels where they will share progress. They define where they will post, what kind of posts they will make, how often they will post, what communities they will observe, and what communities they may eventually launch to.

5. MVP scope. Students define the smallest useful product. They write the target user, main job, core user flow, MVP features, explicitly out-of-scope features, success metric, and first version acceptance criteria.

Deliverables by the end of Module 1: problem discovery notes, JTBD statement, community map, build-in-public plan, target user, MVP scope, core user flow, initial product pitch, initial GitHub repo, and README skeleton.

Suggested README section:

```markdown
# Product Name

## Problem

## Target user

## Jobs To Be Done

When I am ___, I want to ___, so I can ___.

## MVP scope

### In scope
-

### Out of scope
-

## Core user flow

1.
2.
3.

## Communities researched

-

## Build-in-public plan

-
```

## 6. Module 2: End-to-End MVP Deployment

Goal: build and deploy the thinnest possible full-stack product.

This module can be inspired by the Full-Stack Vibe Coding workshop: https://aishippinglabs.com/workshops/full-stack-vibe-coding . The workshop builds a full-stack app end to end with a coding assistant, including a React frontend, an OpenAPI contract, a FastAPI backend, a database, containerization, deployment, and GitHub Actions CI/CD.

The example app is a multi-user Snake game with leaderboard, game watching, login/signup, frontend, backend, and database. This fits well as the running example while keeping the course broader than game development.

Main question: can we deploy a thin end-to-end slice that proves the product architecture works?

This module is not about polish, launch, or perfect UX. The goal is a deployed full-stack skeleton where the core flow works online.

Topics: project structure, frontend scaffold, API contract, backend service, minimal persistence, connecting frontend and backend, environment configuration, basic tests or smoke tests, Docker or container setup if appropriate, basic CI/CD, first public deployment, and a README with run/deploy instructions.

The running example can be a small web game: a game UI frontend, a game/session API backend, persistence for users/scores/sessions, a deployed playable URL, CI/CD that deploys on push, and a README with run and test instructions. Students can apply the same structure to other products.

Deliverables by the end of Module 2: GitHub repo, deployed application URL, working frontend, working backend, minimal persistence if needed, basic CI/CD, README with local run instructions, README with deployment instructions, and a basic smoke test or health check.

Build-in-public assignment. Students share what they are building, the first deployed version or technical milestone, what worked, what was harder than expected, and what they plan to make usable next.

```text
I just deployed the first end-to-end version of my product for Product Shipping Zoomcamp.

It is still rough, but the frontend, backend, database, and deployment are connected.

Next step: make the core flow usable enough for other people to test.
```

## 7. Module 3: MVP Polish and Peer-Test Readiness

Goal: turn the deployed thin slice into a minimal usable version with clear focus. Module 2 answers "does it work end to end?" Module 3 answers "can another person understand and use it?"

Main question: can a peer reviewer open the deployed product, test the core flow, and give useful feedback?

Topics:

1. Scope tightening. Students reduce ambiguity - remove unfinished features, hide broken sections, remove placeholder pages, focus on one main flow, document known limitations, and avoid adding random features before the midterm.

2. First-use clarity. Students improve the first 30 seconds - a clear homepage or start screen, a simple explanation, one primary CTA, empty states, success states, basic instructions, and clear navigation. For the game example: what is the goal, how do I start, what controls do I use, what counts as success, and what happens after a game ends.

3. Core flow polish. Students make the main path reliable - fix obvious bugs, handle loading states, handle error states, prevent dead ends, improve forms, make buttons clear, ensure fresh users can complete the flow, and make sure the deployed version matches the README.

4. Free reviewer access. If the application has login, payment, credits, subscriptions, API limits, or gated features, the student must provide a free testing path. Acceptable options include test account credentials, a reviewer access code, a demo mode, a mocked payment flow, Stripe test mode, a seeded demo user, a temporary unlocked reviewer mode, or a bypass flag for reviewers.

```markdown
## How to test for free

Use this reviewer account:

Email: reviewer@example.com
Password: demo-password

Or use this access code:

ZOOMCAMP-REVIEW
```

If reviewers cannot test the product without paying, the midterm submission loses points.

5. Feedback collection. Keep this lightweight - a feedback form, a bug report link, one question after the main flow, or 1-3 specific questions for reviewers. Full analytics comes later in Module 5.

6. Review-ready documentation. The README must explain what the product does, who it is for, the deployed URL, how to test it, how to test it for free, the main flow reviewers should try, known limitations, and what feedback the student wants.

Deliverables by the end of Module 3: deployed MVP, free testing instructions, feedback mechanism, review-ready README, known limitations, specific reviewer questions, and a commit hash for midterm submission.

Build-in-public assignment. Students share what the MVP does, who it is for, what kind of testers they need, the deployed link if appropriate, and one clear feedback request.

```text
My MVP is ready for early testing.

It helps ___ do ___ by ___.

I'm looking for feedback on:
1. Is the main flow clear?
2. Where do you get stuck?
3. Would you use this again?

Link:
```

## 8. Midterm Project: Deployed MVP Peer Review

The midterm is the first formal interaction point. Students submit a deployed MVP and review 3 peer projects. The goal is not a polished final product. The goal is: can another person open the application, understand it, test it for free, complete the core flow, and give useful feedback?

Each student submits: GitHub repo, commit hash, deployed application URL, landing page URL if separate, README, product description, target user, JTBD statement, MVP scope, free testing instructions, setup/run instructions if local testing is possible, known limitations, a feedback form or feedback link, and 1-3 reviewer questions.

Each student must review 3 peer projects. For each project, the reviewer should open the deployed application, test it without paying, try the main user flow, read the README, check known limitations, submit rubric scores, and leave written feedback.

Midterm evaluation criteria:

| Criterion | Points |
|---|---:|
| Product idea and target user are clear | 0-2 |
| JTBD/problem framing is clear | 0-2 |
| MVP scope is focused and realistic | 0-2 |
| Application is deployed and accessible | 0-3 |
| Reviewer can test the product for free | 0-3 |
| Core user flow works end to end | 0-4 |
| First-use experience is understandable | 0-2 |
| README explains how to use/test the app | 0-2 |
| Feedback collection exists | 0-1 |
| Known limitations and next steps are clear | 0-1 |

Total: 22 points.

Each reviewer answers:

```markdown
## Review

### Could you access the deployed app?
Yes/No

### Could you test it without paying?
Yes/No

### What is the product for?

### Who is the target user?

### Could you complete the main flow?

### What was confusing?

### What worked well?

### What broke or behaved unexpectedly?

### What is the most important improvement before final launch?

### Would you share this with someone? Why or why not?
```

## 9. Module 4: Feedback-Driven Product Iteration

Goal: use midterm peer feedback to improve the product. This module is about disciplined iteration, not adding random features.

Main question: did students turn feedback into better product decisions?

Topics:

1. Feedback synthesis. Students collect all feedback from peer reviews, external testers, community comments, build-in-public responses, and their own observations. They group feedback into bugs, UX confusion, unclear positioning, missing information, feature requests, technical problems, and launch concerns.

2. Prioritization. Students decide what to fix now. They classify work as must fix before final, should fix if time allows, later, or will not do. They should be able to explain why.

3. Product iteration. Students improve the core product. Possible changes include simplifying onboarding, improving the core flow, removing confusing features, fixing bugs, updating copy, improving layout, adjusting pricing/free access if relevant, improving landing page clarity, updating the README, and updating reviewer/tester instructions.

4. Changelog. Students document what changed since the midterm:

```markdown
## Post-Midterm Changelog

### Feedback received
-

### Changes made
-

### Feedback not implemented
-

### Why not
-

### Updated product URL
-
```

Deliverables by the end of Module 4: improved deployed application, feedback synthesis, prioritized issue list, post-midterm changelog, updated README, and an updated build-in-public post.

Build-in-public assignment. Students share a "feedback to product decision" post:

```text
I got feedback from my midterm reviewers.

Top issues:
1. ___
2. ___
3. ___

I fixed ___ and decided not to implement ___ because ___.

The updated version is here:
```

This teaches students that build-in-public is not only promotion. It is also public learning and public iteration.

## 10. Module 5: Product Analytics, Monitoring, and Readiness

Goal: make the product measurable and safer to expose to more users. Persistence and basic state already belong in Module 2. Module 5 should not be "data and state." Instead, it should focus on analytics, monitoring, and launch readiness.

Main question: when users arrive, will we know what happened?

Topics:

1. Product analytics. Students define the key funnel for their product. Example funnel: user opens app, user starts core flow, user completes core flow, user submits feedback / signs up / shares / returns. They add events such as app_opened, signup_started, signup_completed, core_flow_started, core_flow_completed, core_flow_failed, feedback_submitted, share_clicked, and payment_started or upgrade_clicked if relevant. For the game example: game_started, game_completed, game_lost, score_submitted, leaderboard_viewed, replay_clicked, share_clicked.

2. Activation metric. Students define the product's activation moment. Examples: user completes first game, user creates first item, user sends first message, user saves first result, user invites someone, user submits first score. The question: what action means the user actually experienced the value of the product?

3. Drop-off analysis. Students track how many users start, how many complete the main flow, where people leave, what errors occur, and what should be fixed before launch.

4. Qualitative feedback loop. Students connect analytics with human feedback. They add or improve a feedback form, a bug report link, a post-flow question, a "Was this useful?" prompt, and a contact link.

5. Monitoring and error visibility. This is not CI/CD - CI/CD already happens in Module 2. Module 5 is about knowing what happens after deployment. Students add basic visibility: error logging, frontend error tracking if possible, backend logs, a health endpoint, an uptime check, a basic monitoring dashboard, and simple alerting if practical. The goal: if the app breaks during launch, will the student notice?

6. Launch readiness checklist. Students verify the app is publicly accessible, the free testing path works, the core flow works on a fresh account/session, main events are tracked, feedback can be submitted, errors are visible somewhere, the README is up to date, the landing page has a clear CTA, known limitations are documented, launch channels are selected, and the build-in-public audience has been warmed up.

Deliverables by the end of Module 5: analytics events list, activation metric, basic analytics view or event table, feedback mechanism, error/monitoring setup, launch readiness checklist, and updated product URL.

Analytics plan template:

```markdown
# Product Analytics Plan

## Core user flow

1.
2.
3.

## Activation event

The activation event is:

## Events tracked

-
-
-

## Current numbers

Visitors:
Core flow started:
Core flow completed:
Feedback submissions:
Errors observed:

## Biggest issue before launch

## What I will improve before launch
```

Build-in-public assignment. Students share a learning post based on usage or readiness:

```text
I added analytics to my product and found that users start the main flow but drop off at ___.

I'm fixing ___ before launch.

This changed how I think about the product because ___.
```

## 11. Module 6: Launch, Distribution, and Build-in-Public Finale

Goal: launch to the audience and communities students have been building since Module 1. Module 6 should not be the first time students think about launch. It is the moment where earlier community research, build-in-public posts, tester conversations, and product iteration come together.

Main question: can students get the product in front of the right people and learn from the launch?

Topics:

1. Positioning refresh. Students update their message based on what they learned. They answer who it is for, what job it helps with, why someone should try it, what the one-line pitch is, what the CTA is, and what changed since the original idea.

2. Landing page finalization. Students finalize the headline, short description, screenshot or preview, CTA, "how it works," target user, free access instructions if relevant, and social proof or early feedback if available.

3. Launch channel selection. Students choose channels based on the community work from Module 1. They should not blindly post everywhere. They prepare a launch plan:

```markdown
## Launch Channels

### Channel 1
Why this channel:
Audience:
Posting rules:
Launch message:
Expected outcome:

### Channel 2
...
```

4. Launch copy. Students prepare a short launch post, a longer launch post, a direct outreach message, a community-specific post, a follow-up message, and comment response templates.

5. Launch. Students launch publicly or semi-publicly. Possible launch actions: post in a target community, direct outreach to users, post on LinkedIn/X, post in a relevant Discord/Slack, submit to Product Hunt, post on Indie Hackers, share on Hacker News, publish to itch.io if relevant, or write a launch blog post.

6. Post-launch response. Students respond to what happens - reply to comments, thank testers, ask follow-up questions, fix urgent bugs, track metrics, summarize results, and update the roadmap.

Deliverables by the end of Module 6: final landing page, launch copy, selected launch channels, launch evidence, launch metrics, post-launch feedback summary, final roadmap, and final capstone submission package.

Launch report template:

```markdown
# Launch Report

## Product URL

## Target audience

## Build-in-public summary

Where I shared progress during the course:
-

What audience/community I built:
-

## Launch channels used

1.
2.
3.

## Launch copy

## Results

Visitors:
Users/signups:
Core flow starts:
Core flow completions:
Feedback submissions:
Comments/replies:
Shares:
Other meaningful metric:

## What worked

## What did not work

## Bugs or issues found

## What I changed after launch

## What I would do next
```

## 12. Final Project: End-to-End Product Capstone Review

The final project is the second formal peer-review point. The midterm asks "is there a deployed MVP that others can test?" The final asks "did this become an end-to-end product that was improved, measured, launched, and explained clearly?"

Each student submits: GitHub repo, commit hash, deployed application URL, free testing instructions if needed, README, landing page, launch evidence, analytics/metrics summary, feedback summary, changelog since midterm, build-in-public summary, final reflection, and future roadmap.

Each student reviews 3 final projects. For each project, the reviewer should test the deployed product, verify free access, inspect the README, try the core user flow, review the launch materials, review the analytics/metrics summary, review changes since midterm, score using the rubric, and leave written feedback.

Final evaluation criteria:

| Criterion | Points |
|---|---:|
| Product problem, audience, and JTBD are clear | 0-3 |
| Product works end to end | 0-5 |
| Application is publicly deployed and accessible | 0-3 |
| Reviewer can test it for free | 0-3 |
| UX/onboarding improved since midterm | 0-3 |
| Evidence of iteration from midterm feedback | 0-4 |
| Analytics or feedback loop is implemented meaningfully | 0-4 |
| Monitoring/error visibility or readiness checks exist | 0-2 |
| Landing page and launch materials are clear | 0-3 |
| Build-in-public activity is documented | 0-3 |
| Public launch or outreach was attempted | 0-3 |
| Metrics and learnings are reported honestly | 0-3 |
| README makes the project easy to evaluate | 0-2 |
| Final reflection and roadmap are clear | 0-2 |

Total: 43 points.

Bonus points for real users beyond classmates, strong external feedback, meaningful usage metrics, signups/waitlist/revenue or other conversion, strong community engagement, clear response to analytics, a polished launch post, a thoughtful roadmap, and excellent documentation.

## 13. Final course timeline

Option A: 6 modules plus midterm plus final.

| Week | Activity |
|---|---|
| 1 | Module 1: Problem Discovery, JTBD, Communities, and MVP Scope |
| 2 | Module 2: End-to-End MVP Deployment |
| 3 | Module 3: MVP Polish and Peer-Test Readiness |
| 4 | Midterm Project Submission and Peer Review |
| 5 | Module 4: Feedback-Driven Product Iteration |
| 6 | Module 5: Product Analytics, Monitoring, and Readiness |
| 7 | Module 6: Launch, Distribution, and Build-in-Public Finale |
| 8 | Final Project Submission and Peer Review |

Option B: compact 6-week version.

| Week | Activity |
|---|---|
| 1 | Module 1 |
| 2 | Module 2 |
| 3 | Module 3 + Midterm submission |
| 4 | Midterm review + Module 4 |
| 5 | Module 5 |
| 6 | Module 6 + Final submission |
| 7 | Final peer review, if needed |

The cleaner version is Option A because the midterm and final review windows are separate and students have enough time to review peers properly.

## 14. Summary of the learning arc

The course progression is Discover, Build, Polish, Review, Improve, Measure, Launch, Review. More explicitly:

1. Discover the problem, audience, job, and communities.
2. Build a deployed full-stack MVP.
3. Polish it until another person can use it.
4. Review peer MVPs at the midterm.
5. Improve based on feedback.
6. Measure usage and detect problems.
7. Launch to communities developed during the course.
8. Review final shipped products.

The most important design decision is that community and build-in-public start in Module 1, not Module 6. By the time students launch, they should not be shouting into the void. They should already know where their users are, what language they use, what problems they care about, and where to share the product.

## 15. References and inspiration

- AI Shipping Labs Full-Stack Vibe Coding workshop: https://aishippinglabs.com/workshops/full-stack-vibe-coding
- DataTalks.Club ML Zoomcamp project structure: https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/projects
- DataTalks.Club LLM Zoomcamp project structure: https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md
- Vibe Shipping repository: https://github.com/ad3002/masters-course-2026-vibe-shipping

## Sources

[^1]: [20260701_130457_AlexeyDTC_msg4649.md](../../inbox/used/20260701_130457_AlexeyDTC_msg4649.md)
[^2]: [20260701_130457_AlexeyDTC_msg4650.md](../../inbox/used/20260701_130457_AlexeyDTC_msg4650.md)
