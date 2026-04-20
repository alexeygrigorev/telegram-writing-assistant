---
title: "User Interviews"
created: 2026-04-02
updated: 2026-04-20
tags: [ai-shipping-labs, community, user-research]
status: draft
---

# User Interviews

Notes from conversations with community members about what they want from AI Shipping Labs.

## Interview 1: AI Buildcamp Participant

Talked to one of the participants of AI Shipping Labs who came from the AI Engineering Buildcamp course. Reached out to all new members with a personal message asking what they'd find interesting. This person was the only one who offered to jump on a call. Calls turned out to be a very useful format for quickly discussing everything[^1].

### What they want: accountability, not content

The main insight: this person already has plenty of content from the course and hasn't finished going through it. The same problem exists in other bootcamps and courses - participants simply don't complete them[^1].

I showed them our plan from the website - Code Alone Sessions and other activities. They said that the main value of the community for them would be accountability and a clear set of deadlines to follow while building projects. Not just one project, but multiple[^2].

This is exactly what we discussed before: new people join, pick an idea, set a deadline, and start working on a project. Then they present their progress to the community[^2].

When asked what we could do on our side, they said they want a clear pipeline for working on projects. For example, a first deadline for one part of the project, a second deadline for the next stage. A breakdown into stages with gradual deadlines, and accountability through presenting progress[^2].

### Content is not the problem

What surprised me: when I mentioned the idea of doing hands-on workshops and asked if that would be useful (since they said they can't get through existing content), they said they don't need more content. They said if they need something, they go to Andrew Ng's DeepLearning.AI site and take a free mini-course on whatever new technology came out. Content is not the problem. The problem is accountability[^3].

They also said that content would naturally emerge from the projects people build inside the community. For example, if 5 projects are running, each with its own stack, someone could write an article about each part of the stack or about the whole project[^3].

Thanks to the accountability created in the community, members could also share progress on LinkedIn, create GitHub repositories. They said there's tons of information available, but actually getting around to applying it - that's what they lack. They work full-time and can't always organize themselves to implement projects[^3].

### Takeaways

The general idea is clear - they want accountability, not more content. This is actually great because it doesn't require as much time investment from us. Running office hours and answering questions is much simpler than maintaining a content plan and producing content that ultimately nobody watches[^4].

This applies especially to those who are participants of the AI Engineering Buildcamp (first or second cohort). When people who haven't bought the course start joining the community, they'll probably have slightly different needs. But for now there aren't many of those, so we can talk to each one individually and create a plan for them. And if I know what their plan is, I can make announcements in the community or organize events where they present their projects - without requiring Alexey's time[^5].

## Interview 2: Jacob

Valeriia talked to Jacob. He decided to join the community and buy the Tier 1 plan. She explained the difference between the tiers[^7].

### Background

Jacob switched to a new job recently and now has more free time. He found Alexey through a recommendation and took the AI Engineering Buildcamp. Before that, he tried the LLM Zoomcamp and another AI Engineering course from a different creator. He started with Data Science, then Computer Science, and now Applied AI. He is studying these topics at his university[^7].

### The problem: accountability, not content

Jacob said he does not have a problem finding content. His problem is accountability - maintaining a steady study routine and staying consistent. This is the same pattern as Interview 1. He joined Tier 1 because he likes how Alexey teaches and his approach to courses, but said Tier 1 was not very useful for him because it was more theoretical[^7].

### Moving to Tier 2

Valeriia suggested that if his goal is accountability and consistency, Tier 2 might be a better fit. Tier 2 includes joining the community, getting initial support from Alexey to plan a project, and regular meetings (once a week or twice a month) where community members share their projects[^8].

Jacob said he was convinced. He will try subscribing for one month at 50 euros. If he likes how things go, he will continue. Otherwise he will leave. Valeriia told him she is always happy to stay in touch and hear his feedback[^8].

### Python course interest

Valeriia told Jacob that he inspired the creation of a Python course. He said he was very happy to hear that and that such a course would be very useful for him. He already took a Python course elsewhere but would be happy to take one from Alexey to reinforce his knowledge, because he likes how Alexey teaches[^9].

Valeriia said she would ask Alexey which tier will have access to this course. She remembers that early access could be given to those who just joined[^9].

### Ideas from the conversation

Valeriia had an idea about Tier 1 content strategy. Even though Jacob said he does not have a problem finding content, some topics are still unclear to him. The idea is to have text-based content inside the newsletter covering specific topics like MCP, RAG, and others. This way people in Tier 1 learn through text content on topics that interest them or that they struggle with. The paid newsletter could also share what community members built after a month of work - "if you joined, you could build this too"[^9].

The second idea is that the newsletter could provide more fundamental, beginner-friendly content with explanations for those starting from scratch. For those who want more support and want to continue at a deeper level, they go into the community (Tier 2)[^9].

## Community Survey Responses

Reached out to AI Shipping Labs members asking what they want to see in the community. Here are the responses[^10].

### Lucia

Anything related to OpenClaw is interesting. She started a demo of a skill in a hackathon and wants to integrate it with OpenClaw. It is her hobby project[^11].

### Chandra

His goal with AI is to build something he can sell as a side income or build his brand. He has gotten good at using Kiro (Amazon) and is picking up speed with Claude Code. Where he is stuck is how to push something to production[^12].

Two broad areas he wants to learn about[^12]:
- Inference optimization - how to optimize costs by finding the right inference layer
- How to use evals to automate this

When asked if he already has ideas, he said no - it feels like drinking from a firehose and he doesn't know where to start. He will keep working on it[^12].

### Member responses on topics of interest

One member said the hottest topic at the moment is OpenClaw, so anything related to that is interesting[^13].

Another member is curious about inference and how to run models locally on cheaper machines. They recommended starting with the Baseten inference engineering book (https://www.baseten.co/inference-engineering/) and an interview with Scott Hanselman (https://www.youtube.com/watch?v=lcC1rtHjDrw). They are also interested in hearing from someone who has taken an AI product to production as a side income - their learnings, gotchas, and starting points[^14].

One member wants to discuss relevant topics but also the challenges people face with the constant buzz of new tools, frameworks, and paradigms. Despite trying to keep up, they feel constantly behind, and it can be overwhelming[^15].

### MCP and multi-agent workflows request

One member wants to learn about writing custom MCP (Model Context Protocol) servers, particularly for long-term memory and context storage. They see the biggest bottleneck in AI-assisted coding as managing context without blowing out the context window with bloated .md files[^16].

Specific topics they want tutorials or deep dives on[^16]:
- Building a persistent memory bridge - how to write a local MCP server (using SQLite, pgvector, etc.) to store state across sessions
- Multi-agent workflows - how to use shared memory to set up a "Worker/Supervisor" dynamic, for example showing how Gemini can act as the executor writing drafts to the MCP context while another model like Codex or Claude reads that same memory space to act as a reviewer

They haven't built this themselves yet, but learning how to construct a shared brain so multiple models can collaborate and iterate on the same project is what they hope to get from the community[^16].

## Member Outreach Responses (April 2026)

Valeriia reached out to all existing Slack members with personal messages, announcing community events and activities and offering to create individual learning plans. Four people responded besides Jacob. She plans to talk to each of them (or receive written responses) and then send notes for Alexey to review and use for creating plans[^17].

Valeriia has been continuing to collect answers from members about their content preferences[^28]. She also suggested creating personalised plans for AI Shipping Labs members. So far, these members have shared that they are interested: Carlos Pumar, Chandra, Edu Gonzalo Almorox, Grace, Jakob Zischka, SPERYDON KOUMARIANOS, Vancesca Dinh, and vishnu[^29].

<figure>
  <img src="../../assets/images/user-interviews/interested-members-list.jpg" alt="List of AI Shipping Labs members interested in personalised plans">
  <figcaption>Members who have shared that they are interested in personalised plans</figcaption>
  <!-- Shows the current list of members Valeriia is collecting inputs from for personalised plan creation -->
</figure>

### Leonor

Leonor wants to have a 30-minute chat sometime in May. For her plans with agentic AI, she first wants to finish her capstone project. She has been reaching out to colleagues to let them know she is building AI engineering skills and wants to join agentic AI projects in the future. She wants to experiment with different forms of agentic memory, particularly methods based on knowledge graphs (e.g. Cognee). She is also interested in developing a text-to-SQL translation workflow[^18].

Leonor also said she will watch the replay of the launch stream. She did Alexey's Maven course and there is a lot of content in there that she will go through progressively. She does not have any additional requests at the moment[^19][^20].

### Marco Teran

Marco is happy to share the topics he wants to learn about. He also mentioned a technical issue - he cannot access Slido and gets an access denied error[^21].

### Luciano Pecile

The most valuable content for Luciano would be practical, real-world AI use cases, especially around building reliable copilots and agents, evaluation frameworks, and how teams are taking things to production. He is also interested in patterns for integrating AI into existing products and workflows, not just greenfield demos[^22].

### Vancesca Dinh

Vancesca initially said she would respond after reflecting more on what she wants[^23]. She later shared a detailed response, apologising that her son had been home for Easter so her focus had been scattered. She confirmed she is definitely interested in being part of the community[^27].

She is currently searching for an AI role and wants to build a strong portfolio. She completed one project as part of the AI Buildcamp and wants to add another, but has been feeling stuck on coming up with an idea[^27].

She also wants to contribute to the DataTalks community, especially on projects involving LLM/agents, and would love to hear about potential projects she can work on to support the DTC community. She would really like to deploy applications on AWS and is especially interested in evaluating agents[^27].

To maintain motivation, she would like to have a coffee chat with the community where anyone can join and talk about AI, their projects, and things they are working on - kind of a peer learning thing. She would not mind hosting it if it is something we can build[^27].

Valeriia said this input can be used directly to build Vancesca's plan[^30].

### Scott DeGeest

Scott said he needs to look around a bit first and then will give more structured input and feedback[^24].

### Archie

Archie wants to see discussions about the latest tech advancements in the field to stay up to date[^25].

### Brad Smith

Brad replied to Valeriia's outreach. His main interest with AI Shipping Labs is to develop portfolio projects that are interesting to potential employers, while also learning about AI Engineering and applying the findings to his current role. He acknowledged that this is overly broad[^31].

He has taken (not completed) Alexey's bootcamp on Maven and enjoys his approach. The hardest part for him is understanding how to develop solutions and build apps with a consistent tech stack. Deployment specifically is an issue, and getting data into useable forms consistently is his second most pressing issue. He offered to discuss further[^31].

### Anonymous AI Shipping Labs participant

One AI Shipping Labs participant shared what they would like to see next. They thanked Alexey and Valeriia for the opportunity to learn and said they would love to see more courses with a practice-first approach. Specific topics they mentioned: harness engineering for coding agents, and testing and evaluation. They are currently trying to build their own CLI coding agent based on Spec-Driven Development and RAG[^32].

### Plan Status

Valeriia put together a current status of the personalised plans[^30]:

- Jakob Zischka: his input is already collected, so Alexey can review it and prepare a plan
- Vishnu: already had a call with him, but Valeriia needs to ask him some clarification questions
- Vancesca Dinh: the input above can be used directly for her plan
- Others: Valeriia needs to ask them additional questions so that a plan would be more tailored to their goals

Valeriia will share their answers as soon as they are ready[^30].

### Plan Input Collected (April 2026-04-20)

To keep each member's input separate and easy to review, personalised plan inputs now live in their own folder at [articles/ai-shipping-labs/plans/](plans/_index.md) instead of all being mixed into one place. Alexey will review each input and record follow-up notes per member[^33][^34].

Full intake collected so far: Jakob Zischka, Carlos Pumar, Vancesca Dinh, Grace, and Edu Gonzalo Almorox. Carlos has already written a lot on his own, so no separate follow-up questions were sent to him[^35].

## Jacob Follow-Up Call

Valeriia had a follow-up call with Jacob and prepared a list of questions for him to understand what kind of plan he wants[^26].

Jacob wants to start building things independently but does not know where to start or what is required to become an AI engineer. Valeriia showed him the AI learning path. His background is non-technical - he is essentially starting from scratch. He knows some theory about how computers work and the history of artificial intelligence, but from a practical standpoint he has no coding experience. He only recently completed one Python course[^26].

When asked what he wants to learn in AI engineering, he answered some questions with "I don't know." He wants the learning approach to be hands-on and learn-by-building, like in Alexey's courses. He said he already started going through the LLM Zoomcamp, so it might be possible to combine it with the LLM Zoomcamp, or the community could replace the LLM Zoomcamp for him entirely[^26].

Jacob also said there are many resources available but it is not always clear which ones are good. One proposed approach: Alexey creates a list of topics or steps Jacob can take over the next 1-3 months, Valeriia searches for resources (or uses AI to find them), and then they do a final review of what was found to create the final version of the plan[^26].

## Sources

[^1]: [20260402_185517_AlexeyDTC_msg3129_transcript.txt](../../inbox/used/20260402_185517_AlexeyDTC_msg3129_transcript.txt)
[^2]: [20260402_185517_AlexeyDTC_msg3130_transcript.txt](../../inbox/used/20260402_185517_AlexeyDTC_msg3130_transcript.txt)
[^3]: [20260402_185517_AlexeyDTC_msg3131_transcript.txt](../../inbox/used/20260402_185517_AlexeyDTC_msg3131_transcript.txt)
[^4]: [20260402_185517_AlexeyDTC_msg3132_transcript.txt](../../inbox/used/20260402_185517_AlexeyDTC_msg3132_transcript.txt)
[^5]: [20260402_185517_AlexeyDTC_msg3133_transcript.txt](../../inbox/used/20260402_185517_AlexeyDTC_msg3133_transcript.txt)
[^6]: [20260402_185532_AlexeyDTC_msg3139_transcript.txt](../../inbox/used/20260402_185532_AlexeyDTC_msg3139_transcript.txt)
[^7]: [20260410_074954_valeriia_kuka_msg3327_transcript.txt](../../inbox/used/20260410_074954_valeriia_kuka_msg3327_transcript.txt)
[^8]: [20260410_075425_valeriia_kuka_msg3329_transcript.txt](../../inbox/used/20260410_075425_valeriia_kuka_msg3329_transcript.txt)
[^9]: [20260410_095445_AlexeyDTC_msg3331_transcript.txt](../../inbox/used/20260410_095445_AlexeyDTC_msg3331_transcript.txt)
[^10]: [20260410_172207_AlexeyDTC_msg3353.md](../../inbox/used/20260410_172207_AlexeyDTC_msg3353.md)
[^11]: [20260410_172220_AlexeyDTC_msg3355.md](../../inbox/used/20260410_172220_AlexeyDTC_msg3355.md)
[^12]: [20260410_172509_AlexeyDTC_msg3357.md](../../inbox/used/20260410_172509_AlexeyDTC_msg3357.md)
[^13]: [20260410_184334_AlexeyDTC_msg3359.md](../../inbox/used/20260410_184334_AlexeyDTC_msg3359.md)
[^14]: [20260410_184350_AlexeyDTC_msg3361.md](../../inbox/used/20260410_184350_AlexeyDTC_msg3361.md)
[^15]: [20260410_184358_AlexeyDTC_msg3363.md](../../inbox/used/20260410_184358_AlexeyDTC_msg3363.md)
[^16]: [20260410_184425_AlexeyDTC_msg3365.md](../../inbox/used/20260410_184425_AlexeyDTC_msg3365.md)
[^17]: [20260415_111523_AlexeyDTC_msg3400_transcript.txt](../../inbox/used/20260415_111523_AlexeyDTC_msg3400_transcript.txt)
[^18]: [20260413_195429_AlexeyDTC_msg3381.md](../../inbox/used/20260413_195429_AlexeyDTC_msg3381.md)
[^19]: [20260414_081553_valeriia_kuka_msg3383.md](../../inbox/used/20260414_081553_valeriia_kuka_msg3383.md)
[^20]: [20260414_081615_valeriia_kuka_msg3385.md](../../inbox/used/20260414_081615_valeriia_kuka_msg3385.md)
[^21]: [20260414_081635_valeriia_kuka_msg3387.md](../../inbox/used/20260414_081635_valeriia_kuka_msg3387.md)
[^22]: [20260414_081711_valeriia_kuka_msg3389.md](../../inbox/used/20260414_081711_valeriia_kuka_msg3389.md)
[^23]: [20260414_081821_valeriia_kuka_msg3391.md](../../inbox/used/20260414_081821_valeriia_kuka_msg3391.md)
[^24]: [20260414_081832_valeriia_kuka_msg3393.md](../../inbox/used/20260414_081832_valeriia_kuka_msg3393.md)
[^25]: [20260414_124902_valeriia_kuka_msg3395.md](../../inbox/used/20260414_124902_valeriia_kuka_msg3395.md)
[^26]: [20260415_111523_AlexeyDTC_msg3399_transcript.txt](../../inbox/used/20260415_111523_AlexeyDTC_msg3399_transcript.txt), [Gemini meeting notes](https://docs.google.com/document/d/1cRa5kvXgdHNaWMgqwES6I9HZ7lBvQu_ckNpvMIODu_s/edit?usp=sharing) via [20260415_122753_AlexeyDTC_msg3405.md](../../inbox/used/20260415_122753_AlexeyDTC_msg3405.md)
[^27]: [20260416_130638_valeriia_kuka_msg3413.md](../../inbox/used/20260416_130638_valeriia_kuka_msg3413.md)
[^28]: [20260416_140631_valeriia_kuka_msg3415.md](../../inbox/used/20260416_140631_valeriia_kuka_msg3415.md)
[^29]: [20260416_140816_valeriia_kuka_msg3417_photo.md](../../inbox/used/20260416_140816_valeriia_kuka_msg3417_photo.md)
[^30]: [20260416_141112_valeriia_kuka_msg3419.md](../../inbox/used/20260416_141112_valeriia_kuka_msg3419.md)
[^31]: [20260416_200522_AlexeyDTC_msg3426.md](../../inbox/used/20260416_200522_AlexeyDTC_msg3426.md)
[^32]: [20260420_053838_AlexeyDTC_msg3439.md](../../inbox/used/20260420_053838_AlexeyDTC_msg3439.md)
[^33]: [20260420_083829_AlexeyDTC_msg3451_transcript.txt](../../inbox/used/20260420_083829_AlexeyDTC_msg3451_transcript.txt)
[^34]: [20260420_083951_AlexeyDTC_msg3453_transcript.txt](../../inbox/used/20260420_083951_AlexeyDTC_msg3453_transcript.txt)
[^35]: [20260420_083739_AlexeyDTC_msg3442.md](../../inbox/used/20260420_083739_AlexeyDTC_msg3442.md)
