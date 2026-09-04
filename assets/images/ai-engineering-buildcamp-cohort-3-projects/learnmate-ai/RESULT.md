# LearnMate AI screenshot result

Repository: https://github.com/dinobronx/learnmate-ai

## Run commands

From the repository root:

```bash
uv sync
cd web
npm install
```

The documented demo seed and local servers were then run with isolated stores:

```bash
LEARNMATE_DB=/tmp/buildcamp-ws4.BPcQgi/learnmate.db LEARNMATE_CHROMA_DIR=/tmp/buildcamp-ws4.BPcQgi/.chroma_data uv run python -m learnmate.persistence.seed
OPENAI_API_KEY=sk-local-demo LEARNMATE_DB=/tmp/buildcamp-ws4.BPcQgi/learnmate.db LEARNMATE_CHROMA_DIR=/tmp/buildcamp-ws4.BPcQgi/.chroma_data PYTHONPATH=. uv run uvicorn learnmate.api.app:app --host 127.0.0.1 --port 8521
VITE_API_TARGET=http://127.0.0.1:8521 npm run dev -- --host 127.0.0.1 --port 8522
```

## Screenshots

- `review.png` - Active Learning review with a question, student answer, tool status, and evaluated feedback.
- `progress.png` - Swift Array Methods knowledge map with mastery bands, weakest concepts, and session history.

Both PNGs are tightly clipped to the app UI with browser chrome and terminals excluded. They were captured at 2× device scale for readable article rendering.

## Inputs and limitations

The upstream `make seed` command populated the documented `Swift Array Methods (demo)` course without network calls. Temporary SQLite fixture rows were added for a mixed mastery map and two session-history entries so the progress view demonstrates the spaced-repetition states.

The dashboard/progress REST calls and due-concept selection used the real local FastAPI backend. For `review.png`, the browser intercepted only `/ws/review` and `/session` with deterministic local messages; this avoids OpenAI, YouTube, and Logfire network calls while exercising the real React review screen. `sk-local-demo` is not a real credential. No public deployment was listed in the repository README.

Relevant upstream files: `README.md`, `DEMO.md`, `learnmate/persistence/seed.py`, `learnmate/api/app.py`, `web/src/screens/Review.jsx`, and `web/src/screens/Progress.jsx`.
