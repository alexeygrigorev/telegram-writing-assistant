---
title: "AI Tools Assessment: A Productized Service Business Model"
created: 2026-10-09
updated: 2026-10-09
tags: [interview, ai-business, productized-service]
status: draft
---

# AI Tools Assessment: A Productized Service Business Model

https://youtu.be/dhbcVxYhWaQ

Small business owners know they should use AI, but most don't know where to start. They're too busy running their business to learn about new tools. They're afraid their competitors are getting ahead of them. So they bury their heads in the sand and never take the first step.

Corey Ganim built a productized service around that gap - the AI Tools Assessment. The model works like a doctor writing a prescription. You meet with a business owner, identify their biggest time drains, and prescribe off-the-shelf AI tools that fix them. You charge $999 for the assessment, and about half of clients want you to implement the solutions afterward - which opens the door to thousands of dollars in follow-up work.[^1]

You don't need to know how to code. You don't need to build anything. You don't need to implement anything. You're prescribing tools that already exist - many of them are just SaaS products the business owner didn't know about. A lot of what gets recommended are Claude skills, but even those take 20 to 30 minutes to build for a specific workflow.

This article covers the full playbook: the assessment offer and its four delivery phases, six upsell services that turn a $999 engagement into $3K-$10K+ in lifetime value, seven ways to find clients with no audience and no capital, and the AI concierge retainer that generates $1,000-per-hour consulting revenue.

## The Assessment Offer

The AI Tools Assessment is a structured service with a clear promise. You sit down with a small business owner for 45 minutes, run a structured interview to uncover bottlenecks, and then prescribe three to seven off-the-shelf AI tools they can implement immediately to reclaim 5 to 10 hours per week.

The guarantee: if you can't find at least 5 hours per week in opportunity where AI can help, the client gets 100% of their money back. The only thing they risk is 45 minutes of their time. The average client saves about 7 hours per week.

The price is $999. That's just the foot in the door. The lifetime value of an assessment client runs $3K to $10K or more, depending on upsells. Corey sold about 15 of these assessments in the first part of 2026, and 50% of clients wanted implementation help afterward.

Maybe 5% of companies use any AI tool other than ChatGPT. There are millions of businesses in the US alone. Even if everyone watching the episode went and implemented this model, there would still be opportunity left over.

## Target Market

The sweet spot is small business owners with:

- 2 to 20 employees
- $500K to $5M per year in revenue

These owners are working 40, 50, 60 hours a week. They don't have time to learn AI. They see the headlines, worry that their competitors are getting ahead, and then do nothing because they don't know where to start.

## The Four Phases

Delivering the assessment has four phases: a discovery call, AI-powered analysis, report generation, and a review call with the client.

<!-- illustration: four-phase workflow diagram showing discovery call → AI analysis → report → review call -->

### Discovery Call

Phase one is a Zoom or Google Meet call with the client. Record the call with an AI note-taker - Fathom, Otter, Fireflies, or any similar tool. You need the transcript for phase two.

The only goal on this call is to ask questions and pull out problems. Don't pitch anything. Don't prescribe tools. Even when you recognize the exact tool they need, bite your tongue. The first call is only for probing.

Questions to ask:

- Walk me through your day yesterday.
- What do you tend to do in a typical business day?
- What tasks in your business do you dread doing?
- Where does your work pile up?
- What have you tried to automate in the past and failed?
- If you could wave a magic wand and delete any process in your business, what would it be?

That last question is the best one. A surprising number of business owners say email. "If I never had to answer an email again, I'd be a different person." That's solvable to a degree with AI.

Most business owners have many of the same problems. Corey says he has to bite his tongue on every single call because the solution is obvious to him right away. But prescribing on the first call defeats the purpose. You need the full picture before you start matching tools to problems.

### AI Analysis

Phase two uses AI to analyze the call transcript. Take the transcript from your AI note-taker and feed it to Claude.

Corey built a Claude skill that takes the transcript and runs deep research to pull out pain points, then searches the internet for the exact tools that can fix them. You can start with a simpler prompt:

```
I just had a call with a business owner. Attached is the transcript
of our conversation. Go on the internet and research off-the-shelf
SaaS or AI tools that can fix the pain points mentioned in this
transcript.
```

Claude catches patterns you might miss. It pulls out pain points you didn't think were solvable and finds tools to address them.

Don't take Claude's output at face value. Review every recommendation. Claude might prescribe Salesforce for a four-person landscaping business - you need to make that judgment call and swap in a CRM that fits a small business.

For the first two or three assessments, the AI analysis gets you 60 to 70% of the way there. You'll need to make judgment calls and substitutions on the tool recommendations. Once you've done four or five assessments and fed past transcripts and finished reports back into the skill, it gets much more accurate. At that point, the output is often copy-paste ready.

Two good resources for researching AI tools:

- futurepedia.io - a large AI tool directory (acquired by HubSpot), with tools tagged by industry
- theresanaiforthat.com - another large directory where you can sort tools by industry

### The Report

Phase three is the client-facing deliverable. This is what you send to the client and review with them in phase four.

Corey originally built reports in Gamma (gamma.app), then switched to Claude Design. The template is available for download at audittemplate.ai. The report has been iterated 12 times, each time asking: what can we delete, what can we simplify, what can we rearrange to make the ROI obvious and the implementation easy?

The principle behind every iteration: a confused mind doesn't implement. A confused mind doesn't get the ROI. A confused mind doesn't buy upsells. Everything in the report aims for maximum simplicity.

The report sections:

The title slide includes the client name, date, business type, and primary focus.

The executive summary shows the main one or two pain points, the outcome the client can expect from implementing the tools, and the hours they can reclaim each week. That number is usually in the 5 to 10 range, with 7 as the average. The executive summary also lists the primary focus of the report. Every AI tool or implementation pulls one of three levers:

- Effectiveness - makes you more money
- Efficiency - saves you time
- Quality - increases the quality of your product or service

You look at the tools you're prescribing, determine which lever most of them pull, and list that as the primary focus. The client can look at this one slide and know exactly what they're getting.

The effort versus impact matrix is a standard framework with four quadrants. The report focuses on the top-left quadrant: high impact, low effort. These are quick wins - off-the-shelf tools you can sign up for and start using immediately.

The quick wins summary has one line per pain point, pointing to a tool. For example: "5 hours a week in email" points to SaneBox (the most-prescribed tool for email). "Taking notes by hand in meetings" points to Fathom.

The recommended solutions slide is the deep dive. This is where 50% of the review call gets spent. For each tool, you list:

- Name of the tool
- Pain point it solves
- Cost of the tool
- Setup time
- Time it saves per week

The format for presenting each recommendation: "This is your pain point. This is the tool. It costs $10 a month. It takes 30 minutes to set up. It saves you 2 hours a week." Then on to the next one.

<!-- illustration: example recommended solutions slide showing tool name, pain point, cost, setup time, time saved -->

The four-day quick start plan addresses a common problem. Many clients feel overwhelmed looking at a report, even a simple one. They freeze and do nothing. The quick start plan tells them exactly what to do on each of four days. Each day takes no more than 10 minutes. If they follow the plan, they get the vast majority of the report's benefit in just 4 days.

The "what comes after quick wins" slide tees up upsell opportunities. The effort versus impact matrix has a top-right quadrant: major projects. These are solutions that are high impact but also high effort - things like building a dedicated agent or a knowledge base. You list these major projects on this slide. The natural next question from the client: "Can you help us do that?"

The financial impact slide quantifies the ROI. The formula:

```
Monthly net ROI = (weekly time returned x hourly rate) - monthly tool cost
```

The average cost of the prescribed tools is about $60 per month. Most business owners' time is worth hundreds of dollars per hour, sometimes thousands. The monthly net ROI is always in the four-figure range, sometimes five figures.

The next steps slide usually has two items: implement the four-day quick start plan and book the review call.

### The Review Call

Phase four is a 30-minute Zoom call. Email the report to the client before the call so they have time to look it over. On the call, share your screen and walk through each recommendation.

Then ask three closing questions:

1. Of these recommendations, which is the most urgent for you?
2. Do you want to do this yourself, or would you like my help implementing some of these solutions?
3. What's your timeline? Are these pain points really hurting you, or could you live another 60 days with them?

These questions are the bridge to upsells. 50 to 60% of the time, clients want implementation. They say things like: "These are great, but I have no idea how to build a Claude skill. Can I just hire you to coach me on it, or can you come build it for me?"

The assessment model means clients are literally paying you to uncover opportunities for them to pay you more. That's what a good audit does.

## The Upsell Menu

The $999 assessment is the foot in the door. After the assessment, you can offer six different follow-up services.

### Process Redesign

Sometimes you need to fix a broken process before you can automate it. A process redesign takes a 16-step workflow and turns it into 7 steps. No AI, no automation - just fixing the process itself.

Example: an e-commerce seller was spending 10 hours a week monitoring Amazon ad spend. The seller wanted to automate the whole thing. But the process was broken. Throwing AI at a broken process makes things worse. The engagement was to fix the process first - map the current state, then deliver the future state as a blueprint. Automating the new process was a separate engagement.

Corey has sold process redesigns for $3,000 and $3,500.

### Automation Builds

Simple Zapier, Make.com, or n8n flows. These work best for processes with a clear input, a clear output, and one to three steps - situations where a Claude skill would be overkill.

Example: a wedding venue rental business. Every time they got a new client, the operations manager had to go into Asana and duplicate a bunch of project items - deliverables, tags, assignments. The same process every time. A single Zap handles it automatically now and scales as the business grows. The charge was $1,500 for about 30 minutes per week in time savings. Thirty minutes per week sounds small, but a growing business turns that into 2 hours per week within a year.

Anyone can learn to build these. A couple of hours of YouTube tutorials on Zapier is enough. Or just ask Claude what to do.

### Knowledge Systems

A knowledge system uses AI to answer repetitive questions from a company's information.

Example: a business broker sells businesses, getting six to eight listings per year. Each listing is high dollar value, low volume. Every time a new listing goes up, 400 to 500 emails come in from interested buyers, all asking the same five questions - EBITDA, time in business, and similar details the broker has already documented.

The solution was a custom GPT trained on the listing's marketing package. Instead of giving out an email address to interested buyers, the broker sends them a link to the custom GPT.

Both the buyer and the seller responded positively. The broker called it "the most interesting experience we've ever had when it comes to buying or selling a business." The solution pulled two of the three ROI levers at once: efficiency (zero emails instead of 500) and quality (a better experience for both sides of the deal).

### Custom Workflows

A custom workflow takes a proprietary business process and turns it into a Claude skill. You build the skill, set up reference files, train the team on it, and let them plug and play.

You can build recurring revenue into this offering. Business operations change over time. A client might pay $3,000 for a set of skills for their customer onboarding process, then pay monthly or quarterly for maintenance as those processes evolve and need updates.

### Full Implementation

A full implementation is any combination of the services above. A client might need two processes redesigned, a couple of Claude skills built, and a Zapier workflow set up. That might be an $8,000 package.

### Pricing Strategies for Upsells

One effective tactic: credit the $999 assessment fee toward the implementation cost. Instead of $5,000, it's $4,000. The client feels the assessment was "free." An even better approach: mark up the upsell by an extra $1,000 and credit the assessment regardless. You make the same money (or slightly more), and the client feels great about the discount.

You can also structure retainers around any of these services. Examples:

- $3,000 per month for up to two knowledge systems
- $2,000 per month for up to three automated workflows

Monthly retainers are easier to sell after you've built trust through a one-time engagement. Sometimes you have to show them the first result - "I built this skill. It works. You want more of these? For $1,000 a month I can give you two."

## Seven Ways to Get Clients

None of these methods require capital or an existing audience. Most of them work because 99% of people won't do them. The ones who do quit after 3 days. If you stick with any of these for 7 days, you're ahead of almost everyone.

### 1. Local AI Meetup

Host a local "AI for Business" meetup. Partner with a co-working space - offer to bring 30 local business owners through their doors in exchange for a free conference room for an hour.

You're automatically positioned as the expert because you organized the event. The format:

- 10-15 minutes of networking
- A 20-minute presentation (teaching how to use Claude works well - simple enough for business owners to understand, advanced enough to impress them)
- Work the room and collect contact information at the door
- Follow up within 24 hours offering the assessment

This method is like SEO. The first event probably won't produce a client. The third, fourth, or fifth event will. The goal is to turn it into a monthly event and build a local brand around it.

You can combine this with the agency partners method below. Partner with a local professional - a realtor, an accountant - and host the meetup in their office. They invite their clients and colleagues. Corey partnered with a well-connected local realtor in Charlotte, hosted the meetup in her office, and got a client from it.

### 2. Door Knocking

Walk into local service businesses, ask to speak with the owner or manager, and pitch the assessment.

This is the opposite of the meetup approach - results are immediate. One listener heard Corey talk about door knocking on a podcast, visited 30 local service businesses, set up 5 meetings, and closed 2 clients. Out of roughly 150,000 listeners, that was the only person who did it. It worked because almost nobody does it.

If you need a client today, go knock a door. If you need a client this week, go knock a door.

Door knocking is also the single best way to learn sales.

### 3. LinkedIn DMs

These are not automated spam messages. You target local business owners in your city or town. You probe about their pain points. You ask how they're currently using AI. Don't pitch in the first message.

Here's an example of a first message:

"My name's Corey. I probably live somewhere down the street from you. Very curious about how you're using AI in your business. Would love to give you some free feedback on ways you could implement AI."

Voice messages and short video messages also work on LinkedIn. The "I probably live down the street from you" line is a strong hook for local outreach.

### 4. Free Audits for People in Your Network

Everyone knows business owners - from the gym, from their neighborhood, from their kids' activities. Send a text:

"I'm getting into the AI services world. I'd love to spend 15 minutes with you completely free of charge and show you one way AI could benefit your business. Would you be open to that?"

The mini audit is a lead magnet. You prescribe one tool for free. The full assessment is the upsell.

A good way to frame it: worst case, they learn about one or two tools they never heard of. Best case, they get a partner who can build AI solutions for them.

### 5. Agency Partners

Insurance agents, accountants, marketing agency owners, coaches, and consultants all have clients who fit your target market. Many of those clients are already asking them AI questions they can't answer well. Not having a good answer makes the professional look bad.

Go to these professionals and say: "I'm in the AI space. I'd love to help any of your clients with AI-related questions. I'll send you a referral fee if I end up working with anyone you send my way."

Follow-up makes this work. You won't get referrals from one outreach attempt. Check in every 2 to 3 weeks: "Any of your clients ask about AI lately? Would love to act as a resource. Happy to meet anytime."

You can also do co-branded workshops with these partners. A session like "Using AI to Optimize Your Finances," co-hosted with an accountant, keeps them top of mind with their clients while giving you access to their customer base.

### 6. AI Office Hours at Co-Working Spaces

Approach a co-working space and offer to come in once a week for an hour. You sit in the space, work on your laptop, and make yourself available for AI questions from the tenants.

This is a win for everyone:

- The co-working space gets a value-add for their tenants
- The tenants get free AI consulting
- You plug directly into your ideal customer profile - everyone in that office is a potential client

If you do a good job and answer their questions well, they'll naturally want more. They'll want to hire you.

One person in Corey's community reached out to 10 co-working spaces and got 2 to agree. Before the first session, they door-knocked local businesses and restaurants for free gift cards - $175 worth - and used them as incentives to get people to show up. Eleven people came to the first session. Two of them scheduled follow-up calls.

### 7. Building in Public

Document your wins by creating short videos, posting on X, or sharing images. A "win" doesn't need to be dramatic. "Someone texted me a question about ChatGPT and I gave a good answer" counts. Your wins are probably less significant than you think, and people can still benefit from them.

In the early days, you won't have many real results to share. Create value-focused content for your target audience instead. Post a useful prompt every day, create a weekly carousel, share a tool recommendation. Commit to 90 days of consistent output. As you get clients and complete assessments, the real results start coming in and you can layer those on top.

## The AI Concierge

This is Corey's favorite upsell and the one that generates recurring revenue. It's done-with-you consulting: two 45-minute Zoom calls per month where you help the client use Claude and build Claude skills. Corey calls it the AI concierge offer.

Of the first six people Corey pitched this offer to, five said yes. He generated $8,000 in monthly recurring revenue in the first 10 days. He kept raising the price for each new client, and people kept saying yes.

The pricing progression for his first five clients:

- Client 1: $1,200/month
- Clients 2-3: $1,500/month
- Client 4: $1,800/month
- Client 5: $2,000/month

At $1,500 per month for two 45-minute calls, the effective hourly rate is $1,000.

Between calls, clients get unlimited Voxer (voice messaging) access with a 12-business-hour response time. This sounds like a lot of work, but it's not. Of five clients over about two and a half months, only three have sent a message, one message each. The workload is virtually zero. But the perceived value is very high - clients like knowing they have someone on call for any AI question.

Corey caps this service at six clients. On sales calls, he tells prospects: "I'm taking one more client for this offer. I have two other calls this week with people who are interested. If you say no today and one of them says yes, I'm not working with you until one of my other clients leaves." This has to be legitimate scarcity - and for him, it is.

A pricing strategy for people starting out: advertise tiered spots. Four spots at $800 per month, then the price goes to $1,200, then $1,600. This creates urgency because prospects don't want to pay the higher tier.

### Session Structure

The first call is onboarding only - no building. Corey built a Claude plugin that walks clients through a guided onboarding process:

- Connect their tools
- Create context files
- Create global instructions
- See what a scheduled task looks like
- See what a skill does

This first call sets the foundation so every call after it is far more effective.

Every subsequent call follows the AOA framework:

1. Audit - the client shows how they do a process today
2. Optimize - cut the fat (turn a 13-step process into 7 steps)
3. Automate - turn it into a Claude skill

You repeat this for every workflow the client has, for as long as they stay a client.

### Premium Touches

Before the first call, send the client a Google Form as a pre-engagement questionnaire. The most useful question: "90 days from now, what would make this engagement feel like a win?" Clients give very specific answers to this.

Four of Corey's five clients achieved their stated 90-day win in about 60 days. When that happens, you remind them: "When we first started working together, you said this would be success, and we already exceeded that." This reinforces the value and opens the door to expanded engagements.

The entire client engagement lives in a Notion one-pager that serves as a hub. It includes an inventory of everything accomplished together during the engagement. This gets updated and emailed to the client after every call. When they see a running list of everything you've built together, the monthly fee feels justified.

## Niching Down

You can differentiate in two ways:

- Geographic niche: become the go-to AI person in your city. In-person meetups and office hours at co-working spaces support this approach.
- Industry niche: become the AI person for a specific industry. If you have 10 years of experience in financial services, brand yourself as the person who does AI assessments for financial services. You can charge more and face less pricing pressure with that kind of domain expertise.

For focus, pick the assessment plus one upsell. Corey recommends assessment plus AI concierge, but you could also pair the assessment with knowledge systems or Claude skills - whatever fits your strengths.

The pie is large enough for everyone. There are millions of businesses that need this help. The competition is low. The people who execute on any of these strategies and stick with them for more than a week will find clients.

## Sources

[^1]: https://youtu.be/dhbcVxYhWaQ
[^2]: [20261009_071527_AlexeyDTC_msg5022.md](../../inbox/used/20261009_071527_AlexeyDTC_msg5022.md)
