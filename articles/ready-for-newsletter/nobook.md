---
title: "Nobook: Plain Python Files as Jupyter Notebooks"
created: 2026-02-13
updated: 2026-02-13
tags: [jupyter, python, tooling, nobook]
status: draft
---

# Nobook: Plain Python Files as Jupyter Notebooks

https://github.com/alexeygrigorev/nobook

I wanted Jupyter notebooks that use plain `.py` files instead of `.ipynb` JSON. The standard `.ipynb` format is a huge JSON file that is hard to read, hard to diff, and inconvenient for both humans and AI assistants[^1].

I ran an experiment I had been wanting to do for a long time. I built Nobook - a tool that uses plain `.py` files as Jupyter notebooks instead of `.ipynb` JSON files. Claude Code with the latest Opus wrote all the code in one evening while I spent about an hour checking and correcting. See the separate article on [Nobook](nobook.md) for details[^3][^4].

## Why I Built This

I want code in my documentation to come from Python files so I can cover them with tests. I need to be sure that the code I include in documentation - whether it's a course, a book, or anything else - always executes correctly, has no syntax errors, and produces output[^1].

When I update a library version, I want to catch breaking changes in the library interface that would break existing code. That's why I started this project with that specific goal in mind[^1].

I also want to run these notebooks interactively in Jupyter mode for my own experiments. And I want to easily include the results in documentation[^1].

Since I work with AI assistants, it is much more efficient for them to read and write plain Python files than JSON notebooks. With `.ipynb` files there is token overhead for reading and writing JSON. I made some tools to help with that, but reading and writing a plain Python file directly is much more efficient[^1].

## How It Works

The file format is a plain `.py` file. You add `# @block=name` markers to split code into cells. Each block becomes a Jupyter cell. A block starts at `# @block=name` and runs until the next marker or end of file[^4].

Example notebook file:

```python
# @block=setup
import math
x = 42

# @block=compute
result = math.sqrt(x)
print(f"sqrt({x}) = {result:.4f}")
```

The architecture uses stock Jupyter - both the UI and the IPython kernel are unmodified:

```
Jupyter UI (standard, unmodified)
        |
IPython Kernel (standard, unmodified)
        |
NobookContentsManager          <-- intercepts file I/O
        |
.py files with # @block markers
```

The `NobookContentsManager` subclasses Jupyter's `LargeFileManager`. On `get()`, it parses `# @block=` markers and returns a notebook model (blocks as code cells). On `save()`, it converts the notebook model back to `.py` format[^4].

`.py` files without `# @block=` markers are served normally as plain text files.

## Running Without Jupyter

You can run blocks from the command line:

```bash
uv run nobook run example.py
```

Output goes to `.out.py` with results inlined as comments:

```python
# @block=setup
import math
x = 42
# >>>

# @block=compute
result = math.sqrt(x)
print(f"sqrt({x}) = {result:.4f}")
# >>> sqrt(42) = 6.4807
```

Errors show as `# !!! ...` lines. Since output and errors are plain comments, `.out.py` files are valid Python - you can run them directly with `python example.out.py`[^4].

## Zero-Install with UVX

Users don't need to install anything. They just run `uvx nobook` and it launches. The only prerequisite is having UV installed[^3].

```bash
uvx nobook
```

Jupyter opens. Right-click a `.py` file in the file browser and select "Open as Nobook." It renders as a notebook. Run cells, edit them, save - the file stays `.py`[^4].

As a project dependency:

```bash
uv add nobook
uv run nobook
```

## JupyterLab Extension

Nobook includes a JupyterLab extension that adds:

- Launcher card - click "Nobook" in the launcher to create a new `.py` notebook
- "Open as Nobook" context menu - right-click any `.py` file to open it as a notebook
- Block name labels - editable labels on each cell showing the `@block` name

The extension is bundled with the package and installs automatically[^4].

## Background

I built this in one evening using Claude Code with the latest Opus model. I spent about 1 hour checking, correcting, and giving feedback while working on other things in parallel. It was not fully hands-off - I periodically reviewed what was happening and provided corrections[^1].

## Sources

[^1]: [20260213_070408_AlexeyDTC_msg1574_transcript.txt](../inbox/used/20260213_070408_AlexeyDTC_msg1574_transcript.txt)
[^2]: [20260213_070458_AlexeyDTC_msg1576.md](../inbox/used/20260213_070458_AlexeyDTC_msg1576.md)
[^3]: [20260213_070551_AlexeyDTC_msg1578_transcript.txt](../inbox/used/20260213_070551_AlexeyDTC_msg1578_transcript.txt)
[^4]: [nobook README](https://github.com/alexeygrigorev/nobook)
