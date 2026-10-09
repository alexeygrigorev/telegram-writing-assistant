# Lessons Loop

Source: Lieberman Content Machine [^1]

The reinforcement loop that makes the machine improve with use. Every edit you make is a training signal, captured as prose rules the drafting step must obey on all future pieces.

## Inputs

- The machine's draft (from `drafts/`)
- The final version you actually published or approved
- Any verbal feedback you gave along the way ("this line is AI-cringey")

## Steps

### 1. Diff

Compare draft vs. final, sentence by sentence. Collect: deletions, rewrites, reorderings, additions.

### 2. Abstract

Turn each meaningful change into a generalizable rule, categorized:

- Tone - register errors ("too breathless", "false modesty")
- Structure and flow - ordering, pacing, where the piece sagged
- Language - specific words or constructions the user removes on sight
- Format - platform-specific habits (fold behavior, line breaks, emoji)

The abstraction test: would this rule have prevented the edit AND apply to future pieces? One-off factual fixes are not lessons.

Not a lesson: "Changed 'six months' to '6 months'." (one-off formatting preference)

Too vague: "Make it sound more natural." (unenforceable)

A real lesson: "TONE - Never use the setup-punchline construction 'They're both right - and that's exactly the problem.' User flags this cadence as AI-cringe. State the tension directly instead."

### 3. Approve - never auto-append

Present the proposed lessons as a numbered list. The user approves, rejects, or edits each. Only approved lessons are written. A lessons file polluted with wrong rules degrades every future draft.

### 4. Append

Add approved lessons to `content-lessons.md` under their category, dated. Check for contradictions with existing lessons - if a new lesson contradicts an old one, surface the conflict and ask which wins. Never hold both.

### 5. Confirm

Report what was appended and the new lesson count per category.

## Gate

The loop is complete only when:

- Diff performed
- Lessons proposed with categories
- User explicitly approved
- File appended
- Contradictions resolved

If the user gave feedback mid-draft ("that hook is cheesy") that didn't make it into a lesson, ask about it here. Spoken feedback that evaporates is the loop's failure mode.

## Sources

[^1]: https://github.com/derekcedarbaum2/content-machine/blob/main/skills/lessons/SKILL.md
