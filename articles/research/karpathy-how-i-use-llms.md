---
title: "Karpathy: LLM Knowledge Bases - Building Personal Wikis with LLMs"
created: 2026-04-06
updated: 2026-04-06
tags: [research, llm, ai, knowledge-management, obsidian]
status: draft
---

# Karpathy: LLM Knowledge Bases

Andrej Karpathy describes a pattern for using LLMs to build and maintain personal knowledge bases. Instead of traditional RAG (retrieve and generate on every query), the LLM incrementally compiles raw sources into a persistent, interlinked wiki of markdown files. The wiki is the artifact - it compounds over time, and the LLM does all the maintenance work that humans typically abandon.[^1][^2][^3]

## What I Want to Understand

How to use LLMs not just for code generation but for knowledge management - building structured, persistent knowledge bases that compound over time. What makes this different from RAG, and what are the practical workflows for implementing it.

## Resources

### Karpathy Tweet: LLM Knowledge Bases

Source: https://x.com/karpathy/status/2039805659525644595

Overview: Karpathy shares that a large fraction of his recent LLM token usage goes into manipulating knowledge (stored as markdown and images) rather than code. He describes a workflow where source documents are indexed into a raw/ directory, then an LLM incrementally compiles a wiki of .md files with summaries, backlinks, categories, and concept articles.

Key Ideas:
- Data ingest: source documents (articles, papers, repos, datasets, images) go into a raw/ directory. The LLM then "compiles" a wiki - a collection of .md files in a directory structure with summaries, backlinks, categories, and concept articles
- Obsidian serves as the IDE "frontend" for viewing raw data, the compiled wiki, and derived visualizations. The LLM writes and maintains all wiki data - the human rarely touches it directly
- Once a wiki reaches sufficient size (example: ~100 articles, ~400K words), you can ask complex questions against it. The LLM researches answers across the wiki without needing fancy RAG
- The LLM auto-maintains index files and brief summaries, which works well at small scale for navigation and retrieval
- Output formats include markdown files, slideshows (Marp format), and matplotlib images - all viewable in Obsidian
- "Filing" query outputs back into the wiki means explorations and queries always compound in the knowledge base
- LLM "health checks" over the wiki find inconsistent data, impute missing data with web searches, and find interesting connections for new articles
- The natural next step is synthetic data generation and finetuning to have the LLM "know" the data in its weights instead of just context windows

### Karpathy Gist: LLM Wiki Pattern

Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Overview: A detailed idea document describing the LLM Wiki pattern. Designed to be copy-pasted to your own LLM agent (Claude Code, Codex, OpenCode, etc.) so the agent can instantiate the pattern for your specific domain. The document is intentionally abstract - it describes the pattern, not a specific implementation.

Key Ideas:
- Traditional RAG rediscovers knowledge from scratch on every question. There is no accumulation. NotebookLM, ChatGPT file uploads, and most RAG systems work this way
- The wiki is a persistent, compounding artifact. Cross-references are already there, contradictions are already flagged, synthesis reflects everything read so far
- Three-layer architecture: raw sources (immutable, never modified by LLM), the wiki (LLM-generated and LLM-maintained markdown), and the schema (a config document like CLAUDE.md or AGENTS.md that defines conventions and workflows)
- The schema is the key configuration file - it makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve it over time
- Two special navigation files: index.md (content-oriented catalog of everything) and log.md (chronological append-only record of ingests, queries, lint passes)
- The index-based approach works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure

Key Insights:
- The core problem with traditional wikis is not reading or thinking - it is the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs do not get bored and can touch 15 files in one pass
- The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else
- Good answers to queries should be filed back into the wiki as new pages. This means explorations compound just like ingested sources do
- The pattern is related to Vannevar Bush's Memex (1945) - a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became. The part he could not solve was who does the maintenance

Actionable Patterns:

Three core operations:
- Ingest: drop a source into raw/, tell the LLM to process it. The LLM reads it, writes a summary, updates the index, updates relevant entity and concept pages. A single source might touch 10-15 wiki pages. Can be done one at a time (supervised) or batched (less supervision)
- Query: ask questions against the wiki. The LLM searches relevant pages and synthesizes answers with citations. Answers can be markdown pages, comparison tables, slide decks, charts. Important - file good answers back into the wiki
- Lint: periodically health-check the wiki. Look for contradictions, stale claims, orphan pages, missing concepts, data gaps. The LLM suggests new questions and sources to investigate

Use cases:
- Personal: goals, health, psychology, self-improvement - structured picture built over time from journal entries, articles, podcast notes
- Research: going deep on a topic over weeks or months - papers, articles, reports compiled into a comprehensive wiki with evolving thesis
- Reading a book: chapter-by-chapter wiki with characters, themes, plot threads - like building a personal fan wiki
- Business/team: internal wiki fed by Slack threads, meeting transcripts, project documents, customer calls
- Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives

Technical Details:

Recommended tools:
- Obsidian as the IDE frontend for viewing and browsing the wiki
- Obsidian Web Clipper browser extension for converting web articles to markdown
- Download images locally: Obsidian Settings, Files and links, set "Attachment folder path" to a fixed directory (e.g. raw/assets/). Bind "Download attachments for current file" to a hotkey (e.g. Ctrl+Shift+D)
- Marp plugin for Obsidian for rendering slide decks from markdown
- Dataview plugin for running queries over page frontmatter (tags, dates, source counts)
- qmd (github.com/tobi/qmd) for local search over markdown files - hybrid BM25/vector search with LLM re-ranking, has both CLI and MCP server
- The wiki is just a git repo of markdown files - version history, branching, and collaboration come for free

Log format trick:
- Start each log entry with a consistent prefix like `## [2026-04-02] ingest | Article Title`
- This makes the log parseable with simple unix tools: `grep "^## \[" log.md | tail -5` gives the last 5 entries

LLM image handling workaround:
- LLMs cannot natively read markdown with inline images in one pass
- Have the LLM read the text first, then view referenced images separately for additional context

Quotes:
- "raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian"
- "The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you have read."
- "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs do not get bored, do not forget to update a cross-reference, and can touch 15 files in one pass."
- "I think there is room here for an incredible new product instead of a hacky collection of scripts."

## Notes

- This pattern is highly relevant to how this very telegram-writing-assistant project works - raw inbox items are processed and compiled into articles. The key difference Karpathy highlights is making the LLM responsible for maintaining cross-references and consistency across all articles, not just processing individual items
- The three-layer architecture (raw sources, wiki, schema) maps well to the inbox/articles/CLAUDE.md structure already in this project
- The "lint" operation is an interesting idea - periodically asking an LLM to health-check all articles for consistency, contradictions, and gaps
- Related to context engineering research - the schema file (CLAUDE.md / AGENTS.md) is essentially context engineering for the wiki maintenance agent

## Sources

[^1]: https://x.com/karpathy/status/2039805659525644595
[^2]: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
[^3]: [20260406_071234_AlexeyDTC_msg3211.md](../../inbox/used/20260406_071234_AlexeyDTC_msg3211.md)
