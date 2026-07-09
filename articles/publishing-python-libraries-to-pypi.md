---
title: "How I Publish Python Libraries to PyPI"
created: 2026-07-09
updated: 2026-07-09
tags: [python, pypi, libraries, agents, skills, ci-cd]
status: draft
---

# How I Publish Python Libraries to PyPI

Over the past year I've been creating a lot of libraries, and I use them regularly. I've published 24 packages on [PyPI](https://pypi.org/user/alexeygrigorev/) [^4]. This article is about how to publish libraries to the Python Package Index (PyPI) [^1].

I started publishing libraries a long time ago, back when I was writing the Machine Learning Bookcamp book. That was probably before covid, I don't remember exactly when. While writing the book I covered deploying deep learning models with TensorFlow Serving and with AWS Lambda, and even then I needed to publish parts of the code as libraries. Back then the process was manual and I used different tools than I use now [^1].

minsearch was one of the first of these libraries. I first made it for Machine Learning Zoomcamp, then made a version for LLM Zoomcamp, and I wrote about it [^1]. You can read the [minsearch write-up](https://alexeyondata.substack.com/p/minsearch-the-small-search-library) for what it does.

I used to release these libraries rarely. Over the last year, with agents, it started happening more and more often. People were interested in how to write libraries, so I decided to explain how I do it [^1].

Here's what changed. Earlier I did everything manually. I had to remember the steps and keep notes - you can still find my old notes inside the minsearch repo so I wouldn't forget how to do it. Now everything is in skills and automated. I don't even remember how it's done anymore, and it's all on autopilot [^1].

The rest of this article follows the process in order: how a library starts, how I publish it manually, how I moved the release to CI, and then how I automated the whole thing with skills.

## Every Library Starts with an Idea

You want to build something and you realize it could be useful - either as a command-line utility, or as a project you can reuse in other projects. First you need to understand what you're building and that it's worth reusing, for yourself or for someone else [^2].

Not every idea is worth implementing. I have a process for deciding what's worth building before I start, which I've described before - for example when I wrote about [building SQLiteSearch](https://alexeyondata.substack.com/p/how-i-built-sqlitesearch-a-lightweight) [^2].

I usually start with ChatGPT (GPT-5). I export the conversation so it's clear what I want to build. That gives me clarity before I write any code [^2].

## Choosing a Name

The next step is choosing a name, and this is harder than it sounds. It's not enough to pick a name. You need a name that isn't already taken on PyPI. That's difficult, because there are already many libraries, and a lot of people also use agents to build and publish, so names get taken quickly [^2].

Once I have clarity from ChatGPT, I start a session with an agent. I paste the exported conversation describing the problem, say I want to build a library for it, and ask the agent to help pick a name and check whether it's available. Agents know how to check PyPI - a simple GET request tells you whether a package name is taken [^2].

Take Heru as an example. The idea was "one tool to rule them all". I thought I could play with Lord of the Rings, find a short word, maybe something Elvish. I started brainstorming with the agent and we ended up with Heru. Same story for Quse (Qs). The agent checks if a name is taken, and if it is, it suggests other options. This back-and-forth can take about 10 minutes [^2]. I wrote about how Heru and Quse got their names in [Six Projects That Didn't Make It](https://alexeyondata.substack.com/p/six-projects-that-didnt-make-it).

## The First Version

Once the name is settled, the next step is to make a first version and publish it. I create a GitHub repo - I have a skill for that. With a name chosen, this part is easy [^2].

I usually make the repo public, for two reasons [^2]:

- I contribute a lot to open source and want others to see the code, use it, and maybe contribute.
- Public repos get a larger GitHub Actions CI/CD quota than private ones. Private repos have tighter limits.

My first version is usually 0.0.1. If you read versions as major.minor.patch, that's the first patch. I publish 0.0.1 for two reasons [^3]:

- To put a skeleton of the application in place.
- To reserve the name on PyPI so nobody takes it while I'm still building.

A minimal working version is enough to publish. It can be 0.1 or something even more minimal, maybe just a CLI. It doesn't matter at this stage [^3].

## Publishing Manually

Now the publishing itself. My process is: first build, then test. You must have tests - some tests should always be there [^3].

The project structure matters. Before publishing, it's worth deciding what goes into pyproject.toml - what the project should look like. Across my projects the structure is fairly consistent. I use hatch (hatchling as the build backend) and uv for tooling [^3].

Here's the shape of a pyproject.toml for one of my libraries:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "minsearch"
dynamic = ["version"]
description = "Minimalistic text search engine that uses sklearn and pandas"
readme = "README.md"
license = {text = "WTFPL"}
authors = [{name = "Alexey Grigorev", email = "alexey@datatalks.club"}]
requires-python = ">=3.10"
dependencies = ["numpy", "pandas", "scikit-learn"]

[tool.hatch.build.targets.wheel]
packages = ["minsearch"]

[tool.hatch.version]
path = "minsearch/__version__.py"
```

The version is not hardcoded in pyproject.toml. It's declared as dynamic, and hatchling reads it from a separate file. I always keep the version in its own file, `__version__.py` [^3]:

```python
__version__ = "0.0.1"
```

If the library ships a command-line tool, I add an entry point so the command becomes available after install:

```toml
[project.scripts]
stylint = "stylint.cli:main"
```

When you release, you bump this version. A simple bug fix bumps the patch version. Something more substantial, or a breaking change, bumps the minor version. Deciding to cut a 1.x release rarely happens [^3].

To publish, you create two accounts: one on test.pypi.org and one on pypi.org. Test PyPI is for checking that everything works before you publish to the real index. You publish to test PyPI first, verify it's fine, then publish to the real one [^3].

This is the old manual flow, which I documented in the minsearch README:

```bash
uv sync --extra dev
uv run hatch build
uv run hatch publish --repo test
uv run hatch publish
rm -r dist/
```

This builds the package, publishes to test PyPI, then to real PyPI, and cleans up afterwards. I had a `make publish` target that ran this [^3].

## Getting Tokens

For publishing you need API tokens. Create the accounts on test.pypi.org and pypi.org, generate an API token on each, and put them in `~/.pypirc` in your home folder. The file has separate token-authenticated entries for pypi and testpypi, and it should be `chmod 600` [^3]:

```ini
[pypi]
username = __token__
password = pypi-...

[testpypi]
username = __token__
password = pypi-...
```

Hatch reads these credentials when publishing. You can also pass them through environment variables (`HATCH_INDEX_USER=__token__` and `HATCH_INDEX_AUTH=<token>`) [^3].

## Releasing Through CI

The release can be done manually, but I do it through CI. Instead of running hatch publish on my own machine, I let GitHub Actions do it on a tag push [^3].

The workflow lives in `.github/workflows/publish.yml` and triggers on any `v*` tag. It does three things:

- builds the package with `uv build`
- verifies the built artifact version matches the tag
- publishes with the official `pypa/gh-action-pypi-publish` action

The action authenticates with a GitHub secret called `PYPI_API_TOKEN` - the same token from `~/.pypirc`, stored as a repo secret so the credentials never sit on my machine at release time [^3].

So the release becomes: bump the version in `__version__.py`, commit, create a `v<version>` tag, and push it. I have a `make release` target that reads the version from the file, tags it, and pushes:

```make
release:
	@VERSION=$$(grep -E "^__version__" minsearch/__version__.py | sed -E "s/.*['\"]([^'\"]+)['\"].*/\1/"); \
	git tag "v$$VERSION"; \
	git push origin "v$$VERSION"
```

Pushing the tag triggers the workflow, and CI does the build and upload [^3].

## One Universal Publish for Everything

This isn't only about Python. A library could be in Rust, or a project in Kotlin, or something else. I want publish to always be universal: you create a tag and push it, and CI does the publishing - whether that's to PyPI, to another registry, or building an artifact and uploading it somewhere [^3].

The flow is the same everywhere. You always push a tag via GitHub, and from there the logic can be custom. For all Python projects the logic is roughly the same. You just need to put your token into a GitHub secret [^3].

rustkyll is a good example. It's a static site generator written in Rust. On a `v*` tag, its workflow cross-compiles the binary for six platforms, attaches them to a GitHub Release, and publishes binary-bundled wheels to test PyPI and then PyPI. Different publishing logic, same trigger: push a tag [^3].

## Automating It with Skills

Now the part that makes all of this fast. I've turned the whole process into skills. My tokens already live in `~/.pypirc` in my home folder (documented in the minsearch README), and agents know how to take a token from there and set it as a GitHub secret [^3].

Three skills cover the pipeline:

init-library scaffolds a new Python package. You give it a name, a short description, the dependencies, and whether it needs a CLI. It generates the standard layout - the package directory with `__init__.py` and `__version__.py` seeded at 0.0.1, a tests directory, pyproject.toml, Makefile, and README - and sets everything up with uv. When the repo is on GitHub, it hands off to the next skill.

setup-pypi-ci converts a project to tag-triggered CI publishing. It copies the publish.yml workflow, adds the `make release` target, reads the PyPI token from `~/.pypirc`, and pushes it to GitHub as the `PYPI_API_TOKEN` secret. After this, releasing is just bump-and-push-a-tag.

release cuts a release. It bumps the version in the source-of-truth file (defaulting to a patch bump), commits, pushes the tag, watches the GitHub Actions run to completion, and writes the GitHub release notes from the git log. It's registry-agnostic - it works for PyPI, crates.io, npm, and anything else with a CI publish keyed off `v*` tags.

These skills live in my .agents repo - my AI assistant dotfiles, a single source of truth that syncs the same skills across Claude Code, Codex, and OpenCode. So the same skills work with every agent I use. The repo is on my machine and also on GitHub [^3].

The core idea is that I never touch PyPI directly at release time. The token is configured once as a GitHub secret, and every release after that is just bumping a version and pushing a tag. This is why I now have so many libraries: what used to be a manual process I had to keep notes for is now a few skills I don't have to think about [^3].

## Sources

[^1]: [20260709_153422_AlexeyDTC_msg4726_transcript.txt](../inbox/used/20260709_153422_AlexeyDTC_msg4726_transcript.txt)
[^2]: [20260709_154013_AlexeyDTC_msg4730_transcript.txt](../inbox/used/20260709_154013_AlexeyDTC_msg4730_transcript.txt)
[^3]: [20260709_154658_AlexeyDTC_msg4732_transcript.txt](../inbox/used/20260709_154658_AlexeyDTC_msg4732_transcript.txt)
[^4]: [20260709_153046_AlexeyDTC_msg4725.md](../inbox/used/20260709_153046_AlexeyDTC_msg4725.md)
