---
title: "Defining the Role of AI Engineer: Webinar Q&A"
created: 2026-02-24
updated: 2026-02-25
tags: [ai-engineering, career, webinar, q-and-a]
status: draft
---

# Defining the Role of AI Engineer: Webinar Q&A

After the "Defining the Role of AI Engineer" webinar, there were many questions from the audience. I answered all of them here[^1].

The [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) repository contains all the data and analysis referenced in this article[^4]. The first session recording and summary is available at the [AI Shipping Labs blog](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective)[^48].

## Programming Languages in AI Engineering

Question from Kevin J: Do you have any analysis on demand for particular programming languages for AI engineering roles?[^2]

Yes, the data is in the [AI Engineering Field Guide repository](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)[^4]. From the analysis of 895 job descriptions[^4]:

- Python - 738 jobs (82.5%)
- TypeScript - 209 jobs (23.4%)
- Java - 133 jobs (14.9%)
- Go - 101 jobs (11.3%)
- SQL - 88 jobs (9.8%)

Python is the dominant language. TypeScript is in second place, which aligns with what we see in the field. Java and Go also appear frequently[^3].

## Example AI Engineer Job Role Breakdown

Question from Sandipan: Can you give an example job role and breakdown of the expectations and the skills used?[^2]

The [job market data](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/job-market) in the repository contains both raw and structured job descriptions[^6]. You can look at a few AI engineer vacancies there to see what the expectations look like[^5].

TODO: Take several AI engineer job postings from the repository and do a detailed breakdown analysis.

## PhD in ML to AI Engineering

Question from Azzeddine Rachid: How to move from a PhD in ML research to AI engineering?[^2]

For a researcher, the core AI skills are easy. Sending requests to OpenAI, doing prompt tuning, running experiments with different prompts - all of that is straightforward for someone with a research background[^8].

The hard part for researchers is the engineering side: tests, monitoring, evaluation. These are the areas that need the most attention[^8].

For core AI engineering skills beyond basic API calls[^8]:
- Testing your agents - approaching it the same way you test regular code with pytest and similar tools
- Monitoring - setting up proper monitoring for your AI applications
- Evaluation - this should actually be easier for researchers since they already think in terms of metrics

For infrastructure skills beyond core AI[^8]:
- Docker - important to learn
- CI/CD - important to learn
- Cloud basics - knowing how to deploy something simple
- Kubernetes - can skip this, not essential

There are tools like Claude Code that make all of this much easier. You take an AI assistant and say "I want to set up CI/CD" and it walks you through it step by step. You just try to understand each step and why it works that way. It is not rocket science. If you use GitHub, setting this up is very easy - the assistant does everything, you just try to understand the steps[^8].

The key approach: use AI assistants, but try to thoroughly understand what they recommend rather than just blindly executing "make me CI/CD and forget about it."[^8]

## AI Application Security Roles

Question from Luca: Have AI Application Security roles been relevant in your research?[^2]

I did not encounter separate AI application security roles in the data, so I did not do specific research on this[^9]. But it would be interesting to investigate. All the scraping scripts are in the repository. If someone wants to repeat the analysis specifically for security roles, it would not be too hard using an AI assistant to figure out the order of running the scripts. I would be interested to see the results if someone does this[^9].

## Data Engineers Moving to AI Engineering

Question from Amine B: If we're a data engineer that started working on AI, which skills should we focus on for AI Engineering (other than the obvious RAG / prompt engineering skills)?[^2]

For data engineers, the core AI engineering skills are exactly what you should focus on beyond RAG. These include things like testing, monitoring, and evaluation[^10]. But for data engineers, the transition is relatively fast - maybe 3-4 months and you are ready. You do not need to spend a lot of time on it because you already have the engineering skills[^10].

When job searching, the focus can be on this: "I am a data engineer, I know engineering, I can build data pipelines, and because I am a great data engineer, I have an advantage over other AI engineers who do not have this skill."[^10]

By core AI engineering skills (beyond RAG and prompt engineering) I mean: having tests that test your agent, having monitoring, having evaluation, writing clean code where tools for the agent are in a separate folder, and being able to work with agents so they do what you need - not just RAG and prompt engineering[^11].

## Are Data Scientist Jobs Safe?

Question from Vasileios Palaskas: Are jobs of data scientists safe after the arrival of the "era" of AI engineer role?[^2]

Historically, to productionize a model, for every 1-2 data scientists you needed several engineers. Often, for simple tasks, an ML engineer could handle them just fine and data scientists were not even needed. With the arrival of AI, this became even easier - any engineer who can run code can train an XGBoost model[^12].

What makes data scientists valuable? ML and product management skills. They are also very good with experiments and evaluation. ML engineers may not be as strong in designing experiments. So if data scientists want to move into AI engineering, they should focus on the engineering side and showcase their strong evaluation and metrics skills[^12].

For example, search is very important and data scientists typically know how to evaluate ranking models. Engineers may know less about this. That is the kind of edge data scientists have[^12].

TODO: Find the LinkedIn post about why data scientists are having a harder time in the AI era. I already answered this question before and made a good post about it[^13].

Note: The transcription sometimes renders "AI engineer" as "European engineer" - this is a transcription error[^14].

## TDD and Testing in Job Descriptions

Question from Debabrata Mishra: We have not seen the keyword "TDD" in the data. Does Pytest and others get captured under Evaluation?[^2]

I honestly do not remember seeing TDD explicitly mentioned in job descriptions. But I think it is an important practice. It might fall under the evaluation cluster, because sometimes when we do evaluation, we can split our dataset into parts - one part with things that must pass (like "the answer must be relevant" or "tool calls must be used in this dataset"). This is essentially a test that just looks and is configured a bit differently. Some companies do it exactly this way[^15].

The reason TDD might not appear explicitly: look at ML engineer or software engineer job descriptions - do they often mention tests? Not really. But all ML engineers and software engineers write tests. It is simply assumed as a best engineering practice. It is just not written directly but implied[^16].

I consider it very useful when you approach testing your agent the same way you approach testing your code - using pytest and similar tools[^15].

TODO: Run analysis to check how often TDD and testing appear in AI engineer job descriptions. It might fall under the evaluation cluster, which is why it does not appear directly[^15].

## Software Engineering Experience vs End-to-End AI Projects

Question: Instead of simple Software Engineer experience, should we also add an end-to-end AI or ML project (finetune LLM) as a better approach?[^2]

I am not entirely sure what "simple Software Engineer experience" means here. But having an end-to-end AI project is always useful. Fine-tuning LLMs - as I said during the talk, this is not really a core skill, it is more of a niche skill. Adding it is useful if you are interested, but if we are talking about what is generally more valuable based on the data, regular software engineering skills are more useful than niche LLM skills[^17].

## GitHub Projects and Recruiters

This section addresses multiple questions from eunjoa c about GitHub projects, recruiters, and portfolio quality[^2].

### Do Recruiters Check Your GitHub?

Recruiters themselves most likely do not check and will not look at it. They do not have the expertise for that. Who will actually look is the hiring manager - the team manager[^18].

When I was hiring people, I did not have time to look in detail. Maybe 5-10 minutes before the interview I would open the resume, look at the GitHub link, open it, and see what is there in general. I would not have time to read details. A project would have to really interest me for me to want to look at the code[^18].

That is why I invest a lot of attention in the README - it is the most important part of the project. I look at the README to see what is described there, and that is usually it. I limit myself to that because I do not have time to read more[^18].

Organization plays a very important role. If I do want to look deeper, I need to understand where to find things. Links to code, to important implementations right in the README can be very helpful. For example, when I look at a project, I might want to see the prompts - how exactly they are structured - or look at the tools the agent has. If the README links directly to these things, it helps me quickly find what I need[^18].

As a hiring manager, if I can see this information right in front of me, it is very useful because I only have maybe a couple of minutes to look at the project before the interview. Sometimes during the interview itself the candidate mentions a project, and I ask if it is on GitHub. If they say yes, I go there and look in real time during the interview. I will not read in detail - I just quickly look at whether it looks decent or not[^18].

### What Do Hiring Managers Focus On?

Recruiters will most likely not look at anything - they will just check whether some project exists or not. They will not read anything[^19].

As a hiring manager, what I want to see[^19]:
1. The project solves a real problem - what it does, why it exists
2. A clear description so I can open the README and immediately understand what is going on
3. Signs that the project is close to production: tests, evaluation, CI/CD, deployment

The more of these checkboxes I see, the better. Tests add a plus, CI/CD adds a plus, good code adds a plus, images, demos, videos add a plus. The more pluses, the better[^19].

Does this mean every personal project must have evaluation or tests? Of course not. Pet projects are pet projects. But if a project solves a real problem and has multiple iterations invested in it, I will be interested in discussing it even without tests[^19].

The project I use as an example is Children's Scary Stories - making scary stories from pictures. The code is not great, there are no tests, no evaluation, but the project itself is interesting and I gave several talks about it at different conferences. Technically nothing complex, but there is something to talk about[^19].

That said, I would not use this project as-is for my portfolio right now. I would definitely clean it up first[^20].

### README Quality

This is probably the most important part of your project. The most important file is the README[^24].

You need to make sure the file is not too big and not too small, that it has all the important information but not too much. Writing a README now is not hard - you open Claude Code or any other assistant and say "generate a README for me." But in that case, first, it will be obvious that it was generated, and second, there will be useful information mixed with a lot of not-very-useful information[^24].

In many of our courses, I tell students how to write a good README. I also cover this in the [AI Engineering course on Maven](https://maven.com/alexey-grigorev/from-rag-to-agents)[^24].

For me the most important thing: the README should describe the project clearly, the project should solve a specific problem (not just "I did this because it was interesting" but "this solves a specific problem"), and there should be a reasonable description so I can open the project and immediately understand what is happening[^22]. Everything else adds bonus points: having tests described, having CI/CD, having good code, having images, demos, videos[^22].

When I see all these checkboxes checked, I see that a person really put effort into this project and it is not embarrassing to show. I have my own projects - some I am not embarrassed to show, some I would not show without cleaning up first[^22].

TODO: Add link to course README guidelines and outline of what should go in a README[^24].

### Two Audiences for Your README

For projects done in our courses, and also on my Maven course, all projects go through peer review. Three other students review each project. I tell people: write your README for two different audiences[^23]:

1. The first audience is the other student who will review your project. They have time to check everything, and you need to show that all evaluation criteria are satisfied. This motivates you to write good code, clearly and without cutting corners[^23].

2. The second audience is a hiring manager. They have almost no time at all, and you need to convey the maximum amount of information in the shortest time[^23].

If the parallel with other students does not appeal, you can imagine that this is your take-home assignment and the hiring manager will read it. Try to guess what their internal checklist looks like and try to check all the boxes[^21].

And you do this first and foremost for yourself, not so that someone will look. The chances that someone will really read your code in detail are not that high. So first you do it for yourself, and second, to impress someone[^25].

### How Deeply Do Interviewers Inspect Code?

If we are talking about a hiring manager - there is no time to check in detail. I open it, look for 1-2 minutes, and that is probably it. In rare cases I might look at the prompts, maybe look at the tools, check if tests exist at all. I will not read the tests - I just open them, look if they are there. Whether they are big or small - for me it is more important that they simply exist rather than anything else[^21].

But for take-home assignments, of course people will read more carefully. Some hiring managers actually run the code and really look at it. Some do not - they just read the code. It varies by person. For take-home assignments, it is better to follow engineering best practices: write tests, have code coverage ideally[^21].

### Commit History and Contribution Consistency

I have never in my life looked at commit history. And I do not think anyone will look at this. I do not know who this could be interesting to. I see no point in spending time on this. When I look at a project, I look at the project in its current state. I do not know why anyone would need to look at the history[^26].

### Other Documentation

Other documentation can also be important, but there are really two situations - for yourself, and everything else is as circumstances dictate[^27].

I try to document a lot of things. For example, if I am working on a feature and had to make a decision and did a benchmark, I often have the agent document the decision so that next time when I or the agent continues working on this task, there is enough context. The simplest way is to ask during the active session to document all decisions that were made. This can be GitHub issues, pull requests, or files - anything to keep decisions documented somewhere[^27].

But this is not always important. For some projects it matters, for some it does not. README is important. Other things depend on circumstances[^27].

### End-to-End Projects vs Experimental Notebooks

I think the answer here is obvious. No additional comments needed[^28].

### Tutorial-Based vs Original Projects

If someone tells me in an interview "this was a course, I just copied from there" - I immediately lose interest. If someone tells me they had an idea or a problem and they solved it using some tool, or they were interested in this area and wanted to learn more and that is why they came up with this project - that is a huge plus for me[^29].

If someone just took a video and repeated what was in the video, the value is not zero but not super high either. During a conversation this can come up[^29].

There are important distinctions[^29]:
- If it is a course with step-by-step instructions that you just repeat - everyone will have the same project with the same code. Not much value in that
- If it is a course homework where the task is given but the implementation is yours - that is much more valuable. For example, in the AI Engineering Buildcamp, students need to do their own implementation
- If it is an original project that you came up with and built from scratch - that has enormous value. Both for you personally and for me as a hiring manager, because it is much more interesting to discuss

The level of commitment is very different and it shows. When you were really involved in the task, you will have answers to my questions because you lived through it, not just copied it[^29].

### Project Complexity vs Clarity

I think the answer here is also obvious[^30].

### Production-Level Practices in Personal Projects

Companies do not expect production-level engineering practices in personal projects. And that would be over-engineering - it would look forced. It is very hard to have real production-level problems in personal projects. So it would be an overly complicated project that is hard to understand at first glance[^30].

Clarity is more important - everything should be clean and understandable, solving your problem. But do not forget about basic best practices that are important in any project. We are not talking about thousands of requests per second - just a normal project that solves your specific task. Nothing more is needed[^30].

If you have a personal project that genuinely requires production-level infrastructure, you probably do not need a job - you already have one[^30].

### Tests and CI/CD Pipelines

Tests and CI/CD are pretty easy to implement, especially with AI assistants. I do not see a reason not to do it. You need to write tests regardless. And once you have tests, asking Claude to wrap them in GitHub Actions is a 5-minute thing[^31].

Of course, you should understand what is happening. If you do not know this yet, I recommend spending an evening to figure it out. If you already understand what tests are, it is easy. If you do not understand what testing is at all, one evening will not be enough - you need to invest several weeks depending on your background[^31].

Start with regular unit tests, then integration tests, then end-to-end tests, then LLM-as-judge evaluations[^31].

TODO: Elaborate on these test types based on the existing article about testing agents with the judge pattern.

We are also launching a new paid community where I plan to make a course specifically about testing. You can join [AI Shipping Labs](https://aishippinglabs.com) - the premium plan includes courses where I plan to teach all of this. Everyone who joins now has the opportunity to influence what content gets created[^31].

## Using Claude Code in Your Portfolio

Question: Would mentioning Claude Code usage be a positive on a portfolio/resume or negative?[^2]

For me this is neutral. If you do not use Claude Code or some assistant, you are missing out. But I do not see a reason to specifically mention it[^32].

If you want to be open about it, you can say at the end that the project was built using AI-assisted development and you can indicate your contribution. As someone who uses these assistants extensively, I understand the value they bring and also understand that it is not as simple as just giving commands - you need to understand what you are doing[^32].

If you discuss this with the hiring manager, the conversation might go into how exactly you used the assistant, how you gave instructions, how you made sure the agent did not make mistakes. If your answer is "I gave a prompt and everything worked from the first try" - I will have questions. Because it never works from the first try. If you had many iterations with it, that is very valuable and I consider it a very useful skill[^32].

Whether to write about it or not is your call. I see nothing wrong with writing it. I see nothing wrong with not writing it[^32].

Also: if the code in the project is 100% written by the assistant and you fully understand it - great. But if there is an expectation that you deeply understand the code, and something goes wrong in production, and you suddenly do not have access to the agent - can you fix the problem without the agent? If yes, perfect. If not, it is not the end of the world, but you should understand how involved you are in the project[^33].

For personal projects, not understanding 50% of the code is fine - I have many such projects myself. For critical production projects, you should have a deeper level of understanding[^33].

## AI Developer vs AI Engineer

Question from Guzel Bayazitova: Is AI Developer role similar to the role of AI Engineer?[^2]

For me this is all semantics, honestly. I cannot say there is some huge difference. There is supposedly an industry opinion that a developer is a level below in the sense that a developer is more of an executor while an engineer thinks more holistically. I think this is all semantics[^34].

A good executor, a good engineer - whatever you call them, developer or anything else - if they have a task, they will do it well and will think not just about their specific part but more globally[^34].

I know there are places that make distinctions. For example, in outsourcing, there was "Java Developer" and "Software Engineer" with different scopes - the developer just gets a Jira ticket and implements it without looking elsewhere. I know this exists but I cannot imagine people being against expanding your scope and ownership. From my experience mostly in product companies, I have always encountered engineers rather than developers in this narrow sense[^34].

I would be curious to talk to someone who is called an AI Developer and ask how their role differs from AI Engineer and whether they want to become an AI Engineer[^34].

## AI Engineer vs Software Engineer Using AI

Question from Le Phu: What are the differences between AI Engineer and Software Engineer using AI in their application?[^2]

The line is pretty thin. Most likely, from software engineers the expectation is more of a generalist - a person who can do everything. While AI engineer is probably a more focused role. But in practice, like duck typing in Python - if the methods are the same, there is essentially no difference regardless of what you call it[^35].

## Job Description Quality and Filtering

Question from Migz: Were you able to distinguish between JDs which actually know what they want vs JDs made by recruiters just throwing buzzwords?[^2]

No, I did not have this filter when scraping data. The number of such low-quality job descriptions is likely not zero. I know there are job postings that exist just for show - to signal to investors that the company is actively hiring. In reality they are not hiring anyone[^36].

If a recruiter was just told "post an AI engineer job" without anyone specifying what exactly is needed, then of course someone might just ask ChatGPT to create a job description and publish it. I did not do any filtering for this. I hope that if I see such a description I can tell something is off, but I would need to test that[^36].

## ML Understanding and Reasoning Skills

Question from Debabrata Mishra: Am I right to say that good conceptual understanding of ML/neural modeling with reasoning skills stands first, as a wrong model shipped would negate effort?[^2]

Understanding ML and neural networks is useful for AI engineers. As we saw in the data, about 64% of AI engineering roles require some ML knowledge. But if we look purely at AI engineering core skills, the ML component is not always required[^37].

However, it often happens that at large volumes, LLMs become expensive. You need to be able to do what the LLM does but faster and cheaper. Typically this means: take the LLM, use it to label data, and train a classical model on that data that works faster and cheaper. I remember at a company I worked at, we used LLMs for data labeling and it worked quite well at scale - the savings were real[^37].

Such use cases exist especially at scale. In those cases ML skills are needed. But I would say this is more about ML engineers who know AI rather than AI engineers who know ML - though the question is, what is the difference between them? Maybe there is none[^37].

## Market Pushing AI Adoption

Question from Pavan: Is the market pushing enterprise companies to adapt to AI by dumping stocks, despite many not having figured out AI integration yet?[^2]

Yes, this happens. There are stories where management sends down the order: "we need to show investors that we use AI, so everyone start doing AI immediately."[^38]

What to do with this? If you are an executor - say a data scientist - and you are suddenly told to do AI but there is no real problem that AI solves: on one hand, this could be a good opportunity to learn something new. AI might actually be useful somewhere. On the other hand, you can say "I think we have many other unsolved problems to focus on."[^38]

It all depends on the specific situation. If you work at a company and you are a regular employee and it is not a startup where time is critical, you can just enjoy learning new things. Even if this AI solution does not end up solving user problems, you still learn something new[^38].

On one hand this is practical human advice, on the other hand we want to build products that bring real value to users. So everyone decides for themselves[^38].

## ML Jobs Becoming GenAI/LLM

Question from eunjoa c: 99% of job postings with ML engineer job title in Canada/US are related to GenAI/LLMs. It seems the traditional ML jobs are no more, one must do the shift.[^2]

It would be interesting to verify this claim. I might try to run the same analysis process but for ML engineers. Take New York as a representative city that sets trends and see what is there. If we see this trend in New York, we can assume we will see it in other cities too[^39].

Whether I will have time to do this, I will see. I just need to give Claude Code the command to run it. If I do not forget, I will do it soon. It would make an interesting article[^39].

I am not making any promises right now, but subscribe to my [Substack](https://alexeyondata.substack.com/) - if I do this analysis, I will definitely write about it there. I have a lot of things in my backlog that I want to work on, plus I have a course, so it is hard to find time for new things. But if it does not require too much effort from me, I will do it soon[^40].

## Front-End Skills for Data Engineers and AI Engineers

Question from Renz: I checked the guided path for Data Engineer. Do I need to learn how to integrate it in front-end like more of like a full-stack than just Jupyter Notebooks?[^2]

For front-end specifically, I do not know. We can look at the numbers for full-stack requirements[^41].

From the data: 31.4% of AI-First roles mention frontend skills, 49.6% mention backend skills, and 21.6% mention full-stack (both). So it is more backend-focused[^41].

In general, we understand that AI engineer is a full-stack role - the data confirms this and many guests on the DataTalks.Club podcast have confirmed it too. But the expectation is not that an AI engineer will proactively push things to the front-end. If you work at a startup and this task falls on you and you do not mind, and you have Claude Code which will handle it - why not?[^41]

Each role has its specialization. Data engineers should work on pipelines, front-end developers on front-end. But if the need arises, it is fine[^41].

I personally cannot say that front-end is a must-have skill for a data engineer. But I will add that back when I was a data scientist (around 2018), I decided to learn React. I spent time doing tutorials and building things. This helped me enormously because none of the other data scientists around me knew React. Before Streamlit existed, I could build a quick interface to show management what I was working on - show it to product managers, to technical people who are not data scientists. This was extremely helpful at hackathons too[^41].

Now this is less relevant because Streamlit exists and AI assistants can write front-end code for you. But knowing how to ask an agent to write front-end code for you is still quite useful[^41].

About the Jupyter Notebooks part: everything that happens outside Jupyter Notebooks is useful. I have big questions about a data engineer who only works in Jupyter Notebooks - because that is clearly not the core responsibility of a data engineer. Even data scientists spend time outside notebooks. If a data engineer only does things in notebooks, I have serious questions about what they are doing[^41].

## Top 3 Projects for FAANG Interviews

Question: What are top 3 projects we can do to crack FAANG interviews?[^2]

I am afraid I cannot help much with this. I even have a story about an interview I failed at Facebook - I was asked to design an ML system, I thought I designed it well, but the interviewer wanted me to talk about neural networks, which I thought was strange[^42].

I would check Twitter and Reddit for what people write about FAANG preparation, but I would focus not on FAANG specifically but on what interests you. That is the most important thing - that you enjoy the process, not just the goal of getting into FAANG[^42].

For FAANG specifically: they care more about LeetCode and system design than about projects. LeetCode you just have to grind, and system design you have to study. Pet projects do not help with either of these[^42].

There is also ML system design and now AI system design. Big companies ask about system design for senior roles and above. The difference between regular system design and ML system design may already be shrinking, and AI system design could be similar. But these are my speculations[^42].

## Local Hardware for Running Models

Question from Pavlo: Some people mention using MLX / Mac hardware for big models - is it just to check some large models or are there justified cases?[^2]

There are justified cases. In some companies, data is very sensitive and must not go to any cloud. Germany especially has people and companies for whom this is very important. If you want to work with financial or medical data, you need to be maximally careful - have your data center in Germany, better yet your own machine[^43].

Some startups keep their own GPUs to host their own models. This is for compliance reasons and to ensure your data does not leak. For Germans it is important that data does not end up in the hands of "evil capitalists."[^43]

Some people run models like Qwen locally on Mac just to avoid paying Anthropic. But in reality they buy a device for $2,000 instead of paying $100/month to Anthropic. Personally I would rather pay $100/month than have the ownership cost. But everyone looks at this differently[^43].

About the future of local LLMs: right now models from Anthropic and others are heavily subsidized through subscriptions - you pay much less than the actual cost. This cannot last forever[^44].

On the other hand, local models are gradually catching up with cloud models. You can already run something like Qwen3 on a MacBook and it will work reasonably well - not comparable to the latest Opus, but quite usable[^44].

My hope is that by the time Anthropic says "we can no longer offer $100-200 plans with lots of tokens, now it costs $2,000," local models will be comparable in quality. Then you just run your Qwen locally and keep coding[^44].

## EU-Remote Work Percentage

Question from Pavlo: What percentage of roles support EU-remote work, or are they primarily onsite in IT hub cities?[^2]

This can be checked in the data. I could do this analysis, but it would also be great if someone from the community dug into the data and answered this question themselves. You can repeat what I did or use the existing data to try to answer this question yourself[^45].

## Identifying First/Only AI Role from Job Description

Question from Pavlo: How to identify from a job description if it's not the first and only AI role, and what percentage of such roles are there from your perspective?[^2]

This is hard. You need to talk to people and ask. From a job description alone, it is hard to tell. But sometimes you can see it when the requirements are too broad - when it looks like a job description for a data engineer, AI engineer, and ML engineer all in one. That is likely a first hire[^46].

But my question is: why is this bad? Sometimes when you join a startup as the first person, you can learn a lot. Depending on your goals and opportunities, this might not be the worst thing. Especially with all the AI tools and assistants I keep mentioning - they can help you handle a broader scope[^46].

You can discuss this with people during interviews. Ask them what they think, what their expectations are. It is not always bad[^46].

## Entry-Level AI Engineer Positions

Question from Devesh Mehra: How about entry-level positions for an AI engineer?[^2]

You can figure out the answer to this question yourself by analyzing the data. I have given you the data and the direction. You can collect the data, analyze it, draw conclusions, and based on those conclusions create a concrete learning plan and start learning[^47].

And you can write about this - every day share what you learn, do learning in public, building in public. You will grow your network, people will notice you. This way you will not only find the answer to this question but also potentially find a job and many like-minded people[^47].

## GitHub Repository and Resources

Question from Benjamin Daniel: Is there a GitHub repo or resource available to go through this session in detail?[^2]

Yes: [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide)[^48]. The first session is also available: [What is an AI Engineer - Alexey Grigorev's Perspective](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective)[^48].

## Data Engineering Zoomcamp with AI Stack

Question from Leonid Charey: Do you have a plan to make a DE Zoomcamp based on the AI stack?[^2]

We have LLM Zoomcamp. Beyond that, there are no plans to add new free Zoomcamps on this topic. We already have enough free Zoomcamps to cover the whole year: Data Engineering, then LLM, then ML Zoomcamp, AI DevTools. That fills the entire year[^49].

About MLOps Zoomcamp - most likely we will not launch it this year. I definitely will not be doing it myself, but maybe we can find volunteers. I am also looking for sponsors for LLM Zoomcamp[^49].

There will be new paid courses as part of [AI Shipping Labs](https://aishippinglabs.com) - a new community I am building. There will probably also be a new course on Maven. For now, you can join AI Shipping Labs and help shape what content gets created - people who join now have the opportunity to influence the community content[^49].

## Frontend/Full-Stack Skills for AI Engineers

Question from Andrei A: Is it required to have frontend/fullstack skills for an AI Engineer?[^2]

Same as what I said before about front-end. There are no expectations that you will write front-end code. But if you want to and if the front-end team is busy with other tasks and you have a feature to ship, you can use Claude Code to figure it out. Of course you would not just commit to production directly - you would make a pull request and ask a front-end developer to review it[^50].

I cannot say these are core skills. We saw that the focus is more on backend - Docker, Kubernetes, etc. Front-end appears rarely. But it does not mean it is useless[^50].

There is an interview with Paul where he says that in a startup he does absolutely everything, even though his title is AI Engineer: [DataTalks.Club Podcast - AI Engineering Skill Stack, Agents, LLMOps, and How to Ship AI Products](https://datatalks.club/podcast/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products.html)[^51].

## AI Engineer Interview Stages

Question from Geet Vilas Jamdal: What are the typical stages of an AI engineer interview after resume screening, and how important is DSA in the overall hiring process?[^2]

There will be two events about this soon[^52]:
- [AI Engineering: The Interview Process](https://maven.com/p/69550a/ai-engineering-the-interview-process)[^53]
- [AI Engineering: Take-Home Assignments](https://maven.com/p/250595/ai-engineering-take-home-assignments)[^53]

## Learning Without LangChain Frameworks

Question: From what you've explained, it seems that one needs to know a bit of AI automation. Is that necessary? Can I learn without those LangChain frameworks?[^2]

There seem to be two parts to this question. First, about AI automation - I consider it super useful regardless of whether you are an AI engineer or just writing code. It is very useful. Browser automation (I am still not fully familiar with it myself) is also reportedly super useful[^54].

Second, about LangChain - yes, you can absolutely learn without LangChain. I even recommend not starting with LangChain. Start with the basics: tool calling, the tool calling loop. And only then start using a framework[^54].

I think this is better because you understand what happens inside, and even if you need to use LangChain, you roughly understand how it is structured. On my course I use Pydantic AI and I did not see it mentioned in job descriptions. I think this is because people who use Pydantic AI do not put it in job descriptions - anyone who needs to can figure it out in a day[^54].

LangChain is not a bad framework, though I would not use it in my own projects. I cover it on the course too. But you can definitely learn without it. If you really want, do one project with it so you understand what it is, but essentially it is all roughly the same as other frameworks[^54].

## Fine-Tuning for Healthcare

Question from Usung Uduak: I'm in the medical team, so will I need to learn fine-tuning for healthcare companies?[^2]

It all depends on the use case. You might not need fine-tuning at all. Fine-tuning is often used when a model works OK for general purposes but not great for a specific task. But you need to host the model yourself because you cannot use general-purpose models[^55].

There is a movement called small language models (as opposed to LLMs). It is exclusively fine-tuning: take a small model, distill it to the minimum, fine-tune it for your specific task, and it handles that task very well - cheaply and quickly. I have not investigated this much yet. I know a startup here in Berlin that does this, and they are doing well - they went from just starting out to sponsoring conferences, so they have money and clients[^55].

The point about money is: if they have money, they have clients, which means the thing is in demand. But again, based on what I see, this is a niche thing[^56].

Based on the data I collected, I would not focus on fine-tuning right now. There are many other things to learn first. Unless you know a specific company and position needs it - then go for it. If you are choosing what to focus on, focus on other things first. But if you are excited about it and want to learn, of course go ahead[^56].

## Comparing AI Roles: LLMOps, AI Platform Engineer, AI Production Engineer

Question from Naresh T: Can you please compare AI Engineer, MLOps Engineer, AI Production Engineer, AI Platform Engineer, and LLMOps?[^2]

LLMOps is like DevOps - DevOps is not really a person, it is a set of practices about how you write code, how you have CI/CD, how you organize your process. MLOps is the same thing - a set of practices about how to deploy models to production. But there is a role called MLOps Engineer - usually they are the people who organize the platform so that ML engineers can deploy models[^57].

LLMOps and AI Platform Engineer could be the people who do the same but for LLMs. This might include deploying your own models (or not), but overall it is about organizing the process. Setting up monitoring, making it so that when you press a button, your agent deploys and monitoring automatically connects, you can collect logs and do evaluation based on those logs - I would call that an AI platform[^57].

As for AI Production Engineer - I can only guess what that means[^57].

All of this is not based on data, these are my speculations. MLOps is a more established role that I can speak about confidently. For the rest, I am extrapolating from MLOps. You need to talk to people who actually have these titles and ask them. I do not know many such people personally[^57].

## Will AI Engineer Replace Traditional MLE?

Question from Andrei A: Will the AI Engineer role replace a traditional MLE role?[^2]

I do not think so completely. The overlap is large and right now there is more hype around AI engineering. But I think this is temporary. Things will calm down and there will be more understanding of when to use AI and when not. In many cases you do not need AI, and in some cases it is actually harmful[^58].

GenAI is here to stay. But through the hype cycle, traditional ML is still needed and important. There are use cases you can optimize with ML later, guardrails made with ML (not GenAI) because they need to be fast[^58].

ML is not going anywhere. What happens with AI engineering we will all see in five years. But I think there is a lot of hype right now. Some companies push AI just to please investors. In a year or two this will calm down and there will be more clarity on when to use AI and how. Then we can talk more precisely about roles[^58].

Right now it is like data science 10 years ago - everyone wanted to do it but nobody understood what it was. Now there is understanding. The same will happen with AI engineering[^58].

## Is SaaS Dead?

Question from Taylor: Is SaaS dead?[^2]

Of course not. I can vibe-code something quickly. But many services I use and pay for - it would be more expensive for me to host them than to pay. For example, I keep paying for Zapier even though I could theoretically build my own thing, but I do not want to implement and host all the things Zapier gives me[^59].

Some things are becoming more commoditized - if I have a very specific use case and cannot find anything ready-made, I can now build it faster. Like with the new community platform for AI Shipping Labs - we could not find anything that 100% satisfies our requirements, so we decided to build it ourselves. In that sense, yes - some SaaS platforms I previously used despite them not perfectly fitting my needs now face competition from custom solutions[^59].

But SaaS is definitely not dead. Stripe, for example, is not going anywhere. Many services provide value that is hard to replicate. You can now vibe-code alternatives for some things, but not for everything[^59].

## Previous Session Access

Question from AkhilTej: Please tell where we can access your previous video session.[^2]

Everything is in the [GitHub repository](https://github.com/alexeygrigorev/ai-engineering-field-guide)[^48]. The first session: [What is an AI Engineer](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective)[^48].

## How I Use AI/ML in Daily Activities

Question from Naresh T: How are you using AI/ML in your day-to-day activities?[^2]

ML - very little. I cannot think off the top of my head of how I use ML specifically. AI for automation - everywhere. As a data scientist I have extensive ML experience and can train a model of any complexity when needed, but I just do not have tasks that I could automate with ML right now[^60].

For AI: I use coding agents frequently, then I use various AI tools for work automation - simple things like our FAQ system and similar things. In my personal work, I use assistants extensively. First, to write code faster. Second, to automate things. I write about all of this on my [Substack](https://alexeyondata.substack.com/) - you can read about it there[^60].

## How to Adapt to AI

Question from Challa Chinna Obulesh: How can we adapt for AI? What is the first step to adapt AI and how can we plan to learn AI?[^2]

"How to adapt" is a very general question. If you are worried that AI will take your job, then study these automation tools and automate your own work. I personally am very actively doing this. I really like the tools we have now, where things are going, the efficiency gains, and the things I can do now with AI that I could not do two years ago[^35].

The 20 hours you invest in learning this will pay off within a couple of months at most. The productivity gains from using programming tools and automation tools are very real[^35].

If you want to build agents yourself, that is also great. There is a huge space for integrating AI into products and automation. It is very interesting[^35].

For specific first steps: it depends on what you want to learn. On my [Substack](https://alexeyondata.substack.com/) I write about how I use AI and how other people use it[^36b]. If some ideas resonate, try to repeat them. If you have your own ideas, try to implement them. If you do not have your own ideas, look at what others are doing, see what resonates, try to repeat it and adapt to your situation[^36b].

For coding assistants and AI tools at some point they might not handle all the tasks you want. Then you need to look into agents and how to integrate AI into products. But again - if you do not have your own ideas, look at what others are doing and try to repeat it[^36b].

The key thing: do not fall into dopamine traps. I do this as my full-time job, so it is not fair to compare yourself with me. If you read all the posts on the internet, it seems everyone is super productive, everyone has time, everyone is building things. In reality, we are all simple mortals. Focus on what interests you personally and do not rush. If something is interesting, just do interesting things and see how you can apply AI[^36b].

## Do Local LLMs Have a Future?

Question from Naresh T: Do you think local LLMs will become more relevant in the future, both for AI engineering work and normal use?[^2]

Yes. Right now models from Anthropic and others are very subsidized - you pay much less than the real cost through subscriptions. This cannot last forever. The free ride will end at some point[^44].

On the other hand, local models are gradually catching up with cloud models. You can already run models that are quite usable on regular hardware. My hope is that by the time cloud providers raise prices significantly, local models will be comparable in quality. Then you just run your local model and keep working[^44].

## Sources

[^1]: [20260224_175508_AlexeyDTC_msg2256_transcript.txt](../inbox/used/20260224_175508_AlexeyDTC_msg2256_transcript.txt)
[^2]: [20260224_175510_AlexeyDTC_msg2258.md](../inbox/used/20260224_175510_AlexeyDTC_msg2258.md), [20260224_201409_AlexeyDTC_msg2344.md](../inbox/used/20260224_201409_AlexeyDTC_msg2344.md)
[^3]: [20260224_175701_AlexeyDTC_msg2260_transcript.txt](../inbox/used/20260224_175701_AlexeyDTC_msg2260_transcript.txt), [20260224_175711_AlexeyDTC_msg2264_transcript.txt](../inbox/used/20260224_175711_AlexeyDTC_msg2264_transcript.txt)
[^4]: [20260224_175702_AlexeyDTC_msg2261.md](../inbox/used/20260224_175702_AlexeyDTC_msg2261.md), [20260225_072926_AlexeyDTC_msg2384.md](../inbox/used/20260225_072926_AlexeyDTC_msg2384.md)
[^5]: [20260224_175755_AlexeyDTC_msg2266_transcript.txt](../inbox/used/20260224_175755_AlexeyDTC_msg2266_transcript.txt)
[^6]: [20260224_175809_AlexeyDTC_msg2268.md](../inbox/used/20260224_175809_AlexeyDTC_msg2268.md)
[^7]: [20260224_175824_AlexeyDTC_msg2270_transcript.txt](../inbox/used/20260224_175824_AlexeyDTC_msg2270_transcript.txt)
[^8]: [20260224_180200_AlexeyDTC_msg2274_transcript.txt](../inbox/used/20260224_180200_AlexeyDTC_msg2274_transcript.txt)
[^9]: [20260224_180308_AlexeyDTC_msg2276_transcript.txt](../inbox/used/20260224_180308_AlexeyDTC_msg2276_transcript.txt)
[^10]: [20260224_180424_AlexeyDTC_msg2278_transcript.txt](../inbox/used/20260224_180424_AlexeyDTC_msg2278_transcript.txt)
[^11]: [20260224_180521_AlexeyDTC_msg2280_transcript.txt](../inbox/used/20260224_180521_AlexeyDTC_msg2280_transcript.txt)
[^12]: [20260224_180832_AlexeyDTC_msg2282_transcript.txt](../inbox/used/20260224_180832_AlexeyDTC_msg2282_transcript.txt)
[^13]: [20260224_180956_AlexeyDTC_msg2284_transcript.txt](../inbox/used/20260224_180956_AlexeyDTC_msg2284_transcript.txt)
[^14]: [20260224_181037_AlexeyDTC_msg2286_transcript.txt](../inbox/used/20260224_181037_AlexeyDTC_msg2286_transcript.txt)
[^15]: [20260224_182327_AlexeyDTC_msg2288_transcript.txt](../inbox/used/20260224_182327_AlexeyDTC_msg2288_transcript.txt)
[^16]: [20260224_182421_AlexeyDTC_msg2290_transcript.txt](../inbox/used/20260224_182421_AlexeyDTC_msg2290_transcript.txt)
[^17]: [20260224_182546_AlexeyDTC_msg2292_transcript.txt](../inbox/used/20260224_182546_AlexeyDTC_msg2292_transcript.txt)
[^18]: [20260224_183516_AlexeyDTC_msg2294_transcript.txt](../inbox/used/20260224_183516_AlexeyDTC_msg2294_transcript.txt)
[^19]: [20260224_183912_AlexeyDTC_msg2296_transcript.txt](../inbox/used/20260224_183912_AlexeyDTC_msg2296_transcript.txt)
[^20]: [20260224_183944_AlexeyDTC_msg2298_transcript.txt](../inbox/used/20260224_183944_AlexeyDTC_msg2298_transcript.txt)
[^21]: [20260224_185150_AlexeyDTC_msg2304_transcript.txt](../inbox/used/20260224_185150_AlexeyDTC_msg2304_transcript.txt)
[^22]: [20260224_184408_AlexeyDTC_msg2300_transcript.txt](../inbox/used/20260224_184408_AlexeyDTC_msg2300_transcript.txt)
[^23]: [20260224_184742_AlexeyDTC_msg2302_transcript.txt](../inbox/used/20260224_184742_AlexeyDTC_msg2302_transcript.txt)
[^24]: [20260224_185501_AlexeyDTC_msg2310_transcript.txt](../inbox/used/20260224_185501_AlexeyDTC_msg2310_transcript.txt)
[^25]: [20260224_185204_AlexeyDTC_msg2306_transcript.txt](../inbox/used/20260224_185204_AlexeyDTC_msg2306_transcript.txt)
[^26]: [20260224_185328_AlexeyDTC_msg2308_transcript.txt](../inbox/used/20260224_185328_AlexeyDTC_msg2308_transcript.txt)
[^27]: [20260224_185755_AlexeyDTC_msg2312_transcript.txt](../inbox/used/20260224_185755_AlexeyDTC_msg2312_transcript.txt)
[^28]: [20260224_185911_AlexeyDTC_msg2314_transcript.txt](../inbox/used/20260224_185911_AlexeyDTC_msg2314_transcript.txt)
[^29]: [20260224_190208_AlexeyDTC_msg2316_transcript.txt](../inbox/used/20260224_190208_AlexeyDTC_msg2316_transcript.txt)
[^30]: [20260224_190501_AlexeyDTC_msg2318_transcript.txt](../inbox/used/20260224_190501_AlexeyDTC_msg2318_transcript.txt)
[^31]: [20260224_190743_AlexeyDTC_msg2320_transcript.txt](../inbox/used/20260224_190743_AlexeyDTC_msg2320_transcript.txt)
[^32]: [20260224_191018_AlexeyDTC_msg2322_transcript.txt](../inbox/used/20260224_191018_AlexeyDTC_msg2322_transcript.txt)
[^33]: [20260224_191152_AlexeyDTC_msg2324_transcript.txt](../inbox/used/20260224_191152_AlexeyDTC_msg2324_transcript.txt)
[^34]: [20260224_193006_AlexeyDTC_msg2326_transcript.txt](../inbox/used/20260224_193006_AlexeyDTC_msg2326_transcript.txt)
[^35]: [20260224_204640_AlexeyDTC_msg2346_transcript.txt](../inbox/used/20260224_204640_AlexeyDTC_msg2346_transcript.txt)
[^36]: [20260224_193147_AlexeyDTC_msg2328_transcript.txt](../inbox/used/20260224_193147_AlexeyDTC_msg2328_transcript.txt)
[^36b]: [20260224_204926_AlexeyDTC_msg2348_transcript.txt](../inbox/used/20260224_204926_AlexeyDTC_msg2348_transcript.txt)
[^37]: [20260224_193442_AlexeyDTC_msg2330_transcript.txt](../inbox/used/20260224_193442_AlexeyDTC_msg2330_transcript.txt)
[^38]: [20260224_193659_AlexeyDTC_msg2332_transcript.txt](../inbox/used/20260224_193659_AlexeyDTC_msg2332_transcript.txt)
[^39]: [20260224_193809_AlexeyDTC_msg2334_transcript.txt](../inbox/used/20260224_193809_AlexeyDTC_msg2334_transcript.txt)
[^40]: [20260224_193856_AlexeyDTC_msg2336_transcript.txt](../inbox/used/20260224_193856_AlexeyDTC_msg2336_transcript.txt)
[^41]: [20260224_194404_AlexeyDTC_msg2338_transcript.txt](../inbox/used/20260224_194404_AlexeyDTC_msg2338_transcript.txt)
[^42]: [20260224_194820_AlexeyDTC_msg2340_transcript.txt](../inbox/used/20260224_194820_AlexeyDTC_msg2340_transcript.txt)
[^43]: [20260224_195058_AlexeyDTC_msg2342_transcript.txt](../inbox/used/20260224_195058_AlexeyDTC_msg2342_transcript.txt)
[^44]: [20260224_205146_AlexeyDTC_msg2350_transcript.txt](../inbox/used/20260224_205146_AlexeyDTC_msg2350_transcript.txt)
[^45]: [20260224_205239_AlexeyDTC_msg2352_transcript.txt](../inbox/used/20260224_205239_AlexeyDTC_msg2352_transcript.txt)
[^46]: [20260224_205637_AlexeyDTC_msg2354_transcript.txt](../inbox/used/20260224_205637_AlexeyDTC_msg2354_transcript.txt)
[^47]: [20260224_210105_AlexeyDTC_msg2356_transcript.txt](../inbox/used/20260224_210105_AlexeyDTC_msg2356_transcript.txt)
[^48]: [20260225_072926_AlexeyDTC_msg2384.md](../inbox/used/20260225_072926_AlexeyDTC_msg2384.md), [20260225_072853_AlexeyDTC_msg2382_transcript.txt](../inbox/used/20260225_072853_AlexeyDTC_msg2382_transcript.txt)
[^49]: [20260224_210611_AlexeyDTC_msg2360_transcript.txt](../inbox/used/20260224_210611_AlexeyDTC_msg2360_transcript.txt)
[^50]: [20260224_210801_AlexeyDTC_msg2362_transcript.txt](../inbox/used/20260224_210801_AlexeyDTC_msg2362_transcript.txt)
[^51]: [20260224_210805_AlexeyDTC_msg2364.md](../inbox/used/20260224_210805_AlexeyDTC_msg2364.md)
[^52]: [20260224_211154_AlexeyDTC_msg2366_transcript.txt](../inbox/used/20260224_211154_AlexeyDTC_msg2366_transcript.txt)
[^53]: [20260224_211220_AlexeyDTC_msg2368.md](../inbox/used/20260224_211220_AlexeyDTC_msg2368.md)
[^54]: [20260225_065001_AlexeyDTC_msg2370_transcript.txt](../inbox/used/20260225_065001_AlexeyDTC_msg2370_transcript.txt)
[^55]: [20260225_065127_AlexeyDTC_msg2372_transcript.txt](../inbox/used/20260225_065127_AlexeyDTC_msg2372_transcript.txt)
[^56]: [20260225_065217_AlexeyDTC_msg2374_transcript.txt](../inbox/used/20260225_065217_AlexeyDTC_msg2374_transcript.txt)
[^57]: [20260225_065555_AlexeyDTC_msg2376_transcript.txt](../inbox/used/20260225_065555_AlexeyDTC_msg2376_transcript.txt)
[^58]: [20260225_065847_AlexeyDTC_msg2378_transcript.txt](../inbox/used/20260225_065847_AlexeyDTC_msg2378_transcript.txt)
[^59]: [20260225_072829_AlexeyDTC_msg2380_transcript.txt](../inbox/used/20260225_072829_AlexeyDTC_msg2380_transcript.txt)
[^60]: [20260225_073128_AlexeyDTC_msg2386_transcript.txt](../inbox/used/20260225_073128_AlexeyDTC_msg2386_transcript.txt), [20260225_073129_AlexeyDTC_msg2387.md](../inbox/used/20260225_073129_AlexeyDTC_msg2387.md)
[^61]: [20260225_073217_AlexeyDTC_msg2390_transcript.txt](../inbox/used/20260225_073217_AlexeyDTC_msg2390_transcript.txt)
[^62]: [20260224_175839_AlexeyDTC_msg2272_transcript.txt](../inbox/used/20260224_175839_AlexeyDTC_msg2272_transcript.txt)
