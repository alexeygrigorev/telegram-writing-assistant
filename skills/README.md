# Reference Skills

Skills kept here as reference examples for content workflows. Most were saved from other people's packaged skills to study their patterns; `recap-the-series` is one we authored ourselves after actually running the workflow once. Not active skills for this repo's bot - they live here so we can study and reuse the patterns later.

## shoot-the-article

A skill that drafts a long-form article for Vadym Grin's Eidos Design (Substack) and Medium, end to end, plus its companion social posts. It arrived as a packaged `.skill` file (a zip); the unpacked contents are stored here.

The part worth reusing is its research workflow: `references/research.md` is a playbook for scanning the design community as it is right now (designer Substacks, design publications, LinkedIn design leaders, Hacker News / Reddit, Product Hunt and AI tool radars), then turning what is being argued about into a few sharp article angles with a quality bar each angle must pass. That is a concrete template for doing research on interesting topics across social media before writing about them.

Contents:

- `SKILL.md` - the end-to-end workflow: kickoff questions, research, template + outline, section-by-section drafting, final draft with platform deltas and SEO, then the social posts
- `references/research.md` - where to research, source URLs, topic-quality heuristics, the angle-presentation format
- `references/voice.md` - banned patterns, positive signatures, the signoff and CTA, a pre-delivery self-check
- `references/structure.md` - the four article templates with word counts and annotated scaffolds
- `references/social.md` - teaser and announcement social post templates for LinkedIn, X, and Threads

## recap-the-series

A skill for drafting a condensed "recap"/"intro" article that summarizes an existing multi-part series - written after actually doing this for the *AI Dev Tools Zoomcamp* series' Article 0. The first attempt regenerated the series' content from scratch and read as generic; the rework that worked instead copies the source articles' real prompts verbatim, flags what needs to change (app-specific vs. tool/stack-specific), builds the draft as a bullets-plus-transitions skeleton before any prose, and only then hands it to a pinned-model rewrite pass via the `prose-write` subprocess pattern.

Contents:

- `SKILL.md` - the full workflow: copy-don't-regenerate, the two axes of "does this need to change," filling tool-choice gaps, the bullets/transitions skeleton, choosing a new running example, and the final prose handoff (including a real failure mode to avoid: never let the rewrite subprocess write the target file directly)

## scan-the-tools

A weekly digest skill authored after running the workflow for real on 2026-09-04: scans the past 7 days of open-source AI engineering tool releases (agent harnesses, MCP tooling, evals, context/memory, inference/serving, coding agents; tools only, no models) via the x.ai Grok search over X/Reddit plus the HN Algolia Show HN feed, verifies GitHub repos, and writes the digest as a ready-to-paste "Tools" section formatted exactly like the Tools sections in Alexey's Substack articles (`reference/substack/*.md`): bold linked tool name, lowercase one-line "a X that ..." description, concrete numbers, and a usefulness line.

Contents:

- `SKILL.md` - the weekly workflow: date anchoring, the Grok query template, the HN Show HN script, selection criteria (OSS only, repo link required, visible traction), the strict Tools-section format spec, output path `clo/digests/<date>-tools.md`, and the Russian chat-summary report format
