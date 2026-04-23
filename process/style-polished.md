# Polished Writing Style

Voice, tone, and prose rules for polished article content (newsletter-ready pieces, research articles, anything beyond raw-curation output). Agents should read this before preparing a final version of any article.

Inherits from `process/style-curation.md` - every rule there (no bold/italic, no horizontal rules, banned words, sentence structure, active voice, no "Additionally/Moreover" openers, etc.) also applies here. This file adds the voice-and-tone layer on top.

## Voice and tone

- Write in first person, conversational - like talking to a friend, not presenting to an audience
- Use contractions naturally: "don't", "I've", "we're", "it's", "wouldn't" - not "do not", "I have", "we are"
- Avoid phrases that sound like a sales pitch or marketing copy: "Now for the fun part", "on the table", etc. (But these articles are marketing content, so CTAs like "subscribe" or "follow along" are fine)
- Prefer direct statements over framing devices. Instead of "One benefit of a private community: you can share things you would not discuss publicly" write something like "A private community also means you can talk about things you wouldn't bring up publicly"
- Don't over-explain or over-sell. State what it is and move on
- Use "we" when talking about shared efforts, "I" when talking about personal decisions

## Structure

- Put "who this is for" early - readers want to know quickly if it's relevant to them
- Don't use "Part 1" / "Part 2" labels - just use regular headers, let the content flow
- Flat header structure (## level) for main sections, ### only when truly nested (like subsections within a technical walkthrough)
- Don't start headings with question words like "Why", "How", "What", "When". Rewrite as a statement instead. "Why This Matters" -> "RAG Beyond Q&A"; "How the Bot Got Built" -> "Building the Bot"
- Prefer lists over inline prose when the content is already list-like. If a sentence packs several items together with commas or "and", convert them to a bullet list
- Avoid walls of text - break up long paragraphs. Use lists, shorter paragraphs, or illustrations between dense sections
- No paragraph should be longer than 3-4 sentences. If it is, split it or convert part of it to a list
- Alternate between prose and structured elements (lists, tables, illustrations) to keep the reader moving
- Paragraphs should connect to each other - if two consecutive paragraphs feel disconnected, add a bridge sentence or restructure
- Sections should also connect to each other. At the start of a long article, give a short map of what is coming - which sections cover which groups of things, and how those groups relate. When moving from one section to the next, add a short bridge that reminds the reader where they are and what comes next. Sub-sections inside a section should relate to each other clearly, not read as separate fragments
- Place content in the section where it logically belongs. If a paragraph answers "why something new" it goes in that section, not in "the problem"
- Use `<!-- illustration: description -->` comments to break up dense sections and give the reader visual breathing room

## Lists and tables

- Use bullet lists for activities, features, course ideas - anything where the reader wants to scan
- Use tables for comparisons and pricing
- Use numbered lists for sequential processes (like build steps)
- Break long paragraphs into lists when there are 3+ items buried in prose
- Keep descriptions short and direct - one line per item
- When telling a story with multiple steps or threads (like "first X, then Y, then Z"), convert to a list instead of a run-on paragraph
- Use lists for problems/complaints too ("The agents made decisions I didn't agree with:" + list)

## Describing features and courses

- Keep descriptions short and practical - what you learn, not why it's important
- Bad: "becoming a good product manager for AI agents, because when the specification is not good, the agent produces garbage"
- Good: "how to write clear specifications and manage a team of AI agents"
- Make it clear when things are plans, not commitments: "These are ideas, not promises"

## Expanding on a topic

When going deeper on something, follow this pattern:

1. Personal motivation first: "I get asked for mentoring all the time. I usually say no because I don't have the bandwidth"
2. The insight: "what most people actually need is not a mentor - they need an accountability structure"
3. The solution, described concretely
4. What the reader gets out of it: "Plus you also learn a lot from each other"

## Addressing the reader

- Write for a specific reader. For technical articles, assume a developer who can read code and diagrams but does not have time to investigate the project themselves - you are doing that investigation on their behalf
- Address the reader as "you", not "the user". Instead of "A user sends a message on Telegram" write "You can talk to Hermes through Telegram". Instead of "The user swaps providers" write "You can swap providers"
- Every technical detail must connect to what it means for the reader. A sentence that only lists structure ("the agent directory holds domain components, the tools directory holds 47 tool files") is not finished until you explain what those components do and why the reader should care
- When mentioning a file, folder, or component, briefly say what role it plays in the whole system and what it lets the reader do

## Technical writing

- Do not anthropomorphize products, projects, or frameworks. Phrases like "OpenClaw asks, what is the permanent structure that owns the assistant?" or "Hermes answers with..." do not make sense - a project cannot ask or answer. Describe what the project is and how it works directly
- Avoid hype phrases, unnatural framings, and filler that sounds like marketing copy or AI-generated summary. "A conversation turn in Hermes is mostly a prompt building exercise followed by a provider-agnostic tool loop" is the kind of sentence to avoid - say it in plain terms, like "Each turn in Hermes builds a prompt, then runs a tool loop that works with any provider". Write like a person explaining the system to a colleague, not like a system summarizing itself
- When introducing a technical term (e.g., "frozen identity vs mutable identity", "manifest-first", "hub-and-spoke"), define it briefly in plain language on first use. Assume general software-engineering knowledge but not familiarity with the project's docs
- If a term is uncommon or project-specific, say so and give a short concrete meaning. For example: "Frozen identity means you cannot change the system prompt mid-conversation; mutable identity means you can." Tie the definition back to what the reader can or cannot do because of it

## Things to avoid

- Forced transition phrases: "Now for the fun part", "Let me expand on a few of these"
- Starting paragraphs with rhetorical questions ("And why not just...?", "But what about...?") - make a statement instead
- Naming specific people as examples in public articles
- Idioms that feel unnatural: "on the table", "at the end of the day"
- Over-formal framing: "The idea:", "The idea was", "The result:", "One benefit of X is Y", "I want to be clear:", "X is a reminder that Y" - any phrase that announces what you're about to say before saying it, or that frames a point instead of making it. Just say it directly.
- Redundant sentences that repeat what the previous sentence just said
- Repetitive descriptions across sections (e.g. describing the same thing in both an overview and a detail section)
- Internal positioning language in public articles ("the focus is narrow on purpose") - the reader doesn't care about your strategy, tell them what they get
- "need" when "may need" is more accurate and less presumptuous
- Overly wordy constructions when a simpler verb works: "I've had this idea for a long time to X" -> "I wanted to X for a long time", "I'd already described" -> "I already described"
- Walls of text - dense paragraphs without visual breaks
- Incomplete or fragment sentences used for dramatic effect ("An AI community platform, built by AI agents.") - use proper sentences. Also applies to hanging phrases like "Same approach as the other projects, one difference", dropped subjects ("Can't install plugins" -> "I can't install plugins"), and "Not X, but Y" constructions used as standalone sentences ("Not for simple pages, but for complex projects." -> "It's for complex projects where you can't just start a session and go."). Always use full sentences with subjects and verbs.
- "ceremony" and similar jargon ("pull request ceremony")
- "do" for emphasis before verbs ("Or you do start" -> "Or you start")
- Trailing comma + single word at the end of a sentence for emphasis ("build something together, live" or "ship it, fast") - feels unnatural
- Long sentences with dash-enclosed clarifications in the middle ("A project like this - with all the integrations, the course management - would take...") - one dash in a sentence is usually fine, but two dashes creating a parenthetical is a problem. Split into shorter sentences or drop the clarification
- Punctuation inside quotes when the quote is not a full sentence: use "platform". not "platform."
- "have the same story" - prefer "share the same story"
- "building with AI" is ambiguous (building using AI tools vs building AI products) - be specific about which one you mean
- When listing overview bullets then expanding each one below, don't repeat the same information - the overview is a table of contents, the expanded sections add new detail
- Awkward "X is what you'll ..." / "X are what you'll ..." constructions when a simpler sentence is clearer. Instead of "Scripts are what you'll write for most of the course" write "You'll write a lot of scripts in this course"

## Formatting rules

Base formatting rules (no bold/italic, no horizontal rules, spaces around dashes, etc.) live in `process/style-curation.md`. Additional rules specific to polished articles:

- DataTalks.Club (with dots) is the correct spelling
- Use straight quotes (' and ") not curly/smart quotes
- Include `<!-- illustration: description -->` comments where images should go
- Don't touch existing `<figure>` blocks when editing - leave illustrations as they are
