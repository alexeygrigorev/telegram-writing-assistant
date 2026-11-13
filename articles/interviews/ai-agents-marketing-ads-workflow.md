---
title: "AI Agents for Marketing: Static Ads, UGC Video Ads, and the Full Workflow"
created: 2026-11-13
updated: 2026-11-13
tags: [research, marketing, ai-agents, ads, interviews]
status: draft
---

# AI Agents for Marketing: Static Ads, UGC Video Ads, and the Full Workflow

https://youtu.be/uJuxenfe-NU

Cody Schneider (Graft) walks through how to use coding agents (Claude Code, Grokbot, or any harness) to produce marketing creative at scale. The episode covers the full stack: data infrastructure, platform access, tool APIs, static ad generation, AI avatar UGC video ads, motion graphics, and the feedback loop that ties ad performance back to creative decisions.[^1][^2]

The core idea: all marketing is now code and tokens. The labor that used to require a graphic designer, a copywriter, a UGC creator, a video editor, and a motion graphics person can be handled by agents - as long as those agents have the right environment.

## The marketing environment

Before any creative gets made, the agent needs three things:

1. Data - access to business data from all sources
2. Platform access - ability to publish to ad platforms
3. Tools - APIs for image generation, video generation, voice cloning, transcription, and lead enrichment

Without this environment, agents either hallucinate on large data pulls, violate API terms of service, or produce generic output. The environment is the whole job - build it, and the agent becomes a top-tier marketer.

## Step 1: Set up the data infrastructure

### The problem with direct API queries

Agents querying ad platform APIs directly causes two problems:

- They send thousands of requests per second and get your account banned for violating terms of service
- They try to stuff large data pulls into context or build local databases with duplication errors

### The solution: data pipeline plus data warehouse

Build two things:

1. A data pipeline using Airbyte (open source). Airbyte connects to all data sources - Facebook Ads, Google Analytics, HubSpot CRM, payment processors - and streams data into the warehouse
2. A data warehouse using ClickHouse. All data from all sources lands in one place

The agent reads data only from the data warehouse. It never reads directly from ad platform APIs.

### Why a centralized warehouse matters

With all data in one place, the agent can trace the full path: ad impression to website visit to CRM entry to payment. It can answer questions like "which ad creative produces the highest customer lifetime value" - not just "which ad got clicks."

The warehouse syncs continuously in the background. The agent can query it as often as needed without hitting rate limits or violating any platform's terms of service.

## Step 2: Set up platform access (write-only)

The agent needs API access to ad platforms, but only for writes:

- Facebook Ads Marketing API - for uploading ad creative, turning off ads, moving ads between ad sets
- Google Ads API - same pattern

All data reads go through the data warehouse. The API connection is one-directional: write only.

This separation exists because agents behave like "drunk patrons at a restaurant" with APIs. They will send thousands of read requests and trigger account bans. The write-only pattern prevents this. Getting a Facebook Ads API token takes about 5 minutes using the Marketing API documentation.

## Step 3: Connect the tools

The agent needs API access to creative tools. The open source version means getting individual subscriptions:

- KAI AI - unified API for image generation models (ChatGPT Image 2.5, Nano Banana, others)
- Fal - voice cloning and transcription
- Open Router - LLM access
- GetLeads or Apollo - email data and person enrichment
- Seed Dance - AI video generation
- Tesseract (from Mirage) - video editing, motion graphics, captions

Each tool gets an API key. The agent uses these APIs to do the actual creative production work.

## Static ad creation workflow

This is the complete process for generating static image ads from scratch.

### Input

A single brand URL. Nothing else required.

### The process

1. Extract the brand style guide from the website - fonts, colors, visual identity
2. Check the Facebook Ads Library for the brand's existing ads (if any)
3. Research pain points and desired outcomes by extracting conversations from Reddit and social media
4. Propose five static ad concepts with headlines based on the research
5. Generate the actual ad images using ChatGPT Image 2.5 (via KAI AI)
6. Upload the finished ads directly to Facebook Ads via the Marketing API

### What the output looks like

For Idea Browser, the agent produced five concepts:

- "Stop guessing which idea to build" - every idea scored on demand, pain, and timing
- "Build what people already search for"
- "Your ChatGPT ideas are generic"
- "Don't waste 6 months on a dud"
- "1,948 ideas worth building"

Each concept becomes a rendered static ad matching the brand's visual style.

### Customization

You can provide a markdown file defining your brand style guide (fonts, colors, tone) as a skill file. The default workflow extracts this from the website, but a manual override produces more on-brand results.

You can also swap the image generation model. ChatGPT Image 2.5 produces the best results as of this recording, but KAI AI's unified API supports Nano Banana and others.

## UGC avatar ad creation workflow

This is the complete process for generating AI avatar video ads with voice, lip sync, and motion graphics.

### Step 1: Write the script

Start from the static ad concepts. The agent writes a UGC-style script based on the pain points and desired outcomes already researched.

### Step 2: Generate the audio

The script goes to Fal's voice clone API. The output is an MP3 file of the ad read. This is separate from the video generation.

Why separate audio first: sending just a script to Seed Dance produces garbled pronunciation. Pre-generating the audio with a voice clone gives clean enunciation.

### Step 3: Generate the video

Three inputs go to Seed Dance simultaneously:

1. The MP3 audio file
2. A reference image of the creator/avatar
3. The script text

The reference image controls what the avatar looks like. Without it, Seed Dance invents a random person. The reference image can be a real UGC creator photo that gets remixed - change the background, age, ethnicity, etc. Using a real human reference eliminates the "plasticky" look that pure AI-generated faces often have.

The output is a 480p video. Use 480p for cost efficiency - higher resolution (1080p) costs around $14 per video versus roughly $4-5 at 480p.

### Step 4: Verify pronunciation

The agent does word-by-word transcription of the generated video and matches it against the original script.

If a word is mispronounced (example: "Calendly" comes out as "Calenla"):

1. The transcript identifies the exact word that is wrong
2. The timestamps for that word are isolated
3. The agent generates the correct pronunciation
4. The correct audio replaces the mispronounced segment

This entire edit happens automatically within the agent workflow.

### Step 5: Upscale and polish

The 480p video gets upscaled and blur gets added using FFmpeg. The goal is a video that looks like a human filmed it on their phone.

### Step 6: Add captions and motion graphics

Tesseract (from Mirage) takes the word-by-word transcription and adds:

- Captions synced to the audio
- Motion graphics overlays
- Call-to-action elements
- Pop-up graphics at relevant moments

The agent can review the result frame by frame using a vision model and make alignment adjustments.

### Cost breakdown

The full UGC ad workflow costs approximately $4.75 per video at 480p. Motion graphics add a few more cents. Total per ad: roughly $5.

For comparison, the same ad made with a human UGC creator, video editor, and motion graphics designer costs $300-500 per video.

At scale: 10 ads cost $50. 100 ads cost $500.

## Quality control loop

For regulated markets (financial services, healthcare), add a review step between generation and publishing.

The process:

1. Agent generates the ad creative
2. A vision model reviews the creative against compliance rules - what can and cannot be said, what cannot be promised
3. If the creative fails: the vision model sends specific change requests back to the image generator
4. The image generator modifies the creative
5. The vision model reviews again
6. Loop continues until the creative passes

This typically converges in two to three iterations. ChatGPT Image 2.5 is good at making targeted modifications to existing images without remixing the whole thing.

## Human UGC creator hybrid workflow

AI avatars are not the only option. The same workflow works with real human creators, using agents as the coordination layer.

### Tools

- Tribe - UGC creator marketplace with API access
- Side Shift - another UGC creator network

### The process

1. The agent generates the script (same as the AI avatar workflow)
2. The script gets sent to human UGC creators via the Tribe or Side Shift API, along with a brief and creative direction
3. Creators film and submit their videos (example rate: $40 per video)
4. The agent adds motion graphics and captions to the human-created video using Tesseract
5. The finished ad gets uploaded to the ad platform

The agent acts as the creator manager - a role that previously required a dedicated person handling relationships, briefs, and review cycles.

## The creative velocity strategy

Facebook's Andromeda algorithm matches creative to buyers automatically. The algorithm is better at audience targeting than any human. The bottleneck is creative volume.

The strategy:

- Ship cohorts of 30 ads at a time
- Each ad might get two conversions at a low cost, then Facebook stops spending on it because it found the people who convert
- The next cohort picks up new audience segments
- Companies that shipped 10 ads per month move to 300

The formula for how many ads to ship depends on ad budget and cost per lead. More budget means more ads in each testing cohort.

## The data feedback loop

Every ad generation call is a JSON blob sent to an API. Store that JSON blob in a database. This creates a cellular-level breakdown of every creative decision.

The loop:

1. Generate ads (store the generation parameters)
2. Upload to Facebook Ads
3. Performance data flows back through Airbyte into ClickHouse
4. The agent queries the warehouse to find which creative parameters correlate with revenue and customer lifetime value
5. Future ad generation uses those insights

At 1,000 ads, this dataset becomes a competitive advantage. The agent can answer: "when we use this style of headline with this visual approach, we get higher lifetime value customers."

## The swipe warehouse

Traditional swipe files (collections of ad inspiration) are not enough at AI scale. You need thousands of examples.

Tools for building a swipe warehouse:

- Sublime.app
- Cosmos
- Facebook Ads Library scraping (built into the static ads workflow)

Feed the swipe warehouse into the agent as context. The more examples of effective creative the agent has, the better its output. For the creative direction step, ingesting advertising books (David Ogilvy's work, for example) and transcripts of top creative directors gives the agent a foundation in advertising principles.

## Tool summary

| Category | Tool | Purpose |
|----------|------|---------|
| Data pipeline | Airbyte | Connect all data sources, stream into warehouse |
| Data warehouse | ClickHouse | Central store for all business data |
| Image generation | ChatGPT Image 2.5 (via KAI AI) | Static ad creative |
| Video generation | Seed Dance | AI avatar video ads |
| Voice cloning | Fal | Ad read audio generation |
| Video editing | Tesseract (Mirage) | Motion graphics, captions, long-form editing |
| LLM routing | Open Router | Multi-model LLM access |
| Lead enrichment | GetLeads, Apollo | Email data, person data |
| UGC creators | Tribe, Side Shift | Human creator marketplaces with API access |
| Ad platforms | Facebook Ads Marketing API, Google Ads API | Write-only ad management |
| Agent harness | Grokbot, Claude Code, Dots | The coding agent that runs the workflows |
| Managed platform | Graft | All-in-one marketing engineering cloud (optional) |

## The managed alternative

Graft (graft.com) packages all of the above - data pipeline, warehouse, platform access, tool APIs, skill files - into a single platform. Free to start. Supports multiplayer (multiple team members using their own agent harnesses against shared infrastructure). The skill files demonstrated in the episode are available through the Graft CLI.

Everything shown in the episode can be built from open source components. Graft is the shortcut for getting started in 10 minutes instead of assembling the pieces yourself.

## Sources

[^1]: [20261113_074858_AlexeyDTC_msg5057.md](../../inbox/used/20261113_074858_AlexeyDTC_msg5057.md)
[^2]: YouTube: https://youtu.be/uJuxenfe-NU
