---
title: "Research: Free / Cheap LLM Access (Sep 2026)"
created: 2026-09-09
tags: [research, free-tiers, cheap-llm, list]
source: Grok `algrigor-thread` (20260909_190301) + `cheap-llm-ways-sep09` (20260909_190304)
request: Alexey — research socials for free/cheap LLM ways; his thread as starting point only
---

# Free / cheap LLM access, Sep 2026

## From @Al_Grigor thread (x.com/Al_Grigor/status/2096543638687756663, ~Sep 6-9)
Original question (quoted @enjojoyy): "What do I do to have unlimited tokens"
Thread's own list:
- 3 Codex resets
- Free Muse 3 on OpenCode Zen; very cheap Muse 3 / Omen Alpha on OpenCode Go
- Unlimited glm-5.3-flash on chat.z.ai (plans from 5pm every day, 10-hour windows)
- Hy3 free on multiple platforms
- Follow-up: ChatGPT limits independent from Codex limits; GitHub PRs from ChatGPT
Replies: @Bechamle "Muse 1.3 is seriously the best tool out there"; @PastorSotoB1 switching OpenCode free models + Antigravity; @lylytrann206 glm-5.3-flash free window saves students money. Other replies: questions/comments only.

## Free API tiers (X viral thread x.com/0xbobaaa/status/2083562067613667668 Aug 1; HN id=47821043; kdnuggets)
- **Groq**: no CC; Llama-3.1-8B ~30 RPM / 14,400 RPD / 6k TPM / 500k TPD; 70B-class (Llama-3.3-70B, GPT-OSS-120B, Qwen) ~30 RPM / 1,000 RPD / 100-200k TPD; dynamic per key (visible in headers)
- **OpenRouter :free**: one key, many models (DeepSeek, Qwen, Gemma-4 26B/31B, Nemotron, Ling-3.0 Flash); ~20 RPM / 50 RPD; ~1k RPD after $10 top-up; congestion on popular routes. x.com/exploraX_/status/2083611421464531043
- **NVIDIA NIM/Build**: 40+ RPM, 40+ open models (Nemotron 3, DeepSeek Flash, GLM), often no CC/phone
- **Google AI Studio / Gemini API**: Flash ~15 RPM / 1,500 RPD; free tier data may train models
- **Cerebras**: ~1M tokens/day GPT-OSS-120B (wafer-scale); trial-like, some models paywalled recently (samuel.town/blog/free-models-14-days)
- **Others**: Cloudflare Workers AI (~10k neurons/day), Mistral, Cohere, Hugging Face, GitHub Models, SiliconFlow, LLM7.io, Bytez (100k+ models), Pollinations (no-auth unlimited some)
- **Directories**: freeinference.dev, freellm.net (verified daily), GitHub xyzs996/free-llm-api (28k+ stars, 426 commits)

## Free chat tiers
ChatGPT free, Gemini (praised, generous), Grok (X, rate-limited), Claude free, DeepSeek/GLM/Kimi/Mistral chats; Chinese models top usage charts (x.com/samchbe/status/2096901352676876395)

## Coding agents / deals
- Tencent Hy4 (770B open) free tier on WorkBuddy/CodeBuddy (x.com/NewsTongueX/status/2094130979677892841)
- Trial credits: Modal/Baseten $30, Scaleway/DeepSeek $5-30; cloud startup/student credits

## Local (truly free)
- r/LocalLLaMA Aug 2026 recs: Qwen3.6/3.8 27B (24GB VRAM), DeepSeek V4 Flash 0731, Gemma-4, LFM2.5; 1-8B at 100+ tok/s on 6-8GB VRAM (RTX 4050 benchmarks); 3090/3080/M4 Macs; Ollama + LM Studio dominant; llama.cpp MTP acceleration
  reddit.com/r/LocalLLaMA/comments/1vkmhyl/best_local_llms_august_2026/

## Cheap paid + discounts
- OpenRouter routes to cheapest providers; DeepSeek/Qwen cheapest $/1M; 33x cost variance by call shape (HN id=49586810)
- Batch/off-peak/prompt-caching: barely discussed in Sep free-tier threads (free tiers dominate the conversation); DeepSeek off-peak discounts exist

## Caveats
Limits fluctuate; free pools congest; some models paywalled mid-Sep; don't abuse (community explicitly warns tiers die from abuse)
