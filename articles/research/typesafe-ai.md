---
title: "Jev: A Decision Model That Does Not Generate Text"
created: 2026-09-18
updated: 2026-09-18
tags: [research, ai-models, typesafe, jev, system-one, structured-output, inference]
status: draft
---

# Jev: A Decision Model That Does Not Generate Text

https://typesafe.ai/

If you have been to X in the last few days, chances are that you have seen posts about Jev. In fact, every time I open my timeline, I see people making posts about it.

https://x.com/CompleteSkeptic/status/2099925682726002904

Recently [the model was released on OpenRouter](https://openrouter.ai/typesafe/jev-1.13), so I decided to give it a try. 

In this post I want to talk about this model and a quick experiment I did with it - using it as an agent hands-off router. 


## Jev and TypeSafe AI


TypeSafe AI appeared on September 15, 2026 (came out of steath) with Jev 1.13. Jev doesn't generate text. When I first read the announcement I was like "Huh? No text?". But after reading a few posts, I quickly realized that it could be quite useful for quick decision making.

The model is a text classifier - you give it text, and it can very quickly make a decision based on that. This makes it a perfect router:

- Should I send this request to a heavy model or a light one?
- Which agent should I select? 
- TOOD another one? 

[TypeSafe calls Jev a "System One Model"](https://typesafe.ai/blog/introducing-system-one-models-and-jev). They took the name from "Thinking, Fast and Slow" (I read it, interesting ideas, but very long and boring book). System 1 is the fast, intuitive judgment your brain makes without effort. System 2 is slow, deliberate reasoning. So, Jev is System 1, and LLMs are System 2. Or, in other words, it's a very smart if statement.


## The API

You send Jev one request containing two things:

- a state (unstructured text or a JSON object describing the situation)
- a set of typed questions

Jev answers all questions in parallel and returns structured JSON with probability distributions.

There are three question types ([TypeSafe calls them "primitives"](https://docs.typesafe.ai/primitives)):

- Noul: a yes/no question. Returns a single probability from 0 to 1. "Does this message request a refund?" might return `0.93`. Think binary classifier.
- Choice: pick one option from a set. Returns the selected option, a probability distribution across all options, and a confidence score. Up to 255 options per question. Think multiclass classification. 
- Score: position on an ordered scale you describe. Returns a weighted score, the distribution across levels, and confidence. Between 2 and 10 levels. Think TODO.

Here is how it looks based on their docs:

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "is_urgent": { "type": "noul", "noul": 0.93 },
    "department": {
      "type": "choice",
      "choice": "billing",
      "probabilities": { "billing": 0.84, "technical": 0.15, "sales": 0.0, "other": 0.01 },
      "confidence": 0.6
    },
    "frustration": {
      "type": "score",
      "score": 1.3,
      "probabilities": { "0": 0.0, "1": 0.7, "2": 0.3 },
      "confidence": 0.54
    }
  }
}
```

TODO: describe it.

In our code we can now use it to make decisions:

```python
urgency = answers["is_urgent"]["noul"]
departament = answers["department"]["choice"]
departament_confidence = answers["department"]["confidence"]

if urgency > 0.8 and departament == "billing":
    escalate_to_billing()
elif departament_confidence < 0.5:
    route_to_human()
```

## Benchmarks

[TypeSafe built a benchmark suite](https://evals.typesafe.ai/) of four business workflows to show how it works:

- security incident triage
- agent trace observability
- invoice processing
- customer service

Each model ran through the same workflow harness, and results were compared against a reference policy derived from the average judgments of GPT-6 Astra and Claude Fable 5.1.

| Workflow | Cases | Jev accuracy | Jev cost | Jev latency | Nearest comparator |
|----------|-------|-------------|----------|-------------|-------------------|
| Security incidents | 240 | 61.7% | $0.0001 | 0.3s | Opus 66.2% at $0.0574, 15.1s |
| Agent trace observability | 117 | 71.6% | $0.0003 | 0.5s | Sol 76.6% at $0.0575, 40.3s |
| Invoice processing | 150 | 61.8% | $0.0011 | 0.5s | Sol 79.1% at $0.2152, 34.3s |
| Customer service | 204 | 76.0% | $0.0001 | 0.4s | Sol 78.3% at $0.0323, 10.1s |
| Aggregate | 711 | 67.8% | $0.0004 | 0.4s | Sol 74.1% at $0.0836, 23.3s |

A separate [code-review benchmark by an independent developer](https://github.com/gemanor/jev-code-review-benchmark) compared Jev against Gemini Flash and Claude Fable on Python linting rules.

- Jev cost 45x less than Gemini Flash and 274x less than Claude Fable.
- Its median response time was 0.75 seconds (vs 3.59s for Flash and 4.31s for Fable).
- Jev scored 98% correctness versus 100% for both comparators.


## Applications People Have Built

I have seen a lot of stuff on X of what people did with Jev over the last few days.

Self-Driving Simulations

- A 2D top-down browser simulation where Jev acts as the driving classifier, receiving road state and making steering decisions. Source: https://github.com/vinilana/live-jev
- A 3D Three.js driving simulator with autopilot. Jev receives a compact JSON snapshot of current speed, speed limit, next turn distance, nearby vehicles and pedestrians with relative positions and speeds, traffic signals, and predicted hazards. It returns a typed driving decision. Source: https://github.com/standardagents/jevdrive
- An interactive playground with 3D driving simulations showing real AI decisions with visible sensor inputs. Source: https://github.com/kavehmz/typesafe-playground

### Games

TypeSafe's demo showed that the model can play Doom, and the cost is around $7 per hour. (TODO link)

People also made it play chess:

- Jev vs OpenAI model. Source: https://github.com/wondertwins/jev-benchmark
- Two Jev instances playing against each other. Source: https://github.com/TholeG/typesafe-chess


Other games:

- NPC demo tested whether Jev could decide which characters should respond when a player speaks aloud through speech-to-text. The game engine sends the transcript and NPC descriptions, and Jev decides which NPC the player is addressing. (TODO source)
- demonstrated Wikiracing - navigate from one Wikipedia page to another using only links on each page. Jev had to choose among hundreds or thousands of links per page. (TODO source)

## Use Cases for Jev

Jev is not a replacement for LLMs. It is a layer before.

[TypeSafe's documentation describes several ways to use it](https://docs.typesafe.ai/patterns):

- TODO ? same as next? Routing: set thresholds for automatic action, LLM escalation, and human review based on Jev's confidence scores
- Intent routing: use Jev to classify user intent, then dispatch to different handlers
- Fan-out: run multiple Jev questions in parallel speculatively, then pick the path that applies (TODO example)
- Composite scoring: split complex judgments into independent Score questions and combine them in code (TODO example)


It can also act as a guardrail. We have a workshop in AI Shippings Labs about guardrails where we describe that a guardrail is a binary classifier. This classfier can be Jev.


