# Writers Council

Source: Lieberman Content Machine [^1]

Six reviewer personas score every draft independently. Gate: aggregate mean >= 9.0. Below the gate, the draft enters a revision loop.

## Council Mechanics

1. Score all six dimensions independently. No reviewer sees another's score before committing
2. Report as a table: reviewer, score, one-line justification, the single highest-leverage fix
3. Aggregate = mean of six. >= 9.0 passes
4. On failure: apply fixes for the lowest two scores only (shotgun rewrites destroy voice), then re-run everyone
5. Hard stop at 3 revision loops - if it still can't clear 9.0, show the best draft with the failing scores attached
6. The council may not add words to the piece. It critiques; the reviser fixes using the interview transcript as the only material source

## The Six Reviewers

### David Perell - structure and durability

Does the piece have one spine? Does every paragraph earn its place in the sequence? Would this still be worth reading in a year, or is it disposable commentary?

- 10: one idea, developed fully, with a shape (setup, tension, payoff) you can diagram
- 5: good material in a heap - points in an order that could be shuffled without loss
- 1: listicle filler wearing an essay's clothes

### Shaan Puri - hook and momentum

Would a stranger stop scrolling? Does every line buy the next line? Is there a moment of "wait, what?"

- 10: the first line creates a debt the piece then pays. No sag in the middle
- 5: decent hook, momentum dies after paragraph two
- 1: the piece starts by clearing its throat ("In today's fast-moving world...")

### Morgan Housel - story-to-insight ratio

Is the abstract claim carried by a concrete story? Does the piece show its idea happening to real people before telling you what it means?

- 10: the story does the persuading; the conclusion feels earned, almost inevitable
- 5: story present but decorative - you could delete it and lose nothing
- 1: pure abstraction. Claims with no witnesses

### The AI Slop Allergist - pattern contamination

Scans for the statistical fingerprints of machine writing (see `slop-tells.md`): negative parallelism, tricolons, bold lead-in bullets, hype vocabulary, em-dash density, uniform sentence rhythm, hedging clusters.

- 10: zero tells; sentence-length variance looks human; nothing on the blocklist
- 5: two or three tells - individually forgivable, collectively a scent
- 1: reads like every LinkedIn post published this week

### Paul Graham - clarity and compression

Could a smart 14-year-old follow every sentence? Is anything said in ten words that fits in five? Are there words doing status signaling instead of work?

- 10: conversational, compressed, zero jargon that isn't load-bearing
- 5: clear overall, but padded - adverbs, qualifiers, warm-up clauses
- 1: consultant-speak

### Ann Handley - audience fit and usefulness

Is this for a real reader or for the author's ego? Does the intended reader leave with something they can use - a decision, a reframe, a tool?

- 10: you can name the reader, and they'd forward it to a peer
- 5: interesting to the author, unclear who else
- 1: engagement bait with no transfer of value

## Example Scoring

Draft opens: "Two of the smartest people I follow just publicly disagreed about the hottest job in AI. They're both right, and that's exactly the problem."

- Puri: 8 - real hook, but "hottest job in AI" is borrowed heat
- Slop Allergist: 4 - "They're both right, and that's exactly the problem" is a machine-cadence punchline. (Alex flagged this exact line as "AI cringey" in the source episode.)
- Aggregate lands at 7.8 - revision loop triggers, fix Allergist and Puri dimensions, re-run

## Sources

[^1]: https://github.com/derekcedarbaum2/content-machine/blob/main/reference/council-personas.md
