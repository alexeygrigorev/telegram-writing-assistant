# Datawarehouse Agent

Source: https://github.com/larsvasseldonk/datawarehouse_agent/blob/main/README.md

Run outcome: the local Streamlit UI rendered successfully with an isolated minimal warehouse fixture and deterministic agent responses.

Run commands attempted:

`uv sync`

`uv run python -m src.db.setup_db`

`uv run python - <<'PY' ... DuckDBManager().build_database(fact_row_count=500) ... PY`

The repository has no public Streamlit deployment. Its app requires both a locally seeded `db/db.duckdb` and `OPENAI_API_KEY`. The full deterministic seed process remained in disk I/O for about seven minutes while growing a DuckDB WAL, including the reduced 500-row attempt, so it was stopped. For the screenshot, the repository schema was created in an isolated DuckDB file and populated with two Utrecht Centraal incidents. The Streamlit app was launched with `SCREENSHOT_MOCK=1` and a local deterministic answer, so no key or external API call was needed.

Screenshot:

- `datawarehouse-agent-answer.png` - the real Streamlit chat UI showing an incident question, answer, success flags, and the generated read-only SQL.

Limitation: the full 10,000-row warehouse seed and live OpenAI refinement/SQL calls were not run. The screen uses the repository's real UI and schema with a tiny local fixture and deterministic mock response.
