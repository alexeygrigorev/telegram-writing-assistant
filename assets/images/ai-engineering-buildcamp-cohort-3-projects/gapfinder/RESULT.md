# GapFinder

Repository: https://github.com/katjaweb/gapfinder

Install command used:

```text
uv sync --python 3.13
```

Run command used for the local screenshot demo:

```text
PYTHONPATH=. GAPFINDER_DEMO_MODE=1 GAPFINDER_DEMO_STAGE=summary uv run python -m streamlit run gapfinder_agent/app.py --server.port 19002
```

For the report capture, `GAPFINDER_DEMO_STAGE=report` was used. The real Streamlit app was launched with a local deterministic transcript/agent conversation injected through a temporary checkout-only demo flag. YouTube, OpenAI, and Logfire were not contacted and no credentials were used.

Screenshots:

- `01-summary-and-guided-learning.png` - processed video sidebar, transcript summary, and guided-learning prompt
- `02-gap-report.png` - complete gap report with understood concepts, missed concepts, and timestamps to revisit

Limitations:

- The screenshots exercise the project UI and display structure, but the transcript ingestion and LLM calls are local fixtures rather than live YouTube/OpenAI responses.
- The documented Streamlit command needed `PYTHONPATH` set to the repository root in this environment so the `gapfinder_agent` package could be imported.
