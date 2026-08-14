# How to Do Evals in 2026
## A tool-agnostic framework for evaluating AI agents

Across all 4,894 AI engineering job descriptions that I collected for the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide), evaluation consistently comes up as the number one skill that AI Engineers must have.

It also appears in interview questions. In interviews, you'll definitely hear something like "how do you evaluate a RAG pipeline?" or "how do you measure agent performance?". If you don't include evals in your home assignemnt, it's a red flag.

Why is it such an important skill? Becase it's important and it's hard. 

It's easy to build an agent these days. I show how to do it in my ["AI Hero: 7-Day AI Agents Crash-Course"](https://aishippinglabs.com/courses/aihero). You need to get an OpenAI key, take any agentic framework, define the instructions and the tools, and that's it. You have an agent.

But this agent will break in so many ways. It will:

- Give a wrong answer
- Confidently hallucinate a plausible answer
- Finish without giving any answer
- Get into a loop with tool use and call the same tool over and over again
- Exhaust the context
- Call a tool with invalid arguments

That's just the tip of the iceberg. To make sure this agent works reliably, you need to test and evaluate it. 

Also, without evaluations, you're blind. You don't know how the agent is performing. You also can't really change anything: every change you introduce may break the systems in so many ways, also in the areas where you least expect it.

Agent evaluaiton is not simple. It takes a lot of time to understand the problem, get input from real users, gather the right data. It's not something you can just delegate to Claude and forget about it.

That makes evals such an important part of our job as AI Engineers. 

In this article, I will tell you how to approach evaluations:

- Start manually by "vide-checking" the system but also starting collecting logs as early as possible
- Then create a tool for labelling the logs and start putting together a gold standard dataset
- With the dataset, create a judge and make sure it's aligned with our judgement
- Then break the agent using ideas from QA like equvalence partitioning and boundary testing
- Start collecting data from real users, but also get more data by generating it synthetically
- Evaluate your system ongoingly with online evaluation and always refine your gold standard dataset by including real data

Let's get into details.

## Collecing the Gold Standard dataset

You have an agent. What's next?

There's nothing wrong with "vibe-checking" it: you poke it, ask questions you want it to answer, and look at the results. If they aren't good, you figure out how to fix it.

But already at this step you can be a bit more organized and start logging what the agent is doing. When you ask a question and see the answer, make sure they are saved somewhere. You do a few vibe-checking sessions, and you already have 10-15 logged records.

Now you can systematically look at these logs and classify each into

- "good": the answer is what you expect
- "bad": the answer is not what you wanted to see

To help me do it, I usually vibe-code a small lebelling tool.

This gives you a "version 0" of the gold standard dataset - the dataset you will use for evaluating your system (sometimes it's also called the "ground truth" dataset).

Don't delegate this step to coding assistants. It's only a few examples, so you can go relatively quickly through them. But this way, you will a lot of insights into how your agent is behaving, what's working and what isn't.


## Judge alignment

Once you manually labelled 10-15 examples, it's time to start automating it. 

I use coding assistants for that:

- Ask the assistant to analyze the logs and classify the examples into good or bad.
- See if the results match yours. If they don't, ask the agent to explain the decision to see if you missed something, or the agent didn't have enough context.
- Iterate until you both agree.
- At the end of the session, ask the agent to create a judge.md file that describes the classification rules.
- Read this file carefully to see that the rules are generic and not specific to the examples you have in the dataset. 

We just created a judge - a system that evaluates our agent. 

Now we need to test that using judge.md alone is sufficient:

- Start a new session
- Ask to start a subagent which reads judge.md and classifies the records in your dataset
- If something is off, ask the agent to change judge.md
- Iterate until you both align on what's good and bad

This process of is called "alignment" - we align the judge with what we think is good or bad.

It's the same as training a binary classifier that predicts your decisions. But instead of weights, you have a judge.md file. (And it's also helpful to have a train-test split here too! But later, when you have more data.)

At this point, you also get a metric - the fraction of good examples. Now if you change something in your agent, you can re-run the judge and make sure this metric doesn't go down.

## Breaking the agent

We have the initial version of our gold standard dataset. But it's not enough. Now we want to find cases that break our system.

QA engineers have been breaking software for many decades. For coming up with cases that should derail our agent, we can borrow some concepts from their frameworks.

### 1. Equivalence partitions

The first step is [equivalence partitioning](https://www.ministryoftesting.com/software-testing-glossary/equivalence-partitioning).
You divide the input space into groups where inputs within each group should produce similar behavior.

If we have a RAG agent that answers questions about our docs, it could be:

- Questions about topics in the documentation,
- Questions about relevant topics but not in the documentation,
- Questions about irrelevant topics,
- Ambiguous questions,
- Questions in different languages

Once you come up with a list of grous, come up with 2-3 questions from each group. You can ask AI to help you with the entire process.

### 2. Boundary testing

The next concept is [boundary testing](https://www.ministryoftesting.com/software-testing-glossary/boundary-testing).

We already have some questions from the previous step, but we can be even more aggressive in our testing.

After definining the partitions, QA engineers would test the bounderis of each partition. We can do the same.

For a RAG agent, come up with a questions that:

- Exactly matches a document that we have in our database (easy case),
- Semantically related but uses different words (typical case),
- Semantically related to multiple documents (ambiguous case),
- Completely off-topic (boundary case).

## Further alignment 

This way you can easily get 30-40 more questions to your gold standard dataset. 

Let's take all the data we have, and run it against our agent. Then use the judge to classify the output.

We already have a tool that we created earlier for manual evaluation. At this point, I adjust this tool to also support checking output for the judge. For each record, I need to make two decisions: "agree" or "disagree". I find it more convenient than labelling the new logs as "good" or "bad". 

If we have many "disagree" cases, tune the judge following the same process as before. We will never have 100% alignment, so we don't need to be too strict about it, but the judge should be correct most of the time.

## Using the Judge to improve your agent

Now we have a fully automated process that:

1. Runs the agent against our data
2. Run the judge against the output of step 1
3. Outputs a metric - the fraction of "good" results

Because it's automated, we can use it to improve our agent. You can ask the coding assistant to do it. 

I recommend following the [implementer-tester pattern](https://alexeyondata.substack.com/p/ai-native-development-specifications) for that:

- Define the implementer subagent that modifies the agent
- Define the judge subagent that uses judge.md to evaluate the output
- Iterate until your "good" ratio is acceptable


## Start testing on real users as soon as possible

We have evaluated our agent on 50-60 cases, and it's good enough to give us some confidence that it's working okay. But we need more.

Now iet's time to put it in front of real users:

- Invite people for user interviews (TODO how to call it?) to check your system
- If you plan to integrate it into an existing product, include it in a small subset of the traffic
- If it's a small personal project, ask your friends and family to test it. 
- If it's a course project, ask your classmates to play with it. 
- Share it on social media. 

Make sure you're collecting the logs (be direct with the user about what you're collecting) and use this for adding new cases into the gold standard dataset.

## Synthetic data

So far we focused on the quality of our gold standard dataset. In this section, I want to talk about the quantity.

Quantity is also important because agents are non-deterministic. Even if we get our agent to work properly with our small dataset, it will definitely break when we get more traffic. Just because of ... 
just bacause of the ... (probablity and statistics).
Here you want quantity. When you expose your agent to a bigger number of inputs, things will break - statistically, with more repetitions you increase the chances of something going wrong.

We can generate a lot more data using AI. Open your AI assisntant, ask it to analyze your code, describe to it your target users, and then tell it to generate questions that these users are likely to ask.

For a RAG system, you can:

- Take a document from your knowledge base
- Ask AI to come up with 5 questions based on this document
- Do it for all documents

You will end up with a lot of questions. You can keep all of them, or take a sample.

Then follow the same proccess: run your agent against this data and then use the judge to evaluate the results. 

This way you will probably run into many different problems:

- The agent will loop without stopping and exhaust the context
- It won't follow the instructions and do something that it shouldn't
- A tool will break and your agent won't complete work

And many others. You don't know in advance what you can get, that's why you want to be exposed to a big variety of different inputs. 

Once you identify the scenarios where your agent breaks or doesn't perform well, add them to your gold standard dataset. 

Then you can fix the agent, and re-run the whole evaluation set to make sure you don't introduce any regressions.

## Online evaluation

We have a system for offline evaluations: we run the agent agains our dataset and we use the judge to score the output to see how good it behaves.

It's okay, but it's not scalable. Instead, we want to run it ongoingly: every time somebody uses our agent, we react to this in real-time: save the logs, evaulate them, and display the result on the dashboard.

We can't really continue using our coding agent for that, so we'll need to create a stand-alone judge. 

It will give you ... (todo describe what).

Periodically inspect bad results, and if you see something new, add these cases to your gold standard dataset. Also, check good results too to make sure they are actually good. 

For inspecting the this live traffic I also often use coding assistants. I take a sample of the data, save it locally and ask them to go through these cases with me.

TODO Add a centense or two about this: - [ ] User feedback (explicit or implicit) is collected
- [ ] Hallucination sampling is in place (review 5-10% of outputs)


TODO how to finish?

### The agent evaluation checklist

TODO: update on the actual text from the article

Gold standard dataset:

- [ ] 10-15 logged interactions labeled "good" or "bad"
- [ ] Test cases cover all equivalence partitions (happy path, edge cases, corner cases)
- [ ] Boundary cases are included

The judge:

- [ ] judge.md describes the classification rules in generic terms
- [ ] The judge's verdicts align with your own assessment most of the time
- [ ] Off-topic and adversarial inputs are tested

Online evaluation:

- [ ] Full conversation traces are logged (LLM calls, tool calls, retrievals)
- [ ] Task completion rate is monitored
- [ ] Failing traces are exported and added to the offline test suite regularly
- [ ] User feedback (explicit or implicit) is collected
- [ ] Hallucination sampling is in place (review 5-10% of outputs)


Agent evaluation is software testing applied to nondeterministic systems. The fundamentals transfer. Equivalence partitioning, boundary testing, regression suites, integration tests. These are not new ideas. They're old ideas applied to a new kind of system.

Start small. Write five test cases. Use your own agent until it breaks. Turn that breakage into a test case. Repeat. In a few weeks, you'll have a test suite that catches real problems. In a few months, you'll wonder how you ever shipped without one.


If you want to practice this hands-on, the [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents) covers the full evaluation pipeline with real code, real tools, and real agents. The next cohort starts September 21.
