# How to Do Evals in 2026
## A tool-agnostic framework for evaluating AI agents


[IMAGE: Diagram showing the three layers of agent evaluation: final answer quality, trajectory quality, and system behavior, with feedback arrows from production back to test cases]
Caption: 1. Final answer quality. 2. Trajectory and tool-call quality. 3. System behavior (cost, latency, safety). Production feedback loops feed all three.

I have a dataset with 4,894 AI engineering job descriptions that I scrape and analyze for the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide). The most common 

It also shows from the interviews side. If you interview for AI engiieering role you will be asked "how do you evaluate a RAG pipeline?", "how do you measure agent performance?". Hiring managers say that having no evals for your home assigniment is a red flag. 

It's very easy to build an agent these days. There are many frameworks that make it super simple (my favorite one is [Pydantic AI](https://ai.pydantic.dev/)). But testing and evaluating them is not that easy. it takes a lot of time to undestsand the problem (you can't just delegate all that to an agent) collect the right data, collect the data from users, etc () 

TODO describe why we need to care about evals.

You also need to evaluate the agent from the right (surface?). You can check if the answer is good. That's the simplest. But was the answer achieved in an optimal way. You also need to evaluate the journey, not just the destination.

There are many things that we can borrow from traditional SWE. 

Equivalence partitioning,
boundary testing,
integration tests,
regression suites.



These patterns transfer to agents. This guide shows how, tool-agnostic and framework-agnostic, across the three agent patterns you're most likely shipping: coding agents, RAG agents, and workflow/task agents.


## Evaluation set

You build an agent. What's next. (also think where to link my course https://aishippinglabs.com/courses/aihero)


TODO we also need to say somehwere that if you have a working systme from which you can sample questions from the live system. And you should use them. If you already have that, you probably can skip this section and go to the next one. Always take real user input if you alreayd have a system that can supply them. 

If you're just starting with an agent, ther'es nothing wrong with "vibe" evaluation: you poke it, ask questions you want it ot answer, and check the results. If they aren't good, you figure out how to fix it. You always need to do this at the beginning. 

But from the first moments you can be a bit more organized and start logging this data.

You do your vibe check session, and then look at the logs. 

To help me to it, I usally vibe-code a small tool for viewing them. I mark "good" or "bad". Do it for 10-15 examples. Now you have your v0 of the gold standard dataset (also know as "ground truth").

Then you look at the logs for the bad ones. You try to figure out what's wrong. Then you try to fix your agent when you do it, you use the dataset you collected previously and make sure good stay good and bad turn into good. 

I find it helpful to still do it manually. It's only a few examples and you can qiuckly go though them and see if good ones are still good, and if bad ones are fixed. 

At the beginning I recommend doing it manually because you get a lot of insights into how your agent is behaving.

## Alignment 

At this point you can ask Claude Code or Codex to also analyze the logs and ask them to classify the examples into good or bad. Ask the agent how it does it and see if it matches with your reasoning. If it doesn't, you figure out why. Maybe you missed something. Maybe agent didn't have enough context. But you iterate until you both agree. 

How I do it: 

- Point the agent to the logs and ask to classify each into good or bad
- Try to undestand the decisions and learn from them
- Ask the agent to create judge.md file that will describe the classification rules
- Inspect the file to see that the rules are generic and not specific to the examples you have in the dataset
- Ask the agent to laynch a subagent and use the judge.md file to do the evals
- You iterate until you both align on what's good and bad

This process is called "alignment" and you used the coding agent as a judge.

## Borrowing from QA 


The data you produced while vibe-checking is okay but it's not complete. Now we need to find cases that break our system. 

QA engineers have been breaking software for many decades. For coming up with cases we can borrow some concepts from their frameworks. 

1. Equivalence partitions

The first step is [equivalence partitioning](https://www.ministryoftesting.com/software-testing-glossary/equivalence-partitioning).
You divide the input space into groups where inputs within each group should produce similar behavior.

For a RAG agent that answers questions about your documentation, it could be:

- questions about topics in the documentation,
- questions about relevant topics not in the documentation,
- questions about irrelevant topics,
- ambiguous questions,
- questions with multiple valid answers,
- questions in different languages

You can ask AI to help you define these groups.

Next, for each group, come up with 2-3 questions. After that, run all these questions through your agent.

Use the coding agents and the judge.md file to classify them into good or bad, but make sure you check them manually too. 

I typically take the vibe-coded evalaution tool I create earlier and adjust it os it can also support cehcking the decisions from the judge. If in some cases you don't agree with the judge, you can conitnue the alignment process and tune it to be more argreable. You will never have 100% alignment, so don't be too strict about having judge always agreeing with your decision. The judge should be correct most of the time though. 


2. Boundary testing.

https://www.ministryoftesting.com/software-testing-glossary/boundary-testing

The previous questions rpobably already identified some gaps in your agent. 
But we can be even more agreessive into our testing. 

Test the boundaries of each partition. For a RAG agent:

- a query that exactly matches a document title (easy case),
- a query that's semantically related but uses different words (typical case),
- a query that's semantically related to multiple documents (ambiguous case), and a query that's completely off-topic (boundary case).


3. Define Corner cases

These are combinations of boundary conditions.

- A user asks an off-topic question in a language the agent partially supports.
- A user provides context that conflicts with the documentation.
- A user asks a follow-up question that changes the topic mid-conversation. 

These are the scenarios that break in production, and they're almost never in your test suite.

Here's what this looks like in practice, for the three common agent patterns:

RAG agent test cases:

- Direct factual question from the documentation (happy path)
- Question that requires synthesizing information from multiple documents (integration)
- Ambiguous term with multiple meanings (boundary, like the word "judge" meaning both a legal official and an LLM evaluation pattern)
- Completely off-topic question (corner case)
- Question with context that should personalize the answer (boundary, like "I have a dataframe with columns X, Y, Z")
- Question in a different language (corner case)
- Follow-up question that changes topic mid-conversation (trajectory check)


Add these questiosn to your gold standard dataset.

You will probably have 50-60 questions from the users. Run your agent, test it against the judge. You can still do throug them and check them manuaully. 

By now you have a judge that is aligned to your deccisions

so you can start improving your agent. here you can also ask your AI assistnat to help:

- point to the dataset you have 
- say you want to improve it

follow the [implementer-tester split](https://alexeyondata.substack.com/p/ai-native-development-specifications): don't do them in the same agent context. 

define the implementer that will tune the agent
define the tester that will use the judge to evaluate it
iterate until your "good" ratio is acceptable


## Start testing on real users asap 

We have evaluated our agent on 50-60 cases and it's good enough to give us some confidence that it's working okay.

But I also want to test it on more data. If you have a real system, sample the data from there. If you don't, you can already deploy and start collecting data. You don't have to roll this feature out to all the users. You can do it to 0.1% of them. Or get test subjects. Ask your friends and family to use it. Share it on social media and ask peole to use the system. 

## Synthetic data


In parallel to that, you can generate more data using AI. You can describe your system, describe your target users, and ask it to generate quesitons that these users will ask.

If you're testing a RAG system, you can

- Take a document from your knowledge base
- Ask AI to come up with 5 questions based on this document
- Do it for all documents (or a sample)

You will end up with a lot of questions. You can keep all of them, or sample. You can ask AI to compare these quesitons with your existing gold standard dataset and select ones that are not similar to the existing ones. 

Your want to have a big variety of test cases and in many numbers. Here you want quantity. When you expose your agent to a bigger number of inputs, things will break - just statistically with more repetitins you increase changes of something going wrong.

So yo utest your system on a big number of test cases and you see where things get wrong. Your agent can start looping without finishing, (add other problems). You want to use the synthetic data to surface cases like that. If you managed to find a case that causes the agent to behive strangely - analyse the behavior, see how you can fix it, add it to your gold standard, and make sure when you fix your agent, it doesn't degrade the performance for the rest of the test cases.  

You don't use synthetic data to replace real user data. You use it to generate a lot of examples, hoping that at least a fraction of them will cause your agent misbehave. 

But that's not a replacement for logs from real users. 

## LLM-as-a-Judge: ongoing evaluation

So far we used a coding agent to do the evals. It's okay but not scalable. At some point you will want to create a special agent - a judge that will evaluate the perfomance of your agent in real-time, so you don't have to run your coding agent for that. 

- Run the system
- Run the judge on all the traffic (or on a sample)
- Display the judge eval metrics on the dashboard
- Pay attention to bad results, inspect them periodically and add them to your goold standard
- Also sample good results to make sure they are actually good

For inspecting good and bad results I often use coding agents. I find them quite powerful so I take a bunch of logs and ask Codex or Claude to go throgh them with me. 


## What else to evaluate

We defined only "good" or "bad" output. I dind't really describe what it is becaues it can vary from project to project.

In practice we can have several categoies of "good/bad" output.

SO we can evaluate the agent from differnt angles:

- the final result of the agent matches our expectation
- no hallucination - the result is actually grounded in the documents that exist in our database
- the trajectory (the steps the agent used to arrive to the final result) is optimal
- did the agent follow the instructions correctly?
- TODO: what else? the system? 

For the last one: cases where agent can break

- give wrong answer
- hallucinate
- loop with tool use, call the same tool over and over again
- exhaust the context (so needs stoping)
... what else?

TODO probably we should put it at the beginning?


### The agent evaluation checklist

TODO: update it based on the article I wrote
TODO: also add some actionable things to do in sections before 

A copy-pasteable checklist for evaluating your agent before shipping and in production.

**Before shipping (offline evaluation):**

*Final answer quality:*
- [ ] Test suite covers all equivalence partitions (happy path, edge cases, corner cases)
- [ ] At least 20% of test cases are derived from real usage (or manual testing if no users yet)
- [ ] LLM-as-judge criteria are written and validated against human review
- [ ] Off-topic and adversarial inputs are tested

*Trajectory quality:*
- [ ] Tool call sequence is verified for at least the happy path cases
- [ ] Agent handles tool failures gracefully (simulate a tool returning an error)
- [ ] No unnecessary tool calls on simple tasks
- [ ] Multi-turn conversations are tested (at least 3-5 turns)

*System behavior:*
- [ ] Cost per test run is tracked and within budget
- [ ] Latency is within acceptable bounds for the use case
- [ ] Error recovery is tested (what happens when the LLM output is malformed?)
- [ ] Safety boundaries are tested (does the agent refuse inappropriate requests?)

**In production (online evaluation):*

- [ ] Full conversation traces are logged (LLM calls, tool calls, retrievals)
- [ ] Task completion rate is monitored
- [ ] Cost per task is tracked and alerted on
- [ ] Failing traces are exported and added to the offline test suite regularly
- [ ] User feedback (explicit or implicit) is collected
- [ ] Hallucination sampling is in place (review 5-10% of outputs)

### How to know your evals are working

**Good signs:**
- Your test suite catches regressions before users do
- Production incidents are decreasing over time
- New failures map to gaps in your test coverage (which you then fill)
- The judge's verdicts align with your own assessment most of the time
- Cost and latency are predictable, not surprising

**Warning signs:**
- All tests pass but users complain about quality
- The same type of production failure keeps recurring
- Your test suite never fails when you change the agent's prompt or tools
- The judge disagrees with your assessment frequently
- You have no idea what your agent costs per conversation

If you see warning signs, the fix is almost always the same: get more real conversation data, add the failing cases to your test suite, and iterate. Your test suite should grow every time production breaks. That's the system working.

### What I believe

Agent evaluation is software testing applied to nondeterministic systems. The fundamentals transfer. Equivalence partitioning, boundary testing, regression suites, integration tests. These are not new ideas. They're old ideas applied to a new kind of system.

Start small. Write five test cases. Use your own agent until it breaks. Turn that breakage into a test case. Repeat. In a few weeks, you'll have a test suite that catches real problems. In a few months, you'll wonder how you ever shipped without one.

The teams that ship reliable agents in 2026 are the ones that treat evaluation as a first-class engineering discipline. The teams that don't are the 88%.

If you want to practice this hands-on, the [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents) covers the full evaluation pipeline with real code, real tools, and real agents. The next cohort starts September 21.
