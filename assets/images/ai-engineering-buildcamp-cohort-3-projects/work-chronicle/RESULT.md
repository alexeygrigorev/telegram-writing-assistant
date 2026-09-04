# WorkerChronicle result

Repository: https://github.com/MikiYamFos/work-chronicle

Run path

- Installed dependencies with `uv sync` in an isolated clone.
- Created a local demo library and job description from the repository's fictional `TEST_CONTENT.md` material.
- Ran `ANTHROPIC_API_KEY=fake-local-demo COVERLETTER_MODEL=claude-haiku-4-5-20251001 uv run clio sync --paragraphs demo/library.md --no-embed --no-angles`.
- Used the real `extract_to_review`, `insert_from_review`, and `build_outline` functions with a local fake provider replacing model calls. Three claims and their evidence were inserted into SQLite, then grouped into two outline blocks.

Screenshots

- `work-chronicle-overview.png` - the attached project overview, cropped to remove the narrow side borders, describing WorkerChronicle's experience library and cover-letter generator.
- `work-chronicle-outline.png` - the generated claim-evidence outline before cover-letter generation, showing the thesis, job requirements, argument categories, grounded claims, preserved anchor phrases, and editable block structure.

Limitations

- The normal WorkerChronicle flow requires an Anthropic, Mistral, OpenAI, or Cohere key. No key was available or used, so the extraction and grouping calls were deterministic local mocks.
- The screenshot demonstrates the real SQLite, review, and outline structure with local fictional material; it is not a live provider-generated cover letter.
