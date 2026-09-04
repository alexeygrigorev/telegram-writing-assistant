# Project screenshot guide

This guide documents the repository-local workflow used to capture project screenshots for an article. It uses `ai-engineering-buildcamp-cohort-3-projects.md` as the worked example, but the same process applies to any article that links to runnable GitHub projects.

The goal is to produce an honest, useful figure for the article. A screenshot can use local fixtures or deterministic mocks when a live API is unavailable, but the result note and caption must say so. A local mock is not presented as a live production result.

## The workflow in one pass

1. Read the article and make a project inventory.
2. Give each project its own isolated checkout, port, temporary data directory, and asset directory.
3. Read the project README and identify its real entry point, seed command, integrations, and useful demo state.
4. Try the documented public deployment when one exists, without creating accounts or making paid requests.
5. Run the project locally with `uv`, `npm`, or the documented command.
6. Replace only unavailable external dependencies with local fixtures or deterministic mocks.
7. Drive the real UI with a headless browser, or capture the real CLI artifact when the project has no UI.
8. Inspect the raw image, crop it without cutting text, and inspect the final PNG again.
9. Add one descriptive `<figure>` near the matching project section.
10. Record the source, command, fixture, mock, screenshot, and limitation in `RESULT.md`.
11. Verify paths, markdown, image dimensions, tests, and running processes before committing.

## 1. Inventory the article first

Start from the article rather than from the GitHub organization. This prevents screenshots for projects that are not actually mentioned and preserves the article's order.

```bash
article=articles/raw-articles/ai-engineering-buildcamp-cohort-3-projects.md
rg -n 'github\.com|illustration:|<figure>|assets/images' "$article"
```

For each project, record these fields before launching anything:

- The project name and author as written in the article.
- The GitHub URL and the exact repository subdirectory, if the project lives below the repository root.
- A public app or demo URL, if the article contains one.
- The existing illustration placeholder or the section where a figure belongs.
- The most informative state to capture, such as a result page, review screen, dashboard, generated artifact, or report.

The Buildcamp article had twelve GitHub-linked projects and one project without a GitHub link. We captured the twelve linked projects and left Salma's existing illustration placeholder in place. A public Streamlit URL was treated as a lead, not as evidence that the page would be accessible. Several public deployments redirected to authentication or timed out, so their local checkouts became the capture source.

Use a stable slug for each asset directory:

```text
assets/images/ai-engineering-buildcamp-cohort-3-projects/<project-slug>/
```

Keep only final PNGs and the run record in that directory. Raw screenshots and temporary browser output belong in `/tmp`, not in the article asset directory.

## 2. Split the work into five disjoint workstreams

Five agents were used for the Buildcamp article. Each agent received a disjoint project list and was told to write only to its own asset directories. The parent process kept ownership of the article markdown, so agents could not overwrite each other's figures or change article prose.

The actual grouping was:

1. Amar's ATS Gap Analyser, Marco's Applied ML Teaching Copilot, and Lars's Datawarehouse Agent.
2. Leo's Chess Coach Agent, Paulien's Document Preparation Agent, and Miki's WorkerChronicle.
3. Hana's Research Radar and Thet's AI Diet Coach.
4. Wesley's AI Learning OS and Dianne's LearnMate AI.
5. Nitesh's Multi-Agent Software Development Platform and Katja's GapFinder.

The prompt for each workstream should include the source URL, output directory, a local port range, and these constraints:

```text
You own only these project asset directories: <list of directories>.
Read each repository README and run the smallest documented path that produces a meaningful screen.
Use an isolated temporary checkout. Do not edit the article or any other agent's directory.
Do not use real credentials, paid model calls, external writes, or real user accounts.
Use built-in examples, repository fixtures, local data, or deterministic mocks when an integration is unavailable.
Capture the real project UI or the real CLI artifact. Do not invent a fake product screen.
Save final PNGs and a RESULT.md in your assigned asset directory.
For every screenshot, record the exact source file, run command, input data, mocked integrations, and limitations.
Stop servers before reporting completion.
```

Each agent reports a result even when a project cannot be run. The report distinguishes “real UI with local fixture” from “live integration” and explains why a public deployment was not used. This makes later article editing and review possible without relying on memory from the terminal session.

## 3. Inspect a repository before changing or running it

Read the README, dependency files, startup files, and seed scripts. Search for the commands and environment variables instead of guessing them.

```bash
rg -n 'uv sync|streamlit|uvicorn|npm (ci|install|run)|make seed|OPENAI_API_KEY|ANTHROPIC_API_KEY|GROQ_API_KEY|DATABASE_URL|STOCKFISH|README' \
  README.md pyproject.toml Makefile app.py src web gapfinder_agent 2>/dev/null || true
```

Then answer four questions:

- Is this a web app, an API plus frontend, a CLI, or a library with a demo script?
- Which command creates the data the UI expects?
- Which integrations are required only at import time, and which are called during the capture?
- Which screen demonstrates the project's distinctive behavior rather than an empty landing page?

The exact upstream source file should be recorded in the result note. Use the repository's blob path, not only the repository root:

```text
Source: https://github.com/OWNER/REPOSITORY/blob/main/path/to/README.md
```

For a project whose relevant instructions are in `DEMO.md`, `app.py`, or `src/db/setup_db.py`, cite that file as well. The source line is the link between the screenshot and the code that was actually inspected.

## 4. Use an isolated checkout and temporary state

Never patch the main writing-assistant checkout with project-specific application code. Clone each project into a uniquely named temporary directory and put databases, vector stores, caches, and generated files under that directory.

```bash
work_root="$(mktemp -d /tmp/twa-project-screenshot.XXXXXX)"
git clone --depth 1 "https://github.com/OWNER/REPOSITORY.git" "$work_root/repository"
cd "$work_root/repository"
uv sync
```

Use a different `work_root` and port for every project. For databases, pass an absolute temporary path instead of allowing a clone to reuse a developer database. The Chess Coach capture used a temporary SQLite file and a downloaded local Stockfish binary. The LearnMate capture used separate temporary SQLite and Chroma paths. These choices kept one project's state from influencing another project's screenshot.

If a project has a lock file, use its corresponding reproducible install command. The runs in this article used `uv sync`, `uv sync --extra dev`, or `uv sync --python 3.13` as required by the repository. For JavaScript frontends, use `npm ci` when `package-lock.json` exists and `npm install` when the repository documents that command.

## 5. Run the smallest useful local path

Bind local servers to `127.0.0.1`, assign a unique port, and disable analytics where the framework supports it. A typical Streamlit command is:

```bash
OPENAI_API_KEY=sk-local-demo uv run streamlit run app.py \
  --server.headless true \
  --server.address 127.0.0.1 \
  --server.port 8511 \
  --browser.gatherUsageStats false
```

The placeholder key above is deliberately not a credential. It can satisfy a client constructor, but it must never be allowed to reach a provider. If the application makes a request after startup, replace that call with a local fixture before opening the page.

For the ATS app, the documented entry point was under `src/` and the built-in example was the best deterministic path:

```bash
uv sync
GROQ_API_KEY=mock-not-a-secret uv run streamlit run src/app.py \
  --server.headless true \
  --server.address 127.0.0.1 \
  --server.port 8501
```

The browser then selected “See example”. The screenshot showed the real layout, result cards, score, missing keywords, suggestions, and cover-letter section. It did not claim that a live CV analysis had run.

For an API plus frontend, start the backend first and point the frontend at the local port. LearnMate used this pattern:

```bash
uv sync
cd web
npm install
```

The isolated data stores and servers were then started as separate processes:

```bash
LEARNMATE_DB=/tmp/buildcamp-ws4.BPcQgi/learnmate.db \
LEARNMATE_CHROMA_DIR=/tmp/buildcamp-ws4.BPcQgi/.chroma_data \
uv run python -m learnmate.persistence.seed
```

After the seed completed, the FastAPI backend ran on port `8521` and the Vite frontend on port `8522`:

```bash
OPENAI_API_KEY=sk-local-demo \
LEARNMATE_DB=/tmp/buildcamp-ws4.BPcQgi/learnmate.db \
LEARNMATE_CHROMA_DIR=/tmp/buildcamp-ws4.BPcQgi/.chroma_data \
PYTHONPATH=. uv run uvicorn learnmate.api.app:app --host 127.0.0.1 --port 8521
```

The frontend was pointed to the local backend in a separate shell:

```bash
VITE_API_TARGET=http://127.0.0.1:8521 npm run dev -- --host 127.0.0.1 --port 8522
```

For a CLI-only project, run the actual CLI and capture the generated artifact instead of pretending that a UI exists. The Document Preparation Agent was run like this:

```bash
uv sync
uv run python -m rag_dataprep_agent.cli data/Arxiv \
  --output-dir /tmp/twa-rag-prepared \
  --max-files 1
```

The screenshot rendered fields from the generated `prepared/manifests/2605.00016v1.json`, including the source path, document type, title, authors, keywords, chunk id, and extracted text. It was labeled as a manifest result and not as a product dashboard.

## 6. Change only the isolated project copy

There were four kinds of local changes in the Buildcamp runs:

1. Fixture files were added when a repository had no committed demo data. AI Learning OS received temporary queue, knowledge-base, progress, and monitoring JSON files. Research Radar received local run records built from its checked-in ground-truth paper data. AI Diet Coach received a demo profile, meal plan, logs, and traces based on its recipe files.
2. A required service was replaced at the narrowest boundary. Teaching Copilot and WorkerChronicle kept their retrieval, database, review, and outline logic, while their model call was replaced with a deterministic local response. Datawarehouse kept its schema and Streamlit UI, while its refinement and SQL answer was supplied by a local screenshot mode.
3. A local fixture server supplied integration responses. The Multi-Agent platform UI was pointed at a local deterministic API that returned PM stories, a task artifact ZIP, and a review-stage pull request state. Jira, GitHub, and the LLM were not contacted.
4. A browser-only mock supplied the real-time messages that the UI expected. LearnMate used deterministic local WebSocket messages for `/ws/review` and `/session`, while its REST calls, backend, progress calculations, and review screen remained real local application code.

Apply a patch only inside the temporary checkout. Keep the patch small, and record its purpose in `RESULT.md`.

```bash
apply_patch <<'PATCH'
*** Begin Patch
*** Update File: path/to/temporary/checkout/file.py
@@
     result = call_external_provider(prompt)
+    # Screenshot-only local fixture. Keep this change in the temporary checkout.
+    result = local_demo_result(prompt)
*** End Patch
PATCH
```

The example above shows the boundary, not a patch to copy blindly into a project. The actual patch must match the project's functions and data types. A patch is acceptable when it lets the real UI exercise the same state transitions and rendering code. It is not acceptable when it replaces the whole application with a static image or fabricates data that the UI would never display.

Before and after a run, check the process output for accidental network calls. A fake key only prevents some SDKs from failing during initialization; it does not guarantee offline execution. The result note must list every skipped integration, such as OpenAI, Anthropic, Groq, arXiv, YouTube, USDA, Google Maps, Resend, Jira, GitHub, or Logfire.

## 7. Capture the browser state with Playwright

The available local browser was Chromium. Playwright was imported with `/usr/bin/python3`, and the browser executable was selected from the installed Playwright cache. The capture used a fixed viewport, waited for the page to settle, performed the useful interaction, reset the scroll position, and saved a PNG without browser chrome.

This is the reusable capture skeleton:

```bash
SCREENSHOT_URL=http://127.0.0.1:8511 SCREENSHOT_PATH=/tmp/project-raw.png \
/usr/bin/python3 - <<'PY'
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

url = os.environ["SCREENSHOT_URL"]
output_path = Path(os.environ["SCREENSHOT_PATH"])

with sync_playwright() as playwright:
    browser_candidates = [
        os.environ.get("PLAYWRIGHT_CHROMIUM", ""),
        "/home/alexey/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome",
        "/usr/bin/chromium",
        "/snap/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    browser_path = next(
        (candidate for candidate in browser_candidates if candidate and Path(candidate).exists()),
        None,
    )
    launch_options = {"headless": True, "args": ["--no-sandbox"]}
    if browser_path:
        launch_options["executable_path"] = browser_path
    browser = playwright.chromium.launch(**launch_options)
    page = browser.new_page(
        viewport={"width": 1440, "height": 900},
        device_scale_factor=1,
    )
    page.goto(url, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(2500)

    # Replace this with the interaction that produces the project's useful state.
    page.evaluate("window.scrollTo(0, 0)")
    page.screenshot(path=str(output_path), full_page=False)
    browser.close()
PY
identify /tmp/project-raw.png
```

The cached Chromium directory can change when Playwright is upgraded. If that path is absent, use the installed Chromium binary or set the executable path for the current environment. Keep the viewport and device scale factor explicit so a later capture can be compared with the first one.

Interactions are performed before the final screenshot. For the ATS example, the relevant interaction was:

```python
page.get_by_role("button", name="💡 See example").click()
page.wait_for_timeout(1700)
page.evaluate("window.scrollTo(0, 0)")
page.screenshot(path=str(output_path), full_page=False)
```

For a chat screen, fill the real input and submit it, then wait for the result. For the Datawarehouse screen, the question was entered with its placeholder and the SQL expander was opened:

```python
question = page.get_by_placeholder("Ask a question about incidents...")
question.fill("How many incidents happened at Utrecht Centraal in 2024?")
question.press("Enter")
page.wait_for_timeout(2500)
page.get_by_text("🛠️ SQL details").click()
page.wait_for_timeout(500)
page.evaluate("window.scrollTo(0, 0)")
page.screenshot(path=str(output_path), full_page=False)
```

Use accessible roles, labels, and placeholders when possible. They survive layout changes better than coordinates. Use coordinates only when a canvas or board makes semantic selectors impossible, and record that choice in the run note.

Choose `full_page=False` for an article figure when one viewport contains the useful result. Use `full_page=True` only when the full page is the artifact, then crop it deliberately. For long reports, a wider viewport is usually safer than shrinking the page because small text becomes unreadable and responsive columns can overlap.

## 8. Handle projects without a live API

The order of preference is:

1. A repository-provided example or fallback, such as ATS Gap Analyser's “See example”.
2. A checked-in fixture, sample PDF, sample PGN, recipe file, or ground-truth dataset.
3. A local deterministic fixture inserted through the project's normal database or file format.
4. A narrow local replacement for one external provider call.
5. A local HTTP or WebSocket fixture server when the frontend needs a separate service.

The Chess Coach run used the included sample PGN and local Stockfish, so engine analysis and practice grading stayed local even though the LLM explanation used the project's deterministic fallback. The WorkerChronicle run used its real SQLite extraction, review, and outline functions with fictional local material and a fake model provider. GapFinder used a temporary checkout-only demo flag that injected a deterministic transcript and agent conversation, while the real Streamlit report page rendered the result.

Do not silently turn a failed live run into a success claim. Use language such as “real Streamlit UI with a local fixture” or “actual CLI manifest rendered from a local sample PDF”. Do not use language such as “the production agent generated this answer” unless the production call really happened and was authorized.

Public deployments are checked without credentials first. If a deployment redirects to auth, requires an account, times out, or has a broken dependency, stop there. Do not sign up, upload private data, or trigger a paid request simply to obtain a screenshot. Continue with the documented local path and write down the public-deployment outcome.

## 9. Crop and inspect every image

The raw browser viewport is not automatically article-ready. First inspect its dimensions and then open it visually. During this run, `identify` checked dimensions and the local image viewer inspected the actual content. The crop was chosen only after checking that headings, labels, answer text, and status badges were complete.

```bash
identify /tmp/project-raw.png
```

Use ImageMagick's `convert` with an explicit rectangle:

```bash
convert /tmp/project-raw.png \
  -crop 1440x875+0+0 +repage \
  assets/images/ai-engineering-buildcamp-cohort-3-projects/project-slug/project-result.png
identify assets/images/ai-engineering-buildcamp-cohort-3-projects/project-slug/project-result.png
```

The crop syntax is `WIDTHxHEIGHT+X+Y`. `+repage` removes the old canvas offset so the final PNG has the expected dimensions. Keep the project title and the result that explains why the screenshot belongs in the article. Remove browser chrome, terminal windows, empty margins, duplicate navigation, and unused input controls. Never remove a line of text merely to make the image shorter.

Two crops from this article show the decision process:

```bash
convert /tmp/gapfinder-report-wide-2.png \
  -crop 1800x970+0+0 +repage \
  assets/images/ai-engineering-buildcamp-cohort-3-projects/gapfinder/02-gap-report.png
```

GapFinder was rendered at `1800x1100`, but the lower part contained clipped text. A top crop of `1800x970` kept the complete report rows and removed the damaged area. Datawarehouse used the same top-crop approach after the real UI was rendered at `1440x1100`:

```bash
convert /tmp/datawarehouse-agent-mock-top.png \
  -crop 1440x875+0+0 +repage \
  assets/images/ai-engineering-buildcamp-cohort-3-projects/datawarehouse-agent/datawarehouse-agent-answer.png
```

If the first capture clips text, recapture at a wider viewport before cropping. Do not solve a responsive-layout problem by making the final image smaller. If the page scroll position lands on the input, reset it before the screenshot. If a fixed header covers the first line, adjust the page scroll or capture clip rather than cutting the line after the fact.

Avoid `-trim` as a default. White application backgrounds and sidebars can be meaningful, and automatic trimming can produce inconsistent widths across a set of figures. An explicit crop gives predictable article layout. After cropping, inspect the final PNG at its actual size and confirm that small text remains readable.

## 10. Keep a result record beside the images

Every project directory should contain `RESULT.md`. It is the audit trail for the capture and prevents a future editor from mistaking a fixture for a live run.

Use this template:

````markdown
# Project name result

Source: https://github.com/OWNER/REPOSITORY/blob/main/path/to/relevant-file.md

Run outcome: real local UI or CLI artifact with a local fixture.

Run command:

```bash
uv sync
uv run <documented-command>
```

Inputs and fixtures:

- Describe the sample file, seed data, or temporary fixture.

Mocks and skipped integrations:

- Name every provider or service that was not contacted.

Screenshots:

- `project-result.png` - describe the visible state.

Limitations:

- Explain public deployment failures and what the screenshot does not prove.
```
````

The actual Buildcamp result notes are under `assets/images/ai-engineering-buildcamp-cohort-3-projects/*/RESULT.md`. They include the local commands, filenames, dimensions, deterministic mock boundaries, and limitations for ATS, Chess Coach, RAG Data Prep, Research Radar, Diet Coach, Learning OS, Teaching Copilot, Datawarehouse, WorkerChronicle, Multi-Agent, LearnMate, and GapFinder.

Do not put keys in `RESULT.md`. Values such as `sk-local-demo`, `fake-local-demo`, and `mock-not-a-secret` are placeholders used only to satisfy local initialization code. They are not credentials and must not be changed to real keys for this workflow.

## 11. Add the figure to the article

The target article is two directories below the repository root, so its image paths start with `../../assets/`. Use one figure close to the project description and keep the alt text factual.

```markdown
<figure>
  <img src="../../assets/images/ai-engineering-buildcamp-cohort-3-projects/project-slug/project-result.png" alt="Project result screen showing the completed analysis and its key status details">
  <figcaption>Project result screen showing the completed analysis and its key status details</figcaption>
</figure>
```

The caption should describe what is visible, not what the project promises in its README. If the result came from local data, that fact can go in the caption when it matters, and it must always go in `RESULT.md`. Keep the original placeholder when the article has no GitHub source or when no honest capture can be produced.

Do not change the article's prose just to make a screenshot fit. If a figure needs a different state, recapture the project and replace the PNG. If a screenshot is removed, remove its figure and its asset together.

## 12. Verify before committing

Check that every article image reference resolves from the article's directory:

```bash
article=articles/raw-articles/ai-engineering-buildcamp-cohort-3-projects.md
rg -oP '(?<=src=")[^"]+' "$article" | while IFS= read -r relative_path; do
  full_path="articles/raw-articles/$relative_path"
  if test -f "$full_path"; then
    echo "OK $full_path"
  else
    echo "MISSING $full_path"
    exit 1
  fi
done
```

Check all final image dimensions and look at the final files, not only the raw captures:

```bash
find assets/images/ai-engineering-buildcamp-cohort-3-projects \
  -type f -name '*.png' -print0 | xargs -0 identify
```

Run the repository checks:

```bash
git diff --check
python scripts/check-links.py
pytest -q tests/test_check_links.py
```

The link-check test may print messages from its temporary fixture, including a “Fixed” line. That output belongs to the test fixture; confirm the working tree afterward with `git status --short`. Also check that no capture server is still running and that no temporary database or generated file was copied into the repository.

```bash
git status --short
rg -n 'illustration:|<figure>|assets/images/ai-engineering-buildcamp-cohort-3-projects' "$article"
```

Only after these checks should the article, final PNGs, result notes, and this guide be committed. Push the branch and share the commit URL so the rendered markdown and image paths can be reviewed remotely.

## Troubleshooting

### The public app asks for authentication

Do not create an account for a screenshot. Use the repository's local startup path and record that the public URL redirected to authentication. This happened for several Streamlit projects in the Buildcamp run.

### Import fails because Logfire or an SDK expects a key

Determine whether the key is needed only during initialization. Disable telemetry or provide a clearly fake local value in the temporary checkout, then verify that the code path does not make a network request. Do not add the value to the writing-assistant repository.

### The seed process hangs or grows a database WAL

Stop the bounded attempt, preserve the evidence in `RESULT.md`, and create the smallest schema-compatible fixture in the isolated checkout. Datawarehouse's full seed remained in disk I/O even after reducing it to 500 rows, so the screenshot used the repository schema with two local Utrecht incidents and a deterministic answer in the real Streamlit UI.

### A fake API key still causes an outbound request

Replace the provider call before it runs, or intercept the exact local HTTP or WebSocket route. Check the server logs and the mock implementation. A fake key is not an offline mode by itself.

### The screenshot is clipped or unreadable

Increase the viewport width, wait for the app's final state, expand the relevant details, reset the scroll position, and recapture. Crop only after the layout is correct. Keep the final image large enough that the result can be read in the article.

### The project has no UI

Run the real CLI against a checked-in sample, then render the generated JSON or other artifact with its actual fields. Label the figure as a CLI or manifest result. Do not create a fake dashboard to imply that the project has a web interface.

### A frontend shows an empty page

Start the backend first, verify its local health or API response, set the frontend API target explicitly, and then open the Vite or other frontend port. Use separate ports and temporary data stores for every project.

## Worked capture summary for this article

The final figures followed this evidence pattern:

- ATS used its built-in example with no API credits.
- Chess Coach used the sample PGN, local Stockfish, SQLite, and the deterministic no-key practice fallback.
- RAG Data Prep used the real CLI and a manifest generated from the included arXiv PDF.
- Research Radar, Diet Coach, and AI Learning OS used real local dashboards populated with repository data and clearly synthetic local state.
- Teaching Copilot, WorkerChronicle, Datawarehouse, and GapFinder used the real application path with a narrow deterministic local replacement where a provider call was unavailable.
- Multi-Agent used the real Streamlit UI with a local fixture API for PM, artifact, and review states.
- LearnMate used the real local backend and React screens with deterministic WebSocket messages only for the live review conversation.

The screenshots therefore show working application surfaces and meaningful states, while the result notes preserve exactly which external integrations were not exercised.
