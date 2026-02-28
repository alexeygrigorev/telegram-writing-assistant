---
title: "Getting a Data Science Job"
created: 2026-02-27
updated: 2026-02-28
tags: [data-science, career, job-search, interviews]
status: draft
---

# Getting a Data Science Job

A summary of the presentation about getting a data science job[^1]. This is from an old video, made before DataTalksClub, but much of the advice is still relevant today[^2].

The presentation covers the full job search process: how to look for a job, what data science interviews look like, and what happens after.

<figure>
  <img src="../assets/images/getting-a-data-science-job/summary-slide.jpg" alt="Summary slide from the presentation with key tips for getting a data science job">
  <figcaption>Summary slide from the presentation</figcaption>
  <!-- Frame from the original video, showing the key takeaways covered throughout the talk -->
</figure>

## The Job Search Algorithm

The algorithm is simple in steps but requires a lot of work:

1. Network - go on LinkedIn, connect to people, attend meetups
2. Apply - apply to jobs regardless of qualifications
3. Build - do pet projects, share them online
4. Interview - note what they ask, improve
5. Repeat

Andrej Karpathy's advice on how to become an expert at something complements this well[^3]:

1. Iteratively take on concrete projects and accomplish them depth-wise, learning "on demand" (do not learn bottom-up breadth-wise)
2. Teach and summarize everything you learn in your own words
3. Only compare yourself to your younger self, never to others

<figure>
  <img src="../assets/images/getting-a-data-science-job/karpathy-how-to-become-expert.jpg" alt="Andrej Karpathy's tweet on how to become an expert at something">
  <figcaption>Andrej Karpathy on becoming an expert - learn by doing projects, teach what you learn, compare only to yourself</figcaption>
  <!-- Karpathy's three rules: depth-first projects, teach/summarize in own words, self-comparison only -->
</figure>

## Networking

Connect to everyone you know on LinkedIn and also to people you don't know. Find people from your university, from bootcamps, from your city, people who work in the field where you want to work.

Talk to people who were recently hired, especially juniors or those hired after a bootcamp. Ask how they landed the job. Ask if they have other open positions - chances are they do. They will often be happy to refer you because many companies give a referral bonus when a referred person gets hired.

Be active and share content online. This way you get noticed more easily.

## Applying to Jobs

When you look at job listings, apply anyway regardless of what you see. Descriptions often describe a perfect candidate who doesn't exist. The hiring manager has a perfect candidate in their head and writes a description of this person, but they will have trouble finding them. So even if you think you're not qualified, apply anyway - companies will see they can't find the perfect candidate and decide the available candidate is also fine.

When looking at job postings, note what skills they ask for. If you see something like NLTK or TensorFlow popping up in many job postings, you should learn it. Do a small pet project with it, put the code on GitHub, and write a blog post or a README about it. This way you acquire new skills and get noticed.

## Interviews

An interview is not an exam - it's a two-way process. You also assess the company. Do as many interviews as you can. After each interview, write down the questions you got and do a retrospective: think about what went well and what you can do better next time.

Rejections are fine. There can be millions of reasons: they hired a different candidate, they ran out of money, the company went bankrupt. Don't take them personally. Just keep interviewing.

### Initial Call with Recruiter

A general introduction: the recruiter explains what the company does and what the position is about, then asks you to tell about yourself.

Tips:
- Recruiters aren't technical but may ask technical things - keep replies simple, not too technical
- Prepare a short introduction about yourself (a few sentences) and learn it by heart
- They will ask about salary expectations

### Salary Expectations

Two approaches:
- Say the number upfront - works well when you already know the market and have experience
- Postpone the conversation - works when entering a new field, relocating, or when you don't know the market yet

Regardless of which approach you choose, do research and have a number in mind. Recruiters can be pushy and may not accept "let's talk later" as an answer.

### Theory Screening

Theoretical data science and machine learning questions: what is linear regression, what is overfitting, what is the ROC curve, etc.

The interviewer doesn't expect detailed answers. A few sentences that answer the question on an intuitive level are enough, without going deep into mathematics. If they ask something you don't know, be upfront about it - the interviewer will give a hint or move to another question.

### Coding Screening

A technical screening, often done online using platforms like CoderPad or even Google Docs. Sometimes on-site on a whiteboard.

For data science positions, SQL and Python are important. Some companies treat data scientists as software engineers and also check computer science basics (data structures, algorithms).

For basic coding: they check if you know Python basics - lists, sets, dictionaries, loops, if statements.

For algorithmic questions (binary trees, linked lists, etc.): check with the recruiter first if this is actually part of the process, because very few companies do this. If they do, LeetCode is a great source for practice.

When solving exercises, take notes so you can come back and review them later.

### Home Assignments

A task to do at home: they give you a dataset and ask you to build something - train a model, predict prices, classify listings.

Warning signs to watch for:
- You get an automatic email with an assignment immediately after applying (the company may not even be actively hiring)
- Instructions are deliberately unclear and they say "we want to see how you deal with ambiguity"
- The task "can be solved in two hours" but actually requires weeks

Positive side: home assignments are a great opportunity to add projects to your portfolio and learn new skills/libraries.

If you don't want to invest time but still like the company, you can tell them: "I already have similar projects, check my GitHub, I'm happy to continue talking without the assignment." Many will say no, but some will agree.

After the assignment, some companies have a defense session where you present your solution and discuss it. Having this step is actually a good sign.

### Case Study Interviews

Similar to home assignments but without code. A discussion on how to approach a problem.

Examples: "Build a model for predicting car prices - what would you do?" or a vague question like "We want to increase user engagement - how?"

For vague questions, you need to ask clarifying questions: how do we measure engagement, what do users do on the platform.

A useful approach: start with a simple baseline, quickly iterate, roll out to production, then improve with more complex models.

Learning from Kaggle competitions is great preparation for case studies. Go to past competitions, understand the problem, data, features, target, evaluation metric, and check forums to see what solutions worked.

### System Design Interviews

Focuses on the engineering side. Examples: design a system for duplicate detection, spam detection, search autocomplete.

Traditional system design is what software engineers get (design Instagram, design an online library). For machine learning engineers and data scientists, the questions involve machine learning components.

To approach this:
- Ask as many questions as possible from the interviewers
- Break down the system into components
- Explain your reasoning for decisions (relational vs. non-relational database, etc.)
- Think about what happens if load increases 10x

This is hard to prepare for because it requires experience. Best preparation comes from doing these things at work. Also look up system design resources online, go to conferences, read tech blogs. Before interviewing at a specific company, check their tech blog.

This is typically not for junior positions. Senior positions include it more often.

The difference between case studies and system design: case studies focus on the initial steps (formulating the problem for machine learning), while system design is about productionizing and engineering the solution.

### Behavioral Questions

Questions to see if there's a cultural fit. Examples: "Tell me about a time when you disagreed with someone," "When you needed to go beyond your duties."

Preparation:
- Research the company's values (if publicly available)
- For each value, think of 2-3 situations where you demonstrated it
- Structure answers in STAR format (Situation, Task, Action, Result)

Example in STAR format: "I had a problem with a library nobody knew. Nobody could help me, but I needed to fix it because it blocked my progress. I found an online course, took it, fixed the problem, and showed others how to do it."

If the company doesn't have public values, check Amazon's 14 leadership principles - they are a good generic set to prepare with.

## After the Interview

Two outcomes: you get an offer, or you don't.

If rejected: don't take it personally. Treat it as a learning experience. Do a retrospective, understand what went wrong (often nothing was wrong with you personally - someone was just better, or they ran out of money). If you lack some skill, build a project to improve it.

If you get an offer: don't rush into agreeing immediately. If you have interviews with other companies, finish them first. Once you get the first offer, tell other companies about it to speed up their process. Having multiple offers is the ideal situation for negotiating salary and benefits. With just one offer, negotiation is difficult.

If you already named a salary number in the initial interview and they offer that exact number, it's very hard to negotiate upward.

## Sources

[^1]: [Getting a Data Science Job - YouTube](https://www.youtube.com/watch?v=jYYR1fH8k7o)
[^2]: [20260227_140004_AlexeyDTC_msg2572_photo.md](../inbox/used/20260227_140004_AlexeyDTC_msg2572_photo.md) and [20260227_140020_AlexeyDTC_msg2574.md](../inbox/used/20260227_140020_AlexeyDTC_msg2574.md)
[^3]: [20260228_170401_AlexeyDTC_msg2610_photo.md](../inbox/used/20260228_170401_AlexeyDTC_msg2610_photo.md)
