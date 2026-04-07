---
title: "How We Built AI Shipping Labs"
created: 2026-04-07
updated: 2026-04-07
tags: [community, ai-shipping-labs, building, v0, agents, newsletter]
status: draft
---

# How We Built AI Shipping Labs

This is the story of how the AI Shipping Labs platform was built - from the first version created with V0 to the agent-built Django platform running today.

## Starting simple

You do not need to overthink things when launching something. When I started DataTalks.Club, the website was just a form for entering your email, and that was it - nothing else. I wanted to check whether people would sign up. They did, and that became the simplest possible MVP. You can still see what it looked like on the [Web Archive](https://web.archive.org/web/20201101141103/https://www.datatalks.club/) - though the email form is not visible on mobile for some reason[^1].

The same principle applies here. If you want to launch something, you do not need to build something complicated. The first version of the AI Shipping Labs website has been running for over a month, people can buy subscriptions and pay - and it works. That is the minimum you need to get started[^2].

Now with AI agents, you can delegate even more of the work. What I am building now in Django is definitely not a simple MVP, and in some sense it contradicts all the canons of product development. But since agents do most of the work and Valeriia and I are the only developers, for me it is very interesting to learn how to manage a team of agents. In practice though, you can often just define an MVP and let agents build it for you[^3].

## How Valeriia built the first version

The first working version of [aishippinglabs.com](https://aishippinglabs.com) was built by Valeriia[^4].

It started with the idea to create a paid community. I already had DataTalks.Club as a free community with many free courses and participants. I also had a paid course with engaged students who were willing to pay and interested in AI engineering. The idea was to bring these people into a separate space and continue the conversation after the course ends - and also attract people who did not take the course but want to grow in AI engineering. Typically these are people who want to find a new job or get a promotion[^4].

### Planning activities and tiers

We started thinking about what activities to offer and what value the community would provide. We looked at existing AI engineering communities and potential competitors to see what they were doing. We also thought about what our target audience needs[^5].

Valeriia made a list of potential activities using ChatGPT and her own ideas. Based on that list, she designed the subscription tiers - what types of subscriptions we could offer and what each tier includes. This information lived in a separate document[^5].

We discussed the activity list and tier descriptions together and came to a final version of what each tier would contain, with brief descriptions for each activity. It was not yet the final version of how the descriptions look now, but we decided it was enough to build a web interface. The plan was to launch it locally and then use the visual interface to edit and refine the content[^6].

### Building with V0

Valeriia went to [V0](https://v0.app/) - an AI tool from Vercel for creating interfaces and applications[^7]. You can put V0 alongside other tools like Lovable and Replit that let you develop applications from an interface, connect to your GitHub, and deploy on their infrastructure. Vercel originally became popular because its creators are the people behind Next.js, a React-based framework for web applications. Many developers who write Next.js use Vercel for deployment[^8].

V0 was not new to Valeriia - she had used it before and liked it. When you ask V0 to build something, it typically generates a Next.js site. She had worked with Next.js at a previous company, so the framework was familiar[^8].

The advantage of V0 is that, like other platforms, it offers free credits. But compared to other platforms, what V0 creates can already be a working application from a single prompt. At the time she was doing this, in February 2026, one prompt did not consume as many credits as you might expect. She also tried Replit for other sites and got decent results from two or three prompts. Lovable, on the other hand, would sometimes build only one page instead of the whole site and leave the rest empty. The best experience overall was with V0[^9].

The prompt she gave V0 was a brief instruction with descriptions of all the tiers - tier names, purposes, what each tier includes, pricing, and positioning for whom each tier is aimed[^10]. Something like: "Create a landing page for a paid, invite-oriented technical community focused on AI, data, and engineering practitioners" followed by the full tier descriptions[^11].

She started by adding my bio and testimonials from the paid course - V0 itself suggested adding testimonials. It also proposed adding an application form or waitlist. Since we planned to connect the community launch to the Alexey on Data newsletter and launch through it, we added a newsletter signup form instead[^12].

What is great about V0 is that you can connect it to your GitHub or just download the generated code. Valeriia connected her GitHub, downloaded the code locally, and started working with it through Cursor[^12].

### Blog, resources, and project ideas

She organized the site content into sections: Project Ideas, Event Recordings, Curated Links, and Blog[^13].

For the blog, all the newsletters from Alexey on Data went in. Since Substack does not have its own API and does not allow adding content programmatically, she used scripts from the DataTalks.Club GitHub repository. These are Python scripts that use GitHub Actions to download text and images from a Google document by its link and convert them into a Markdown file. Valeriia copied the newsletter content manually from Substack into separate Google Docs, then ran the script for each document. The script handled the bulk of the work - copying over all the blog posts to the site. It was not perfect and required some manual editing afterward, but the heavy lifting of copy-pasting was done by the script[^13].

For the Curated Links section, she took the list of tools and resources that I share and find useful. She asked Cursor to build a grid interface where each element is one recommended resource, with filtering by tools, models, courses, and other[^14].

The Event Recordings section gathered recordings of events. Project Ideas came from several sources: from the Demo Days of the first cohort of AI Engineering Buildcamp where there were five capstone projects from graduates, from LinkedIn and Twitter posts where people mention me and their projects, and from the newsletter editorials where I share a project I built and offer it as a pet project idea[^14].

### Stripe, AI Engineer resources, and hosting

After the initial version of the site was ready, I went to Stripe and set up the payment integration. Now people can buy a subscription, and we get a notification when someone does[^15].

Valeriia also published articles based on my research into the AI Engineer role - what job descriptions look like, what requirements exist, what people say about it, how interviews work. Based on this research, she built an AI Engineer Learning Path page - a visual interface showing what skills are needed, what you need to know within each skill, what tools to use, and what portfolio projects you can build, with a link to the Project Ideas section. She also added an AI Engineer Interview Questions page. These pages will keep growing and updating as I continue collecting data, and some parts will likely become exclusive to community members[^15].

The first version of the site was hosted on GitHub Pages. Then we moved it to AWS, served through S3. The Next.js site that Valeriia built currently deploys to AWS and is served from S3. When the Django platform is ready, we will just switch the domains[^15][^16].

## How I built the new platform

Now that you know how the first version was built, I also wanted to share how I built the new platform behind it. It was built almost entirely by AI agents working autonomously.

I recently wrote about [how I use a team of AI agents for software development](https://alexeyondata.substack.com/p/i-built-an-ai-agent-team-for-software) - with an orchestrator directing a Product Manager, Software Engineer, Tester, and On-Call Engineer through a structured pipeline. That is exactly how I built this platform.

The original plan was to use something existing. We evaluated several platforms:

- Substack - natural fit for a paid newsletter, but did not support the tier plans we needed
- Ghost - works perfectly for articles behind a paywall, but falls short for course management, event scheduling, and community features
- Maven - great for courses, but no API for programmatic student registration and missing other features we needed

No single platform could handle everything we needed. So I decided to build one using the agent team approach.

## From requirements to a working platform

The requirements gathering happened through my Telegram bot. I dictated features into the bot. Valeriia discussed hers in ChatGPT, and we added those too (the bot could easily access them).

Then I told Claude Code to turn that raw requirements list into specifications. It created a "specification" folder with 15 files. I reviewed them, gave feedback, and then said: now turn these specs into tasks on GitHub Issues.

The first attempt at task decomposition was not great - too granular, no acceptance criteria. I iterated on the format until each task had a clear scope, acceptance criteria with checkboxes, and a "human" tag for anything that needed manual verification. I chose Django because I've known it since 2010 and could step in if something went wrong.

<!-- illustration: screenshot of a GitHub issue showing the task format with scope, acceptance criteria checkboxes, and human tag -->

Setting everything up took one evening. Then the agents worked overnight. In the morning, 41 out of 46 tasks were done. By the 12-hour mark, it was 51 out of 56 - the backlog had grown as the Product Manager decomposed additional work.

<img src="../../assets/images/community-platform-implementation/claude-code-12-hours-progress.jpg" alt="Claude Code task list showing 56 tasks with 51 completed after 12 hours">

When I logged into the platform for the first time, the key integrations just worked:

- Gmail and GitHub OAuth
- Zoom integration
- Slack integration 
- Stripe payments

<img src="../../assets/images/community-platform-implementation/user-dashboard.jpg" alt="AI Shipping Labs dashboard showing Continue Learning, Active Polls, Upcoming Events">

## Not a one-shot 

AI helped. A lot. But it was not "type a prompt and get a platform". All the integrations needed API keys and configuration that only I could do, and each one required testing manually - does the Zoom meeting actually get created, does the Stripe payment go through, does the Slack invite arrive.

The agents also made decisions I did not agree with:

- They put too many things in the Django admin panel instead of building a proper interface
- Some features had no clear path to find them - there was simply no place in the UI to access them
- Other things were missing entirely, like a user dashboard, which I had to explicitly ask them to build

That was the first 24 hours. But later it took multiple weeks of polishing - understanding where things should be, fixing UX. The system is available now at [prod.aishippinglabs.com](https://prod.aishippinglabs.com). I am still working on making it more production ready - right now the [main website](https://aishippinglabs.com) still runs on the Next.js version that Valeriia built, but I am actively working on it and as soon as it is ready, it will be replaced.

A project like this would take six months to a year to build the traditional way. We got a working platform in weeks. It is not magic - it is project management, the same skills you need to manage a team of human engineers, applied to AI agents.

For me the important part is that I am learning a lot while doing all this. Going from a vague idea to a working product using AI agents is exactly the kind of thing we will be exploring together in AI Shipping Labs. If any of this resonates with you, check out aishippinglabs.com.

## Sources

[^1]: [20260407_115215_AlexeyDTC_msg3255.md](../../inbox/used/20260407_115215_AlexeyDTC_msg3255.md), [20260407_115117_AlexeyDTC_msg3253_transcript.txt](../../inbox/used/20260407_115117_AlexeyDTC_msg3253_transcript.txt)
[^2]: [20260407_114738_AlexeyDTC_msg3248_transcript.txt](../../inbox/used/20260407_114738_AlexeyDTC_msg3248_transcript.txt)
[^3]: [20260407_115117_AlexeyDTC_msg3253_transcript.txt](../../inbox/used/20260407_115117_AlexeyDTC_msg3253_transcript.txt)
[^4]: [20260407_122730_valeriia_kuka_msg3257_transcript.txt](../../inbox/used/20260407_122730_valeriia_kuka_msg3257_transcript.txt)
[^5]: [20260407_122740_valeriia_kuka_msg3259_transcript.txt](../../inbox/used/20260407_122740_valeriia_kuka_msg3259_transcript.txt)
[^6]: [20260407_122929_valeriia_kuka_msg3261_transcript.txt](../../inbox/used/20260407_122929_valeriia_kuka_msg3261_transcript.txt)
[^7]: [20260407_123118_valeriia_kuka_msg3263_transcript.txt](../../inbox/used/20260407_123118_valeriia_kuka_msg3263_transcript.txt)
[^8]: [20260407_123225_valeriia_kuka_msg3267_transcript.txt](../../inbox/used/20260407_123225_valeriia_kuka_msg3267_transcript.txt)
[^9]: [20260407_123248_valeriia_kuka_msg3269_transcript.txt](../../inbox/used/20260407_123248_valeriia_kuka_msg3269_transcript.txt)
[^10]: [20260407_123353_valeriia_kuka_msg3271_transcript.txt](../../inbox/used/20260407_123353_valeriia_kuka_msg3271_transcript.txt)
[^11]: [20260407_123406_valeriia_kuka_msg3273.md](../../inbox/used/20260407_123406_valeriia_kuka_msg3273.md)
[^12]: [20260407_124022_valeriia_kuka_msg3277_transcript.txt](../../inbox/used/20260407_124022_valeriia_kuka_msg3277_transcript.txt)
[^13]: [20260407_124700_valeriia_kuka_msg3281_transcript.txt](../../inbox/used/20260407_124700_valeriia_kuka_msg3281_transcript.txt)
[^14]: [20260407_125110_valeriia_kuka_msg3283_transcript.txt](../../inbox/used/20260407_125110_valeriia_kuka_msg3283_transcript.txt)
[^15]: [20260407_125614_valeriia_kuka_msg3287_transcript.txt](../../inbox/used/20260407_125614_valeriia_kuka_msg3287_transcript.txt)
[^16]: [20260407_130121_valeriia_kuka_msg3289_transcript.txt](../../inbox/used/20260407_130121_valeriia_kuka_msg3289_transcript.txt), [20260407_132758_AlexeyDTC_msg3297_transcript.txt](../../inbox/used/20260407_132758_AlexeyDTC_msg3297_transcript.txt)
