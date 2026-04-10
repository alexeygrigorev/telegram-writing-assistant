---
title: "Code Review Graph: Graph-Based Code Review Analysis"
created: 2026-04-09
updated: 2026-04-09
tags: [research, code-review, graphs]
status: draft
---

# Code Review Graph

A tool that builds a persistent knowledge graph of your codebase so AI coding assistants read only the files that matter. Instead of scanning your entire repository on every task, it traces the "blast radius" of each change and provides just the relevant context.

Source: https://github.com/tirth8205/code-review-graph

## The Problem

AI coding tools (Claude Code, Cursor, Windsurf, etc.) re-read large portions of a codebase on every task. This wastes tokens and money. For monorepos the problem is worse - thousands of files get loaded when only a handful are relevant.

## How It Works

The pipeline has four stages:

1. Parse the codebase into an AST using Tree-sitter
2. Store the structure as a graph in SQLite (nodes = functions, classes, imports; edges = calls, inheritance, test coverage)
3. On each change, trace all callers, dependents, and tests that could be affected (the "blast radius")
4. Serve this minimal context to the AI assistant via MCP (Model Context Protocol)

### Graph Schema

Nodes have five kinds: File, Class, Function, Type, Test. Each node stores its qualified name, file path, line range, language, parameters, return type, and a SHA-256 hash of the file content.

Edges have seven kinds: CALLS, IMPORTS_FROM, INHERITS, IMPLEMENTS, CONTAINS, TESTED_BY, DEPENDS_ON. Each edge links source and target by qualified name.

The database is SQLite in WAL mode, stored at `.code-review-graph/graph.db`. Thread safety uses `threading.Lock` for caches and `check_same_thread=False` for the connection.

### Blast Radius Analysis

When a file changes, the graph does a BFS (breadth-first search) traversal from the changed nodes outward through edges. It collects every caller, dependent, and test that could be affected. The AI then reads only these files instead of the whole project.

The analysis has 100% recall (never misses an affected file) with average 0.38 precision (some false positives). The conservative approach is deliberate - better to flag too many files than miss a broken dependency.

### Incremental Updates

On every git commit or file save, a hook fires. The system diffs changed files, checks SHA-256 hashes, and re-parses only what changed. A 2,900-file project re-indexes in under 2 seconds. Parsing uses a thread pool (up to 8 workers by default, configurable via `CRG_PARSE_WORKERS`).

### Change Impact Analysis

The `changes.py` module maps git diffs to affected functions. It parses `git diff --unified=0` output, extracts line ranges per file, then maps those ranges to graph nodes. Each change gets a risk score based on how many dependents, flows, and test gaps it touches. Security-sensitive changes (matching keywords from a built-in list) get flagged separately.

### Execution Flow Detection

The `flows.py` module detects entry points (functions with no incoming CALLS edges, framework-decorated handlers, conventional patterns like `main`, `test_*`, `handle_*`). It traces execution paths via forward BFS through CALLS edges and scores each flow for criticality.

Framework detection covers: Express/Flask/FastAPI route decorators, Click commands, Celery tasks, Spring annotations, and more.

### Community Detection

Groups related code using the Leiden algorithm (via igraph) or simpler file-based grouping. Produces an architecture overview with coupling warnings. Can auto-generate a markdown wiki from the community structure.

## Architecture

Core package: `code_review_graph/` (Python 3.10+)

Key modules:

- `parser.py` - Tree-sitter multi-language AST parser. 19 languages plus Jupyter notebooks. Maps file extensions to languages. Extracts nodes and edges from syntax trees.
- `graph.py` - SQLite-backed graph store. BFS impact analysis using NetworkX. Parameterized SQL queries only (no f-strings for values).
- `main.py` - FastMCP server entry point. Registers 22 tools and 5 prompts. Stdio transport.
- `incremental.py` - Git-based change detection with file watching via watchdog. Parallel parsing with ThreadPoolExecutor.
- `changes.py` - Risk-scored change impact analysis. Parses unified diffs, maps to graph nodes.
- `flows.py` - Execution flow detection with criticality scoring.
- `communities.py` - Leiden algorithm community detection and architecture overview.
- `search.py` - FTS5 hybrid search combining keyword and vector similarity.
- `embeddings.py` - Optional vector embeddings via sentence-transformers, Google Gemini, or MiniMax.
- `tools/` - 22 MCP tool implementations.
- `visualization.py` - D3.js force-directed graph generator.
- `refactor.py` - Rename preview, dead code detection, refactoring suggestions.

## Technologies

- Tree-sitter (via `tree-sitter-language-pack`) for AST parsing
- SQLite in WAL mode for graph storage
- NetworkX for graph traversal algorithms
- FastMCP for MCP server
- Watchdog for file system monitoring
- igraph for community detection (optional)
- sentence-transformers for vector embeddings (optional)
- D3.js for interactive visualization
- Hatchling for build system

## MCP Integration

The tool exposes 22 MCP tools. The recommended workflow starts with `get_minimal_context(task="...")` which costs about 100 tokens and returns graph stats, risk score, top communities/flows, and suggested next tools. All subsequent calls should use `detail_level="minimal"` unless more detail is needed. Target: 5 or fewer tool calls per task, 800 or fewer total tokens of graph context.

Five MCP prompt templates provide structured workflows: `review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check`.

## Benchmarks

Tested against 6 real open-source repositories (13 commits total):

- Average token reduction: 8.2x (naive vs graph approach)
- Best case: gin at 16.4x reduction
- Worst case: express at 0.7x (small single-file changes where graph metadata overhead exceeds raw file size)
- Impact accuracy: 100% recall, 0.54 average F1
- Search latency: 0.4ms to 1.5ms
- Build performance: 83-1,122 files parsed, producing 1,200-6,300 nodes and 7,900-27,100 edges

Monorepo case: Next.js with 27,700+ files funneled down to about 15 files for review - 49x fewer tokens.

## Security Design

- No `eval()`, `exec()`, `pickle`, or `yaml.unsafe_load()`
- No `shell=True` in subprocess calls
- Path traversal prevention via `_validate_repo_root()`
- Prompt injection defense via `_sanitize_name()` (strips control characters, caps at 256 chars)
- HTML entity escaping in visualization output
- SRI hash on CDN script tags
- API keys only from environment variables

## Key Patterns

### Token-efficient context serving

The "get minimal context first, then drill down" pattern is worth noting. Instead of dumping everything, the system returns a compact summary (about 100 tokens) with suggestions for what to query next. This is a pull-based architecture for AI context.

### Conservative blast radius

Perfect recall at the cost of precision. The system would rather give the AI a few extra files than miss a broken dependency. This is the right trade-off for code review where false negatives (missed bugs) are more costly than false positives (reading an extra file).

### SHA-256 hash-based change detection

Files are hashed on read. The hash is stored in the graph. On update, only files whose hash changed get re-parsed. This is faster than timestamp-based detection and avoids unnecessary work when a file is touched but not modified.

### Structural context over raw code

Instead of feeding raw source files to the AI, the graph provides structural summaries: which functions call which, what tests cover what, where the inheritance chains go. This is a more token-efficient representation of the same information.

## Limitations

- Small single-file changes: graph metadata overhead can exceed the raw file size
- Search quality (MRR 0.35): keyword search needs ranking improvements
- Flow detection (33% recall): only reliable for Python frameworks; JavaScript and Go need work
- Precision trade-off: deliberately conservative, so some false positives in large dependency graphs

## Notes

This is an MCP-native tool. It was designed from the start to work with AI coding assistants rather than being retrofitted. The MCP integration is not a wrapper around a CLI - the CLI and MCP tools share the same core logic.

The project has 572 tests and CI runs across Python 3.10-3.13 with 50% minimum coverage.

The approach is related to static analysis tools like CodeQL and Semgrep but focused on a different problem: not finding bugs, but reducing the context an AI needs to review code effectively.

## Resources

### GitHub Repository

Source: https://github.com/tirth8205/code-review-graph

The main repository. MIT licensed. Version 2.2.2 at time of writing. Active development with CI pipeline (lint, type-check, security scan, test matrix).

[^1]: [20260409_064713_AlexeyDTC_msg3315.md](../../inbox/used/20260409_064713_AlexeyDTC_msg3315.md)
