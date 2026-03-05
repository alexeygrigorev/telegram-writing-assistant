---
title: "Project Discovery AI Agent"
created: 2026-03-05
updated: 2026-03-05
tags: [research, agents, design-thinking, projects]
status: draft
---

# Project Discovery AI Agent

An AI agent that acts as a Design Thinking facilitator, guiding people through multiple sessions to go from "I don't know what to do" to a concrete engineering project idea[^1].

This is not a regular Q&A bot. It is closer to coaching and discovery. The agent asks questions, clarifies, and helps think - it does not immediately propose ideas.

See also: [Design Thinking for Finding Project Topics](design-thinking-for-projects.md) - the frameworks and methodology this agent is based on.

## Overall structure

The process is split into 4 sessions, each about 15-30 minutes. Between sessions there are homework assignments[^1].

Session flow:
1. Session 1: Interests and Context
2. Session 2: Problem Discovery
3. Session 3: Idea Generation
4. Session 4: Project Selection

## Session 1: Interests and Context

Goal: understand what the person's life looks like[^1].

The agent asks open-ended questions and follows up with clarifications.

### Hobbies block

Questions:
- What hobbies do you have?
- What do you enjoy doing in your free time?
- What do you like to read or watch videos about?
- What topics can you talk about for hours?

Follow-ups:
- How long have you been doing this?
- What tools do you use?
- Are there communities around this?

### Work and activity block

- What are you currently doing (work, study, projects)?
- What tasks do you do most often?
- What takes the most time?

### Interests block

- What technologies interest you?
- What projects do you consider cool?
- What would you like to learn to do?

### Session result

The AI creates a profile with key areas, interests, technologies, and tools.

### Homework

The AI asks the person to pay attention to their daily routines during the next few days and write down things that annoy them, take too long, or feel manual.

## Session 2: Problem Discovery

Goal: find real problems[^1].

Questions:
- What problems did you notice in the last few days?
- What tasks repeat?
- What annoys you?

### Category-specific questions

Automation: What do you do manually?

Information: What is hard to find?

Data: What data do you have?

Tools: What apps annoy you?

### Hobby-specific questions

- What is inconvenient in your hobby?
- What tasks repeat there?
- What do people discuss as a problem in those communities?

### Expanding the list

The AI helps expand the problem list based on the person's profile from Session 1.

### Homework

Talk to colleagues, friends, and online communities. Ask them: "What problem would you solve if you could?"

## Session 3: Idea Generation

Goal: turn problems into many solutions[^1].

### Step 1: Select 3 problems

The AI asks:
- Which problem seems the most interesting?
- Which one comes up most often?
- Which one do you understand best?

### Step 2: Generate ideas

Rule: at least 10 ideas per problem.

### Catalyst questions

The AI uses directed questions to trigger ideas:

- Automation: can this be automated?
- Prediction: can something be predicted?
- Recommendation: can something be recommended?
- Classification: can something be classified?
- Search: can search be improved?
- Analysis: can data be analyzed?

### Result

A list of 10+ ideas grouped by problem.

## Session 4: Project Selection

Goal: choose the best project and formulate it[^1].

### Evaluation criteria

The AI asks the person to rate each idea:

| Criterion | Question |
|-----------|----------|
| Interest | Is it interesting to work on? |
| Usefulness | Does it solve a problem? |
| Data | Is data available? |
| Complexity | Can it be done? |

### Technical specification

After choosing an idea, the agent asks engineering questions:

- Data: what data is needed?
- Input: what does the user enter?
- Processing: what algorithm?
- Output: what does the system produce?
- Evaluation: how to measure success?

### Final result

The AI generates a project card with the problem, solution, data, model, output, and evaluation metric.

## Agent behavior guidelines

The agent should not immediately propose ideas. It should:

- Ask questions
- Clarify answers
- Help the person think

After each step, the AI creates a summary of what was discussed.

### Idea triggers

If the person is stuck, the AI can show example projects from similar domains to spark inspiration. This significantly speeds up the process.

## Sources

[^1]: [ChatGPT conversation on project frameworks](https://chatgpt.com/share/69a997f4-9d50-800a-a2e7-32823e7b293b) via [20260305_145128_AlexeyDTC_msg2754.md](../../inbox/used/20260305_145128_AlexeyDTC_msg2754.md)
