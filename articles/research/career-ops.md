---
title: "Career Ops: AI-Powered Career Management"
created: 2026-04-09
updated: 2026-04-09
tags: [research, career, ai-agents]
status: draft
---

# Career Ops: AI-Powered Career Management

Career-ops is an open-source system that turns Claude Code into a full job search command center. It was built by Santiago Fernandez, who used it to evaluate 740+ job listings, generate 100+ tailored CVs, and land a Head of Applied AI role.

The repo is at github.com/santifer/career-ops.

## What It Does

The system automates the entire job search pipeline: discovering job listings, evaluating fit, generating tailored CVs, preparing for interviews, and tracking applications.

It is not a "spray and pray" tool. It is a filter. The system scores each offer on a 1-5 scale and recommends against applying to anything below 4.0. The human always makes the final decision. The system never submits applications automatically.

Key capabilities:

- Scan 45+ company career pages automatically using Playwright
- Evaluate each job against your CV using a structured A-F scoring system
- Generate ATS-optimized PDF resumes tailored to each job description
- Build an interview story bank with STAR+Reflection format
- Track all applications in a single markdown file
- Batch-process 10+ offers in parallel using sub-agents

## Architecture

The system is built as a collection of "modes" (prompt files) that Claude Code reads as instructions. There is no traditional application server. Claude Code is the runtime.

### Core Components

The project has two layers, defined in a strict data contract:

User Layer (never auto-updated):
- `cv.md` - your CV in markdown
- `config/profile.yml` - identity, target roles, compensation range
- `modes/_profile.md` - your archetypes, narrative, negotiation scripts
- `data/applications.md` - application tracker
- `portals.yml` - companies to scan
- `reports/` and `output/` - generated reports and PDFs

System Layer (safe to auto-update):
- `modes/_shared.md` - scoring system, global rules, tool configuration
- `modes/oferta.md`, `modes/scan.md`, etc. - 14 mode files
- `*.mjs` scripts - PDF generation, pipeline verification, dedup
- `dashboard/` - Go TUI for browsing the pipeline
- `templates/` - HTML CV template, portal config template

This separation means the system can update itself without touching your personal data.

### Mode System

Each mode is a markdown file that defines behavior for one task. There are 14 modes:

| Mode | Purpose |
|------|---------|
| oferta | Single offer evaluation (A-F blocks) |
| pdf | ATS-optimized CV generation |
| scan | Portal scanning with Playwright |
| batch | Parallel evaluation with sub-agents |
| apply | Live application form filling |
| contacto | LinkedIn outreach messages |
| deep | Deep company research |
| ofertas | Compare and rank multiple offers |
| pipeline | Process pending URLs from inbox |
| tracker | Application status overview |
| training | Evaluate courses and certifications |
| project | Evaluate portfolio project ideas |
| patterns | Analyze rejection patterns |
| interview-prep | Interview preparation and story bank |

Modes also come in German (`modes/de/`) and French (`modes/fr/`) for DACH and Francophone job markets.

### Evaluation Pipeline

When you paste a job URL, the system runs through 6 blocks:

1. Block A - Role Summary: archetype detection, domain, function, seniority, remote policy
2. Block B - CV Match: maps each JD requirement to exact lines in your CV, identifies gaps with mitigation strategies
3. Block C - Level Strategy: detected level vs your natural level, "sell senior without lying" plan
4. Block D - Comp Research: uses web search for salary data from Glassdoor, Levels.fyi, Blind
5. Block E - Personalization Plan: top 5 changes to CV and LinkedIn for this specific role
6. Block F - Interview Prep: 6-10 STAR+Reflection stories mapped to JD requirements

The system classifies every offer into one of 6 archetypes: AI Platform/LLMOps, Agentic/Automation, Technical AI PM, AI Solutions Architect, AI Forward Deployed, or AI Transformation. The archetype determines which proof points and framing to use.

### Batch Processing

The batch system uses a conductor-worker architecture. The conductor (Claude Code with Chrome) navigates career portals. For each job listing, it spawns a `claude -p` worker with a clean 200K token context.

```
Conductor (claude --chrome)
  ├── Worker 1: claude -p → report + PDF + tracker line
  ├── Worker 2: claude -p → report + PDF + tracker line
  └── Worker N: claude -p → report + PDF + tracker line
```

Workers run in parallel (configurable with `--parallel N`). State is tracked in a TSV file for resumability. Failed evaluations can be retried with `--retry-failed`.

### Portal Scanner

The scanner operates at three levels:

1. Playwright direct - navigates each company's careers page, reads the DOM, extracts listings. Most reliable method.
2. Greenhouse API - uses `boards-api.greenhouse.io` for structured JSON data. Faster than Playwright but only works with Greenhouse.
3. WebSearch queries - broad discovery across job boards (Ashby, Greenhouse, Lever, Wellfound). Useful for finding new companies.

Results from all three levels are merged and deduplicated against scan history.

### PDF Generation

CVs are generated as PDF using Playwright/Puppeteer. The system fills an HTML template (`templates/cv-template.html`) with content tailored to each job description, then renders it to PDF. Fonts are self-hosted (Space Grotesk + DM Sans). Unicode characters are normalized to ASCII for ATS compatibility.

## Technologies

- Claude Code as the AI agent runtime (also supports OpenCode)
- Node.js for utility scripts (PDF generation, pipeline verification, dedup, merge)
- Playwright for browser automation (portal scanning, PDF rendering)
- Go + Bubble Tea + Lipgloss for the terminal dashboard UI
- Markdown tables + YAML config + TSV files for data storage
- No database. No server. Everything runs locally on the user's machine.

The only npm dependency is Playwright. Everything else is vanilla Node.js with `.mjs` modules.

## Key Insights

### The system learns from the user over time

The first evaluations are not great because the system does not know you yet. The CLAUDE.md instructions explicitly tell the user this. As you feed it more context - your CV, career story, proof points, preferences - it improves. The onboarding process asks probing questions: "What's your superpower?", "What excites you?", "Any deal-breakers?"

After every evaluation, the system updates `_profile.md` with what it learned from user feedback. This creates a compounding effect where later evaluations are much more accurate.

### Data contract as upgrade strategy

The strict user/system layer separation is smart. It means the project can ship updates (new modes, better scoring logic, bug fixes) without risking user data. The `update-system.mjs` script checks for updates, applies them to system-layer files only, and supports rollback. This is rare for an open-source CLI tool.

### Claude Code as the entire application layer

There is almost no traditional application code. The "application" is a collection of markdown prompt files that Claude Code interprets. The Node.js scripts are thin utilities for tasks that need deterministic behavior (PDF rendering, file merging, dedup). This is an extreme example of "prompt as code."

### Archetype-driven personalization

Instead of generic resume optimization, the system classifies each role into an archetype and adapts everything - which proof points to highlight, how to frame experience, which STAR stories to prepare. This produces much better results than keyword matching.

### The interview story bank compounds

Each evaluation generates 6-10 STAR+Reflection stories mapped to JD requirements. These accumulate in `interview-prep/story-bank.md`. Over time, you build a reusable bank of 5-10 master stories that can answer any behavioral question. The Reflection component (what was learned, what would be done differently) signals seniority.

### Anti-spam philosophy

The system explicitly discourages applying to low-scoring offers. The scoring threshold (4.0/5) is high. The README states: "Your time is valuable, and so is the recruiter's." This is the opposite of the typical job search automation tool that blasts hundreds of applications.

## Actionable Patterns

The profile.yml config structure is a good template for any AI agent that needs persistent user context:

```yaml
candidate:
  full_name: "Jane Smith"
  location: "San Francisco, CA"

target_roles:
  primary:
    - "Senior AI Engineer"
  archetypes:
    - name: "AI/ML Engineer"
      level: "Senior/Staff"
      fit: "primary"      # primary / secondary / adjacent

narrative:
  headline: "ML Engineer turned AI product builder"
  exit_story: "Built and sold my SaaS. Now focused on applied AI."
  superpowers:
    - "End-to-end ML pipelines"
    - "Fast prototyping"
  proof_points:
    - name: "Project Alpha"
      hero_metric: "Reduced inference latency 40%"

compensation:
  target_range: "$150K-200K"
  minimum: "$120K"
```

The batch runner pattern (conductor + `claude -p` workers) is reusable for any task that needs parallel AI processing with state tracking and resumability.

## Resources

### GitHub Repository

Source: https://github.com/santifer/career-ops

### Author's Case Study

Source: https://santifer.io/career-ops-system

## Notes

- This is one of the most complete examples of "Claude Code as application runtime" in the wild. The entire application logic lives in markdown prompt files.
- The data contract pattern (user layer vs system layer) is worth studying for any project that ships AI agent configurations as open source.
- The conductor-worker batch pattern is similar to the parallel agent patterns in the [Claude Agent Teams Research](claude-agent-teams.md).
- The mode system is comparable to gstack's skill modes (see [gstack research](gstack.md)), but career-ops has a more structured data model.

[^1]: [20260409_064531_AlexeyDTC_msg3313.md](../../inbox/used/20260409_064531_AlexeyDTC_msg3313.md)
