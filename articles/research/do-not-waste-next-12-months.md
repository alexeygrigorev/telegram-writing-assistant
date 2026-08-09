---
title: "Distribution Without an Audience: Five Plays Applied to DataTalks.Club and AI Shipping Labs"
created: 2026-08-04
updated: 2026-08-04
tags: [research, distribution, marketing, datatalks-club, ai-shipping-labs, seo]
status: draft
---

todo rename the article to make sense - it hsould be a topic


# Distribution Without an Audience: Five Plays Applied to DataTalks.Club and AI Shipping Labs

https://open.substack.com/pub/capitalofone/p/do-not-waste-the-next-12-months-building

Melvin Luu writes Capital of One, a newsletter for solo founders. In July 2026 he published an essay arguing that "build an audience and post daily for two years" is only one distribution channel, and the slowest one. The essay lists seven plays that need no followers [^2]. This article covers the first five and what each one implies for DataTalks.Club and AI Shipping Labs [^1].

Who this is for: anyone deciding where the next few months of content and platform work at either organisation should go. The essay is written for a solo founder selling software, so most of the work here is translating it to a free open community and a small paid one.

## The argument

Luu defines distribution as access to your buyers' attention. His point is that an audience is one way to get that access, not the only way. You can also plug into attention that already exists somewhere else.

The essay opens with Jagalchi fish market in Busan. Downstairs, fish sellers have the customers and the trust. Upstairs, restaurants cook the fish you just bought. The restaurants need no sign and no menu, because the sellers hand the customer over. The restaurants don't own the attention - they sit inside it.

Every play in the essay is a version of the restaurant. Here is how the five plays covered here hang off that frame.

```mermaid
graph TD
    D["Distribution = access to buyer attention"]
    D --> O["Own it: build an audience"]
    D --> B["Borrow it: plug into attention that exists"]
    O --> S["One channel - slowest, most crowded"]
    B --> P1["1. MCP server<br/>the assistant's attention"]
    B --> P2["2. AEO<br/>the answer layer"]
    B --> P3["3. Free tool<br/>search and word of mouth"]
    B --> P4["4. Programmatic SEO<br/>Google"]
    B --> P5["5. Shareable artifact<br/>your users' feeds"]
```

The rule Luu sets for himself is that every play comes with named companies and verifiable numbers. That holds up - the case studies are specific and linked. The closing advice is to pick two plays, one compounding and one fast, and that picking two slow plays is the common mistake.

The next five sections cover one play each: what the essay claims and what evidence it gives. After that comes the part that matters for us - what each play means for DataTalks.Club and for AI Shipping Labs, and where the essay doesn't transfer.

## Play 2: answer engine optimization

The claim: assistants are becoming the first place buyers research, so the job is to be the source the assistant cites. Luu calls AEO in 2026 what SEO was in 2010.

The evidence:

- He cites SparkToro data that 60% of Google searches end without a click, rising to 80-90% when an AI Overview appears.
- ChatGPT accounts for around 92% of AI referral traffic, and that traffic converts at 7.1% - second only to paid search.
- AI referrals are still below 1% of total web traffic, which is what makes the window open.
- Design studio Broworks ran a 90-day sprint restructuring content into direct answers with schema markup. They report 10% of organic traffic coming from LLMs and 27% of that traffic converting into sales-qualified leads.
- One SaaS brand in HubSpot's compiled case studies grew AI-referred trials from 575 to 3,500+.
- From his own client work: 25 buyer questions identified, 12 pages rewritten as direct answers, placement in two comparison articles. Six weeks later the company appeared in 7 of 20 target prompts. Perplexity moved in two weeks, ChatGPT took over a month, Google's AI Overviews didn't move at all.

The part that's easy to miss: AEO doesn't only happen on your own site. Models pull from comparison articles, review sites, Reddit threads, directories, and roundups. So the work is twofold - write the cleanest answer on your domain, and get mentioned in the places the model already trusts.

The method is concrete. Ask ChatGPT and Perplexity the 20 questions your buyers would ask, log who gets cited, then target that list and re-check monthly.

## Play 3: a free tool that sells for you

The claim: give away a small tool that solves one painful problem, and your paid product becomes the obvious next step. The tool has to sit one step before the purchase.

The evidence:

- HubSpot's Website Grader, launched in 2007, graded over 4 million websites.
- Shopify's Business Name Generator, wrapped in 200+ landing pages targeting nearly 20,000 keywords. Foundation Inc. valued the traffic at $6M per month in equivalent ad spend.
- Ahrefs' free backlink checker, which ranks for the exact query its best customers type and caps the value at $129/month for the real product.
- Tweet Hunter, where two indie makers shipped one small free tool per month and reached a $10M exit in about 18 months with no ads and no audience.
- Photopea as the counter-example where the free tool is the whole business - one person, roughly $3M a year from ads.

Luu's three reasons this works: the person using the tool is already problem-aware, tools spread on their own, and until recently a tool cost months of engineering, so almost nobody has noticed the cost collapsed.

He also answers the obvious objection. A tool survives an assistant that can do the same thing in chat if it either does the job faster than a conversation or runs on data the model doesn't have.

The build sequence is instant value first, email capture second. Give the result immediately, gate the full report. Reverse that and nobody uses it.

TODO what I can do like that for datatalks.club and ai shipping lab?


## Play 4: programmatic SEO

The claim: find a keyword pattern that repeats across thousands of variations, build one useful template, fill it with real data, and publish at scale.

The evidence:

- Nomad List and Remote OK, which Luu uses to argue that Pieter Levels is the right example for the wrong reason - the audience is one pipe, and programmatic SEO built years ago is another.
- Failory's own write-up of getting 97,450 users a month this way.

The structural requirement is a repeatable template plus specific inputs - prices, locations, examples, reviews, ratings, whatever the searcher came for. The template gives structure, the inputs give usefulness.

Two constraints Luu is firm about. Validate the pattern before building: you want hundreds of low-competition variations, not one giant keyword. And publish 100 pages first, then watch indexation in Search Console - if Google indexes 80% or more, scale; if it ignores half, the pages are too thin.

The line separating this from mass-produced junk is the human review step. His words: the gap between people who do this well and people who publish 10,000 pages of slop is that review.


TODO what I can do like that for datatalks.club and ai shipping lab?

## Play 5: something your users want to show off

The claim: give people a result that says something flattering about them, make it easy to share, and they will post it with your product attached.

The evidence:

- Spotify Wrapped reached 200 million engaged users in 24 hours in 2025 and was shared over 500 million times.
- GitHub's contribution graph, Duolingo streaks, and Strava's Year in Sport as the same mechanic for identity rather than a feature.
- Wordle as the solo proof. Josh Wardle noticed players manually typing emoji grids to share results, so he built the grid into the game. It went from 90 players to 300,000 in two months, then 2 million a week later.

The design pattern across all of them: the artifact is about the user's identity, not your feature. "You're in the top 8%" beats "Powered by our product". It's clean enough to post without embarrassment. And it's time-bound, so everyone shares at once and it becomes a wave rather than a trickle.

His starting move is diagnostic rather than creative. Look at your support inbox and social mentions to find what people already screenshot. They may already be sharing something ugly.

That covers the five plays. The rest of this article is about what they imply for two organisations that already exist, with the assets they already have.


TODO what I can do like that for datatalks.club and ai shipping lab?
already do: certificates
what could do better? pages with summary etc with the list to the certificate


## What this means for DataTalks.Club

DataTalks.Club is the open side: free Zoomcamps, a Slack community, a podcast archive, events, and a public site. The plays land unevenly here, because the assets are unusual. There's a lot of structured content and a lot of students, and almost no product to sell.

```mermaid
graph LR
    A["FAQ corpus + faq-assistant Lambda"] --> P1["Play 1: remote MCP server"]
    A --> P2["Play 2: answer-first FAQ pages"]
    B["Dead Courses page,<br/>orphaned data-paths"] --> P2
    C["Cohort scores, leaderboard,<br/>certificates"] --> P5["Play 5: cohort wrapped"]
    E["Podcast, books, people archives"] --> P4["Play 4: podwiki-style pages"]
```

### AEO argues for finishing the Courses page

The unified platform document records that the Courses navigation item on datatalks.club doesn't point to a course listing - it links to a single blog post, and the courses collection holds one stale 2021 file with a "Nothing here, come back later" message [^8].

Read through the essay's lens, that's not only a navigation problem. When someone asks an assistant "what's the best free data engineering course", there needs to be a page for the model to cite, and right now there isn't one. Same for the six role learning paths in data-paths, project-of-the-week, and the reading clubs - all reachable only through Slack or direct GitHub links.

The FAQ is closer to AEO-ready than anything else in the org. It's already question-shaped, per course and per module. What it lacks is the answer-first structure, schema markup, and a domain position that models will cite.

The 20-question exercise is cheap to run this month. Ask ChatGPT and Perplexity things like "best free MLOps course", "how do I learn LLM engineering", "free machine learning course with certificate", and log who gets named. There's already an article in this repo on AI search visibility and AI Overview tracking; the essay supplies the concrete method that article was missing.

### A readiness grader is the free tool that fits

The purchase equivalent at DataTalks.Club is a course registration. So the free tool has to sit one step before that - and the community observations already name the problem it should solve.

Newcomers don't know what depth of skill each course expects. The site says "you know Python", which is abstract. The observation notes there's no expert telling people "you should know this at this level, and that one at a different level", and suggests a Lightning Lesson on skill depth [^7].

A Python readiness check for ML Zoomcamp is the Website Grader shape applied to that problem. You answer or solve a short set of tasks, you get a score, and the score tells you which course to start with and what to fix first. The instant result is the score. The gated part is the personalised gap list.

TODO move it up. come up with other ideas. analyze the content from all 
our courses, content, workshops
for each DTC course for each module come up wih 2-3 ideas
also CV readiness check, portfolio projects scanner, etc
(but also I don't really want to pay for LLM calls)

It also produces a number, which is exactly what play 5 needs.

### Cohort wrapped is the highest-value play here

Of the five, this is the one where DataTalks.Club already owns every ingredient and uses none of them for distribution.

The course management platform holds registrations, homework submissions, peer reviews, scores, and leaderboards. zoomcamp-scoring already generates certificates from final scores. Thousands of students go through a cohort, and they all finish at the same time.

That last part is what Luu says turns a trickle into a wave. Spotify Wrapped works because it lands on one day. A cohort end date is the same kind of calendar moment, and it already exists.

The artifact would be a per-student recap: modules completed, homework submitted, peer reviews given to others, weeks without a missed deadline, rank if the student wants it shown. Identity first, in the essay's terms - "you finished 7 of 7 modules and reviewed 9 other projects" rather than "certificate of completion".

The diagnostic step confirms the demand before anything gets built. Students already post their certificates on LinkedIn. That's Luu's signal that people are sharing something ugly and would share something better.

A homework streak is the GitHub-contribution-graph version of the same thing, running during the cohort rather than at the end.

### Programmatic SEO is the one to be careful with

The raw material is there: about 206 podcast episodes, 438 people pages, 99 books, and FAQ entries per course per module. podwiki is already a generated layer over the podcast archive, with topic hubs, roadmaps, comparisons, and a graph view. It deliberately links back to the canonical pages instead of re-publishing them. That's the right model for anything else generated this way.

The vocabulary idea from the platform notes is a programmatic template in disguise. Every tool and concept, from RAG to MCP, gets one entry page, and every page mentioning it links there. That's one template, real inputs, and internal linking, which is what play 4 asks for.

The tension is real, though. The whole unified-platform effort is about removing duplicated surfaces, and programmatic SEO adds pages. The only version that doesn't make the fragmentation worse is one where the generated pages render from a single canonical dataset, the way podwiki does.

### The five plays are a module in Product Shipping Zoomcamp

The proposed Product Shipping Zoomcamp already has a Module 6 on launch, distribution, and build-in-public, and the working principle in it is to launch where your users already spend time rather than everywhere [^10].

That module currently lists channels - Reddit, Discord, Product Hunt, Hacker News, Indie Hackers, LinkedIn. Every one of those is a place you post. The essay's five plays are a different category: things you build once that keep working. A student who ships an MVP in Module 2 could add a small MCP server or a shareable result card in Module 5 or 6 instead of only writing launch copy.

The framing also fixes an imbalance in Module 1. Community mapping teaches students to find where their users are, which is the borrowed-attention idea, but the course then hands them only posting as the way to use it.

## What this means for AI Shipping Labs

AI Shipping Labs is the paid side: workshops, six-week accountability sprints, personalised member plans, and member projects. There is an actual product to sell here, so the essay transfers more directly - but the constraints are different, and one of them is severe.

```mermaid
graph LR
    F["AI Engineering Field Guide<br/>job dataset"] --> T3["Play 3: free job-match tool"]
    F --> T4["Play 4: job-pattern pages"]
    W["24 workshop pages"] --> T2["Play 2: answer-first pages"]
    W --> T1["Play 1: catalogue MCP server"]
    S["6-week sprint demo day"] --> T5["Play 5: sprint recap card"]
```

### The job dataset is the strongest asset for three plays at once

The AI Engineering Field Guide already scrapes job listings, deduplicates them, and enriches them with an LLM. The FDE research article analysed 113 postings from that dataset. The platform notes describe an agent on top of this data that clusters jobs, matches a profile, and points at gaps - listed as a member feature [^6].

The essay's argument is that a limited version of that belongs outside the paywall, as top of funnel. It passes Luu's survival test cleanly: it runs on data the model doesn't have. And it sits one step before the purchase, because the person checking whether their profile matches AI engineer postings is exactly the person the "Land the AI Engineering Job" course is for.

The same dataset supports play 4. Patterns like "AI engineer jobs requiring [skill]", "[role] jobs in [city]", and "what [tool] experience employers ask for" produce hundreds of low-competition variations from data that's already collected and enriched. Publish 100, check indexation, then decide.

The platform notes already say the value is in the data rather than the agent built on top. The essay agrees and adds two more ways to spend that data.

### The overview-article strategy needs the answer-first rewrite

The marketing notes already describe the shape. A public overview article covers the general topic, while the specifics live inside the community: repository templates, prompts, workflows. The article links out to the community as the reason to join [^5].

That's the right structure. What it's missing is the AEO layer. Answer in the first two sentences, support with comparisons and FAQs, add schema, then get cited in the places models already trust.

The plan also includes concept explainer articles on what RAG is, what GraphRAG is, and what agentic RAG is. Those are AEO assets if they're written answer-first, and ordinary blog posts if they aren't. Same for the listicles and cheat sheets, which the notes already say bring traffic.

The off-site half of play 2 is the part not currently covered anywhere. Getting into comparison articles, roundups, and Reddit threads about AI engineering courses is work nobody is doing today, and the essay's client case study says it moved the needle faster than on-site changes.

### Workshops are a small programmatic surface and an MCP candidate

There are 24 sessions catalogued, already published at aishippinglabs.com/workshops. That's a real template with real inputs, just at small scale. The six-course repackaging in the content plan gives the pages a second axis - a session belongs to a course, and courses can be listed by the problem they solve.

A workshop-catalogue MCP server is the small, one-job version of play 1: someone asks their assistant what to learn next about tracing or evals, and the server returns the matching sessions. It's a modest server, which is exactly what Luu recommends.

### Sprint recap cards fit the format that already exists

The sprint format already ends in a demo week where people show what they built. The activities notes already list sprint-based promotion as a benefit - "our 10th sprint is starting, here are results from sprint 9" [^4].

A per-member recap card at the end of the sprint turns that promotion plan into something members post themselves: what they shipped, how many weekly calls they made, the demo link, what they set out to do in week 1 versus where they landed. The framing is identity first rather than a logo: "I shipped a deployed agent in six weeks".

The B2B objection Luu anticipates doesn't apply here at all. Members are individuals building careers and portfolios, and the whole personal-branding thread in the activities notes says they want to be seen doing it.

### The free tool cadence fits the lead magnet plan

The marketing plan already lists lead magnets as a funnel step, with learning paths as the example. Play 3 is a sharper version of the same idea: ship one small tool a month, give the result instantly, gate the full report behind an email.

Candidates that sit one step before joining:

- A README or portfolio grader, feeding the "Land the AI Engineering Job" course. The member-plan synthesis already lists "a README a hiring committee can read" as a named blocker for six people, so the demand is documented rather than assumed [^9].
- An eval-set starter that turns a description of your app into 20 candidate test cases, feeding the Agent Reliability course.
- The public slice of the job-match tool described above.

Each one maps to a course that already exists in the six-course packaging, which is the alignment test Luu insists on: kill every idea where the tool's output doesn't lead naturally to the paid offer.

## Sources

[^1]: [20260804_040940_AlexeyDTC_msg4839.md](../../inbox/used/20260804_040940_AlexeyDTC_msg4839.md)
[^2]: Melvin Luu, "Do Not Waste the Next 12 Months Building an Audience" (subtitle: "7 Distribution Channels That Don't Need a Single Follower"), Capital of One, 12 July 2026: https://open.substack.com/pub/capitalofone/p/do-not-waste-the-next-12-months-building
[^3]: [AI Shipping Labs Content Plan](../ai-shipping-labs-content-plan.md)
[^4]: [AI Shipping Labs Community Activities](../ai-shipping-labs/activities.md)
[^5]: [AI Shipping Labs Marketing and Content Strategy](../ai-shipping-labs/marketing-and-content.md)
[^6]: [Community Platform Feature Ideas](../ai-shipping-labs/platform-ideas.md)
[^7]: [Community Observations](../ai-shipping-labs/community-observations.md)
[^8]: [DataTalks.Club Unified Platform](../datatalks-club-unified-platform.md)
[^9]: [Workshop and Course Ideas from Member Plans](../workshop-and-course-ideas-from-member-plans.md)
[^10]: [Product Shipping Zoomcamp](../product-shipping-zoomcamp.md)
