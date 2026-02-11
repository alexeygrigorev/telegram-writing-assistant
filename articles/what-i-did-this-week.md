---
title: "What I Did This Week"
created: 2026-02-11
updated: 2026-02-11
tags: [weekly, updates]
status: draft
---

# What I Did This Week

Weekly updates on work in progress. This article serves as a working draft - content is removed when published elsewhere.

## 2026-W06 (February 6-12, 2026)

### Tuesday, February 10, 2026

**2026-02-10 22:11:43 UTC**

Thinking about how to organize marketing and how to find the right target audience - people who have money and can pay. I'm not sure Data Talks Club is the right place because our courses are free there and many people are from India, Nigeria - they're not in a position to pay. We need to find where to look for target audiences who can pay. Of course there are social networks where we can find them, but maybe there are other places. CEO networking comes to mind. Also AI optimization - we should probably look in that direction too.

### Wednesday, February 11, 2026

**2026-02-11 04:29:43 UTC**

There are nuances because I don't want to use a database. I want everything to be generated from GitHub Pages so we don't need to pay for Postgres. If everything can be generated statistically, it will be free. Although for the course we probably need a database. Well, in general yes, but this is a somewhat specific case. For Notes it would be more interesting. Or in principle we can do it with a database and then we'll redo it a bit differently for GitHub Pages.

**2026-02-11 04:30:04 UTC**

Look, end-to-end is when there's a front-end, back-end and database, and it all gets deployed somewhere. That's end-to-end. We basically have that and deployment on GitHub Pages. We just don't have a back-end, everything is statically generated through Jekyll. We have files in Git, and from them this static generator, this Jekyll, generates HTML. The HTML is already deployed to GitHub Pages, so we basically don't have a back-end as such, just the generated static HTML pages. This is really cool for blog-type sites because there's no need for any dynamics, no need to load anything from databases, and so it can be done for free.

**2026-02-11 04:33:39 UTC - Task Management App Idea**

The problem with Grace right now is that she has several To Do lists - she has a To Do list which is a Spreadsheet in Google and Trello. Then in Trello she has tasks within each card. So for her to see what she needs to do today, she needs to go through all these cards and see which tasks aren't done. Plus... It's noisy here.

The dogs and kids threw me off my train of thought. Anyway, the idea is to make something that combines Trello and the ToDo List we have. But not just simple Trello... Let me try to formulate this. I've had this idea for quite a while, just haven't gotten around to doing it.

So the way it works in Trello - we have templates in Trello. From these templates we create cards, and these cards already have subtasks. The idea is to have two types. First, these cards (well we can call them something else). And second, from these cards, a list of specific tasks. Tasks can be from these cards and can be ad hoc tasks. Ad hoc tasks are what I usually... She has some regular tasks. There are tasks that I just ask her to do in Telegram. She has regular tasks, like once a week she needs to do a Mailchimp dump. Or check something else. Or I write to her, like you need to contact this person about the podcast. So there are regular ones and there are ad hoc tasks that don't belong to any card but still need to be done. So she currently has two sources of tasks.

Besides Grace, we could also have tasks for you, for me, just to have an overview of everything we're doing.

I don't know if this would be reinventing the wheel, but I looked at things like Manda and Asana, I didn't find what I needed right away. And Jira isn't quite right either. And Trello, well Trello's main problem is that Grace can't put ad hoc tasks in there, and Grace needs to go through all the cards to understand what tasks are for today.

**2026-02-11 04:33:39 UTC (continued)**

Here's how it works now. I have... We have a group chat, but you're not in it. There's me, Grace and the bot. I have a slash command, slash-todo, where I write like I need to contact this person. And what happens now? It automatically gets added to the todo list. You've probably seen it. It's a Google Spreadsheet. There's a date, a comment, something else. And when Grace completes it, she just changes the status from todo to done and it gets moved to another list, to another spreadsheet. How to make this show in Trello, I don't know. I don't even know what this could look like. I guess Trello has some API. But for these ad hoc tasks, I don't know... when I write something to her in chat, instead of her duplicating and entering the task herself, for the task to automatically be placed where it needs to go. Then there's another integration. The first is todo in Telegram. The second is when some email comes to me and I just forward it to Grace and add another email in copy, and that other email also has automation that adds a task to the todo list about what needs to be done... Need to look at this email and react to what's inside. I also don't know how to automatically push this into Trello.

**2026-02-11 04:33:39 UTC (continued)**

Plus Trello cards, meaning you'd have to create a card for every task. That's a bit overkill. I'd like it to just be in a table format, really simple. You check a box and the task is done. Plus maybe write some comment about the task. Like how our table works now. There's a date, a task, some comment, and a status. So if I ask Grace, I send her a Loom video and ask her to turn it into a process document, she usually writes the link to the process document in the comment when she finishes, so I can then go look and check that document and give her some comments. So table format is somehow more convenient. Anyway, I don't know how to implement this in Trello. Maybe I wasn't looking in the right place. And the main thing is that in Trello, if we have tasks, they end up inside cards. So there's no way to pull these tasks out of the cards and show everything we have in these cards.

**2026-02-11 04:33:39 UTC (continued)**

So I have some thoughts, sorry, again about the todo list. I just have time to talk on the phone right now while the kid is playing on the playground. And while I have the thought, I'll tell you now. You can put this in a Google document or something so I don't forget about it later.

**2026-02-11 04:33:39 UTC (continued)**

So here's the idea. When we create some Trello template, when we create a card from the template, we have some main event there. Usually this is tied to a specific date. And we have some necessary actions that we need to do in a week, in two weeks, or a week after. So we have what you call an anchor date, and from that we can make deadlines for all tasks. I don't know, some announcements two weeks in advance, so that task has a deadline that goes into the general list. Right now we're not dealing with this. Grace spends a lot of time on this. I saw from her reports that she has to go through all the cards and pick out these tasks. So we could have the ability for each of these... first to make plays. Plays can be a newsletter, a template, some mailing template, something else. Then in each play there are some things you do, some things she does. And you can already assign people in the template. Then we make a clone from the template, put a date in that play date, make some task there. And it turns out to be such an anchor date from which all deadlines are calculated. So if we have a task that's two weeks in advance, a week before, or a week after, then all the other tasks can somehow be extrapolated, calculated when they need to be done. That's it. I don't know if you get what I mean or not.

So we'll have templates, we have big tasks that are currently cards in Trello, which are currently being processed in some state, we have tasks from these cards that show up in the general list. Plus on top of that there are ad hoc tasks that I set via Telegram, plus there are tasks that are done regularly on some schedule, say once a week on Wednesday. That's another window where such tasks can be made so they automatically get added to the todo list. It seems to me if it's all in one place, visible immediately, it will be much easier for Grace.

**2026-02-11 04:33:39 UTC (continued)**

Yeah, if you put everything I told you in a document, first I don't know, put it all in a Google doc, then from the Google doc you can formalize it with GPT in about an hour or so, then you'll have a big prompt that describes the whole specification well and in detail, then in a couple of prompts in Lovable, in principle, you can make a ready-made mock that does all this. And then further, well, like in the course, we can make it directly. I can't say it's a super simple task, like Snake. Especially if you make something beautiful there. But plus it's that I think it will really bring real benefit. And maybe someone else will be interested in such a tool too. We can show it - look how we organize work in this Talks Club. Maybe you'll want the same.

**2026-02-11 04:33:39 UTC (continued)**

Well, if anything, you can naturally involve me along the way to give feedback. I'll only be for it.

**2026-02-11 07:47:54 UTC**

In the message I was talking about this thing for the todo list, I have another problem - I forget about invoices. That is, we made some agreement with someone for something, and I forget about needing to make an invoice. I forget to send it, and then when they pay it's easier to check later, but specifically with preparing and sending the invoice, I somehow forget. We can think about how to do this generally in the todo list thing, or make something separate for invoices, or maybe put it in the todo list thing. Right now we adapt processes for this so we don't forget, but maybe we can come up with some software solution using Airtable or write some code so we don't forget about invoices, some kind of reminder system or something.

**2026-02-11 09:33:51 UTC - Weekly Updates Article**

I periodically write once a week, tell some messages about what I did this week. Let's make a separate article for this about what I did this week. And we'll throw there, say, the week number and everything I talked about now. Naturally to find out what the week number is, we need to run some script, say in Python, which shows what the week number is today and based on that add information there. So we can put everything in one article and then we'll just remove from this article what we published. And it will be such a working draft where we constantly add and remove. So in this article describe the rule. That is, to add this article, you need to find out what the week number is. To do this, run this Python script. And in the process.md file, tell us that if I tell something about what I did this week, then write to this article, and in that article there are more detailed instructions. Over time we'll form some guidelines on how to write.

**2026-02-11 09:35:15 UTC - Style Guide Feedback**

Plus I have feedback. I noticed that in the last message we have bold formatting. I don't like bold formatting, and we literally have guidelines where I ask not to use it. For some reason these guidelines weren't used, so we need to now review how we use these style guidelines, where they are at all. Let's put them in a separate file, make a styling guide that we'll put in root, in the root of the repository. And process.md must definitely read this styling guide and at the end, as the last step, make sure that, first, all the pictures are correct, and second, that all files conform to this styling guide. The simplest way to check this is to just grep and see if there are double asterisks or not. But more complex things require reading. I also want to make a styling guide about how I write. I want the text we generate to eventually look like I wrote it. Right now it's not like that. So let's create a Style and Guide where, in addition to such things about formatting, we'll also have a stylistic description of how to write text. We'll keep that there too.

**2026-02-11 09:41:31 UTC - Course Recording Progress**

Regarding what I did this week - this week I'm fully focused at least until today - today is Wednesday - on recording course videos. I've basically finished the main part but haven't reached frameworks yet. I'm showing how I'm re-recording all the videos. I stopped in more detail on how to write agents. Before I would go through it superficially and say here it is but look at the implementation here in the Toyaikit library. Now I decided to describe this in great detail because I think it's important. People use LangChain, people use other libraries and often don't understand what's happening inside. I saw a lot of positive feedback on Twitter about this. People really say they didn't understand how LangChain works until they sat down and figured it out and wrote this agentic tool call loop themselves. So I decided to combine many agentic frameworks into one class called agent, and how to launch all this. So a mini framework turned out. It's naturally not very flexible but as an illustration of what's happening inside these frameworks, I think it turned out very well.

And then from this mini framework we made together, I already say - here's Toyaikit. Toyaikit is the framework I wrote based on workshops and courses I did in the past. With Toyaikit I can achieve... well, how to say it easiest... it's the easiest transition to agent frameworks. That is, first we have super low level, we use pure OpenAI requests, then Toyaikit is a lightweight... I rewrote TOEI and added it as a library. And some concepts I show in Toyaikit before we come to serious frameworks. But I say that Toyaikit is purely for education, purely for debugging, for learning, for prototyping - in production it cannot be used under any circumstances. In production we use OpenAI or any other framework which I show further.

What I haven't managed to do yet... Oh let me tell you what I covered a little bit. We talked about agentic RAG. There's regular RAG, and here it becomes agentic - we give the agent the ability to choose what queries to make. And then we completely move away from the concept of RAG, from agentic RAG we come to agentic search. In Agentic Search, the same thing - the agent sees some information, sees a snippet, sees a title and already decides what from this is really worth looking at, where the answer will be, and already requests the full page. So we move away from RAG and come to agent-like, to this agentic search. And I finished there.

Now I'm recording a lecture about OpenAI SDK. And further I want to show how to use other providers, how to do tool calling there, like in Anthropic and so on. And also, after that I'll show other frameworks. Other frameworks like LangChain, LangGraph, openai-agents-sdk, and others. So I haven't recorded that yet, and that's what I plan to do this week.

**2026-02-11 09:42:12 UTC - Content Preparation for Monday Event**

And also this week is background work for me. I'm thinking about the material we'll be discussing on Monday - this will be our event about AI engineer roles and how I see them. How I prepare material - I just throw all my thoughts here in Telegram, in the system, do a brain dump, and it gets structured that way. I prepare content very conveniently. I have breaks, say I'm tired of recording course videos, or I'm going somewhere, while I'm driving, I have thoughts about this project, the event. I just take out my phone, dictate a voice message to the agent, then it all gets structured and from my brain dump some structured information is made which I can use further to prepare for the event. Based on this I make a transcript for myself which I'll use as the basis for the conversation on Monday.

## Sources

[^1]: [20260210_221143_AlexeyDTC_msg1344_transcript.txt](../inbox/raw/20260210_221143_AlexeyDTC_msg1344_transcript.txt)
[^2]: [20260211_042943_AlexeyDTC_msg1348_transcript.txt](../inbox/raw/20260211_042943_AlexeyDTC_msg1348_transcript.txt)
[^3]: [20260211_043004_AlexeyDTC_msg1349_transcript.txt](../inbox/raw/20260211_043004_AlexeyDTC_msg1349_transcript.txt)
[^4]: [20260211_043339_AlexeyDTC_msg1351_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1351_transcript.txt)
[^5]: [20260211_043339_AlexeyDTC_msg1352_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1352_transcript.txt)
[^6]: [20260211_043339_AlexeyDTC_msg1353_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1353_transcript.txt)
[^7]: [20260211_043339_AlexeyDTC_msg1355_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1355_transcript.txt)
[^8]: [20260211_043339_AlexeyDTC_msg1356_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1356_transcript.txt)
[^9]: [20260211_043339_AlexeyDTC_msg1359_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1359_transcript.txt)
[^10]: [20260211_043339_AlexeyDTC_msg1360_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1360_transcript.txt)
[^11]: [20260211_043339_AlexeyDTC_msg1361_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1361_transcript.txt)
[^12]: [20260211_043339_AlexeyDTC_msg1363_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1363_transcript.txt)
[^13]: [20260211_043339_AlexeyDTC_msg1364_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1364_transcript.txt)
[^14]: [20260211_043339_AlexeyDTC_msg1365_transcript.txt](../inbox/raw/20260211_043339_AlexeyDTC_msg1365_transcript.txt)
[^15]: [20260211_074754_AlexeyDTC_msg1372_transcript.txt](../inbox/raw/20260211_074754_AlexeyDTC_msg1372_transcript.txt)
[^16]: [20260211_093351_AlexeyDTC_msg1375_transcript.txt](../inbox/raw/20260211_093351_AlexeyDTC_msg1375_transcript.txt)
[^17]: [20260211_093515_AlexeyDTC_msg1376_transcript.txt](../inbox/raw/20260211_093515_AlexeyDTC_msg1376_transcript.txt)
[^18]: [20260211_094131_AlexeyDTC_msg1377_transcript.txt](../inbox/raw/20260211_094131_AlexeyDTC_msg1377_transcript.txt)
[^19]: [20260211_094212_AlexeyDTC_msg1378_transcript.txt](../inbox/raw/20260211_094212_AlexeyDTC_msg1378_transcript.txt)
