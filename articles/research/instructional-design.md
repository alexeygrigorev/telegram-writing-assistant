---
title: "Instructional Design for Online Courses"
created: 2026-02-18
updated: 2026-02-18
tags: [research, instructional-design, courses, ai-buildcamp]
status: draft
---

# Instructional Design for Online Courses

Research on instructional design principles for improving course completion rates and student engagement. Based on advice from Alex Migutsky and the book "Instructional Design That Soars."

## Context

After lunch with Alex Migutsky, who also runs a course (focused on career advancement, not engineering), several ideas came up about how to improve course design. Alex asked about completion rates. The numbers are not great: out of about 50 people who signed up for the first cohort, roughly 10 did the first homework, and only 5-6 graduated. That is about 10% completion[^1].

The question is: how can this be improved? The core idea is to make each week maximally actionable, reduce friction, and lead students step by step so they build something real by the end[^1].

## Week-by-Week Guided Project Approach

The idea is to give students a step-by-step guided project that grows week by week. Each week they add a small piece of code or do a specific action. The goal is to make it maximally frictionless so they do not get stuck[^1].

### Week 1: Project Idea and Repository Setup

Ask students to come up with a project idea. During this first week, they should already create a repository with a README where they describe their idea[^1][^2].

### Week 2-3: Agents and Tools

When we get to agents, students need to prepare tools. Even if they do not have tools yet, they should create a design document in the README. Give them a class where the tools are already implemented, and tell them to adapt it to their requirements. Give them an agent that already calls this class. What they need to change is the instructions and the tools[^2].

### Week 4: Tests

Give them code for tests. Show them a test with a judge and a regular unit test. Their task is to adapt these tests for their own project and run them to make sure they work[^2].

### Week 5: Logging

Connect LogFire and have data flowing[^2].

### Week 6: Evaluation

Connect an evaluation tool. Come up with 10 questions on your own or use an LLM to generate 10 questions[^2].

The approach is to lead them step by step, by the hand. In the end they will have their own working project[^2].

### Sample Project Format

The sample project should be in text format, not video. This makes it easier to change and update. Students copy code from it. The idea is not to explain things again, but to provide a reference project: "here is a sample project, you can build yours based on it"[^3].

Can even take a maximally simple project and lead students through it across the entire course[^3].

### Providing Structure

Students can be given a project structure to follow. They can fork a template project or create a project with the specified structure. This way they do not waste time on setup and can focus on making progress on the actual course content. Each week they are told "add this code here, add that there." This keeps things maximally actionable and reduces friction[^1].

### AI Assistant for Completion

Students could launch an AI assistant at the end of the course that would complete the remaining parts of their project based on the code they have built up week by week. The main thing is that they make progress step by step, and then the assistant can finish what is left. The code needs to be prepared in a way that the assistant can work with it[^1].

## Goal for Cohort 3

The goal for the third cohort is to implement this approach. Current focus is on content. Next week the focus shifts to guidance: how to use this content. There is a lot of content and the key is making sure people do not get lost. They should focus more on their project. They can be told: "watch these videos, then immediately do your homework on the topic, then do the mini-homework." Repeat frequently that there is a lot of content and they probably do not need all of it right now - watch it later when it becomes relevant for their project[^1].

## Book: "Instructional Design That Soars"

Recommended by Alex Migutsky. This book covers how to design courses effectively[^4][^5].

## Instructional Design Feedback Agent

A role prompt for getting AI feedback on course design[^6]:

```
## CORE IDENTITY
You are an instructional designer with 20 years of experience designing corporate
training and online courses. You are an expert in learning outcomes, curriculum
sequencing, engagement, and retention. You are obsessed with completion rates. You
hate fluff. You always ask 'What will they be able to DO after this?' You follow
principles from 'Instructional Design That Soars.'

## EXPERTISE AREAS
- Learning outcomes design (Bloom's taxonomy, action verbs)
- Curriculum sequencing and scaffolding
- Cognitive load management
- Practice-to-instruction ratio optimization
- Retrieval practice and spaced learning
- Error prevention and stuck-point design
- Completion rate optimization

## FRAMEWORKS & MODELS
- ADDIE: Analyze -> Design -> Develop -> Implement -> Evaluate
- Bloom's Taxonomy: Remember -> Understand -> Apply -> Analyze -> Evaluate -> Create
- Practice Ratio: Target 40-50% practice time in live sessions
- Cognitive Load Theory: Limit new concepts per session
- Just-in-Time Learning: Teach concepts immediately before needed

## KEY BODY OF KNOWLEDGE
- 'Instructional Design That Soars' book principles
- Adult learning theory (Andragogy)
- Corporate training best practices
- Online course completion rate research
- Cohort-based learning dynamics

## PSYCHOGRAPHICS
- Outcome-obsessed; every element must serve learning
- Skeptical of 'content dump' approaches
- Values transformation over information
- Metrics-driven; tracks completion and application rates
- Precision-focused; every minute should have purpose

## WHEN TO DEPLOY THIS ROLE
Use for: curriculum design, workshop structure review, learning outcome definition,
practice exercise design, cognitive load assessment, completion rate optimization.

Be specific. Point out what works, what doesn't, and exactly how to fix it. Use
learning science to justify recommendations.
```

### How to Use This Agent

Alex explains this is how the agent should be used: before preparing any content, run it through this role for feedback on the curriculum design. This can be applied for new modules that will be planned, though it is unlikely to be applied to the current course since it is already underway[^8].

### Micro Tip: Narrative Arc

Always ask this role about the narrative arc in lectures and modules[^7]. Example prompt: "Check the narrative arc of this week lectures"[^7b].

## Deep Research Plan

Want to do deep research on this topic. The book is good, the skill/role is useful. Will add findings from ChatGPT research and other sources as they are discovered[^9].

## Sources

[^1]: [20260218_115900_AlexeyDTC_msg1925_transcript.txt](../../inbox/used/20260218_115900_AlexeyDTC_msg1925_transcript.txt)
[^2]: [20260218_120056_AlexeyDTC_msg1926_transcript.txt](../../inbox/used/20260218_120056_AlexeyDTC_msg1926_transcript.txt)
[^3]: [20260218_120134_AlexeyDTC_msg1927_transcript.txt](../../inbox/used/20260218_120134_AlexeyDTC_msg1927_transcript.txt)
[^4]: [20260218_120220_AlexeyDTC_msg1928.md](../../inbox/used/20260218_120220_AlexeyDTC_msg1928.md)
[^5]: [20260218_120250_AlexeyDTC_msg1930_transcript.txt](../../inbox/used/20260218_120250_AlexeyDTC_msg1930_transcript.txt)
[^6]: [20260218_120220_AlexeyDTC_msg1929.md](../../inbox/used/20260218_120220_AlexeyDTC_msg1929.md)
[^7]: [20260218_120318_AlexeyDTC_msg1931.md](../../inbox/used/20260218_120318_AlexeyDTC_msg1931.md)
[^7b]: [20260218_120337_AlexeyDTC_msg1932.md](../../inbox/used/20260218_120337_AlexeyDTC_msg1932.md)
[^8]: [20260218_120401_AlexeyDTC_msg1933_transcript.txt](../../inbox/used/20260218_120401_AlexeyDTC_msg1933_transcript.txt)
[^9]: [20260218_120622_AlexeyDTC_msg1934_transcript.txt](../../inbox/used/20260218_120622_AlexeyDTC_msg1934_transcript.txt)
