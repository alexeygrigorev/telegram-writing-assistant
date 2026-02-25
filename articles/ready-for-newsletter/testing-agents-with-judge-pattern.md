---
title: "Testing AI Agents with the Judge Pattern"
created: 2026-01-30
updated: 2026-02-25
tags: [testing, ai, agents, judge, evaluation]
status: draft
---

# Testing AI Agents with the Judge Pattern

When testing AI agents, traditional unit testing approaches don't work well. LLM outputs are non-deterministic - the same input can produce different valid outputs. The judge pattern solves this by using one agent to evaluate another agent's performance.

## The Problem with Testing Agents

AI agents don't produce deterministic outputs. The same prompt to an LLM can result in different responses that are both correct. Traditional assertion-based testing breaks down when the output varies[^2].

This is where using one agent to evaluate another becomes powerful. Instead of checking for exact outputs, we evaluate whether the agent's behavior meets criteria described in natural language[^2].

## The Judge Pattern

The judge pattern works by:
1. Creating a "judge" agent that evaluates results
2. Describing test criteria in natural language
3. The judge examines the input, output, and tool calls
4. The judge determines if criteria are met

This approach lets us test agents using natural language descriptions instead of brittle assertions[^2].

## Example: Testing a Todo Agent

Here is an example from the AI Engineering Buildcamp course - a daily tasks agent with judge-based tests[^1].

### The Judge Agent

The judge is created as a separate agent with specific instructions:

```python
from pydantic_ai import Agent, AgentRunResult
from pydantic import BaseModel

class JudgeCriterion(BaseModel):
    criterion_description: str
    passed: bool
    judgement: str

class JudgeFeedback(BaseModel):
    criteria: list[JudgeCriterion]
    feedback: str

def create_judge():
    judge = Agent(
        name="judge",
        instructions="you are an expert judge evaluating the performance of an AI agent.",
        model="openai:gpt-4o-mini",
        output_type=JudgeFeedback,
    )
    return judge
```

Source: [github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/judge.py](https://github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/judge.py)

### Evaluating Performance

The judge receives the agent's output, tool calls, and evaluation criteria:

```python
async def evaluate_agent_performance(
        criteria: list[str],
        result: AgentRunResult,
        output_transformer: callable = None
) -> JudgeFeedback:
    tool_calls = get_tool_calls(result)
    output = result.output

    user_prompt = f"""
Evaluate the agent's performance based on the following criteria:
<CRITERIA>
{criteria}
</CRITERIA>

The agent's final output was:
<AGENT_OUTPUT>
{output}
</AGENT_OUTPUT>

Tool calls:
<TOOL_CALLS>
{tool_calls}
</TOOL_CALLS>
    """.strip()

    judge = create_judge()
    judge_result = await judge.run(user_prompt)
    return judge_result.output
```

Source: [github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/judge.py](https://github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/judge.py)

### Writing Tests with Criteria

Tests describe expected behavior in natural language:

```python
@pytest.mark.asyncio
async def test_agent_todo():
    runner = create_agent()
    prompt = "What do I have for today?"

    result = await runner.run_prompt(prompt)

    await assert_criteria(result, criteria=[
        "agent should use tools to get todos due today",
        "'Update the API spreadsheet' is in the output",
    ])
```

Source: [github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/test_judge.py](https://github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/test_judge.py)

<figure>
  <img src="../assets/images/testing-agents-with-judge-pattern/judge-test-example.jpg" alt="Judge test example showing pytest test for todo agent">
  <figcaption>A judge test for a todo agent - criteria are described in natural language and evaluated by another AI agent</figcaption>
</figure>

The judge evaluates each criterion and reports whether it passed. This is much more flexible than traditional assertions[^2].

## Benefits of Judge-Based Testing

- Natural language criteria instead of code assertions
- Can evaluate non-deterministic outputs
- Provides detailed feedback on what went wrong
- Easier to maintain and understand test intent[^2]

## Running Tests in CI

This approach can be integrated with GitHub Actions for continuous integration. The agent runs in a session with a described sequence of steps to test. This is more interesting than manually writing complex test code[^2].

## Generating Tests from Usage Sessions

A workflow for generating tests that I really like. The idea: you use your agent for 10-15 minutes on video, commenting as you go - "this I don't like," "this I don't like," "here we could do this," "here everything works well." Then you take the transcript of that session, feed it to ChatGPT, and say: "generate test scenarios based on this." Then you write test code based on those scenarios[^3].

This approach saves a lot of time. You just record yourself using the agent, Whisper transcribes the recording, and the tests get generated. You fix them one test at a time, and each time something breaks, you know about it. It took some time to prepare everything nicely, but the approach is great[^3].

I also made a nice testing library for this. First you write the tests, then you build the evaluation library on top[^3].

## Homework: SQL Analytics Agent Testing

I gave students a homework assignment to implement an agent that converts user queries to SQL. They use New York taxi data, and the agent's job is to do analytics on this data. You talk to the agent, it turns your request into SQL, and returns the results. The homework is to write tests for this agent[^3].

## Sources

[^1]: [20260130_090909_AlexeyDTC_msg679.md](../inbox/used/20260130_090909_AlexeyDTC_msg679.md)
[^2]: [20260130_091056_AlexeyDTC_msg683_transcript.txt](../inbox/used/20260130_091056_AlexeyDTC_msg683_transcript.txt)
[^3]: [20260225_200726_AlexeyDTC_msg2441_transcript.txt](../inbox/used/20260225_200726_AlexeyDTC_msg2441_transcript.txt)

## References

- my-daily-tasks-agent repository: [github.com/alexeygrigorev/my-daily-tasks-agent](https://github.com/alexeygrigorev/my-daily-tasks-agent)
- judge.py: [github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/judge.py](https://github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/judge.py)
- test_judge.py: [github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/test_judge.py](https://github.com/alexeygrigorev/my-daily-tasks-agent/blob/main/tests/test_judge.py)
