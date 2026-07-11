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

A good README covers a set of sections. You don't need all of them, and the order is flexible. Think of it as a checklist: the more boxes your project checks, the stronger your README.

Must-have sections:

- Title and one-line description - what the project is
- Problem - what's the problem it solves and who the user is
- Demo - screenshot, GIF, video, or sample output showing the project working
- Quickstart - exact commands to run the projects locally

Important for AI engineering projects:

- Deployment - where it's hosted, how to deploy it, what services it depends on
- Testing - how to run tests, what kind of tests are there
- Evaluation - what's in the eval set, the metrics, the results
- Monitoring - what you log and how to access it

Nice to have:

- Architecture - a diagram showing the data flow through your system
- Dataset description - what data you used, where it came from
- Project structure - key files and folders with one-line descriptions
- CI/CD setup - what runs on push, how tests and evals are automated

Other potentially relevant sections:

- Self-evaluation - for course projects: the score you'd give your project yourself
- Decisions and trade-offs - why you chose this approach over another
- Limitations - what doesn't work yet, what's out of scope, what you'd do differently
- Future work - what you'd build next if you had more time

Let's walk through the most important ones.


## Title and description

The first thing in your README is the title and a short description. You want to describe the user, the problem, and the solution right at the top.

Coming up with the right description can be hard. I usualy use AI to help me.

Give your coding agent the link to this article, and ask it to analyze the code to draft a description. Or you can copy your existing README into ChatGPT and ask it to come up with the description. If you don't have any README yet, you can also dictate the idea into ChatGPT and ask it to describe it clearly. 

Ask for multiple options, combine the parts you like, and iterate until you like the reuslts. 

You can use the same approach for other sections too. A coding agent can read your code and draft each section for your README.

For Fitness Assistant I use this opener: 

> A conversational AI that helps users choose exercises and find alternatives. It makes fitness more approachable for beginners who find gyms intimidating or can't always access a personal trainer.

In these two sentences it tells you about:

- the problem (fitness is hard for beginners)
- the user (beginners without a trainer)
- the solution (conversational AI for exercise selection)



## Problem

The description at the top gives a hint of the problem. The problem section goes deeper. Use this formula:

- One sentence: what's the user trying to do?
- One or two sentences: what gets in their way?
- One sentence: why don't existing tools solve this?
- One sentence: who is this project for, specifically?

<!-- illustration: screenshot of the Problem section from the Fitness Assistant README -->

For the Fitness Assistant, the problem section opens with the scenario:

- staying consistent with fitness is hard for beginners
- gyms are intimidating
- personal trainers aren't always affordable

Then it narrows to the user: beginners who want guidance but don't have access to a trainer.


## Demo

We described the problem, now we want to show that our project is the solution. The best way to do it is to have a demo. 

Recording a video is the best option for a demo, but it could be a screenshot, a GIF, or sample output.

Most people who read your README won't run it, especially the hiring managers. For them, a demo is proof the project runs and does something real. 

If your project is deployed, put the link at the top of the README too. A live URL is a great addition to the video, so people can try it directly.

To record a video, use Loom, OBS, or QuickTime. Start with showing your application in action. Limit this part to a few minutes, but you don't need to stop there. You can also include the other parts we talk about in this article: the evaluation results, the monitoring dashboard, the architecture.

If a video feels like too much effort, a screenshot of the app or sample input and output is enough.

For the Fitness Assistant, [I recorded a video](https://www.youtube.com/watch?v=RiQcSHzR8_E).


## Quickstart

Include these things:

- prerequisites (Python version, uv, Docker)
- the git clone command
- dependency installation
- environment setup
- the run command

Use actual commands in code blocks. If your setup is complicated, or there are different options to do it, firs show the short version, then the detailed steps.

<!-- illustration: screenshot of the Quickstart section from the Fitness Assistant README -->


## Testing

Explain how to run tests, with one command if possible. If you don't have tests, say so honestly.

For the Fitness Assistant: no automated tests, noted as a limitation. Honesty is better than hiding it.


## Evaluation

An AI project without evaluation is a demo, not a project. Show the numbers and include what's in the eval set: easy cases, messy cases, out-of-scope requests, refusal cases. State the metric you chose, what the baseline showed, and what improved after changes. Put the eval code in a separate location and document how to run it.

For the Fitness Assistant, the evaluation section shows both retrieval metrics (94% hit rate, 90% MRR after boosting) and RAG flow quality (83% RELEVANT with gpt-4o-mini). It includes the boosting parameters that produced the best results and links to the evaluation notebooks and data files. A reviewer can see the numbers, understand how they were produced, and check the code.


## Monitoring

Describe what you log, where the logs are stored, and how to access them. If you have a dashboard, include a screenshot. The point is to show that you treat the project as a running system, not a one-off script.

For the Fitness Assistant, conversations are logged to PostgreSQL and displayed in a Grafana dashboard. The README includes a dashboard screenshot and lists what each panel tracks, including last 5 conversations, user feedback, OpenAI cost, token usage, model used, and response time.

<!-- illustration: Grafana dashboard screenshot from the Fitness Assistant README -->

## Deployment

If your project is deployed, put the URL at the very top of the README, right after the title. A reviewer or hiring manager should see it before anything else. Don't bury it three sections down.

The deployment section itself covers the details: where it's hosted, how to deploy it yourself, and what services it depends on. Common options for AI projects include Streamlit Community Cloud, Render, Railway, or a Docker container on any cloud provider. Document the one you chose and the steps to reproduce it.

For the Fitness Assistant: there's no deployed version, but the README documents how to run it with Docker Compose and how to run it locally.


## Other sections

Nice-to-have sections:

- Architecture - a diagram (Mermaid, image, or text) showing where data enters, what the system does with it, and what comes out. A reviewer who reads only this section should understand the whole system at a glance. For the Fitness Assistant, this is a Mermaid flowchart with the Flask API, minsearch, OpenAI, PostgreSQL, and Grafana.
- Dataset description - what data you used, where it came from, how big it is, and any licensing restrictions. This matters if reviewers want to reproduce your results or check whether your eval set is meaningful. For the Fitness Assistant, the dataset is 207 exercises generated with ChatGPT, stored as a CSV.
- Project structure - a file tree with one-line descriptions for each file or folder. This saves a reviewer from hunting through your repo to find the evaluation code or the prompts. If your code is in notebooks, explain which notebook contains what.
- CI/CD setup - what runs automatically on push or pull request. At minimum, a GitHub Actions workflow that runs your tests. If you also run evals in CI, say so. This shows you treat the project as a system with automated checks, not a one-off script.

Other potentially relevant sections:

- Self-evaluation - if your project is peer-reviewed, go through the rubric yourself and state the score you think you earned for each criterion. This helps reviewers calibrate and shows you engaged with the criteria. Use AI for that too.
- Decisions and trade-offs - explain why you chose this model, this retrieval approach, or this framework, and what you rejected. The reasoning matters more than the tool name. A good format: "I chose X over Y because of constraint Z. The downside was A. I accepted it because B."
- Limitations - what doesn't work yet, what's out of scope, and what you'd do differently. Being honest about limitations doesn't make the project look weak. It shows you understand the boundaries of what you built.
- Future work - what you'd build next if you had more time. Keep it realistic - this is about showing direction, not making promises.

## Things to avoid

I see the same problems in almost every cohort:

- Missing setup instructions. If I can't run it from a clean clone, the project loses reproducibility points.
- No evaluation. An AI project without eval is a demo.
- No demo. If I have to run your code to see what it does, most people won't.
- Giant notebooks with no link from the README.
- Stale READMEs where the deployed version doesn't match what's written.
- A wall of text with no demo, no screenshots, no eval numbers, and no clear explanation of what the project does.
- A README that describes what the project will do (future tense) rather than what it does. If it says "this project will implement monitoring," the reviewer assumes monitoring isn't done.
- Marketing copy instead of evidence. Bold claims with no methodology. The reviewer can't verify them and doesn't learn how the numbers were produced.
- READMEs that are clearly an afterthought. They start with metadata, list the tech stack, show quickstart commands, and stop. There's no problem section, evaluation, monitoring, architecture, or demo.


## Using AI to write your README

I mentioned earlier that a coding agent can help draft individual sections. The same approach works for the whole README. But a few things to keep in mind.

You don't have to tick all the boxes. If there's nothing to say about CI/CD or limitations or future work, don't force it. The README should feel natural, not like a form filled in by checking every field. Don't just give the agent this article and ask it to cover everything. Pick the sections that make sense for your project.

You can also reorder things. Maybe architecture should be at the top for your project, or maybe the evaluation results deserve more space. Ask your AI assistant which order makes sense for your particular project. At the end, the structure is a suggestion, and taste matters.

## Examples from student projects

## AI Diet Coach

Repo: [github.com/thetsuwin66/ai-diet-coach-agent](https://github.com/thetsuwin66/ai-diet-coach-agent) ([course page](https://courses.datatalks.club/ai-buildcamp-3/projects))

A clear first screen - a reviewer can understand the project in 30 seconds without running anything. There's a live deployed demo link right after the problem statement, with screenshots of the chat interface, meal plan, progress tracking, and monitoring dashboard.

The problem section names a specific demographic: "users in Southeast Asia who follow Asian diets, a demographic underserved by Western-centric diet tools." The README includes a Mermaid architecture diagram showing every component. The monitoring section has screenshots of both a custom dashboard and Logfire tracing.


## Research Radar

Repo: [github.com/55382/Research_Radar_agent_phd_assistant](https://github.com/55382/Research_Radar_agent_phd_assistant) ([course page](https://courses.datatalks.club/ai-buildcamp-3/projects))

The one-liner tells you the input (ArXiv papers), the output (a personalized digest email), and the user (researchers in fast-moving fields). It even captures the feedback loop, all in one sentence. It interprets every metric in plain language and shows a parameter tuning table that demonstrates evaluation was used to make decisions. It covers deployment, CI, and 67 tests.


## CineRAG

Repo: [github.com/bielacki/cinerag](https://github.com/bielacki/cinerag) ([course page](https://courses.datatalks.club/llm-zoomcamp-2025/projects))

Two separate eval sections. One for retrieval (five approaches compared with hit rate and MRR numbers). One for LLM answer quality (LLM-as-a-judge with relevance and faithfulness metrics). Each section explains the eval dataset, the metrics chosen, and how to run the eval, with results in tables. A reviewer can see exactly how the project was evaluated without digging into notebooks.


## Applied ML Teaching Copilot

Repo: [github.com/marcoteran/applied-ml-teaching-copilot](https://github.com/marcoteran/applied-ml-teaching-copilot) ([course page](https://courses.datatalks.club/ai-buildcamp-3/projects))

The judge calibration journey is documented across four versions, showing what changed and why at each step. 60 eval scenarios cover multiple categories. Testing is split into unit tests (no API key needed) and judge tests (skip without key, CI stays green). Includes a self-evaluation section where the author scores their own project against the rubric.


Other projects to check: [Chess Coach Agent](https://github.com/leo-cabibihan/chess-coach-agent), [Meal Map](https://github.com/elgrassa/CapstoneMealMapSimplified), [Datawarehouse Agent](https://github.com/larsvasseldonk/datawarehouse_agent), and [AA Bot](https://github.com/marcelonieva7/AA_Bot). You can find more projects on the [Buildcamp Cohort 3](https://courses.datatalks.club/ai-buildcamp-3/projects) and [LLM Zoomcamp 2025](https://courses.datatalks.club/llm-zoomcamp-2025/projects) project pages.



