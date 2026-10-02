---
title: "Specs First: Building a Full-Stack App with AI Coding Agents"
created: 2026-10-02
updated: 2026-10-02
tags: [devmio, guest-article, spec-driven-development, coding-agents, full-stack, openapi, ai-shipping-labs, ai-dev-tools-zoomcamp]
status: draft
---

# Specs First: Building a Full-Stack App with AI Coding Agents

<!-- Guest article for devmio (Stephane Fernandes, Software & Support Media). Target: 15,000-20,000 characters / 3,000-4,000 words. Due before the end of October 2026, ahead of the November session in Berlin. -->

Coding agents now write code faster than anyone can read it. Give Codex or Claude Code a task and it produces a working implementation in minutes, so the bottleneck has moved. We no longer spend most of our time typing code. We spend it saying precisely what we want and checking what came back.

That shift becomes visible when the request is vague. A weak agent that misunderstands the task writes fifty lines of broken code. A strong agent that misunderstands the task creates eight files, wires them together, and adds tests that pass. The code works, but it isn't what we needed.

I once gave Claude Code a single line: "a tool for weekly feedback for projects". It built a command-line tool with documentation and 62 passing tests. What I actually wanted was a web tool for team retrospectives. The agent filled the gaps in my request with its own assumptions, and I had left a lot of gaps. I describe that experiment in [AI-Native Development: Specifications, Loop and Graph Engineering](https://aishippingblog.com/p/ai-native-development-specifications).

We can solve this the old-fashioned way: write the specification first, and let the code follow from it. Below, I show what that looks like on a concrete project. I took the material from the [full-stack workshop](https://aishippinglabs.com/workshops/full-stack-vibe-coding) I run at AI Shipping Labs. It's also the second module of [AI Dev Tools Zoomcamp](https://datatalks.club/blog/ai-dev-tools-zoomcamp.html), the free course we run at [DataTalks.Club](https://datatalks.club/). In the workshop, we build and deploy a multiplayer Snake game in one day, and a coding assistant writes almost all of the code.

I wrote it for developers who already use a coding assistant for small tasks and want to use it for a whole application. You don't need frontend, backend, or DevOps experience, because the assistant covers the parts you haven't worked with before. What you need is general software-development sense and the ability to read the result and decide when to ask for changes.

## Three Levels of Specification

"Spec-driven development" can sound like a heavy process with long requirement documents. In practice, it's a small set of written agreements.

Each agreement works at a different level:

- A project specification describes what we build and for whom. It exists before the first prompt.
- An API specification describes how the parts talk to each other. In a web app, this is the API, and we write it down as an OpenAPI file.
- A task specification describes one change: its goal, the acceptance criteria that decide when it's done, and what's out of scope.

On top of these sits the project context: a file such as `AGENTS.md` that tells every new agent session how the project works.

The rest of the article follows the order in which these documents appear during the build. We start with the project specification and the frontend. Then we extract the API spec and generate the backend from it. After that come persistence, deployment, and CI/CD. At the end, we look at task specifications and a small team of agents that takes over once the first version is live.

## The Example Application

We build a multi-user Snake game. In walls mode you die when you hit a wall, and in pass-through mode the snake wraps around the edges. On top of the game, there's a leaderboard with top scores per mode, a page to watch other players' active games, and login and signup.

The stack is deliberately ordinary:

- a React frontend generated with Lovable
- a FastAPI backend in Python
- SQLAlchemy with SQLite locally and Postgres in containers
- Docker Compose for the local stack
- AWS with CloudFormation for deployment
- GitHub Actions for CI/CD

In the final setup, one FastAPI container serves both the API under `/api` and the compiled frontend. The finished code is in the [snake-royale repository](https://github.com/alexeygrigorev/snake-royale).

<!-- illustration: architecture diagram from the workshop (images/architecture.svg) - React snake game in the browser calls one FastAPI app over /api routes, which stores game data through SQLAlchemy in SQLite or Postgres -->

I use Codex in the workshop, but the prompts are plain English. They work the same way in Claude Code, GitHub Copilot, Cursor, and other assistants. From here on, "the assistant" means whichever tool you use.

## The Project Specification

Before the first line of code, we need to know what we're building. When I only have a rough idea, I don't start in the coding assistant. I talk the idea through with a chat assistant like ChatGPT. I ask it to question me one point at a time about who the users are and what they need.

At the end, it saves the decisions into a markdown file, which goes into the repository as `_docs/plan.md`. This is the project specification.

For the Snake game, the requirements were already clear, so they went straight into the prompt for the frontend.

## Frontend First

We start with the frontend because it lets us see the screens and click through the game before any backend exists. From the UI, we can list the game states, the API calls, and the data the backend has to support.

In the workshop, we use [Lovable](https://lovable.dev/), which generates a complete React app from one prompt. Replit, v0, Bolt, or the coding assistant work too. On a free Lovable account you don't get many chances to correct the result.

That's why the prompt has to be specific:

```text
Create an interactive Snake game with two modes:

- walls (you die hitting a wall)
- pass-through (you wrap around the edges)

Make it multi-user. Add

- a leaderboard showing top scores per mode
- a page to watch other players' active games
- login and signup screens

Centralize every backend call in one services layer, and create a mock
implementation of it so the whole app runs without a real backend.

Add tests.
```

The second half of this prompt matters most for what comes later. We ask for one services layer that contains every backend call, plus a mock implementation of it.

The generated project gets a `services/` folder with an entrypoint that picks either an in-memory mock or a real HTTP client:

```text
src/
├── routes/         # index (home), play, leaderboard, watch, auth - one file per page
├── services/       # the single place every backend call lives
│   ├── index.ts    # the entrypoint: picks the mock or the real backend
│   ├── mock.ts     # in-memory fake backend, so the app runs with no server
│   ├── http.ts     # the real backend client (talks to the FastAPI app)
│   └── types.ts    # User, LeaderboardEntry, ActiveGame, request/response shapes
├── hooks/          # useAuth: who is logged in
└── components/     # SnakeBoard and the UI components
```

Because of the mock, the whole app runs locally with `npm run dev` before any backend code exists. Because of the services layer, the frontend's expectations of the backend are in one place, which is exactly what we need later. We push the code to GitHub, move it into `frontend/`, and continue in GitHub Codespaces, a disposable dev container.

## Project Context in AGENTS.md

Each new agent session starts with no memory of the project. Without context, the agent guesses at the tools we use, and those guesses aren't always right. We use `uv` for Python, for example, but the agent may assume pip. Then it creates a `requirements.txt` we don't need or installs a library into the global Python environment.

We fix this with an `AGENTS.md` file at the repository root. Codex, OpenCode, and most other assistants read it automatically when a session starts.

The first version is short:

```text
for backend, use uv for dependency management. a few useful commands:

uv sync
uv add <PACKAGE-NAME>
uv run python <PYTHON-FILE>

regularly commit code to git
```

Claude Code reads `CLAUDE.md` instead, so for Claude we add a `CLAUDE.md` with a single line, `@AGENTS.md`. The same rules then work with every tool.

The file grows over time. When the assistant repeats a mistake or searches for something it should already know, add a line that gives it the answer up front. This is context engineering: with prompt engineering, we control one message in one session. With context engineering, we control what the agent knows when any session starts. I describe the wider setup, from permissions to skills and subagents, in [How to Set Up Your Coding Agent](https://aishippingblog.com/p/how-to-set-up-your-coding-agent-a).

## The API as a Specification

Now comes the step that holds the rest of the project together. Before building the backend, we write down the API that the frontend and the backend both agree on.

The services layer already lists every call the UI makes. So the frontend decides: whatever it calls is what the backend must provide.

We point the assistant at the client code and ask for an OpenAPI file:

```text
Read the frontend's API client in frontend/

Create openapi.yaml at the repo root that specifies the backend this frontend
expects: every endpoint, method, path, request body, response body, and which
endpoints need authentication
```

The assistant reads the client and produces `openapi.yaml`.

In my run, the endpoints looked like this:

```text
POST /auth/signup     create an account, return a token       (201)
POST /auth/login      log in, return a token
GET  /auth/me         the current user                        (auth)
POST /auth/logout     log out                                 (auth)
GET  /leaderboard     top scores, filterable by mode + limit
POST /leaderboard     submit a score                          (auth, 201)
GET  /games/active    active games to spectate
```

The two game modes appear as an enum, `walls` and `pass-through`, exactly as the frontend uses them. Endpoints that act on behalf of a user, like submitting a score or reading your own profile, require a bearer token.

This step takes a few minutes, and it pays off several times:

- The assistant gets a precise target. It's easier to implement a spec than to infer a backend from frontend code.
- We can change the API while it's still cheap. Once both sides depend on it, every change touches two codebases.
- It saves tokens. When we change something later, the assistant reads one document instead of reverse-engineering the frontend again.
- It settles disputes. When the frontend and backend disagree, `openapi.yaml` decides which side is right.

## Generating the Backend from the Spec

With the spec in place, the backend prompt becomes short. We initialize an empty project with `uv init` in `backend/`.

Then we ask:

```text
Build a FastAPI backend in backend/ that implements the openapi.yaml spec

Use an in-memory store for now (no database yet) and seed it
with a few fake users, scores, and active games so the frontend has something
to show

Add authentication with hashed passwords and bearer tokens for the
endpoints that need it

Split the code into modules - routers, models, store, auth

Write tests
```

We start with an in-memory store on purpose, because first we want a working connection between frontend and backend. A real database comes later and only changes one module.

The assistant adds the dependencies with `uv add` and creates an `app/` package. Each group in the spec gets its own router: `auth`, `scores`, and `active_games`, all mounted under `/api`. Verification is cheap: FastAPI generates live documentation from the actual routes at `http://localhost:8000/docs`. We compare it with our `openapi.yaml`, try the endpoints by hand, and run `uv run pytest`.

We also ask the assistant for a `Makefile` with targets such as `backend`, `frontend`, and `test`. It gives both humans and agents one obvious way to run things.

## Integration: the Spec Settles Disagreements

Connecting the two sides takes one prompt, "Switch the frontend to use the real backend client".

The HTTP client calls a relative `/api` path, and the Vite dev server proxies it to FastAPI on port 8000:

```ts
server: {
  proxy: {
    "/api": {
      target: "http://localhost:8000",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, ""),
    },
  },
}
```

With the proxy, the browser sends every request to one origin, so there's no CORS error. Pointing the client straight at `localhost:8000` is the most common first mistake when connecting a separate frontend and backend.

Even with a spec, the two sides often disagree now, and that's normal.

Typical mismatches look like this:

- a field named one way in the frontend and another way in the backend
- a 422 error from a request body that doesn't match the model
- a missing trailing slash on a route

We always fix them the same way. Give the error from the browser console or the uvicorn log to the assistant together with the request, and tell it to follow `openapi.yaml`. Whichever side doesn't match the spec is the side that changes. Without the spec, the assistant has to guess which side is correct, and it might "fix" the frontend to match a backend bug.

## Tests as Executable Acceptance Criteria

The app now works end to end, but the in-memory store loses everything on restart.

We ask the assistant to replace it with SQLAlchemy and to choose the database from an environment variable:

```text
Replace the in-memory store with a database. Use SQLite and SQLAlchemy

Use an environment variable to configure which DB the server should connect to

Make it database-agnostic - later we will add support for other databases (e.g. postgres)
```

In my run, the assistant named the variable `SNAKE_ROYALE_DATABASE_URL` and defaulted it to a local SQLite file. Later, switching to Postgres only requires a driver and a different URL, with no code changes.

Our unit tests run against a fresh in-memory database. They check that a single request works, but not that data survives across connections, which is exactly what broke before.

So we add a second suite:

```text
Add integration tests in a tests_integration/ folder that run against a
temporary SQLite database

They should exercise full flows:

- sign up
- log in
- submit a score
- read it back from the leaderboard
```

These flows are acceptance criteria written as code. Each one describes something a user must be able to do, and it fails as soon as a change breaks it. Later, the agents check their own work against the same suites.

## From Laptop to Cloud

Deployment works the same way. We describe the target precisely, let the assistant produce the files, verify them, and commit.

For packaging, we ask for a two-stage Dockerfile. A Node stage builds the frontend, and a Python stage copies the static files next to the backend.

The first attempt failed, because the template Lovable uses produces a server bundle, not a static site, so FastAPI had nothing to serve. A participant with frontend experience spotted it. We passed the error and the hint to the assistant, and it added a prerender step, then used Playwright to click through the running container.

You don't need to understand a framework's build system to fix a problem like this. But you do need to pass the error back instead of guessing.

After that, the remaining steps are short prompts:

- Postgres in a container, with the `psycopg` driver added to the backend
- a `compose.yaml` with the app and Postgres, a named volume, and a healthcheck so the app waits for the database
- a CloudFormation template for AWS

The infrastructure prompt reads like a small specification:

```text
Create a CloudFormation template that deploys this app to AWS, with:

- an Aurora PostgreSQL (Serverless v2) database
- the database user and password stored in Secrets Manager
- a single EC2 instance that reads those secrets at boot, builds the image, and
  runs the container with docker
- a public URL for the app
- an idempotent deploy: re-running it must not rotate the secrets
```

An agent won't come up with the last requirement on its own. If it's missing, a second deploy can rotate the database password and break the running app. Requirements like this belong in the spec because they're hard to discover from the code.

For one container, a single EC2 instance is the simplest option. Together with Aurora, it costs a couple of dollars a day, so delete the stack when you don't need it.

## Keep Agents Away from Production

While you're figuring out the infrastructure, the assistant needs AWS credentials. In the workshop, we use an IAM user in a throwaway Codespace. Once the deployment works, that access should go away.

I learned this the hard way. In an unrelated project, I let Claude Code run Terraform against my production account. A mix-up with state files ended in `terraform destroy` removing the database and the rest of the infrastructure behind the DataTalks.Club course platform. The full story is in [How I Dropped Our Production Database](https://aishippingblog.com/p/how-i-dropped-our-production-database). Since then, I follow one rule: an agent should never have a path to production.

In the workshop, that rule translates into a CI/CD pipeline.

We ask for a GitHub Actions workflow with a fixed order:

1. Backend unit tests and frontend tests run in parallel.
2. The slower integration tests run only if both pass.
3. Deploy runs only after that, and only on `main`.

The deploy job authenticates with OIDC and assumes a role that the CloudFormation stack created, so there's no long-lived key in the repository. After the pipeline works, we delete the admin key.

From then on, agents can change code and push it, but only the pipeline deploys, and only when the tests pass. For experiments that need cloud access, I use a separate sandbox account with short-lived credentials. I describe it in [The System I Built for AWS Access Without Keys](https://aishippingblog.com/p/the-system-i-built-for-aws-access).

## Beyond the First Version: Task Specifications

One assistant and one prompt at a time is the right speed for going from nothing to a first version. As the codebase grows, this ad-hoc style starts to fail. The assistant forgets earlier decisions, skips tests, and calls work done too early.

Then I switch to specifying each change before anyone builds it.

A task specification has four parts:

```text
## Goal

One or two sentences on what should be true when this is done.

## Acceptance criteria

- [ ] A statement you can check by looking at the result
- [ ] One line per case, including the awkward ones

## Out of scope

- Something that does not belong in this task, moved to #TASK-NUMBER

## Constraints

- Files this should stay inside
- Libraries to use
- Guidelines to follow
```

Writing a task like this is called grooming. A misunderstanding is cheapest to catch at this stage: the issue is a paragraph, and correcting it costs one sentence. The same misunderstanding found after implementation costs a rewrite.

The project already has a head start. The `openapi.yaml` specifies the API, and the test suites turn acceptance criteria into checks. For a new feature, we extend the spec first, then write the code.

## A Team of Agents

The next problem is verification. When the same agent writes code and judges it, it grades its own homework. Ask it whether the work is correct and you'll get a confident "yes", even when it has missed edge cases.

Real teams solve this with separate roles, and the same works for agents.

I give each job to a separate agent with its own instruction file:

- A product manager grooms a request into a task specification, and later checks the result against the user story.
- A software engineer implements one groomed task, writes tests, and commits, but never closes the issue.
- A QA engineer checks every acceptance criterion against the running code and posts a PASS or FAIL verdict with evidence. It doesn't fix anything.
- An on-call engineer watches the CI/CD pipeline after a push and fixes what breaks.

An orchestrator session coordinates them like a project manager, following a lifecycle from a short `process.md`:

```text
1. Pick the next open issue from the backlog
2. PM grooms it
3. Engineer implements it
4. QA verifies it
5. On FAIL, back to step 3 with the QA comment as input
6. On PASS, close the issue
7. Repeat until the backlog is empty
```

No agent approves its own work. Keeping the writer and the approver separate stops an agent from calling half-finished work done.

The orchestrator still needs something that keeps it running, because coding agents tend to stop after a few tasks and ask whether to continue.

Claude Code and Codex support a `/goal` command for this. The harness checks a stop condition each time the agent stops, and resumes it if the condition doesn't hold yet. The condition has to be checkable. "All issues are closed" or "all tests pass" works, while "make the code better" doesn't, because the model can't evaluate it.

This setup reuses what the workshop already built. The PM writes specifications against `openapi.yaml`, QA runs the existing test suites, and the on-call agent watches the GitHub Actions pipeline.

I've used this process on several projects, including the [AI Shipping Labs platform](https://aishippinglabs.com/). The role files and the results from five real projects are in [I Built an AI Agent Team for Software Development](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software). The approach costs noticeably more time and tokens than a single agent, so it's worth it for projects with many moving parts. For a small utility, one assistant with a good spec is usually enough.

You also don't need the full team to get most of the benefit. With a single assistant, follow the same steps. Write the spec and implement it. Then verify the result against the acceptance criteria and commit.

## Practical Takeaways

Here's what I'd keep from this workflow, whatever stack you use:

- Talk the idea through in a chat assistant before you open the coding assistant, and save the outcome as a file in the repository.
- Ask the frontend generator for a single services layer with a mock backend. It lets you run the UI early and makes the API extractable.
- Write the API contract down before the backend exists, and use it to settle every disagreement between the two sides.
- Keep `AGENTS.md` short and add a line every time the assistant repeats a mistake.
- Commit after every step, so there's always a working state to return to.
- Treat tests as acceptance criteria that run.
- Put requirements the agent can't discover into the spec, such as idempotent deploys.
- Let agents explore infrastructure in a disposable environment, then remove their access and deploy only through CI/CD.
- Once the first version is live, specify every change with acceptance criteria and have someone other than the author verify it.

## Learning More

You can find the complete workshop with every prompt in the [AI Shipping Labs workshop library](https://aishippinglabs.com/workshops). It also covers the deployment and CI/CD parts in full detail.

The same material is part of [AI Dev Tools Zoomcamp](https://datatalks.club/blog/ai-dev-tools-zoomcamp.html), a free course from [DataTalks.Club](https://datatalks.club/). The course covers AI coding tools across the software-development lifecycle, from specifications to deployment and observability.

The follow-up articles on the AI Shipping Labs blog go further:

- [DevOps and Observability for an AI-Built App](https://aishippingblog.com/p/devops-and-observability-for-an-ai) adds monitoring and an on-call agent to the same app
- [From Idea to Production in 28 Prompts](https://aishippingblog.com/p/from-idea-to-production) condenses the entire build into a sequence of prompts
- [Coding Agent Building Blocks](https://aishippingblog.com/p/coding-agent-building-blocks-reusable) covers skills and subagents

## Sources

Internal reference for this draft, not part of the published article:

- AI Shipping Labs workshop "Build and Deploy a Full-Stack App with AI Coding Assistants" (2026-06-23): `/home/alexey/git/ai-shipping-labs-workshops-content/2026/06/2026-06-23-full-stack-vibe-coding/`, published at [aishippinglabs.com/workshops/full-stack-vibe-coding](https://aishippinglabs.com/workshops/full-stack-vibe-coding)
- Specification, grooming, loop and graph engineering material: [AI-Native Development](https://aishippingblog.com/p/ai-native-development-specifications) (`reference/substack/2026-07-22-ai-native-development-specifications.md`)
- Agent team: [I Built an AI Agent Team](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software)
- Production database incident and agent AWS access: [production database post](https://aishippingblog.com/p/how-i-dropped-our-production-database) and [AWS access post](https://aishippingblog.com/p/the-system-i-built-for-aws-access)
- devmio request and guidelines: email from Stephane Fernandes (2026-06-11 and 2026-10-02) - 15,000-20,000 characters, code listings welcome, objective and neutral yet engaging style, [example article](https://devm.io/devops/cloud-native-devops-experience)
