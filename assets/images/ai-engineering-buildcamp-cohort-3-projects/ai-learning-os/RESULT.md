# AI Learning OS screenshot result

Repository: https://github.com/wesleytanjiale/ai-learning-os

## Run command

From the repository root:

```bash
OPENAI_API_KEY=sk-local-demo uv run streamlit run app.py --server.headless true --server.address 127.0.0.1 --server.port 8511
```

The app was launched from an isolated temporary clone. The Python dependencies were installed with `uv sync`.

## Screenshots

- `queue.png` - Learning Queue with three staged resources across Transformers, RAG, and Agents.
- `monitoring.png` - Monitoring Dashboard with interaction KPIs and tool-call frequency.

Both PNGs are 1440 × 810, with browser chrome and terminals excluded.

## Inputs and limitations

The upstream clone contains only `data/.gitkeep`, so temporary demo fixtures were added to `data/queue.json`, `data/kb.json`, `data/progress.json`, and `data/logs.jsonl` to make the built-in Queue and Monitoring pages render meaningful results. The Monitoring entries are synthetic local demo logs.

No OpenAI request, YouTube fetch, ingestion, consolidation, or live Chat turn was run. `sk-local-demo` only satisfies the SDK client constructor; it is not a real credential. No public deployment was listed in the repository README.

Relevant upstream files: `app.py`, `ai_learning_os/tools.py`, `ai_learning_os/monitoring.py`, and `README.md`.
