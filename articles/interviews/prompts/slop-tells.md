# Slop Tells - What the Allergist Scans For

Source: Lieberman Content Machine [^1]

These patterns are the statistical center of LLM output. Any one of them appears in good human writing; the giveaway is the cluster and the density. The Allergist scores contamination, not individual sins.

Root cause: a model emits the mean of its training data and deploys rhetorical devices without taste. The fix is never word-swapping - it's taking a position, getting specific, and varying rhythm.

## Structural Tells

| Tell | Example | Why it reads as machine |
|---|---|---|
| Negative parallelism | "It's not about X. It's about Y." | The single most recognizable LLM cadence of this era |
| Tricolon addiction | "Faster, cheaper, and more scalable" | Rule-of-three deployed every third sentence |
| Bold lead-in bullets | "Speed: the system is fast" | Formatting doing the work thinking should do |
| Punchline appositive | "They're both right - and that's exactly the problem." | Setup-twist rhythm stamped from a mold |
| Symmetric paragraphs | Every paragraph 3-4 sentences, same shape | Humans write ragged; length should follow importance |
| The throat-clear open | "In today's rapidly evolving landscape..." | Zero information in the first 15 words |
| The summarizing close | "Ultimately, the key takeaway is..." | Restating a piece the reader just read |
| Hedge stacking | "could potentially help to somewhat improve" | One hedge is caution; three is no position at all |

## Vocabulary Tells

High-frequency LLM lexicon to avoid: delve, tapestry, landscape, leverage (verb), robust, seamless, unlock, elevate, journey, empower, foster, navigate (metaphorical), crucial, pivotal, game-changer, deep dive, at the end of the day, double-edged sword, treasure trove, testament to, boasts, vibrant, bustling.

Also: em-dash density far above the author's human baseline, semicolons in casual registers, "Moreover/Furthermore/Additionally" as paragraph glue.

## Rhythm Tells

- Uniform sentence length. Human writing has high variance - fragments next to long runs. Machine drafts cluster near the mean
- No fragments. People write fragments. Constantly
- Every sentence a complete thought politely delivered. No interruptions, no asides that trail off

## The Judgment Layer (What Regex Can't Catch)

1. No position. The piece surveys views and commits to none
2. Specificity vacuum. No names, numbers, dates, or quotes - nothing falsifiable
3. One point diluted into five. A strong claim padded with adjacent-but-weaker claims until nothing lands
4. Borrowed authority. "Experts agree," "studies show" - witnesses that don't exist
5. Rhetoric without stakes. Devices (questions, twists, callbacks) deployed decoratively, with nothing riding on them

## Scoring Guidance

- 0-1 surface tells and no judgment-layer failures: 9-10
- 2-3 surface tells OR one judgment-layer failure: 5-7
- 4+ surface tells OR two+ judgment-layer failures: 1-4

## Personal Calibration (Recommended)

The stronger setup is calibrating to your own baseline: measure your pre-AI writing (em-dash rate, sentence-length variance, favorite constructions) and enforce those numbers with a deterministic script.

## Sources

[^1]: https://github.com/derekcedarbaum2/content-machine/blob/main/reference/slop-tells.md
