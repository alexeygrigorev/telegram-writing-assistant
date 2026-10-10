---
title: "Trends in AI Engineering: Lightning Lesson with Hugo Bowne-Anderson"
created: 2026-09-29
updated: 2026-10-11
tags: [ai-engineering, agentic-engineering, career, evals, hugo-bowne-anderson, lightning-lesson]
status: draft
---

# Trends in AI Engineering
## Webinar with Hugo Bowne-Anderson

Last week I ran a webinar with Hugo Bowne-Anderson. Hugo and I met in Berlin about a month before, had a great breakfast, and decided to do something together.

The first step was an open ask-us-anything session - which was the webinar. We had two goals for it:

- help the people who came to the webinar
- understand what we could create together for you longer term

At the end of the session Hugo and I talked about turning this recap into a shared Substack article - this article.

## Who We Are

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/hugo-and-alexey.jpg" alt="Alexey Grigorev and Hugo Bowne-Anderson in a cafe in Berlin">
  <figcaption>Hugo and I at our breakfast in Berlin</figcaption>
</figure>

I have been an educator for about six years. I started with [machine learning engineering](https://github.com/DataTalksClub/machine-learning-zoomcamp), then did [data engineering](https://github.com/DataTalksClub/data-engineering-zoomcamp), and in the last few years I have focused on [AI Engineering](https://maven.com/alexey-grigorev/from-rag-to-agents). Before that I was a hands-on data scientist, machine learning engineer and data engineer - a full-stack data scientist doing whatever needed to be done to work with machine learning and AI.

I like calling myself a product AI engineer: I do whatever it takes to integrate AI from the user's perspective. This is what I teach in my courses.

Hugo's background is in mathematics, physics, and biology. He researched cell biology in Dresden, at the Max Planck Institute, and then at Yale. About 15 years ago, living in New York, he moved to industry because the machine learning and data science scene was so exciting, but he stayed in education. He has worked on machine learning and data products in SaaS for most of those 15 years: DataCamp, education in the SciPy and PyData ecosystems, and developer relations at startups such as Coiled and Outerbounds. He hosts podcasts, and that is how we first met - we have done a bunch of podcasts together.

## Trends in AI Engineering

I maintain the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) repository.

Every month since January 2026 I scrape job postings for the query "AI engineering" in Berlin, Amsterdam, London, New York, and Los Angeles. Some people asked why there were no Indian cities, so I included the whole of India.

I then process the raw data with LLMs to extract structured information: skills, responsibilities, and use cases.

All this data is saved in the AI Engineering Field Guide repo. This is what one processed job posting looks like:

<figure>
  <img src="../../assets/images/trends-in-ai-engineering-lightning-lesson/structured-job.png" alt="Structured YAML extracted from a Senior AI Engineer job posting: company, responsibilities, use cases, and skills">
  <figcaption>A Senior AI Engineer posting from the September 2026 scrape after LLM extraction</figcaption>
</figure>

Nine months of data is not enough to build models that predict the future. But there are already interesting trends that show where the market is going:

- The overall market is growing. Everyone asks "where are all the jobs?" - for now, at least, the data says we shouldn't worry.
- Forward-deployed engineers are the fastest growing part. Within the AI engineering market, FDE roles grow even faster than the market overall. I have a separate analysis of the FDE market: [What AI Forward-Deployed Engineers Do](https://aishippingblog.com/p/what-ai-forward-deployed-engineers).
- Model training roles are shrinking. Before, companies hired people to train LLMs with PyTorch-style skills. The number of these positions is decreasing, and so is inference and serving.
- The industry is converging on a meaning for "AI engineer": mostly invoking models through API calls and building things around them.
- Almost every posting requires RAG and agents, and this is growing.
- There are very few junior positions - only about 1%. AI engineers are usually more experienced people, so starting your career as an AI engineer can be very difficult.

## What Roles Will Exist in a Year or Two

The job data shows what the market looks like today. But what about the future: which roles will exist a year or two from now, and how can humans add real value in their work?

Nobody can see what roles, hiring processes, or even tools will look like then. The second part - how can we add value - is the one to ask. Hugo encourages people, including students at college or university, to learn current tools and technologies that help them add value where they are: their local communities, their businesses, their universities.

The other meta-skill is learning constantly and being a hacker. When a new model comes out - the new Fable, or Sonnet 5.5 that just came out - the valuable person is the one who plays with it, wonders what they can do with it, and then delivers business value or helps people with it.

Some data scientist skills will always be useful:

- A hacker mentality, as described above
- Knowing some statistics, how to analyze data, and how to use data to improve products
- Domain expertise in something - SRE, DevOps, marketing, or anything else

Building retrieval systems is not on this list, although search is becoming increasingly important. Adding value, hacker skills, and knowing how to analyze data and apply it to business problems matter more.

I would add one more skill to the list. I call it problem discovery. I don't know if it has an official name.

There are so many problems around us waiting to be discovered and solved. Look at your own everyday life. There are so many things you repeat, and so many things that are mildly annoying, but you're not doing anything about them yet. Discovering these things and doing something about them is a big source of projects - projects that improve your own life and potentially the lives of others.

With AI, I can finally approach these problems. Every week there is a new model available for free, and you can test it without an expensive subscription. You can see how to use these models to solve your problem. This is the hacker mentality again, but you are not just hacking around - you are hacking something together that solves your particular problem. AI cannot find these problems for you. This is where you as a human can stand out.

## Agentic Verification

Hugo ran a survey on how people do agentic data science.

Many people said AI changes their workflow significantly: 34 said "fundamentally" and 39 said "significantly". Hugo wanted to see what made the difference, so he built a heat map of how much AI changed people's workflow against how they verify AI-generated code. Many people read the code manually, and many run it and inspect the output.

59% of the people whose workflow changed fundamentally use agentic verification and write tests. The share of tests and verification drops as the reported impact drops. It is not causal, but there is a correlation: the more tests you write and the more agentic verification you use, the more value you get from agents.

Hugo is not saying "don't read code manually". He is saying "probably don't read all of your code manually". The people who do robust agentic and deterministic verification see a bigger change in their daily workflows.

I asked what he means by agentic verification. It is using agents to verify the work of other agents.

What convinces people to adopt agents is seeing automation. You have a markdown file that describes a process, and all of a sudden the agent takes a mundane task you've been doing manually and just runs with it. That is the aha moment. Then the next question is: will it always work? What are the edge cases? Proving that these things work is what agentic verification is about.

On the individual level, having the agent run the process is already good enough. It's kind of autopilot, but I'm still holding the wheel and can intervene. Eventually this gives a lot of trust, and I don't need to keep an eye on it constantly.

In AI engineering more generally, this is evaluation, and it is one of the most important skills - this is what I see in the job data too. Knowing evals is the difference between getting hired and not getting hired. If you don't know evals, the conversation with the hiring manager will likely end once they discover that. These systems are not deterministic, so we cannot simply trust them. We need a framework to make sure they can be trusted - for example, an agent that evaluates another agent. For that framework to be sound, the data science skills help a lot: data scientists have done this kind of evaluation for a very long time, because machine learning is non-deterministic too.

## How the Software Lifecycle Changes

Hugo described how he thinks software development is changing. A very reductive software development lifecycle is: spec it out, build it, verify it, and if it works, ship and maintain it. With agents, every step changes:

1. Speccing is agent-assisted.
2. The build is agent-driven - agents write most of the code.
3. Verification has several layers:
   - Automated tests, as before - unit, integration, end-to-end, regression
   - LLM as a judge for correctness, quality, and adherence
   - Agentic review, where agents review code and design
   - Human review for context, UX, and similar things
4. Once you get sophisticated enough, agents monitor, operate, and suggest changes in production.

## Agentic Engineering vs AI Engineering

Hugo then separated two terms that often get confused:

- In agentic engineering (a term coined by Simon Willison), you build software with agents. The agent is part of the dev team. The question is how to use AI as a development partner. Your job is specification, delegation, review, and orchestration.
- In AI engineering, you build agentic search, RAG, or an agent. AI is part of the product. The question is how to use AI within the application. You think about models, prompts, evals, harness engineering, and agentic loops.

The truth is, if you do one of them, you also do the other. If you build AI-powered products, you use agents to build them. If you do agentic engineering, you also build up your harness - skills in your AGENTS.md, MCP servers, sandboxes, guardrails. Once you see they are two different things, you see they collapse into each other. It is still important to separate them, because people say "agentic engineering" when they talk about building a retrieval system.

I see this confusion among people who join my courses. They join a course about AI engineering wanting to learn agentic engineering - how to use AI for coding. There is a lot of overlap. As an AI engineer, your job is to include AI in the product, and your job can also be creating something like Claude Code or Codex. But if you write code with AI, you don't need to know the details of how that tool is evaluated or monitored - that is taken care of. You focus on creating the proper specification, making sure the agent follows it, and enforcing the development lifecycle rules. The work is very different.

## No Handwritten Code

The way we coded one year ago is very different from how we code now, and the reason is agentic engineering. I think we will see more and more of it.

I talk to more and more companies whose policy is "no handwritten code". From now on, you are not allowed to write code yourself - only through an agent.

At one of these companies, many engineers resisted and said they still wanted to write code by hand. The answer was: nobody is keeping you here, go find a different place. I was surprised they were that adamant about it. But it is their choice - they know how to run their business better.

Even when it is not enforced, it is hard to go back to manual coding. You are still the bottleneck when you work with agents, but if you write code directly, you are just so much slower.

## Do Agents Write Sloppy Design and Code?

An attendee asked: don't coding agents, even frontier ones, make sloppy design and code? And isn't it true that only a technical human can refactor and fix that?

Hugo split this into three questions.

Do they make sloppy design? Absolutely. They spew tokens at you - pages and pages of design that are absolute slop. When you design with them, you need to be in the loop and in control. They can be wonderful ideation partners, but direct them well. Ask them to respond in three sentences, or to give you 10 ideas of three sentences each, so you can choose the best one. They can also help you filter ideas down. There are skills like Superpowers and grill-me that ask you a lot of questions.

My approach to design is what I call adversarial design. I don't use any skills for it. I set up two agents: a designer and a senior designer. The designer designs. The senior designer tries to find a reason to reject the design. They share a design system document that describes how the design should look, and they bounce the design between each other until the senior designer is satisfied.

This approach works for everything. There is an implementer and a tester. The tester's goal is to find holes in the implementation and bounce it back to the implementer. The implementation becomes slower - a feature may take 4-5 hours instead of 20 minutes because of the back and forth - but it is still faster than doing it manually, and the quality at the end is better.

If you let it run uncontrolled, you get a lot of slop. So remember the good books. My favorite is Clean Code by Robert Martin. If you just say "follow the principles from the Clean Code book by Robert Martin", the code improves. Sometimes I make it more specific:

- Functions no longer than 30 lines
- Files no longer than 300 lines
- Follow the SOLID principles
- Follow the don't-repeat-yourself principle

Of course it burns more tokens, but I don't want to cry when I look at the code.

It is the same as leading a team of juniors. If you let the team write code uncontrolled, you get code that is very hard to maintain. Even if you don't look at every line, you share the design principles with the team, and you check from time to time: "No, this is not good, I said no ternary operator". Sometimes you see something that isn't in the rules yet, and you think about how to teach the team. For example, list comprehensions are fine, but not when taken to the extreme with nested loops and if statements - so maybe I just ban comprehensions, and the code quality improves. You stay in the loop and look at the code from time to time, but you are not the bottleneck.

Hugo does the same for prose. For marketing copy and blog posts, he uses Strunk and White's The Elements of Style. Some of its principles:

- Omit needless words
- Use the active voice
- Put statements in positive form
- Make the paragraph the unit of composition
- Keep related words together

He has these rules in the AGENTS.md of a bunch of repos and has agents generate prose under them. The agents don't always follow the rules, so he has a verify agent that edits the text to respect them. In fact he runs a trio of verify agents in parallel, because each one messes something up, and then a final agent performs the edit. Then he looks at it quickly.

I took a note of that. I developed my rules empirically, by looking at what went wrong and correcting it. It is much more convenient to point to a resource - Clean Code for code, The Elements of Style for prose.

To the last part of the question - "only a technical human can fix it" - Hugo pushed back. It isn't only a technical human. It is an agent that you have given the correct instructions and the correct verification processes. If you encode the rules in a verifier agent, it will generally be very good at it. It is a skills problem. Give the agents the correct instructions, probably parallelize with a few of them because some will mess up, and have the high-risk, important things surfaced to a human. That doesn't have to mean looking at code - it can be dashboards, information graphics, or cards.

I have done experiments where I turned super sloppy code into code I didn't cry reading. The codebase was fairly large and relatively old. I developed it with AI - first by copy-pasting from ChatGPT, then fully with coding agents. When I noticed a lot of slop, I asked the agent to refactor the entire codebase using these rules. It took two Codex resets, but the result was good.

I used to be a purist about code when I worked as an engineer, and I tried to make my code look really good. With that mindset I can still find flaws. But if I set it aside and ask "is this good, readable code?", the answer was yes. When I notice something, I add a rule. For example, agents love defensive coding. In Python, they check if an attribute exists before accessing it. This is nonsense and makes the code hard to read. The solution is a type checker.

## Working With Agents Is Hard Work

Hugo made another point: this is really hard work, and working with agents requires a different mindset. You can't work with them all day, every day. We haven't evolved to make that many decisions and read that much text. Software engineering has always been hard. Agents didn't make it easy - they made it a different kind of hard. Hardcore software engineers do it too. One engineer who builds the Amp coding agent uses AI to generate pretty much all his code, but he also uses AI to trim and sculpt it until it is beautiful to him. That is a huge amount of work - you can't just generate tokens and get that.

It is also a question of how important code quality really is. If you are building a prototype or bootstrapping a business, crappy code that works is better than ideal code that doesn't. As a founder, you describe an idea, set up the specification, the agent builds it, and you check the UI and verify it works as expected - which is already a lot of work. Even if it is the worst code in the world, if it gets the job done and gets you your first thousand customers, why not? When you have paying customers, you can spend time refactoring. Before that, does it make sense to invest in it? Perhaps, perhaps not.

## Dark Software Factories

Hugo said something he admitted may sound radical. He thinks a lot about agentic software factories. The premise is to move from using a coding harness yourself to a setup with more automation and continuous learning, which does appropriate work while you are asleep or away. You take a few things you do every day with Codex or Hermes, start automating them, add more on top, and build in continuous learning.

The idea of a software factory isn't new. But people are starting to think about dark software factories. A dark factory is one where humans are not present or not allowed at all - there isn't even light inside. There are several in Japan where robots build robots.

In a dark software factory, humans are not allowed to look at the code. They get artifacts that let them make business decisions and verify that everything is correct, but humans are separated from the generated code. Hugo doesn't suggest anyone build one today. But he thinks there is a not-so-distant future where they are economically viable and productive. If that sounds out there, remember that we don't read machine code anymore. There are abstraction layers that make us confident software works. Again, it comes down to good tests, verification, and specification with agents.

I think it is a good point. As a solo founder, a business founder without a technical person, or even a software engineer, your time is limited. If you check everything your agents write, you become the bottleneck and slow everything down. Once you let the agents run without your involvement, you are only the final gatekeeper who accepts or rejects.

In my setup, agents escalate things that need human verification. I had to tune them so they escalate only what I really need to see. They add a human tag to a GitHub issue, and then I look. Most of the time I am out of the loop. I give them specifications or raw input, they create specifications from that, create features, and ship them. Sometimes I need to check.

Often I am involved more than I want, because agents create slop, especially in design. Even with all the design principles, you need to keep an eye on it. Maybe in the future we can have perfect dark software factories. For the backend, they can be dark factories already. For the frontend, not yet. But with new models like Opus 5.5 I feel I can be involved less and less.

## Human Skills Still Matter

An attendee asked whether soft skills and leadership skills stay relevant in the AI era. Hugo said absolutely. A lot of the skills we need will be about working with humans, and with humans and agents together. He prefers to call them human skills rather than soft skills.

Think about it this way. Why do we use agents? To write code. Why do we write code? To solve problems. Whose problems? If we build a product, our customers' problems. Our customers are people, not agents. So we need to communicate with people to solve their problems - otherwise, will they use our product? Probably not. We still need the human connection, the user interviews, and everything product managers and product designers have done for a very long time.

We also need many skills in a team. As a solo founder, I can go far with AI. But my background is engineering. I don't have product management or design skills, and I don't have marketing or sales skills. For me as a solo founder, this is where it hurts most - I can't reliably sell what I build. When the product grows, you need a team, and working with people requires soft skills.

The same applies to freelancers. You need to find clients and convince them why you charge $2,000 per day when a Claude subscription costs $200 per month. Agents will not give you money. And the same applies at work - how do you convince your manager to give you that promotion?

Hugo agreed. The sales cycle is one of the toughest parts for solo founders. It comes down to speaking with people, understanding their problems, and solving them in a way that gives them more value than they pay. His teaching works the same way - this session exists to find out what people are interested in. And the two of us are doing it together because we met in Berlin and had breakfast. All of that is human skills.

## Organizing Many Agents

Hugo uses Codex during the day, jumping between conversations to see what different agents are up to. A few weeks ago he figured out that Codex agents can talk to each other, so he can ask one thread to ping another. People have been thinking about agentic hierarchies with subagents, which is useful for some things, especially context separation. He is excited about what comes next, though he hesitates to call it swarms.

I don't think it is swarms. A corporation is not a swarm. There are different ways to organize work, but there is usually a hierarchy - a CEO or president, then CPO, CTO, CFO, and then the verticals. You can't just tell 10,000 agents to go solve millennium problems. You need organization - for example, a chief scientist who says "you try this, you try that".

When OpenAI made its announcement about the Navier-Stokes problem, what interested me was that it was a team of 10,000 agents. I ran a thought experiment: if I had to approach a problem I don't know, with nearly infinite compute - 10,000 agents - how would I organize the work? I arrived at a hierarchical approach. It all comes from the leadership and soft skills world.

That's why I think product managers are uniquely equipped to run agents. They already have the skills: they know how to organize work in a team, set up processes, define specifications, and check work. This sets them apart from developers who follow whatever processes are set. Heads of product work at an even higher level, and with agents, we need this kind of structure for complicated problems.

In my own work, I haven't found a problem where I need a team of teams. It is mostly one team of agents. At most, I have a project with two teams running in parallel, where the team leads talk to each other. A bigger structure slows things down for me.

Hugo hasn't done much of this either. Chip Huyen told him on his podcast that she ran around 2,000 agents at the same time, but cases like that are few and far between.

## Should AI Engineers Work on the Harness or the Model?

An attendee asked whether it is better for AI engineers to work on the harness or on the model.

Hugo didn't say which is better. Training models is like working on an internal combustion engine. If you are a Formula One driver, it is good to know how it works, but most people who use a car don't need to. Most people building production systems won't train models themselves, although they may be interested in how it works. He wouldn't even say an AI engineer works on the harness. An AI engineer works on a product. That involves working on the harness, but the harness is a technical implementation detail.

I recently read Inference Engineering by Philip Kiely, who spent several years at Baseten working on high-performance inference at scale. It is about hosting open-source models yourself. Most of the time, we send a request to OpenAI, Anthropic, or another provider, get a response, and do something around it. That is AI engineering simplified into two sentences - overly simplified, because there is a lot of work around it to make it reliable.

If you want to look under the hood of what happens when you send a request, the book is very good. It is broad rather than in-depth, and it tells you a lot about how to serve a model once it is trained.

## Becoming an AI Engineer in Three Months

I passed a question on to Hugo: "My goal is to become an AI engineer and get hired in the next three months. Do I need to focus on training and serving, or should I spend my time elsewhere?"

Hugo would take one of our AI engineering courses. Otherwise, he would focus on the data science mentality and the new software development lifecycle. It is not the traditional spec, build, deploy, maintain. It is iterative and experimental:

1. You build.
2. You add observability and traces.
3. You look at your data and build an evaluation set from it.
4. You pull levers based on the failure modes you see.
5. You iterate in production with domain experts.

That is the lifecycle of AI products, which involves the non-determinism of LLMs. The way to learn all of it is by building a project. Hugo likes that my courses are project-oriented: you learn by building an agent or an AI-powered application and getting real users.

Hugo didn't mention training a model from scratch, mastering inference engineering, or fine-tuning. People often ask me whether they need to know LLM internals to work as an AI engineer. I usually say no. You need to know how to send a request to an LLM provider, build everything around it, and have the data science mindset. That is way more important than knowing how LLMs work. At some point you will probably get curious about how these things work, even if you don't need it for your work, but you don't need it upfront.

Some companies do lower-level work and may ask for it, but in my data it is less than 10%. If your time is limited and you want to get into AI engineering, spend it on what Hugo described. Don't spread your focus across areas just because they look interesting and you are not sure whether they are required. To get your foot in the door, you don't need them. Inference Engineering is a wonderful book, but if your goal is to become an AI engineer, read it later and focus on building projects now. If your goal is to become an inference engineer, that is the book to read.

## What Comes Next

Hugo and I want to run a paid course together, like the ones we already run on Maven. There are infinitely many ideas, so we want to understand what people actually want: where they stand, what they want to build, where they are stuck, what their goals are, and what format they prefer. We shared a form that asks about this. It is not a short form and needs some focus time, so as a thank you, people who fill it in will get a discount on the future course once we decide what to build. Hugo added that we want to hear both what pains you and what excites you, so we can build an offering that meets your needs.

We will send the form, the recording, and a transcript by email to everyone who signed up. Hugo will also invite me to do another lightning lesson soon.
