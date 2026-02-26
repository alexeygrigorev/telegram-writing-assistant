---
title: "Community Platform Feature Ideas"
created: 2026-02-26
updated: 2026-02-26
tags: [community, features, ai-shipping-labs]
status: draft
---

# Community Platform Feature Ideas

In the previous articles about student projects and project ideas, some items came up that are not student projects but features for the site itself. This article collects feature improvement ideas for the community platform. Not everything needs to be implemented right away - you can ask people when they join how interested they are in each feature before building it[^1].

## Business Case Simulator

Inspired by the [Karpov.Courses Simulator](https://karpov.courses/simulator-ds)[^2]. The Karpov simulator is a practice-oriented platform where students solve real business cases instead of watching lectures. It has 100+ tasks organized by difficulty, automated checking with instant feedback, and reference solutions from the authors. Topics include Python, SQL, A/B testing, LLMs, recommender systems, forecasting, and model deployment across industries like retail, fintech, and edtech[^2].

Someone mentioned that there is this simulator at Karpov.Courses, and it has been around for a while. The idea is to make something similar but for the international audience and for AI engineering cases specifically. It can be in English, German, and whatever language - the task is how to scale the learning[^2].

The idea is to build something similar for the community so people can practice AI engineering cases. This could work well for the Main (middle) subscription tier. Need to check how to manage costs so users do not consume too much - some limits would be needed. But overall it would be a great feature[^3].

This could also serve as an agent project idea - you have a set of business cases, and the agent helps you work through them[^3].

The chat conversation about the simulator provided more context on how it works[^2]:

- The simulator is a "world" plus all the tools an analyst uses, plus the world reacting to actions. A literal simulation
- For example, there is a task to calculate SKU
- It is built using tokens and runs on LLMs through orchestration
- Claude's new approach of always doing research/planning/clearing/plan execution when facing a new unfamiliar task was also discussed - this is what enabled building such a system
- The discussion also touched on the usefulness for business - it is not just knowing tools, but understanding how to apply them to solve business problems. That is exactly what the simulator addresses with business cases

## Career Help and Job Search Tools

The global vision is to have something that helps people find jobs. After finishing the course, community members may be wondering about next steps. This feature can help them figure that out[^4].

An agent that scrapes new jobs from different locations can be set up. It sends different trends about these jobs - new positions, different trends. You can discuss the trends in the data with the agent. If you have your own profile, it can quickly highlight jobs you are a good match for and highlight areas for improvement. It can cluster jobs, help select a domain, and help select project ideas relevant to those jobs[^5].

Based on the data already collected (like the AI engineering field guide), you can continue collecting more data. Then build a RAG on top of it so people can query it with their profile for personalized recommendations[^5].

## Data Collection

The value might not be in a specific agent built on top but in the data collected for the community. The focus should be on figuring out where to get all this data so that it is genuinely useful to people[^6].

Setting up a process and thinking through where all the data comes from is the key step. The agent or tool built on top is secondary to having good data[^6].

## Sources

[^1]: [20260226_113315_AlexeyDTC_msg2512_transcript.txt](../inbox/used/20260226_113315_AlexeyDTC_msg2512_transcript.txt)
[^2]: [20260226_113425_AlexeyDTC_msg2514.md](../inbox/used/20260226_113425_AlexeyDTC_msg2514.md), [20260226_113544_AlexeyDTC_msg2516_transcript.txt](../inbox/used/20260226_113544_AlexeyDTC_msg2516_transcript.txt)
[^3]: [20260226_113544_AlexeyDTC_msg2516_transcript.txt](../inbox/used/20260226_113544_AlexeyDTC_msg2516_transcript.txt)
[^4]: [20260226_113648_AlexeyDTC_msg2518_transcript.txt](../inbox/used/20260226_113648_AlexeyDTC_msg2518_transcript.txt)
[^5]: [20260226_113217_AlexeyDTC_msg2510_transcript.txt](../inbox/used/20260226_113217_AlexeyDTC_msg2510_transcript.txt)
[^6]: [20260226_113706_AlexeyDTC_msg2520_transcript.txt](../inbox/used/20260226_113706_AlexeyDTC_msg2520_transcript.txt)
