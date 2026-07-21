---
title: "Plan: Mariano Beccaria"
created: 2026-07-21
updated: 2026-07-21
tags: [ai-shipping-labs, plan, community, consulting]
status: draft
---

# Plan: Mariano Beccaria

Internal working document. Share only the `Summary` and plan sections with the member. Everything from `Internal Context` onward stays inside AI Shipping Labs.

## Summary

- Current situation: 25 years as a software and Linux engineer, the last 10 of them in DevOps. Since 2023 he runs his own property maintenance business in North Carolina, and he is building toward an AI consultancy for small and medium businesses outside high tech - trades, property maintenance, local manufacturers. He already has a working prototype: a Streamlit app where a client uploads a CSV and asks questions about it, with RAG, a small multi-agent setup, and forecasting, containerized with Docker and running on an EC2 instance[^1][^2][^7].
- Goal for the next 6 weeks: several prototype workflows he can present as RAG agent demos for brick-and-mortar businesses, each one adaptable to a specific client's needs[^1].
- Main gap to close: breadth. Consulting work rewards having seen many projects and many implementations more than going deep on one. Right now he has one prototype and a set of ideas, and he needs volume - both projects he builds and projects he studies[^3].
- Weekly time commitment: 10 hours per week, steady, mostly in the early morning before client visits start[^1][^7].
- Why this plan is the right next step: he does not need one big build. He needs many different small projects, plus a high-level understanding of how other people build theirs. That is the shape of consulting work, and it also produces the demo set he asked for[^3].

## Plan

The core idea is breadth over depth. For a consultant it matters more to have seen many projects - what the idea was and how it was implemented at a high level - than to go deep on a single one[^3].

Two tracks run in parallel every week:

1. Other people's projects. Get into one new project a week: what problem it solves, how it is implemented, which tools were picked, how the workflow is set up. On top of that, partner with someone who is actively building, learn as much as possible about their project, and help them with it[^3][^4].
2. His own projects. Build small prototypes. Around 10 to 20 hours per project, using AI coding tools as heavily as possible so a prototype fits into that budget[^3].

The first source of projects is his own business. He has more than 100 clients in a CRM, and he has already listed what needs automating there: responding to leads within the hour so they are not lost, producing repair quotes without spending hours on them, social media posting, email replies, and scheduling client visits so the route is short and the gasoline bill drops[^7]. Being his own first client means the problem is real, the data exists, and the demo can be shown to other trade businesses that have exactly the same problems.

## Focus

- Main focus: quantity of projects. One new project understood per week, and his own small prototypes shipped in parallel.
- Supporting focus: one sprint partner to build with, plus calls with several other members to learn what they build, which tools they use, and how their flow is set up.
- Supporting focus: fill the remaining gaps with targeted LLM Zoomcamp modules, and use AI coding tools to get more out of 10 hours a week.

## Timeline

Week 1:

- Set up the sprint partnership with Sergey Sedler. He has a lot of business ideas about where AI can be applied, and coding is his weaker side, which is the opposite of Mariano's profile. Agree on what to work on together over the sprint[^4][^5].
- Pick the first prototype from his own business: the highest-value automation he can demo, most likely lead response or quote generation.
- Book the first call with another member to learn about their project.

Week 2:

- Build prototype 1 end to end and get it to a state where someone else can run it. Stay inside the 10-20 hour budget and lean on AI coding tools to stay there.
- Second member call. Ask the same questions every time: what the project does, how it is implemented at a high level, which tools were chosen, how the workflow is set up.
- Note the gaps that show up while building. If a specific skill is missing, take the LLM Zoomcamp module that covers it rather than a whole course[^3].

Week 3:

- Post prototype 1 in Slack as a demo with a specific ask, not as a code dump. A hosted app plus a short description of what it does and what feedback is wanted[^7].
- Start prototype 2 for a different business type, so the set covers more than one shape of problem.
- Third member call.

Week 4:

- Finish prototype 2. For both prototypes, write down the client problem, what the demo does, and what would change per client.
- Fourth member call.
- Look at the projects being built in the LLM Zoomcamp cohort that is running right now and how they are implemented. This is breadth without having to build everything himself[^3].

Week 5:

- Start prototype 3, chosen from whatever demand came out of the conversations with local businesses.
- Fifth member call.
- Work with Sergey on turning one of his business ideas into a scoped prototype: his idea, Mariano's implementation.

Week 6:

- Finish prototype 3 and pull all three into one presentable set of demos for brick-and-mortar businesses.
- Write a short walkthrough for each demo so it can be shown to a prospect and adapted to their needs.
- Review the sprint: which of the projects seen and built are worth going deeper on next.

## People to talk to

The point of these calls is not networking. It is to find out what other people are building, which tools they use, and how their flow is set up[^5].

- Sergey Sedler - the main partner for this sprint. Strong on business ideas and on where to apply AI, weaker on coding[^4][^5].
- Salma Bouzid - building an edtech startup that helps teachers[^3].
- Carlos Pumar - building a personal agent for small and medium enterprises, the closest match to Mariano's own target market[^3].
- Vancesca Dinh - worth a call to hear what she is working on and how she plans to implement it[^3].
- Scott DeGeest - his cyber security disclosure app is the one Mariano already picked out as his favourite, and cyber security for medium-sized businesses is a topic Mariano wants to work in[^7].

## Resources

- [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) - keep going, and use it module by module for specific gaps rather than end to end. The cohort is running now, so the projects being built in it are also worth studying[^3].
- [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) - this is the one that shows how to use AI coding tools efficiently, which is what makes a 10-20 hour prototype realistic[^3].

## Deliverables

- Three prototype demos for brick-and-mortar businesses, each with a short walkthrough that a prospect could be shown.
- A running set of notes on the projects reviewed: idea, implementation, tools, workflow.
- One sprint partnership with Sergey Sedler, with something built together.

## Accountability

- Weekly check-ins and fixed deliverables. Both are on his own list of what helps, along with demo milestones, async Slack, partner pairing, build-in-public, reflections, and checklists[^1].
- Post a weekly update in Slack: the project reviewed this week and the state of the current prototype. Share a runnable demo with a specific ask rather than raw code - that is the format he already decided works best for him, and it also works around the code-sharing constraint from his other mentor[^7].

## Next Steps

- [ ] [Mariano] Confirm the sprint partnership with Sergey Sedler.
- [ ] [Mariano] Pick the first prototype use case from his own business backlog.
- [ ] [Valeriia] Introduce Mariano to Sergey Sedler and to the other members he should call.
- [ ] [Alexey] Confirm the fourth name from the review notes before the introductions go out.
- [ ] [Valeriia] Confirm whether Alexey has a slot in August for a technical call on Mariano's projects[^7].

## Internal Context

Everything below is for internal use only.

## Persona

Alex (The Engineer transitioning to AI) - assigned by the onboarding questionnaire (`onboarding-alex`). It fits: two decades of engineering, and the blocker he named himself is translating software engineering into AI[^1].

The consulting angle makes him an unusual Alex. He is applying for data engineer and AI engineer jobs, but the real goal is the consultant and entrepreneur route, so the usual portfolio-for-a-hiring-manager advice does not apply directly. Breadth for client work replaces depth for a recruiter[^3][^7].

## Background

Mariano Beccaria, based in North Carolina, United States. Joined AI Shipping Labs on 2026-06-10 on the Main tier and submitted the onboarding survey the same day. Last login 2026-06-30. Slack member. No sprint enrollments, no course enrollments, and no plan on record before this one[^2].

Twenty-five years in the industry as a software and Linux engineer, the last ten as a DevOps engineer. In 2023 the consulting company he worked for was bought by an Indian company, which laid off all the American employees. He has not worked in the industry since[^7].

Since then he runs his own business, unrelated to IT: property maintenance and home services, working with property managers and people who sell homes. He has more than 100 clients in a CRM, his wife handles the admin side, and he has a couple of people who do work for him. The business requires him to be physically at client locations, so his AI work happens early in the morning - he gets up at 5 and has to be with clients by 10[^7].

A year ago he signed up with Data Engineering Academy to move into data engineering. It had good parts, but he had to go outside the program to fill the gaps, and it had no AI focus. In March he signed up with Business Science (Matt Dancho) for an AI course. He learned a lot there and is almost finished, but gaps remained: he could build RAG agents with LangChain and similar tools without really understanding what was happening underneath[^7].

That is why he likes LLM Zoomcamp - it starts from the basics and builds up, with libraries like minsearch, instead of starting from a black box like LangChain. The specific thing that opened his mind was realizing that RAG can be used without an AI agent. He is currently in the Kestra module. He kept missing homework deadlines because of the field work, and he plans to keep submitting as his schedule allows[^7].

He is currently applying for data engineer and AI engineer jobs, but the long-term goal is consulting. He does not want to depend on income from a single company, and he is wary that AI could turn out to be a bubble. The plan is to hire people to run the maintenance business so he can focus fully on AI consulting - although finding reliable people for trade work has been hard[^7].

## Where the demand is

He sees the demand from two sides. First, from his own business and the trades around him - plumbers, air conditioning technicians, and people doing all kinds of repair work on pipes, walls and the rest. He works in that field himself, and he sees that there is a pile of things in that daily work where AI and agents would help, and that nobody is doing it. Managing 100+ clients while working in the field needs automation: an agent that answers a lead within the hour (a lead that is not answered within an hour is 80-90% lost), an agent that produces repair quotes he can send without hours of review, social media and ad automation, email replies, and scheduling that groups client visits geographically so he does not travel an hour between jobs and burn gasoline, one of his biggest expenses[^6][^7].

Second, from local companies that are not high tech at all - metal manufacturers, for example - who are actively asking how to implement AI. Small and medium companies want to forecast things for themselves. They have piles of data sitting in Excel sheets, CSVs, and PDFs that they cannot use at all. What they want is the same three things: how to save money, how to make money, and how to forecast. And when someone works on their own, there is no time to manage any of it, which is where the idea of automating it with AI agents came from[^6][^7].

He is currently going through a data engineering training program that also helps him find potential clients. Through a recruiter from that program he has already found companies that are interested and that describe how they would like to use their data, but they have no expertise for it. The demand is already real - it just needs time to build. Together with the recruiter they are setting up calls and meetings with these companies to understand their data and their business problem, build a prototype, and charge for it. There is also another data engineer living in his town, a remote worker, who he is trying to partner with for exactly this, but that person is busy, so for now he is doing things on his own and the partnership is at an early stage[^6][^7].

He joined the community to get accountability and, as Valeriia understood it, to get this plan. He said Alexey's resources helped him a lot, LLM Zoomcamp in particular, and that was part of why he joined[^6].

## What he has already built

A Streamlit app where a user uploads a CSV or Excel file and asks questions about the data. It uses LangChain, does RAG for the local data, and has a multi-agent setup - one agent plots, one handles SQL, one does forecasting with a simple time series model. It handles arbitrary CSV files. The user supplies their own API key and picks the model. It runs in a Docker container on an EC2 instance. The app came out of the Matt Dancho program, and he did not write all of the forecasting part himself[^7].

He has also written a few smaller RAG agents on his own - for example one that downloads videos, pulls out the words, and answers questions about them, so he does not have to watch an hour of YouTube[^7].

There is a constraint on sharing: his other mentor asked him not to publish that code publicly. He can add individual people to a private GitHub repo, and he can freely share the apps he wrote himself along with descriptions and snippets. He and Valeriia agreed that sharing an interactive prototype with a specific ask works better for him than sharing raw code, both for the feedback he wants and for reviewers' time[^7].

## Intake

### Onboarding survey

Submitted 2026-06-10, questionnaire `onboarding-alex`, persona Alex (The Engineer transitioning to AI)[^1].

1. What is the one concrete outcome you want by the end of the next 6 to 8 weeks?
   "I'm currently partnership with other engineers to setup an AI consultancy targeted to small and medium size businesses (preferable non-high tech) in several industries that are looking to implement AI to automate their business process and produce revenue forecasting."
2. Which best describes that outcome? "Ship new project"
3. How many hours per week can you realistically commit, consistently? 10
4. Will your weekly time be steady, or drop sharply some weeks? "Steady"
5. What usually makes it hard to stay consistent or finish? "Scoping", "Getting started", "Momentum", "No feedback"
6. What kind of accountability helps you most? "Weekly check-ins", "Fixed deliverables", "Demo milestones", "Async Slack", "Partner pairing", "Build-in-public", "Reflections", "Checklists"
7. Do you already have a project or idea, even if rough? Describe it. "At the moment I'm trying to gather real problems from small/medium size business so I can develop agents that can help address those problems"
8. What stage is it at? "Idea only"
9. What result would make the next 6-8 weeks worthwhile? "I'd like to come up with a several prototype workflows that I can present as RAG agent demos for brick and mortar businesses, they can be modify to their needs."
10. What support from Alexey/community would be most useful now? "Scoping", "Architecture", "Eval plan", "Portfolio/README", "Career advice", "Avoid overengineering"
11. Anything else we should know before preparing your plan? "My current background is 20 years as a Linux and DevOps engineer. Currently I'm self-employed running a solo commercial maintenance Service business. I'm comfortable in Python, React, and other languages that I worked in the last 20 years. Last year I've been taking some courses to ramp up Pandas, SQL, Data Engineering. I took a mentorship to transition into Data Engineering roles. Currently I'm almost finishing an AI bootcamp with a different company (Matt Dancho). It's very good but alwas looking to explore other bootcamps to expand my AI knowledge. If the opportunity presents, wold like to get an AI /Data engineering related job to gain more experience, however I'd prefer to go the cunsultant/enterpreneur route."
12. If you build one project now, what should it prove to employers? "A clear vision of their current business model. Help them forecast their revenue. Help them identify where they can save time and money in their current business model. Help them address their cyber-security concerns."
13. Which AI area first? "RAG"
14. What SWE strengths should the plan build on? "RAG, agents, Workflows, multi-agent orchestration"
15. Project-first or foundations-first? "Alternate"
16. Biggest blocker? "Translating SWE to AI"

### Meeting notes

Call with Valeriia Kuka on 2026-07-13, 57 minutes. Mariano is in North Carolina, Valeriia in northern Spain[^7].

What came up beyond the background above:

- Mariano filled in the onboarding survey around 10 June but no plan was created for him. He assumed the plan would come after a call and was trying to book one with Valeriia or Alexey. He was not in a hurry, but he needs the plan now[^6][^7].
- Valeriia explained the sprint: six weeks starting 1 July, focused on accountability and community rather than more content - pair up, post progress in Slack, get feedback from peers. She noted the previous sprint had uneven participation, and the current one runs in a less controlled way[^7].
- Mariano asked directly for suggestions of Slack members to connect with for partnerships or project support, and for Alexey's feedback on his project. He mentioned Scott DeGeest's cyber security disclosure app as one that caught his eye, and said it would be great to see it with a web interface. Cyber security is a topic he is well placed for after years as a Linux engineer, and he sees it as one of the biggest concerns for medium-sized businesses[^7].
- He tried to book a call with Alexey and found no free slots for the rest of July or August. He was fine with that - it gives him a month and a half to develop his projects before a technical review[^7].

## Internal Recommendations

Alexey's working recommendation after reviewing the onboarding survey[^3][^4][^5]:

- There is already enough material to build a plan: the survey, the Google Doc, and Valeriia's call notes[^3].
- He wants to build a consultancy, so honestly he just needs to do a lot of different small projects[^3].
- It will be useful for him to look at as many projects as possible - who is doing what, what the idea is, and how the project is implemented at a fairly high level. Consultants need breadth rather than depth[^3].
- Partner with someone who is building something: find out as much as possible about their projects, help them, understand how exactly they are implemented, and build his own projects alongside that[^3].
- Sergey Sedler is the pairing to make. He has plenty of business ideas about where and how to apply this, but his coding is weaker. Sergey can be the main partner for the next sprint; with everyone else it is enough to have a call to find out what they do, which tools they use, and how their flow is set up[^4][^5].
- People to talk to: the member building the edtech startup that helps teachers, Amit, who is building a project about helping people make projects, Carlos, and Vancesca[^3].
- Also worth looking at the projects in the LLM Zoomcamp cohort running right now, and how they are implemented[^3].
- On skills: he already has an AI bootcamp behind him, so there is some knowledge there. Where something is missing, take the LLM Zoomcamp modules that cover the gap rather than the whole course[^3].
- Push hard on the number of projects. Each week, try to get into a new project and understand what is going on in it, and in parallel build his own. Around 10 to 20 hours per project, using AI as much as possible. The new AI Dev Tools Zoomcamp is useful for exactly that - it shows how to do this more efficiently[^3].

Open questions before sending:

- Alexey named Amit as one of the people to talk to, describing him as working on a project about helping people make projects. There is no member by that name in the plans, interviews, or 1x1 call notes, so the name needs confirming before an introduction is made. The edtech member is Salma Bouzid, who is co-founding an edtech startup with a professor.
- The current sprint started on 1 July and ends in mid-August, so a fresh six-week plan starting now runs past the end of it. Either compress the plan to fit the remaining sprint weeks or let it run into the next sprint - worth deciding before sending.

## Internal Action Items

- [ ] [Alexey] Confirm who "Amit" is before the introductions go out.
- [ ] [Alexey] Decide whether the plan is compressed to the remaining sprint weeks or runs past the sprint end.
- [ ] [Valeriia] Make the introduction to Sergey Sedler and set up the first pairing call.
- [ ] [Valeriia] Suggest the specific Slack members from the list above and make the introductions.
- [ ] [Valeriia] Check Alexey's August availability for a technical call on Mariano's projects.
- [ ] [Valeriia] Send the plan to Mariano and confirm he is joining the current sprint.

## Sources

[^1]: AI Shipping Labs onboarding response 13, questionnaire `onboarding-alex`, submitted 2026-06-10. Fetched through the API - see the AI Shipping Labs section in `process/process.md`.
[^2]: [AI Shipping Labs CRM record 36](https://aishippinglabs.com/studio/crm/36/), shared in [20260720_135334_AlexeyDTC_msg4777.md](../../../inbox/used/20260720_135334_AlexeyDTC_msg4777.md)
[^3]: [20260721_080250_AlexeyDTC_msg4791_transcript.txt](../../../inbox/used/20260721_080250_AlexeyDTC_msg4791_transcript.txt)
[^4]: [20260721_080250_AlexeyDTC_msg4792_transcript.txt](../../../inbox/used/20260721_080250_AlexeyDTC_msg4792_transcript.txt)
[^5]: [20260721_080250_AlexeyDTC_msg4793_transcript.txt](../../../inbox/used/20260721_080250_AlexeyDTC_msg4793_transcript.txt)
[^6]: [20260720_135335_AlexeyDTC_msg4778_transcript.txt](../../../inbox/used/20260720_135335_AlexeyDTC_msg4778_transcript.txt) - Valeriia's notes from her call with Mariano
[^7]: [Intake call notes and transcript, 2026-07-13](https://docs.google.com/document/d/1t3UAYwCgmui66B9hrNBOLappcLDIsP29OeNzT8HVZXs/edit?usp=sharing) - Valeriia Kuka and Mariano Beccaria
