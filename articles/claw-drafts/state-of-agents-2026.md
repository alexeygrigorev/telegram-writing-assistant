# Everyone Runs Agents Now. 41% of Them Break Every Day.

> Subtitle: Temporal surveyed 554 engineers and the result is a report card with A's for adoption and a failing grade for operations. What the numbers say, what they hide, and the four metrics that close the gap.

[IMAGE: Two diverging lines on a chart: adoption (daily agent use rising from 47.3% to 80.8%) climbing steeply, operational maturity (issue-free days) flat below it]
Caption: 1. Daily agent use rose 70.8% in a year. 2. The share of teams hitting agent issues daily stayed at 41.1%. Source: Temporal, State of Development Report 2026.

Two numbers from the same survey, sitting three lines apart. 91.1% of engineers say AI agents have improved or revolutionized their productivity. 41.1% hit agent-related issues every single day, and 9% say their agents misbehave continuously. Both numbers describe the same population of 554 engineers, surveyed by [Temporal](https://temporal.io/reports/state-of-development-2026) between April 29 and May 25 of this year.

That pair is the whole story of agents in 2026. The technology won the adoption argument decisively, and it lost the operations argument just as decisively. Almost nobody is debating whether to run agents anymore. Plenty of people are quietly embarrassed by how often theirs break.

The [2026 State of Development Report](https://www.businesswire.com/news/home/20260825235670/en/) (Temporal's second annual edition, released August 25) is worth reading past the headline, because the interesting material is in the tension between its own sections. This piece walks through what the survey found, where it agrees with four other industry surveys, where to read the fine print, and what a team should actually measure this quarter to end up on the right side of the gap.

### Adoption: the year agents clocked in

The topline numbers describe a step change, and a jump of 70.8% in one year.

- **80.8% of engineers now use agents daily or more**, up from 47.3% a year ago. A fifth use them continuously.
- The median respondent runs **5 agents**. The average is 10.7, dragged up by outliers running dozens; one respondent reported 256. Just 2.2% run more than 51.
- **49.1% describe their use as "in production" or "core to how they ship."** A quarter still use agents mainly as assistants.
- **51.3% go from AI prototype to production-ready code in hours or faster.** Over a quarter say minutes.

And the number that will define a thousand LinkedIn posts: **92.3% of engineers have tried to rebuild software they used to buy**. The report calls it the SaaSpocalypse. When in-house generation costs minutes, every SaaS line item starts to look optional.

None of this is one vendor's spin. Stack Overflow's [May pulse survey](https://stackoverflow.blog/2026/05/27/agents-on-a-leash-agentic-ai-remains-mostly-monitored-at-work/) found workplace agentic usage nearly doubled year over year, from 31% to 59%. McKinsey's [State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) puts 40% of large enterprises in the scaling-agents camp, up from 27%, and, matching Temporal almost exactly, finds about a third now building in-house instead of buying. Gartner, [cited in trade coverage](https://www.webpronews.com/enterprise-ai-agents-surge-from-pilot-to-production-as-adoption-hits-critical-mass/), projects task-specific agents embedded in 40% of enterprise apps by year-end, from under 5% a year ago. Four methodologies, one direction.

### The 41 percent

Here is where the report gets honest, possibly by accident.

41.1% of respondents encounter agent-related issues **daily or more**. 9% chose "continuously," an answer option that exists so people can say their agents never quite stop breaking. And the "successful" teams, the self-identified cohort the report holds up, report issues at essentially the same rate as everyone else. Success in this survey means getting value from agents, and it apparently coexists with daily breakage as a matter of course.

The trust numbers make the picture stranger. 85.5% trust agent outputs at least somewhat, a quarter completely. Yet coverage of the report notes that [developers still verify agent code manually](https://www.developer-tech.com/news/developers-trust-ai-agents-still-verify-code-manually/), which is the behavioral tell: stated trust high, practiced trust conditional. That's a rational stance for software that improves your productivity and also catches fire four days a week.

**Adoption is a solved problem. Operations is the bottleneck, and the distance between those two sentences is the 2027 roadmap for most teams.**

### What actually breaks: state, debugging, money

When the survey asked what blocks greater agent use, the top three answers were:

1. **Tracking state.** Where did the run stop, what did it already do, what was it about to do. If you have read anything I've written this month, you know why this number made me sit up: it is the exact problem durable execution exists to solve, and it's the #1 blocker in the wild.
2. **Debugging.** Agents fail in ways spreadsheets of logs don't explain. Troubleshooting, per the report, often starts on YouTube, then moves to AI tools and private Discord and Slack groups. Your team's reliability strategy is a video platform and a group chat.
3. **Managing costs.** 79.8% say token and compute cost limits their agent use. Cheap per-token prices did not cheapen agents, because chaining multiplies calls (I'm writing a full piece on this next).

The report's own framing links those three to its success cohort: teams that "solved for state, cost, and reliability" run slightly more agents (11.1 vs 8.8 on average) and ship faster. Hold that thought, because there's a fine-print problem with it.

### Read the fine print

Three caveats before you build a slide deck on this thing.

**It's a vendor survey.** Temporal sells durable execution, and the top three blockers it surfaced (state, reliability, cost) are a precise match for its product page. The successful cohort being more likely to use Temporal is presented as an endorsement; a selection effect is the simpler explanation. The questions weren't necessarily leading, but the report's narrative arc lands exactly where the vendor's funnel wants it. Discount accordingly.

**The cohort is self-reported.** "Successful" teams are teams who told Qualtrics they feel successful. The report also finds 84.5% of engineers believe their team is better than competitors at using agents, a number that runs higher among executives. That is the Lake Wobegon effect with a budget, and it should calibrate how you read every self-assessment in the document.

**The free-text answers contradict the checkboxes.** Engineers volunteering written answers expressed more caution and anxiety than the multiple-choice results suggest, and the jobs numbers show the split: 77.5% are more optimistic about their own role, yet 56.7% think it will be harder for junior engineers to find work, 45.5% say the same for seniors, and only 26.4% of companies report actually slowing hiring. Optimism for me, turbulence for thee.

None of this makes the survey useless. It makes it a primary source, which is exactly how you should read every vendor report in this space, including the [Salesforce finding](https://www.salesforce.com/news/stories/agentic-ai-leaders-survey-on-roi/) that agent deployments doubled while meaningful ROI takes about eight months, and LangChain's [State of Agent Engineering](https://the-agent-report.com/2026/05/state-of-agent-engineering-2026-langchain-datadog/), where 57% have agents in production but the same observability-and-quality wall appears. The corroborating surveys carry their own funnels too. Convergent independent data with similar biases is the best we get, and right now it all converges: adoption huge, operations ragged.

### The four numbers that close the gap

If your team is one of the 41%, the survey tells you where the pain lives but says little about treatment. Here's the artifact: four numbers to track weekly, one per blocker. I've written the [long version of the reliability argument](https://alexeyondata.substack.com) separately; this is the dashboard version.

1. **Issues per agent-week.** Count incidents, define incident before counting. The survey's 41% becomes your baseline; the goal is trend, not zero.
2. **Time to recover.** When an agent run breaks, minutes from breakage to a correct resume. This number exposes whether your state story is real (durable state, journaled steps) or aspirational (a status column nobody updates).
3. **Cost per completed task.** Tokens and compute divided by tasks that actually finished. The unit that survived contact with accounting, and the one the 79.8% should be arguing about.
4. **Share of runs that survive a restart.** Kill an agent in staging mid-task weekly and check whether it resumes or restarts. That's the blocker #1 of the report, expressed as a number you can watch move.

A team that tracks those four for a quarter knows more about its agent operations than any survey of 554 strangers can tell it.

### Close

Here's what I believe: the 41% number will age better than the 91%. Productivity surveys capture a moment, and the moment is genuinely good. The operational debt compounds quietly until it decides which teams get to keep their agents in production and which quietly shelve them. The teams pulling ahead, in this data and every other dataset I trust, are the ones treating agents as systems to be operated: state that survives restarts, failures you can debug from a log, costs you measure per task. Everyone else is running a demo with a schedule.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://alexeyondata.substack.com
- Subtitle: Temporal surveyed 554 engineers and the result is a report card with A's for adoption and a failing grade for operations. What the numbers say, what they hide, and the four metrics that close the gap.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "What actually breaks: state, debugging, money".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, AI Agents, Machine Learning, Software Engineering, LLM
- Member-only: no
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- AI agents in production 2026
- agent reliability
- Temporal state of development report
- agent adoption survey
- AI agent survey 2026
- agent operations
- debugging AI agents
- agent cost management
- SaaSpocalypse
- state tracking AI agents

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. Everyone Runs Agents Now. 41% of Them Break Every Day.
2. 91% Say Agents Boost Productivity. 41% Say They Break Daily. Both Are True.
3. The Agent Report Card: A's for Adoption, F for Operations
4. Temporal's 554-Engineer Survey Explains Where Agents Actually Hurt
5. Agents Won the Adoption Argument and Lost the Operations One

### Subtitles
1. Temporal surveyed 554 engineers and the result is a report card with A's for adoption and a failing grade for operations. What the numbers say, what they hide, and the four metrics that close the gap.
2. Daily agent use jumped 70.8% in a year, and 41.1% still hit issues daily. The survey behind both numbers, cross-checked against four others.
3. Adoption is a solved problem, operations is the bottleneck: the survey, the vendor fine print, and four weekly metrics for teams on the wrong side of the gap.
