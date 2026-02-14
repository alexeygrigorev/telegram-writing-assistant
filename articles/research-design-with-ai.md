---
title: "Design with AI: Beating the Default Look"
created: 2026-02-14
updated: 2026-02-14
tags: [research, design, ai, ui, claude-code, vibe-coding]
status: draft
---

# Design with AI: Beating the Default Look

Research into producing high-quality interface design with AI coding tools. The core problem: AI models generate generic-looking UI that screams "AI made this." This research covers a structured approach to overcoming that default behavior through design skills, intent-driven workflows, and systematic design memory.

## What I Want to Understand

How to get AI-generated UI that does not look like slop. What principles and prompting strategies produce professional-quality interfaces instead of the same generic Material Design / Bootstrap / shadcn template every time.

## Resources

### Reddit: "I Condensed Years of Design Experience into a Single Skill"

Source: https://www.reddit.com/r/vibecoding/comments/1r1vhee/

A post by user dammyjay93 on r/vibecoding (232 upvotes) presenting an "interface-design" skill that encodes years of professional design knowledge into a reusable AI skill file. The author claims it produces significantly higher baseline design output that you can iterate from, rather than starting from a generic template every time.

The skill works with Cursor, Claude Code, and Antigravity. It is installable via `npx skills add` or as a Claude Code plugin. The project has 3,200 GitHub stars and 3,300 weekly installs across multiple AI coding tools (OpenCode, Gemini CLI, Codex, GitHub Copilot, Kimi CLI, Amp).

Community feedback highlights:

- Multiple users confirm noticeable improvement over default AI-generated UI
- One user noted it "absolutely took it up a level" for a proof of concept application
- Feedback request: a visual inspection mode using Playwright or browser agents to audit and recommend UX layout improvements
- Suggestion to add ADA accessibility law compliance to the skill
- Some users reported strangely placed buttons and unclear UX flow, showing the skill is not a silver bullet
- Responsive layout handling remains an open question, especially for complex dashboard-style interfaces

### The Interface-Design Skill (Full Analysis)

Source: https://skills.sh/dammyjay93/interface-design/interface-design
GitHub: https://github.com/dammyjay93/interface-design

This is the complete skill file that gets loaded into AI coding assistants. It is essentially a long design brief that changes how the AI approaches UI generation. The skill targets dashboards, admin panels, SaaS apps, tools, settings pages, and data interfaces. It explicitly excludes landing pages and marketing sites.

### The Core Problem It Addresses

The skill opens with a direct statement: "You will generate generic output. Your training has seen thousands of dashboards. The patterns are strong." The gap between stated design intent (described in prose) and actual code generation (which pulls from trained patterns) is where defaults win. Process alone does not guarantee craft. The AI has to catch itself.

### Where Defaults Hide

The skill identifies four areas where AI models default without realizing it:

1. Typography feels like a container. The AI picks "something readable" and moves on. But typography IS the design. A bakery management tool and a trading terminal both need "clean, readable type" but the type that is warm and handmade is not the type that is cold and precise.

2. Navigation feels like scaffolding. The AI builds a sidebar, adds links, and considers it done. But navigation IS the product. It teaches people how to think about the space they are in.

3. Data feels like presentation. The AI has numbers, so it shows numbers. But a progress ring and a stacked label both show "3 of 10" - one tells a story, one fills space.

4. Token names feel like implementation detail. But `--ink` and `--parchment` evoke a world. `--gray-700` and `--surface-2` evoke a template. Someone reading only the CSS variables should be able to guess what product this is.

The trap: thinking some decisions are creative and others are structural. Everything is design. The moment you stop asking "why this?" is the moment defaults take over.

### Intent-First Design Process

Before touching code, the skill requires answering three questions out loud:

1. Who is this human? Not "users" but the actual person. Where are they? What is on their mind? A teacher at 7am with coffee is not a developer debugging at midnight.

2. What must they accomplish? Not "use the dashboard" but the specific verb. Grade these submissions. Find the broken deployment. Approve the payment.

3. What should this feel like? Not "clean and modern" (every AI says that). Warm like a notebook? Cold like a terminal? Dense like a trading floor? Calm like a reading app?

If you cannot answer these with specifics, stop. Ask the user. Do not guess. Do not default.

### The Sameness Test

The skill introduces a powerful heuristic: "If another AI, given a similar prompt, would produce substantially the same output - you have failed." This is not about being different for its own sake. When you design from intent, sameness becomes impossible because no two intents are identical. When you design from defaults, everything looks the same.

### Product Domain Exploration

Before proposing any visual direction, the skill requires producing four outputs:

1. Domain - concepts, metaphors, vocabulary from the product's world (minimum 5)
2. Color world - what colors exist naturally in this product's domain? If this product were a physical space, what would you see?
3. Signature - one element (visual, structural, or interaction) that could only exist for THIS product
4. Defaults - 3 obvious choices for this interface type that you explicitly name so you can avoid them

The test: read your proposal, remove the product name. Could someone identify what this is for? If not, it is generic.

### Craft Foundations

The skill lays out specific technical principles:

Surface Elevation: Surfaces stack with whisper-quiet lightness shifts (a few percentage points). In dark mode, higher elevation equals slightly lighter. Sidebars should use the same background as canvas with a subtle border, not a different color. Inputs should be slightly darker than surroundings (they are "inset").

Borders: Low opacity rgba that blends with the background. Build a progression of intensity matched to importance. The squint test - blur your eyes at the interface, you should still perceive hierarchy but nothing should jump out.

Infinite Expression: Same concepts (sidebar, cards, metrics) have infinite variations. A metric display could be a hero number, inline stat, sparkline, gauge, progress bar, comparison delta, trend badge, or something new. Linear's cards do not look like Notion's. Vercel's metrics do not look like Stripe's.

Color: Every product exists in a world with colors. Before reaching for a palette, spend time in the product's world. Temperature is one axis but also consider: quiet or loud? Dense or spacious? Serious or playful? Geometric or organic?

### Design Token Architecture

Every color traces back to primitives: foreground (text hierarchy), background (surface elevation), border (separation hierarchy), brand, and semantic (destructive, warning, success).

Text hierarchy needs four levels - primary, secondary, tertiary, muted. Using only two makes hierarchy too flat.

Depth strategy: pick ONE approach and commit. Borders-only (clean, technical), subtle shadows (soft, approachable), layered shadows (premium), or surface color shifts.

### The Mandate (Quality Gates)

Before showing the user, the skill requires running four self-checks:

1. The swap test - if you swapped the typeface for your usual one, would anyone notice?
2. The squint test - blur your eyes, can you still perceive hierarchy?
3. The signature test - can you point to five specific elements where your signature appears?
4. The token test - read your CSS variables out loud, do they sound like they belong to this product?

### Design Memory System

The skill saves design decisions to `.interface-design/system.md` which loads automatically in every new session. This file stores: direction and personality, depth strategy, spacing base unit, color palette, and exact component measurements. This prevents the common problem of design decisions drifting across sessions (button heights going from 36px to 38px to 40px, random spacing values appearing).

### Comparison Dashboard

Source: https://interface-design.dev/examples.html

The project includes 16 showcase examples demonstrating the skill applied to different product domains:

- Support Desk with AI-drafted responses
- Film production crew management
- Web3 wallet connection
- Rich text editor with AI originality scoring
- Domestic violence case management
- Project management with sprint timelines
- Product analytics with AI-powered insights
- Employee onboarding
- Finance portfolio dashboard
- Wellness coach practice management
- API test factory
- EdTech teacher dashboard
- Job application form
- Bakery order queue management
- Family meal planner
- Game studio bug tracker with RPG-inspired UI

Each example demonstrates how the same underlying principles produce visually distinct interfaces when applied to different domains.

## Key Insights

1. The AI default problem is real and well-understood. Most AI models (Gemini being a partial exception) produce generic-looking UI because their training data contains thousands of similar dashboards. The patterns are so strong they override stated intent.

2. Design intent must be systemic, not decorative. Saying "warm" and using cold colors is not following through. If the intent is warm, surfaces, text, borders, accents, semantic colors, typography must all be warm. Intent is a constraint that shapes every decision, not a label.

3. The gap between prose and code is where defaults win. You can describe a design perfectly in words, but code generation pulls from patterns. Bridging this gap requires explicit checkpoints before every component.

4. CSS variable naming is a design decision. `--ink` and `--parchment` create a world. `--gray-700` and `--surface-2` create a template. This is a surprisingly effective lever.

5. Concrete visual references beat abstract descriptions. Instead of "make it modern and clean," screenshot 2-3 real products you like and say "match this density, this color temperature, this type scale."

6. Design memory compounds over time. Saving decisions to a system file that loads automatically prevents drift and makes each session faster and more consistent.

## Actionable Patterns

1. Before any UI generation, force the AI to produce four outputs: domain concepts, color world, signature element, and named defaults to avoid. Do not let it skip this step.

2. Use the swap test on every generated UI: could you swap the typeface, layout, or color scheme for a generic alternative and nobody would notice? If yes, you have not made real choices.

3. Name your CSS variables after the product's world, not generic scales. This single change shifts the entire mental model during generation.

4. Pick one depth strategy (borders-only, subtle shadows, layered shadows, or surface shifts) and commit to it throughout the interface. Mixing approaches signals no system.

5. Install the interface-design skill for Claude Code or similar tools to get these principles automatically applied: `npx skills add https://github.com/dammyjay93/interface-design --skill interface-design`

6. For every component, require the AI to state: intent, palette, depth, surfaces, typography, and spacing choices with explicit WHY for each before writing code.

7. Save design decisions to a persistent file (system.md pattern) so they survive across sessions.

## Sources

[^1]: [Reddit post: "I condensed years of design experience into a single skill"](https://www.reddit.com/r/vibecoding/comments/1r1vhee/)
[^2]: [Interface-design skill on skills.sh](https://skills.sh/dammyjay93/interface-design/interface-design)
[^3]: [GitHub repository: dammyjay93/interface-design](https://github.com/dammyjay93/interface-design)
[^4]: [Interface-design examples dashboard](https://interface-design.dev/examples.html)
[^5]: [Interface-design.dev project page](https://interface-design.dev/)
[^6]: [20260214_063929_AlexeyDTC_msg1658.md](../inbox/used/20260214_063929_AlexeyDTC_msg1658.md)
