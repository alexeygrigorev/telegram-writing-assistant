---
title: "Setting Up a Windows Computer for Development"
created: 2026-03-11
updated: 2026-03-11
tags: [windows, dev-setup, tools]
status: draft
---

# Setting Up a Windows Computer for Development

[Video](https://www.youtube.com/watch?v=2H8aC-1nqiE)

I got a new Windows computer and recorded a video of myself installing everything from scratch. I want to start with a clean slate.

I will also create text instructions from this, which might be more useful than the video.[^1][^2]

By the end I want a working dev setup that includes:

- A terminal with bash
- Python and NodeJS
- Docker and VS Code
- The other tools I rely on day to day

## Windows Terminal

Newer versions of Windows already come with Terminal pre-installed. If you don't have it, go to Windows Store and search for "Windows Terminal" - install that app.

## Git and Git Bash

Search for "git for windows" and go to git-scm.com. Download and run the installer.

During installation:
- Check the option to add Git Bash profile to Windows Terminal
- Select nano as the default editor (not Vim)
- Choose "main" as the default branch name
- The rest of the options can stay at defaults

Git for Windows comes with MinGW, which gives you bash on Windows. It also installs Vim and other tools.

After installation, restart Windows Terminal. Git Bash should appear as a new profile. If it did not get added automatically, go to Settings → Profiles and add a new profile pointing at Git Bash.

## Setting Git Bash as default

Go to Settings, Startup, and change the default profile to Git Bash.

## Customizing the terminal

Change the font to Consolas (or your preferred font) and increase the font size for readability - especially useful when recording videos. Adjust the terminal size in columns and rows (for example, 100 columns and 28 rows).

## Configuring GitHub SSH

To be able to clone private repositories, you need to set up an SSH key.

Generate a new SSH key:

```bash
ssh-keygen
```

Use your email when prompted. You can skip the passphrase.

Then go to GitHub Settings, SSH and GPG keys, click "New SSH key", give it a name (like your computer name), and paste the contents of your public key (`~/.ssh/id_rsa.pub`).

After adding the key, cloning private repos should work.

A useful Windows tip: press Windows+V instead of Ctrl+V to access clipboard history with previously copied items.

## Visual Studio Code

Download VS Code from the official website and run the installer.

After installation, configure the font size - go to Settings and change:
- Editor font size to 20 or larger (useful for recording and readability)
- Terminal font size to something comfortable as well

VS Code should automatically detect Git Bash and make it available in the integrated terminal.

The font will default to Consolas, which is readable at small sizes and renders punctuation clearly for code.

Copilot configuration can be done separately - it is not critical for the initial setup.

## Python and UV

Install UV (Python package manager) using the official install command in PowerShell. UV gets installed to the local bin directory.

After installation, restart the shell or run the provided command to add UV to your PATH. Verify with `where uv` (PowerShell) or `which uv` (bash).

## Setting up a global Python

UV can download Python automatically. To set up a "global" Python that is always available:

Create a directory structure for Python installations:

```bash
mkdir -p ~/bin/pythons/python313
cd ~/bin/pythons/python313
uv init
uv run python main.py
```

This downloads Python 3.13 and creates a virtual environment.

Then install pip into it:

```bash
uv pip install pip
```

## Configuring PATH in .bashrc

Edit `~/.bashrc` to add the bin directory and the Python scripts to your PATH:

```bash
export PATH="$HOME/bin:$HOME/bin/pythons/python313/.venv/Scripts:$PATH"
```

The key is to put your custom paths first, so they take priority. After sourcing bashrc, `which python` should point to your UV-managed Python.

This gives you a default Python for tools like Claude Code that just call `python` directly. When you use `uv run python` inside a project, it will use that project's virtual environment instead.

Note: on the first run of a Git Bash session, the `.bashrc` file might not be sourced automatically. Git Bash may create a `.bash_profile` that sources `.bashrc` - this happens once automatically.

## NodeJS and NVM

Install NVM for Windows (Node Version Manager) from the nvm-windows GitHub releases page. Use the installer.

After installation, open a new terminal and install the LTS version of Node:

```bash
nvm install lts
```

NodeJS is needed by many programs. For example, Claude Code requires it.

## Make (via Chocolatey)

To install Make, first install Chocolatey (a package manager for Windows). Run this in PowerShell as administrator:

The Chocolatey install command is available on their website - it sets the execution policy and runs the install script.

Then install Make:

```bash
choco install make
```

This needs to run in an administrator terminal. After installation, `make` is available in any new terminal.

Make requires tabs in Makefiles, not spaces. Install a Makefile extension in VS Code so it uses the correct formatting.

Example Makefile:

```makefile
run:
	uv run python main.py
```

Then just run `make run` - convenient.

## Docker

Search for "Docker Desktop Windows 11" and install Docker Desktop. You can get it from the Microsoft Store or the Docker website.

Choose the WSL 2 (Windows Subsystem for Linux) backend. With this option, you can also have a proper Linux installed on your computer. Docker will handle enabling WSL if needed.

After installation, a computer restart is required. Accept the terms, and Docker should be ready.

Verify with:

```bash
docker run hello-world
```

The installation was straightforward. On Windows 10 Home a few years ago it used to be a real struggle that took days to figure out. Now it just works.

## GitHub CLI

GitHub CLI is a useful tool when working with GitHub, especially with coding agents. It can create issues, create pull requests, clone repos, and turn things into GitHub projects.

Download the installer from the GitHub CLI website and run it.

After installation, authenticate:

```bash
gh auth login
```

Follow the prompts to authorize in the browser.

## Claude Code

Install Claude Code using the native installer. Previously it was installed with `npm install -g @anthropic-ai/claude-code`, which was simpler. Now there is a PowerShell install script.

The npm install approach was more convenient - just one command. The new way requires downloading a binary, which is a bit more complicated.

## OpenCode

Install OpenCode Desktop from their website. OpenCode is used as a desktop app, while Claude Code is used from the terminal.

OpenCode comes with a free model by default, but you will hit limits fast. Configure it with your own provider credentials for better results.

## VS Code Extensions

A few useful extensions to install:
- GitHub Codespaces - connect to Codespaces from VS Code
- Python - Python language support
- Ruff - Python formatting

After installing the Python extension, VS Code automatically detects virtual environments. Test discovery can be configured separately.

## Summary

The whole setup took over an hour.

Everything from the initial list is installed:

- Windows Terminal and Git Bash
- Python (via UV) and NodeJS (via NVM)
- Docker and VS Code
- GitHub CLI, Claude Code, and OpenCode

I probably forgot something, but might record a follow-up later.

## Sources

[^1]: [20260311_194019_AlexeyDTC_msg2832.md](../inbox/used/20260311_194019_AlexeyDTC_msg2832.md)
[^2]: [YouTube: Setting up a Windows computer for development](https://www.youtube.com/watch?v=2H8aC-1nqiE)
