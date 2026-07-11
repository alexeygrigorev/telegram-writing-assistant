# Writing a Good README

Your README is the most important file in your project. It's often the only file other people read.

Think of it as the landing page for your project. If you want people to read and understand what you built, invest time in polishing it. That applies to any project - a pet project, a course project, or a portfolio project you're building to get hired.

At my last job I was heavily involved in hiring. I was doing the first technical screening after the call with the recruiter, so reviewing candidate profiles and their projects was part of my job. I'd open a repo, read the README, and within 10 seconds decide whether to keep going or stop. Most of the time I wouldn't continue. If the README didn't tell me what the project was about or how to run it, I wouldn't spend time trying to figure that out myself.

Now I run courses, and I see the same thing with hundreds of student projects in every cohort. In all my courses, there's a peer review process: your project is reviewed by your peers and you review their projects. Reviewers need to open the repo, understand what it's about, try to understand the code, and score the project.

A README that doesn't help them do that costs you points. I've seen projects lose points because the evaluation results were buried three notebooks deep with no link from the README.

In this article I focus on AI engineering projects, so people taking [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) or [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) will find it relevant. But the same principles apply to [other zoomcamps](https://datatalks.club/blog/guide-to-free-online-courses-at-datatalks-club.html) or pretty much any other project.

To illustrate the idea, I'll use a running example: [Fitness Assistant](https://github.com/alexeygrigorev/fitness-assistant). Fitness Assistant is a RAG application that helps users find exercises and alternatives. I built it two years ago as a reference project for LLM Zoomcamp. It was already in decent condition, but I polished it a bit more for this article.


## Your readers

Your README is read by different people for different reasons. A good README needs to serve all of them.

If it's a course project, the first category of your readers are the peer reviewers. 

Peer reviewers usually spend 15-45 minutes trying to understand the project:

- open the repo
- read the README
- check the illustrations
- try to understand the code
- score against criteria

If the peer reviewers can't find your evaluation or monitoring because it's buried inside your repo, you lose points - even if the work is there.

Some reviewers won't spend money on API keys, so screenshots and demo recordings matter.

In my courses, I recommend cloning the project and running it locally to understand it properly. But most reviewers won't do that unless your README already convinced them it's worth the effort.

Hiring managers won't spend more than a few minutes on your project. They want to quickly understand what it is and how it works. They also want to see if it's relevant to what AI engineers do at their company. That means tests, evaluations, monitoring, and engineering best practices. They don't have time to read your code, so the README needs to show them those things are there.

And then there's your future self. A good README lets you pick up a project months later and remember what it does.

You want to optimize for all three readers:

- Make it easy for hiring managers to skim and see that your project has the components they care about: tests, evals, monitoring.
- Help reviewers see that your project deserves the top score.
- Give your future self enough context to pick the project back up months later.

If your project isn't going to be peer reviewed, it still helps to pretend that it will be. Include the imaginary peer reviewers in your README's target audience.


## The structure

A good README follows a structure. It doesn't have to follow this exact order, and include all these elements, but the more boxes your project checks, the better. 

Must-have sections:

- Title and one-line description - what the project is, in one sentence
- Problem - what problem this solves and who the user is
- Demo - screenshot, GIF, video, or sample output showing the project working
- Quickstart - clone, install, configure, run it locally, with actual commands

Important for AI engineering projects:

- Deployment - where it's deployed and how to go about deploying it
- Testing - how to run tests, with one command if possible, what kind of tests are there
- Evaluation - what's in the eval set, what metric you chose
- Monitoring - what you log and how to access it

Nice to have:

- Architecture - a diagram showing the data flow through your system
- Dataset description - what data you used, where it came from, licensing
- Project structure - key files and folders with one-line descriptions
- Limitations - what doesn't work yet, what's out of scope, what you'd do differently

Other potentially relevant sections:

- Self-evaluation - score yourself against the rubric, so reviewers can compare
- Decisions and trade-offs - why you chose this approach over another
- Tech stack - the libraries and services you used
- CI/CD setup - what runs on push, how tests and evals are automated
- Future work - what you'd build next if you had more time
- Contributing guidelines - for open source projects

Let's walk through the most important ones.


## Title and one-line description

What the project is, in one sentence. If someone reads only this line, they should know what your project does.

Keep it under 25 words. Name the user, the problem, and the solution in one go. If you can't do that in one sentence, your project scope might be too broad.

For the Fitness Assistant: 

A conversational AI that helps users choose exercises and find alternatives. It makes fitness more approachable for beginners who find gyms intimidating or can't always access a personal trainer.

In one sentence it tells you:

- the problem (fitness is hard for beginners)
- the user (beginners without a trainer)
- the solution (conversational AI for exercise selection)


## Problem

Your one-line description tells readers what the project does. The problem section tells them why it matters. Don't write a formula - tell the story. Start with a concrete scenario: what's the user trying to do, what gets in their way, and why existing tools don't help. Then name who your project is for, specifically.

Be specific about who the user is. "A fitness app for everyone" isn't a problem statement. "Beginners who want guidance on exercise selection and form but don't have access to a personal trainer" is. The best problem sections I've seen start with a relatable moment - "people trying to lose weight struggle to turn a vague goal into a daily plan" - and then narrow to a specific user.

<!-- illustration: screenshot of the Problem section from the Fitness Assistant README -->

For the Fitness Assistant, the problem section opens with the scenario: staying consistent with fitness is hard for beginners, gyms are intimidating, and personal trainers aren't always affordable. Then it narrows to the user: beginners who want guidance but don't have access to a trainer. That's what makes the project feel real rather than a technical exercise.



## Demo

Screenshot, GIF, short video, or sample output. Put it near the top. A reviewer who won't run your code can still see the project working. For a hiring manager skimming your GitHub, a demo is proof the project runs and does something real. Without it, the README is just claims.

For a video, use Loom, QuickTime screen recording, or OBS. Keep it under 2 minutes. Show a user interacting with the app, not your IDE, and if a video feels like too much effort, a screenshot of the app or sample input and output is enough.

For the Fitness Assistant: a [YouTube video walkthrough](https://www.youtube.com/watch?v=RiQcSHzR8_E) so a reviewer sees the app running without cloning anything.



## Quickstart

Include these things:

- prerequisites (Python version, Docker)
- the clone command
- dependency installation
- environment setup
- the run command

Use actual commands in code blocks, not descriptions of commands. Show the one-command version first, then the detailed steps.

For the Fitness Assistant: `uv sync` to install dependencies, then `uv run python server.py` to start the app. Fitness Assistant shows the one-command Docker path (`docker-compose up`) at the top, with the full local development setup further down.

<!-- illustration: screenshot of the Quickstart section from the Fitness Assistant README -->


## Architecture

A simple diagram (Mermaid, image, or text) showing where data enters and what comes out.

For the Fitness Assistant, the architecture is a Mermaid flowchart. It shows the Flask API, the RAG module retrieving from minsearch and calling OpenAI, the answer going back to the user, and the conversation logged to PostgreSQL for Grafana.


## Testing

Explain how to run tests, with one command if possible. If you don't have tests, say so honestly.

For the Fitness Assistant: no automated tests, noted as a limitation. Honesty is better than hiding it.


## Evaluation

An AI project without evaluation is a demo, not a project. Show the numbers and include what's in the eval set: easy cases, messy cases, out-of-scope requests, refusal cases. State the metric you chose, what the baseline showed, and what improved after changes. Put the eval code in a separate location and document how to run it.

For the Fitness Assistant, the evaluation section shows both retrieval metrics (94% hit rate, 90% MRR after boosting) and RAG flow quality (83% RELEVANT with gpt-4o-mini). It includes the boosting parameters that produced the best results and links to the evaluation notebooks and data files. A reviewer can see the numbers, understand how they were produced, and check the code.


## Monitoring

Monitoring can start as a local log, but the README should say what you log and how to access it.

At minimum, log:

- request ID
- model name
- prompt version
- retrieved sources
- tool calls
- validation errors
- latency
- token use
- cost
- feedback

For the Fitness Assistant, conversations are logged to PostgreSQL and displayed in a Grafana dashboard. The README includes a dashboard screenshot and lists what each panel tracks, including last 5 conversations, user feedback, OpenAI cost, token usage, model used, and response time.

<!-- illustration: Grafana dashboard screenshot from the Fitness Assistant README -->

## Self-evaluation

If your project is peer-reviewed, include a self-evaluation at the end of the README. Go through the rubric yourself and state the score you think you earned for each criterion. This helps reviewers understand how you see your own work, and it shows you engaged seriously with the evaluation criteria.

If your project is a deployed product with login, payment, or gated features, provide a free testing path for reviewers. Test account credentials, demo mode, or a bypass flag. If reviewers can't test without paying, the submission loses points.

Fitness Assistant includes a self-evaluation because it's a course project. It's not deployed, so it doesn't need a test account. But if it were a deployed web app behind a login, the README would need credentials or a demo mode so reviewers could try it without signing up.

## Other sections

There are more sections you might want to include: deployment instructions, dataset description, project structure, CI/CD setup, future work, contributing guidelines. It's not possible to cover every section in detail. The sections above should give you an idea of what a good section looks like. Each one states what it is, why it matters, and shows it with a concrete example.


## Things to avoid

Common problems:

- Missing setup instructions. If I can't run it from a clean clone, the project lose the reproducibility points (all my courses have this criteria).
- No evaluation. An AI project without eval is a demo.
- No demo. If I have to run your code to see what it does, most people won't.
- Giant notebooks with no link from the README.
- Stale READMEs where the deployed version doesn't match what's written.
- A wall of text with no demo, no screenshots, no eval numbers, and no clear explanation of what the project does. The reviewer opens the repo, sees a long description, scrolls for setup, can't find it, and moves on.
- A README that describes what the project will do (future tense) rather than what it does. If it says "this project will implement monitoring," the reviewer assumes monitoring isn't done.


## Using AI to write your README

You don't have to write the README from scratch. A coding agent like Claude Code or Codex is well suited for this. It can read your entire codebase and understand what the project actually does.

Give the agent the section structure from this article and ask it to generate a first draft. It can read your code, your eval scripts, your monitoring setup, and your tests - so it has real context. Just make sure your project actually has the things the README describes: tests that pass, an eval that runs, a working monitoring setup.

What you get is a first draft, not a finished product. Remove sections that don't apply, add what's missing, and edit the tone. The agent won't know your evaluation numbers or your trade-offs unless you point it at them. Walk it through the decisions you made and the results you got, then let it write.

## Exceptional examples from student projects

I analyzed every submitted project from the zoomcamp and Buildcamp project showcases. I scored them against the rubric from this article. Here are four that stood out, each illustrating a different strength. These are real projects from real students. Use them as reference.


## AI Diet Coach

Repo: github.com/thetsuwin66/ai-diet-coach-agent (Buildcamp Cohort 3)

A clear first screen - a reviewer can understand the project in 30 seconds without running anything. There's a live deployed demo link right after the problem statement, with screenshots of the chat interface, meal plan, progress tracking, and monitoring dashboard.

The problem section names a specific demographic: "users in Southeast Asia who follow Asian diets, a demographic underserved by Western-centric diet tools." It includes a Mermaid architecture diagram showing every component. The monitoring section has screenshots of both a custom dashboard and Logfire tracing.


## Research Radar

Repo: github.com/55382/Research_Radar_agent_phd_assistant (Buildcamp Cohort 3)

The best opening line in the pool. The one-liner tells you the input (ArXiv papers), the output (a personalized digest email), and the user (researchers in fast-moving fields). It even captures the feedback loop, all in one sentence. It interprets every metric in plain language and shows a parameter tuning table that demonstrates evaluation was used to make decisions. It covers deployment, CI, and 67 tests. The most complete README of the group.


## CineRAG

Repo: github.com/bielacki/cinerag (LLM Zoomcamp 2025)

The deepest evaluation section of any project. Two separate eval sections. One for retrieval (five approaches compared with hit rate and MRR numbers). One for LLM answer quality (LLM-as-a-judge with relevance and faithfulness metrics). Each section explains the eval dataset, the metrics chosen, and how to run the eval, with results in tables. A reviewer can see exactly how the project was evaluated without digging into notebooks.


## Applied ML Teaching Copilot

Repo: github.com/marcoteran/applied-ml-teaching-copilot (Buildcamp Cohort 3)

A grounded AI assistant for course materials that takes evaluation seriously. The judge calibration journey is documented across four versions, showing what changed and why at each step. 60 eval scenarios cover multiple categories. Testing is split into unit tests (no API key needed) and judge tests (skip without key, CI stays green). Includes a self-evaluation section where the author scores their own project against the rubric.


Other projects to check: Chess Coach Agent (github.com/leo-cabibihan/chess-coach-agent), Meal Map (github.com/elgrassa/CapstoneMealMapSimplified), Datawarehouse Agent (github.com/larsvasseldonk/datawarehouse_agent), and AA Bot (github.com/marcelonieva7/AA_Bot). All scored 18-21 on the rubric and each has at least one section that stands out.


## Common patterns in weak READMEs

Three things showed up repeatedly in the lower-scoring projects.

First, some projects use marketing copy instead of evidence - bold claims with no methodology. The reviewer can't verify them and doesn't learn how the numbers were produced.

Second, some READMEs are clearly an afterthought. They start with metadata, list the tech stack, show quickstart commands, and stop. There's no problem section, evaluation, monitoring, architecture, or demo. The project may be solid, but the README gives a reviewer almost nothing.

Third, some projects have no demo or screenshots at all. The reviewer has to clone, install dependencies, configure API keys, and run the app just to see what it does. Most reviewers won't, and that's the most common reason projects lose points they could have kept.
