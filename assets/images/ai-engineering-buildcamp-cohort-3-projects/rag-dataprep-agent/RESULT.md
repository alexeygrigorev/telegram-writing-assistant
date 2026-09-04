# Document Preparation Agent result

Repository: https://github.com/PaulienOut/rag-dataprep-agent

Run path

- Installed dependencies with `uv sync` in an isolated clone.
- Ran `uv run python -m rag_dataprep_agent.cli data/Arxiv --output-dir /tmp/twa-ws2-rag-xxn6wX/prepared --max-files 1`.
- The CLI wrote `prepared/manifests/2605.00016v1.json` from the included 22-page arXiv PDF.
- The generated manifest contains 90 numbered chunks, PDF metadata, four authors, an extracted publication date, keywords, and `arxiv_paper` detection with confidence 0.85.

Screenshot

- `rag-dataprep-agent-manifest.png` - a tightly cropped rendering of actual manifest fields, including the source path, document type, title, authors, keywords, chunk ID, extracted chunk text, and CLI result.

Limitations

- This project is CLI-only in the current README and does not provide a public UI to capture.
- The run used the local deterministic metadata extractor with no OpenAI key, so no paid model calls or embeddings were made. The screenshot labels this explicitly.
