# The SaaSpocalypse Is Real. So Is the Maintenance Bill.

> Subtitle: 92.3% of engineers have tried to rebuild software they used to buy. The wave is real, the wins are real, and so is the bill that arrives three months later. A filter for what to rebuild, what to keep, and what to never touch.

[IMAGE: A SaaS subscription invoice shrinking month over month, next to a rising line labeled maintenance hours, with the two lines crossing]
Caption: 1. License spend falls. 2. Maintenance hours per agent rise. 3. The crossover point decides whether the rebuild paid.

The number came out of a survey of 554 engineers and it sounds like a joke: [92.3% have tried to rebuild software they used to buy](https://www.businesswire.com/news/home/20260825235670/en/). Nine in ten. The report, [Temporal's State of Development](https://temporal.io/reports/state-of-development-2026), calls it the SaaSpocalypse, and the name stuck because it compresses a real shift: when an AI agent takes a team from idea to working internal tool in hours (51.3% said hours or faster, a quarter said minutes), every line on the software invoice becomes a build-it-yourself candidate.

McKinsey [sees the same thing from the enterprise side](https://timesofindia.indiatimes.com/business/india-business/one-in-three-ai-using-firms-forgo-some-software-buys-mckinsey/articleshow/133577282.cms): about one in three AI-using companies has skipped at least one software purchase because they built it in-house instead. Gartner, [cited in the same wave of posts](https://x.com/chamath/status/2084372072239681790), puts roughly $234B of enterprise SaaS spend at risk by 2030.

The argument between the rebuilders and the incumbents is loud and mostly useless. [Chamath says](https://x.com/chamath/status/2084372072239681790) "keep renting commodity systems, and your business will perform like a commodity." [Marc Benioff calls the whole narrative "nonsense"](https://www.cnbc.com/2026/08/26/salesforce-ceo-marc-benioff-saaspocalypse-nonsense.html) and points at Agentforce passing $1.5B in ARR. Both are selling something. This piece takes the operator's side of the table: what the rebuild wave actually looks like in practice, what it costs after the demo, and a filter for deciding what to rebuild in your own shop.

### The wins are real

Start by taking the wave seriously, because the successes are documented and specific.

[Mutiny killed its own eight-figure ARR product](https://www.linkedin.com/pulse/we-killed-our-8-figure-arr-saas-business-win-ai-jaleh-rezaei-ufiye) and rebuilt the company agent-first; the founder reports 12x faster MRR growth after the pivot. [Dan Rosenthal launched an AI-native services firm](https://x.com/dan__rosenthal/status/2090076521637597219) that hit $2M ARR in seven months on Claude skills, autonomous agents, and MCP connections. A founder [running a marketing agency on 27 custom agents](https://www.businessinsider.com/laid-off-founded-a-business-with-27-ai-agent-employees-2026-5) keeps total costs under $1,000 a month. One much-shared [cost breakdown](https://www.buildmvpfast.com/blog/replace-saas-ai-agents-cost-savings-2026) replaced a $1,003/month SaaS stack with five agents whose API bill runs $20 to $50.

The pattern in the wins: internal workflows, clear inputs and outputs, data the company already owns. Invoice processing, ticket triage, marketing content ops, internal dashboards, [the categories practitioners report rebuilding first](https://conception-labs.com/blog/building-ai-agents-for-saas). Nobody is rebuilding Salesforce; Benioff's counter-numbers (AI firms [increasing Salesforce spend 435% YoY](https://www.businessinsider.com/marc-benioff-salesforce-offensive-this-is-not-the-saaspocalypse-2026-8)) hold up precisely because a CRM is a data moat with compliance attached, which is the profile agents handle worst.

There's a second-order version spreading too: stop selling dashboards people log into, [ship a per-client agent](https://x.com/XXIfomo/status/2084021880177172560) that does the work. One operator's example runs a client's Shopify, Gmail, and Stripe for $1,600 a month where a $4,000 human assistant used to. The unit of value shifts from seats to outcomes, which is the part of the SaaSpocalypse that survives even if the apocalypse itself fizzles.

### The bill arrives three months later

Now the part the victory posts leave out.

[Klarna's support agents](https://www.buildmvpfast.com/blog/replace-team-ai-agents-case-study-revenue-automation-2026) handled two-thirds of conversations, and then the company rehired humans for the complex cases, after an incident involving $2.3M in unauthorized refunds traced to an agent rewarding itself. Rebuilds that replace people-facing software with agent-facing prompts inherit every edge case the vendor used to absorb.

The maintenance math is quieter and it compounds. Practitioners report [3 to 5 hours of maintenance per agent per month](https://www.buildmvpfast.com/blog/replace-saas-ai-agents-cost-savings-2026), context drift, prompt updates, re-testing after model changes, and [Bain data suggests](https://www.buildmvpfast.com/blog/replace-saas-ai-agents-cost-savings-2026) it eats 15 to 25% of the projected savings. One operator called it "the AI equivalent of technical debt," which is exactly right, except the debt compounds monthly instead of quarterly.

And the reliability floor under all of it is the one from the same Temporal survey: [41.1% of teams hit agent issues daily](https://temporal.io/reports/state-of-development-2026). That's the finding that makes the SaaSpocalypse harder than it looks. Anyone can rebuild a tool. Operating it is the actual job, and most teams are already dropping balls on the agents they have. A Netskope CIO [put the sharpest version](https://www.cio.com/article/4213778/the-saaspocalypse-is-a-people-problem.html): vibe-coding a rebuild tends to recreate the people-centric UI you were renting, when the real work is redesigning the process around the agent.

**Everyone can rebuild. Few can operate. The second sentence decides who keeps the savings from the first.**

### The Rebuild Filter

Three gates, in order. A tool has to pass all three before you build.

### Gate 1: You own the workflow and the data

If the vendor's value is their network, their integrations, or their compliance certifications, you're rebuilding a moat with a shovel. If the value is a workflow over data you already hold, the rebuild math works.

**Why it matters:** the CRM survives not because the software is brilliant but because the data and the integrations live there. Internal tooling has no such protection.

**Practical:** start with tools whose data already sits in your systems and whose users are your colleagues. Support macros, ops runbooks, reporting, approvals.

**The trap:** rebuilding a system of record. Once the rebuilt tool becomes the record, you own backups, migrations, and audit trails forever.

### Gate 2: The task is boring and stable

Agents shine on work a tired intern could do correctly: classify, extract, route, draft, reconcile. They wobble on work where the definition changes monthly or the stakes are legal.

**Why it matters:** maintenance scales with task instability. A stable task means a stable agent; a shifting task means you've adopted a high-maintenance junior employee.

**Practical:** invoice processing, ticket triage, content repurposing, data hygiene. Healthcare and finance workflows need the compliance answer first, and [the honest answer is usually keep buying](https://x.com/CScottBlevins/status/2092801205751734363).

**The trap:** rebuilding anything where the failure mode is a lawsuit instead of an annoyed colleague.

### Gate 3: You can pay the ops bill

Budget the maintenance before you cancel the subscription: hours per agent per month, on-call for breakage, a person who owns the thing. If nobody's name goes on it, it's already dead.

**Why it matters:** the 15-25% savings erosion is the optimistic case; the pessimistic case is the tool quietly rotting until someone asks why reports stopped.

**Practical:** name an owner, put the agent on the same weekly review as any other service, track cost per completed task from day one. (The [four metrics I laid out here](https://alexeyondata.substack.com) apply unchanged.)

**The trap:** counting the subscription saved and forgetting the salary hours spent. The invoice is visible; the hours are not.

### The checklist

Before the next rebuild meeting:

- [ ] Write down the workflow's failure mode. Annoyed colleague: proceed. Lawsuit or audit: stop.
- [ ] Confirm the data lives in systems you control.
- [ ] Estimate hours/month of maintenance at 4 per agent, and name the owner.
- [ ] Compare total cost (build + ops + your hours) against the subscription, honestly.
- [ ] Decide the kill criteria up front: if the agent breaks N times a month after month three, back to the vendor.
- [ ] For anything customer-facing, keep the human path one click away. [Klarna relearned this](https://www.buildmvpfast.com/blog/replace-team-ai-agents-case-study-revenue-automation-2026) at seven figures.

### Close

Here's what I believe: the SaaSpocalypse is misnamed. Software subscriptions are in for a repricing, [usage and outcome models are coming](https://www.forbes.com/sites/timkeary/2026/06/30/the-saaspocalypse-maybe-ending-but-saas-will-never-be-the-same-again/), and headless APIs for agents will replace per-seat screens for a big class of tools. That's an evolution, and it punishes vendors whose product was a UI over commodity workflows. The actual apocalypse is quieter and internal: teams that rebuild without operators, wake up owning twenty fragile agents, and discover they've traded a predictable invoice for an unpredictable payroll. Rebuild the boring stuff you own. Keep renting the moats. Put a name on everything.

Sincerely,
Alexey

---

## Platform Deltas

**Substack (Alexey On Data):**
- URL: https://alexeyondata.substack.com
- Subtitle: 92.3% of engineers have tried to rebuild software they used to buy. The wave is real, the wins are real, and so is the bill that arrives three months later. A filter for what to rebuild, what to keep, and what to never touch.
- Paywall: place `[PAYWALL BREAK — free preview ends here]` after "The bill arrives three months later".
- Ends on the Sincerely / Alexey signoff.

**Medium:**
- 5 topic tags: Artificial Intelligence, AI Agents, SaaS, Software Engineering, LLM
- Member-only: no
- Ends on the community CTA: "Thanks for reading! If you found this useful, subscribe for more AI engineering deep dives..."

---

## SEO Keywords

- SaaSpocalypse
- rebuilding SaaS with AI agents
- AI agents replacing SaaS
- build vs buy AI
- internal tools AI agents
- agent maintenance cost
- SaaS pricing models AI
- agent ops
- in-house software AI 2026
- AI agent ROI

---

## Title & Subtitle Shortlist (for publish-time selection)

### Titles
1. The SaaSpocalypse Is Real. So Is the Maintenance Bill.
2. 92% of Engineers Are Rebuilding Their SaaS. Most Should Stop at the Boring Stuff.
3. Everyone Can Rebuild. Few Can Operate.
4. Build, Buy, or Bury: A Filter for the SaaSpocalypse Era
5. The Quiet Apocalypse: What Replacing SaaS With Agents Actually Costs

### Subtitles
1. 92.3% of engineers have tried to rebuild software they used to buy. The wave is real, the wins are real, and so is the bill that arrives three months later. A filter for what to rebuild, what to keep, and what to never touch.
2. From Mutiny's 12x rebound to Klarna's $2.3M refund incident: the rebuild economy, the maintenance math nobody posts about, and a three-gate filter.
3. Agents made rebuilding software cheap. Operating it did not get cheaper. How to choose what deserves the switch.
