---
title: "AI as Personal Analyst"
created: 2026-02-12
updated: 2026-02-12
tags: [talk, automation, productivity, ai-tools]
status: draft
---

# AI as Personal Analyst

A talk about practical automation using AI to replace complex Excel workflows, clean messy data, and scale document review. The audience is university students (computer science and finance) at Leipzig University.

## Talk Overview

This talk shares practical examples of using AI to automate routine but time-consuming tasks without building complex systems or hiring a team.

### What Attendees Will Learn

- How to replace complex Excel formulas and VLOOKUP chains with simple conversations in ChatGPT
- How to turn messy user input (like 100+ variations of country names) into clean, structured analytics
- How to automate review of 1500+ course applications using LLM-based scoring
- When ChatGPT is enough and when a local AI setup (Claude Code + Python) becomes more powerful

This is not about theory. It is about saving hours every week by treating AI as a personal analyst and automation partner.

## Use Case 1: Replacing Complex Excel Logic with ChatGPT

### The Problem

My partner works in import/export, and her team frequently deals with Excel spreadsheets involving:
- Multiple tables
- Complex VLOOKUP formulas
- Data merges and aggregations
- Manual transformations

For me as a developer, this is straightforward using Python and pandas. But even simple tasks could take 1-1.5 hours when accounting for setup and debugging.

### The New Approach

Instead of writing code manually:

1. Upload the Excel files directly to ChatGPT
2. Describe the required transformation in plain English
3. ChatGPT writes and executes Python code internally
4. It shows the resulting tables
5. Iterate if necessary

Result: 5-10 minutes instead of an hour.

In most cases, I don't even inspect the code. I focus only on the outcome.

Key insight: ChatGPT acts as an interactive data analyst, not just a chatbot.

## Use Case 2: Country Name Normalization

### The Problem

In my free courses, users register via a form and enter their country manually. The input can vary wildly:
- USA
- U.S.A.
- United States
- America
- US
- United States of America

For reporting and sponsor presentations, I need:
- Clean country-level statistics
- Aggregation by regions (North America, Europe, etc.)
- Reliable structured data

### The Solution

Using ChatGPT:
- Upload the dataset
- Ask it to generate a normalization mapping
- Refine the results
- Generate a reusable Python script

Over time, this evolved into a small internal project that:
- Normalizes country names automatically
- Aggregates data by region
- Produces sponsor-ready statistics

Key takeaway: AI helps transform messy real-world data into structured insights quickly.

## Use Case 3: Automating Scholarship Selection with Claude Code

This case required a more advanced setup.

### The Problem

For my paid course, I offer scholarships. In the first year:
- 1500+ applications
- Long-form text answers
- Complex and partially subjective evaluation criteria

Manual review was extremely time-consuming.

### First Attempt (ChatGPT Only)

I copied submissions manually into ChatGPT and asked it to evaluate them. It worked, but required too much manual effort.

### Current Solution (Claude Code + Local LLM Workflow)

Now I:
1. Download the full dataset locally
2. Use Python + Claude Code
3. Create a sub-agent that:
   - Analyzes all submissions
   - Scores them based on predefined criteria
   - Produces a ranking
4. Review the top 100 manually

AI does not replace my judgment. It filters noise and dramatically reduces workload.

This saves dozens of hours per selection cycle.

## When to Use ChatGPT vs Claude Code

### ChatGPT is sufficient when:
- Tasks are small or one-time
- You need quick Excel analytics
- Data sensitivity is not critical
- You don't want to configure a local environment

You only need a subscription.

### Claude Code is better when:
- You work with large datasets
- You analyze text at scale
- The workflow is recurring
- You want full control over code
- Data must remain local

It requires Python setup, but once configured, AI writes most of the code for you.

## Key Message

AI can function as:
- A personal data analyst
- A workflow automation engine
- An information filter
- A force multiplier for your expertise

You don't need to be an ML engineer to use AI for automation.

The real question is: Which repetitive task in your workflow could you delegate to AI tomorrow?

## Sources

[^1]: [20260212_090547_AlexeyDTC_msg1480.md](../inbox/used/20260212_090547_AlexeyDTC_msg1480.md)
[^2]: [20260212_090642_AlexeyDTC_msg1481_transcript.txt](../inbox/used/20260212_090642_AlexeyDTC_msg1481_transcript.txt)
