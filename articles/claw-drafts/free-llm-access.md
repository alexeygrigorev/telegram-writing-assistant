---
title: "Free and Affordable AI-Native Development"
subtitle: ""
---

I recently posted on X that we have access to so many tokens that I'm running out of ideas what to build.

https://x.com/Al_Grigor/status/2096543638687756663

At DataTalks.Club we're running AI Dev Tools Zoomcamp and people are asking me where they can get access to coding agents for free or without paying a lot of money. So I figured that I should write a post and share what I use.

While I do recommend getting a paid Codex or Claude subscription and use it for the course, there are some other providers that can get you a lot of tokens for less money or even for free. 

In this post, I'll share some of them. We'll cover

- Free coding plans
- Cheap coding plans
- Current promotions

Let's go


## Free coding plans

There are multiple platforms that currently offer free coding plans. 

One of them is Tencent. They recently released Hy3 and offer a free tier through its [WorkBuddy](https://www.workbuddy.ai/) and [CodeBuddy](https://www.codebuddy.ai/) assistants. It's not available in Germany, so I couldn't try it - but maybe it'll work for you.

Another one is [OpenCode Zen](https://opencode.ai/zen). They have a variety of models absolutely for free. One of these models is Muse 3 from Meta.

<figure>
  <img src="../../assets/images/free-llm-access/llm-zen-free.png" alt="OpenCode Zen pricing table showing free models including Big Pickle, MiMo-V2.5, Ling 3.0 Flash, Nemotron 3 Ultra, Nemotron 3.5 Lightning, and Muse Spark 1.3 Contributor Free, all with free input, output and cached read pricing">
  <figcaption>OpenCode Zen free models - Muse Spark 1.3 Contributor Free included</figcaption>
</figure>

The full name for this model is "Muse Spark 1.3 Contributor Free". The "contributor" part here means that you're "contributing" your data to meta, so they can use it to improve their model. That's why it's free - you pay for it with your data.

For me it's not a concern. It's quite a powerful model, it feels like Opus 5 level. I can have one or two heavy coding sessions with Muse 3 in OpenCode Zen for free.

Once I hit the limits, I can stay in OpenCode and switch the session to OpenCode Go - their coding plan.

## Affordable coding plans

[OpenCode Go](https://opencode.ai/go) costs $10 per month. For this $10 you get a lot. Specifically, you get the same Muse 3 Contributor, although without the "free" part.

Again, it's a contributor model, so meta is subsidizing 90% of the cost - at least this is what they say. And you can get a lot done with this model. Combine it with 1-2 free sessions from OpenCode Zen, and you'll get 5+ hours of work per day with this plan.

And there are other models, like DeepSeek V4.1 Flash, which currently offers 75% discount (i.e. 4x more usage).

<figure>
  <img src="../../assets/images/free-llm-access/llm-go.png" alt="OpenCode Go usage chart showing estimated requests per 5 hours: Kimi K3 at 110, Kimi K2.7 Code at 1,350, GPT 5.6 Luna at 2,050, MiniMax M3 at 3,200, Qwen3.7 Plus at 4,300, GLM-5.3-Flash at 6,320, DeepSeek V4 Flash at 13,000, DeepSeek V4.1 Flash at 26,000 with 4x usage tag, MiMo-V2.5 at 30,100, Muse Spark 1.3 Contributor at 45,300">
  <figcaption>OpenCode Go usage estimates - DeepSeek V4.1 Flash at 26,000 requests per 5 hours with 4x usage, Muse Spark 1.3 Contributor at 45,300</figcaption>
</figure>


I used to recommend GitHub Copilot as the first coding plan. Not anymore - now it's OpenCode Go.

Other cheap alternatives in the same $8-20 range:

- [ChatGPT Plus](https://openai.com/chatgpt/pricing/) ($20)
- [Z.ai GLM Coding Plan Lite](https://z.ai/subscribe) ($18)
- [MiniMax Token Plan](https://platform.minimax.io/subscribe/token-plan) ($20)
- [Command Code GOAT](https://commandcode.ai/docs/plans/goat) ($10)

One more fresh release: Cognition, the makers of Devin, just launched [SWE-2](https://cognition.com/blog/swe-2) on September 10. It scores 50.0% on FrontierCode 1.1, within a point of Fable 5.1 at 64% lower cost, and it's a post-train of the open-weight Kimi K3. The catch: no public API price, you can only use it inside Devin (Desktop and CLI now, Web soon). So it's not a cheap path yet, but if Devin pricing follows the model cost down, it'll belong in this list.

Prices and quotas change fast, so check the current plan pages.
 

## Cheap API access 

So far we talked about coding plans. Instead, you can pay for API calls yourself and plug any API LLM platform to your coding agent. 

If you do that directly with OpenAI or Anthropic and put $5 into your account, they will disappear before you can say "hello" to your coding agent.

But if you use [DeepSeek's V4.1 Flash](https://api-docs.deepseek.com/quick_start/pricing) during off-peak hours, you'll be getting millions of tokens, which is enough to do multiple coding sessions.

Also, [OpenRouter](https://openrouter.ai/discover) gives access to many free and cheap models. Any model ID ending in `:free` costs zero tokens, but the rate limits are very strict. Once you pay, the limits for free models become less strict.  

<figure>
  <img src="../../assets/images/free-llm-access/llm-open-router.png" alt="OpenRouter most-used free models ranking by weekly tokens: Nemotron 3 Ultra free at 3.6T tokens per week with 1M context, Laguna S 2.1 free at 1.2T with 262K context, Nemotron 3.5 Lightning free at 958.4B with 1M context, Ling 3.0 Flash Fin free at 881.5B with 262K context, Dots3-Note Preview free at 397.9B with 512K context">
  <figcaption>Most-used free models on OpenRouter by weekly tokens - Nemotron 3 Ultra leads at 3.6T</figcaption>
</figure>


## Current promotions


I really like Z.ai. I have used them since September last year through their API, and I've been using their plan since December.

Now they are regularly running promotions and giving away 300 million tokens for glm-5.3-flash. You have to use their [Zcode harness](https://zcode.z.ai/en), and the promotions are typically timed for weekends. Many people complain that these tokens expire before they can spend them.

https://x.com/zcode_ai/status/2098396306750517317

Additionally, right now they are running [a promo for all Z.ai coding plan subscribers](https://docs.z.ai/devpack/notice/event-glm-5.3-flash). If you're one of them, you get unlimited glm-5.3-flash tokens from 5pm to 3am CET.

<figure>
  <img src="../../assets/images/free-llm-access/llm-zai-campaign.png" alt="Z.ai campaign details: every day from 23:00 to 09:00 the following day, GLM-5.3-Flash through GLM Coding Plan - use via ZCode means zero quota consumption for unlimited usage, use via other supported agents means available quota is doubled">
  <figcaption>Z.ai evening promo rules - zero quota consumption via ZCode, doubled quota via other agents</figcaption>
</figure>

Well, they aren't completely unlimited - there are rate-limits. But I don't hit these limits unless I run 20+ agents in parallel.

<figure>
  <img src="../../assets/images/free-llm-access/llm-zai-glm53-flash.png" alt="Z.ai usage trends bar chart for September 5-11 showing total 9.7B tokens, almost all GLM-5.3-Flash at 9.7B with GLM-5.3 at only 10.5M tokens">
  <figcaption>My Z.ai usage for the week - 9.7B GLM-5.3-Flash tokens</figcaption>
</figure>

That plus 300m tokens plus their quota reduction if you use Zcode - that combined gives you a lot of tokens.

One downside of Zcode is that it's GUI only, no TUI. But I figured out how to [connect it to Codex](https://github.com/alexeygrigorev/codex-zcode/), so I can run ZCode from my terminal.

Z.ai is not the only company that runs promos. There are others:

- Tencent Cloud TokenHub gives every new account 1M free tokens per model, covering DeepSeek V4 Pro/Flash, GLM-5, MiniMax M3 and Kimi K2.6.
- Verdant currently offers GLM 5.3 Flash and DeepSeek V4 Flash for free within 5-hour and weekly limits.
- Cursor doubled included usage for its first-party models (Auto, Composer 2.5) on paid plans.
- Cognition (the company behind Devin) just released a new model SWE-2 and they made it unlimited in Devin paid plans.


## Build more

With all these free models and promotions I no longer have a problem of having no tokens. My main problem is deciding what to build next.

I hope you'll have the same problem. Have fun and enjoy building!


## Tools

<figure>
  <img src="../../assets/images/free-llm-access/llm-oto-dock.png" alt="OtoDock GitHub hero: blue robot logo, 'OtoDock - Collaborative Agents', tagline 'The agentic company OS', subtitle 'The brains of your company, built on Claude Code and Codex, working on your Anthropic and OpenAI subscriptions', badges for FSL-1.1-Apache-2.0 license, version 1.6.0, passing CI, docs and website links">
  <figcaption>OtoDock - the agentic company OS built on Claude Code and Codex subscriptions</figcaption>
</figure>

I haven't included the section with new tools for quite some time. Now I want to fix it. 

* **[engrim](https://github.com/timgordontg/engrim)**: a local-first SQLite memory engine that keeps one project-scoped episodic store across Antigravity, Claude Code, Cursor, Windsurf, and Codex. With their approach it's very easy to switch models in the middle of a session, and you don't need to send the whole session transcript when doing it.
* **[oto-dock](https://github.com/OtoDock/oto-dock)**: "The brains of your company, built on Claude Code & Codex, working on your Anthropic and OpenAI subscriptions." It's a self-hosted company OS where agents organized in departments connect to company tools, delegate to each other, and keep working unattended. I'm experimenting with automating as much of DataTalks.Club ops as I can, and this project looks promising.  
