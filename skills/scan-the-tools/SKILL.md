---
name: scan-the-tools
description: Weekly digest of NEW open-source AI engineering tools (agent harnesses, MCP tooling, evals, context/memory, inference/serving, coding agents), pulled from live social signal (Grok over X/Reddit + HN Show HN), written as a ready-to-paste "Tools" section in Alexey's Substack format. Triggers - "weekly tools digest", "new AI tools this week", "tools section", "scan the tools", any request for a recurring OSS tools roundup.
---

# Scan the Tools — Weekly OSS Tools Digest

Produce a weekly digest of **new open-source AI engineering tools** (tools and infrastructure, **not models**) that gained real traction in the past 7 days on X/Twitter, Reddit, and Hacker News. The output document is formatted exactly like the **Tools sections of Alexey's Substack articles** (`reference/substack/*.md`), so it can be pasted into a future article with zero rework.

## Scope

**Include:** agent harnesses/runtimes, MCP servers/proxies/tooling, agent evals and observability, context engineering and memory tools, LLM inference/serving/routing, RAG pipelines, fine-tuning tooling, coding agents, orchestration, LLM security/policy layers.

**Exclude:** model releases and weights (separate topic), closed SaaS with no repo, non-AI tools, anything older than ~3 weeks unless it just got a major update or viral spike.

**Hard requirement per tool:** a real GitHub (or equivalent) repo link, verifiable. Verify the top picks exist (fetch the repo page or `git ls-remote`) before including.

## Workflow

### 1. Anchor the window

Check the current date first (`session_status`). The scan window is the **past 7 days**. Always put "September 2026"-style anchors in queries; unanchored searches return stale results.

### 2. Grok social scan (primary)

```bash
cd ~/git/ai-engineering-field-guide && python3 interview/_internal/xai_search.py \
  'Current date <DATE>. Find NEW open-source AI engineering tools and technologies (NOT models) released or trending in the past 7 days on X/Twitter, Reddit (r/LocalLLaMA, r/MachineLearning, r/MCPservers), and Hacker News. I want GitHub repos: agent frameworks and harnesses, LLM inference/serving tools, eval and observability tools, context engineering and memory tools, MCP tooling, RAG pipelines, fine-tuning tools, coding agents, agent orchestration. For each tool: what it does, GitHub link, why it is gaining traction right now, where it is being discussed (specific X handles/threads, HN links, Reddit threads), stars if known' \
  --tools web_search,x_search --label 'oss-tools-<yyyymmdd>'
```

### 3. HN Show HN scan (secondary)

```python
# past 7 days, Show HN, AI/agent/LLM queries, points > 30
import json, urllib.request, time
week_ago = int(time.time()) - 7*86400
for q in ['Show+HN+AI', 'Show+HN+agent', 'Show+HN+LLM', 'Show+HN+MCP']:
    url = f'https://hn.algolia.com/api/v1/search?query={q}&tags=show_hn&hitsPerPage=12&numericFilters=created_at_i>{week_ago},points>30'
    data = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=10).read())
    for h in sorted(data['hits'], key=lambda x: x['points'], reverse=True)[:8]:
        print(f"[{h['points']}pts {h['num_comments']}c] {h['title']}"); print('   ' + (h.get('url') or ''))
```

### 4. Cross-check and select

Keep 5-10 tools that appear across at least one Grok citation **and/or** a HN/Reddit thread with visible traction (points, upvotes, engagement). Note the pattern of the week (what category dominates) for the chat summary, and save raw notes to `clo/research/oss-tools-<date>.md` if not already there.

### 5. Write the digest in Substack Tools-section format

Save to `clo/digests/<YYYY-MM-DD>-tools.md`. Format copied from the real sections (see `reference/substack/2026-03-20-i-turned-my-telegram-bot-into-a-multi.md`, `2026-02-13-what-is-an-ai-engineer-in-2026-join.md`):

```markdown
## Tools

Week of <Mon date> – <Sun date>. One sentence on the wave of the week. *(optional headline paragraph for the single hottest tool)*

* **[ToolName](https://github.com/org/repo)**: a {category noun} that {what it does in one clause}. {2-4 sentences of standout features with concrete numbers and named differentiators}. {Usefulness line: "It's useful for ..." or "Could be useful for ..."}
* **[NextTool](...)**: ...
```

Format rules, strict:

- Bullet list with `*`, tool name **bold** and linked to the repo, then a colon
- Description starts lowercase: "a document processing library that..."
- Concrete numbers beat adjectives (12MB binary, 5-13x fewer tokens, 30-75% cheaper)
- End each entry with the practical use ("It's useful when/for...")
- When a person surfaced the tool, add "Resource shared by <name> from <community>."
- Optional closing line: "Edited by <name>." only if there is an editor
- English only; no category headings inside the section (his sections are flat lists); no "Signal:" metadata lines in the document, keep discussion links for the chat summary

### 6. Ship and report

1. Commit digest + any new research notes to `telegram-writing-assistant` and push.
2. Reply to Alexey in Russian: the wave-of-the-week pattern, the tools (names + repos + one-liners), where each is being discussed, and the file path.
3. Note in the daily memory file that the digest ran.

## Voice notes for the entries

Match the tone of the reference sections: plain, specific, practical. Describe what the tool actually does and the standout detail, never "revolutionary/seamless/powerful". One extended differentiator per tool is enough; skip tools you can't say something concrete about.

## Run cadence

**Scheduled: every Thursday 09:00 Europe/Berlin** via OpenClaw automation `Weekly tools digest` (`openclaw automations`, isolated session, delivers to Alexey's Telegram). The scan window is the previous Thursday through Wednesday night. Can also run on request ("tools digest", "что нового из инструментов").
