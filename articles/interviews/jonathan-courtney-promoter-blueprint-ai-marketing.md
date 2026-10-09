---
title: "Jonathan Courtney on the Promoter Blueprint: AI Marketing with Claude Code"
created: 2026-10-09
updated: 2026-10-09
tags: [interview, podcast, marketing, claude-code, ai-tools, promotion, startup]
status: draft
---

# Jonathan Courtney on the Promoter Blueprint: AI Marketing with Claude Code

Jonathan Courtney is the founder of AJ&Smart and Facilitator.com, and host of the Unscheduled CEO Podcast. He joined Greg Isenberg on The Startup Ideas Podcast to talk about a problem he sees everywhere: founders who vibe-code products but then get zero customers, zero revenue, nothing[^1].

Jonathan uses AI tools about 20% as much as the typical builder audience. Most of his time goes into the CEO job he thinks people forget about: making money, getting users, increasing revenue. He brought a four-step framework called the Promoter Blueprint and showed how he uses Claude and Claude Code to execute each step[^1].

## The CEO's Real Job Is Promotion

Jonathan opens with a reality check. He asks Greg to name the CEO of Anthropic, of OpenAI, and the person behind Levels.io. Everyone knows these names. The reason is simple: at least 50% of their job is promoting their businesses[^1].

The builder community on X has a narrative that says "just build great things and people will come." Jonathan disagrees. You know the names of the people behind your favorite tools precisely because they are on every podcast, posting constantly, making themselves visible. Building without promoting is a "self-contained procrastination station"[^1].

He uses a restaurant analogy. Imagine you spend a year automating every machine. The food is perfect, the booking system is seamless, everything runs on its own. But you never told even one person the place exists. That restaurant will die, no matter how good the systems are[^1].

AI tools can become "procrastination machines" when founders optimize systems that have zero customers. The tools are great, but they need to serve the actual CEO job: getting users, making money, closing deals[^1].

## The Promoter Blueprint: Four Steps

Jonathan shared a visual framework he normally draws on paper for clients but vibe-coded into a web app for this podcast. The framework has four phases that form a loop[^1].

### Step 1: Traffic

You need to get attention from somewhere. There are only two categories:

- Organic: going on other people's podcasts, running events, networking, posting on social media, creating free content
- Paid: running ads on Meta, TikTok, YouTube, or other platforms

The point of traffic is moving people into your world. Without it, everything downstream starves. Jonathan compares traffic to oxygen for the business[^1].

### Step 2: Holding Pattern

Don't send traffic straight to a product page with a "buy now" button. Push people into a holding pattern where you warm them up over time[^1].

A holding pattern is:

- An email newsletter
- A podcast
- A YouTube channel
- Posts on X that keep people engaged

This is your daily and weekly content. You are not selling here. You are keeping people in your space, giving them value, staying top of mind[^1].

### Step 3: Selling Event

This is the step most people on X skip. They are okay at posting content and building followers, but they don't know how to move people from "I follow this person" to "I am paying this person money"[^1].

A selling event is a specific push from the holding pattern toward a purchase. Examples:

- A webinar or live demo of your product (companies like Superhuman do this constantly)
- A live workshop
- An email campaign (even a simple sequence of three or four emails)
- Retargeting: upload your email list to Facebook, create a lookalike audience, and run paid ads to similar people
- Direct outreach: look at recent signups, find enterprise email addresses, reach out personally

Jonathan got hit with a webinar campaign from Superhuman on the day of the recording. They wanted him to upgrade to Superhuman Teams. That is a selling event in action[^1].

### Step 4: Conversion (and Loop Back)

Some people convert. Most don't. The ones who don't go back into the holding pattern and stay there until the next selling event. The loop never stops[^1].

Jonathan gives concrete math from his own business. When an extra 5,000 people join his newsletter, he can mentally predict that roughly 200 will attend the next webinar, and roughly 12 will buy something. The machinery becomes predictable[^1].

## Real-World Examples of the Loop

Jonathan walks through how visible AI founders use this exact loop without most people noticing[^1].

Peter Levels: his pinned post on X is a long-form promotion for Photo AI. He posted the bump in sales that happened after that post. His "personal" content (cooking steaks in an air fryer, travel stories) is the holding pattern. The promotional posts are selling events[^1].

Dario Amodei (Anthropic CEO): when he appears at Davos getting interviewed by Bloomberg, that is not "for the good of humanity." He is moving enterprise buyers from awareness into Anthropic's world, where the outreach team can close deals. It is promotion[^1].

Greg Isenberg: his podcast is his holding pattern. It gives value and keeps people in his sphere. Traffic comes from guest appearances, X posts, and YouTube. Products like Idea Browser get promoted through that ecosystem[^1].

Jonathan himself uses the same loop in real time during this podcast. He appears on Greg's show (traffic), hopes listeners will search for him (holding pattern entry), and has a webinar campaign running that week (selling event). He expects between $250,000 and $500,000 from the campaign, based on 4,000 webinar signups and historical data from hundreds of previous workshops[^1].

## Inside Claude: The Podcast Preparation Workflow

Jonathan shows his screen and walks through exactly how he prepared for this podcast using Claude[^1].

### Recording a Brain Dump

He recorded a 15-minute voice memo on his phone, a brain dump of all the things he wanted to discuss. He dropped the audio file into a Claude project and had it create an "ADHD-friendly scannable document" he could glance at during the conversation. He uses Whisper Flow for voice input so all his prompts are spoken, not typed[^1].

### Building a Claude Project

He created a Claude project called something like "marketing assistant for Greg's podcast." Inside it, he ran several chats[^1]:

1. Dropped the audio transcript and had Claude turn it into structured notes
2. Had Claude research Greg Isenberg - his X account, YouTube channel, previous podcast episodes - and compiled a research file so future chats wouldn't need to redo that work
3. Asked Claude to identify which of Jonathan's previous episodes on this podcast performed best (views, comments) and where in his script he might lose the audience's attention
4. At the end of each chat, asked Claude to output a pasteable set of instructions he could add to the project's instructions field for the next chat. This way the project's context grew with each session

The initial instruction he gave Claude was: "I'm going to be a guest on Greg Eisenberg's Startup Ideas podcast today. You're going to be assisting me with putting together strong content angles, strong ideas, and strong strategy for delivering the most value to his audience"[^1].

### Transitioning from Claude to Claude Code

When the visual blueprint was at a "good enough" state inside Claude (a simple HTML version), Jonathan asked Claude to do two things[^1]:

1. Generate a CLAUDE.md file that would give Claude Code the full context of the project
2. Spit out the HTML file

He downloaded both files, created a project folder on his desktop, and opened it in Claude Code. There, he asked Claude Code to enter "ask user question" mode (plan mode) and grill him on the podcast ideas, which generated even more context. Then it built the Promoter Blueprint interactive page, pushed it to GitHub, and deployed it to Vercel. The interactive version includes a toggle that shows AI use cases under each step, animated stickers of Jonathan flying around, and an ice cream cursor[^1].

The whole process took about one hour, and most of it ran in the background while he did other work[^1].

## The Marketing Expert Brain: A Deeper Claude Setup

Jonathan shows a separate Claude project he calls his "AJ&Smart marketing expert brain." This is where he goes when he doesn't need Claude Code and is just focusing on marketing strategy[^1].

The project has extensive context files:

- Books he has written
- A 17,766-line document of other people's marketing emails that he compiled, analyzed, and had Claude distill into principles
- Accumulated project instructions refined over time

He demonstrates a live prompt during the episode. He tells Claude: "I just finished a podcast episode with Greg Eisenberg about how I use AI tools as a CEO. I want to create a simple, juicy downloadable or lead magnet that will bring people into my newsletter after this episode. It needs to be free and relevant to the episode. Give me three lead magnet examples"[^1].

He attaches the CLAUDE.md file from the podcast project to give context, without replacing the marketing project's own instructions. Claude suggests three options[^1]:

1. The Promoter Blueprint One-Pager - a PDF of the four-step framework
2. 50 Prompts for the Promoter CEO - a swipe file
3. The Cave Dweller Audit - a self-assessment that exposes whether you are building or promoting

Jonathan likes option three because it is provocative and directly connects to the episode's theme. From here, he would feed the podcast transcript into Claude for more context, generate the lead magnet content, then move to Claude Code to build the landing page. Done[^1].

This process used to take two to three days with his team. Now it takes half a day and produces custom campaigns that feel specific to each piece of content[^1].

## The Webinar Design Trick

A friend running a company called Pipdex told Jonathan to use the "ask user question" skill in Claude Code for designing webinars. Jonathan trained a Claude project on his preferred webinar structure and has it run a 30-minute question-and-answer session where Claude grills him on the webinar content. The output from that session goes straight into the webinar design. He does this in Claude Code because it feels faster - just hitting 1, 2, 3 on the keyboard to answer[^1].

## Warnings and Mindset

### Don't Optimize the Wrong Thing

Jonathan's co-founder Laura spent three days building a custom proposal builder. Then she asked Claude if there was an off-the-shelf solution. Claude immediately gave her one they could have used from day one. The lesson: don't build everything custom. Ask first[^1].

### Abundance Over Efficiency

Jonathan doesn't think efficiency is the right play in 2026. He thinks the move is scaling up. If you have a small team, keep them. Now each person has triple the output with AI tools. Run five campaigns a month instead of one. Create more variations of Facebook ads instead of updating them every six weeks[^1].

Claude Code lets you play big. It feels like cloning yourself. The challenge is making sure the clones are working on things that actually hit your goals of revenue or users[^1].

### Skip the Over-Preparation

The biggest sign that an entrepreneur will move slowly is too much preparation. Jonathan didn't do a test project with Claude Code. He jumped straight into a real campaign page. He learned about context window limits by hitting them, not by reading about them. His first lesson: do projects in small chunks instead of one massive mega-prompt, because the context window compresses and forgets things[^1].

### Start Simple with Claude Code

Greg adds that new users often set up a thousand Claude skills before building a single thing. The right approach: figure out your team (even if it is a team of one), identify the jobs to be done, start using the tools on real work, and add one skill at a time as the need becomes clear[^1].

## Accept the Promoter Role

Jonathan's closing advice: accept that your role as CEO is to be a promoter. Don't be embarrassed about it. If promoting is not something you want to do, find someone in the company who will take that role. It is literally the job. The business won't work without that person[^1].

## Sources

[^1]: [How I use AI Marketing and Claude Code to make $$ - The Startup Ideas Podcast](https://open.spotify.com/episode/0CxJQyFK1OH7GXNBpUh5ZS)
[^2]: [20261009_071430_AlexeyDTC_msg5018.md](../../inbox/used/20261009_071430_AlexeyDTC_msg5018.md)
