# Multi-Agent Software Development Platform

Repository: https://github.com/mishranitesh/AI_Engineering_Buildcamp_From_RAG_to_Agents/tree/main/capstone/multi-agent-dev-platform

Run command used:

```text
API_URL=http://127.0.0.1:19075 streamlit run ui/streamlit_app.py --server.port 19001
```

The Streamlit frontend was launched from the repository checkout. Its backend calls were served by a local `http.server` demo API returning deterministic PM stories, a FastAPI task artifact ZIP, and a review-stage PR state. The Jira and GitHub integrations were not contacted and no credentials were used.

Screenshots:

- `01-pm-agent-user-stories.png` - requirement form and PM Agent user stories, acceptance criteria, and suggested stack
- `02-generated-project-pr-lifecycle.png` - generated artifact download state and PR Lifecycle at Ready for Review with review comments

Limitations:

- The screenshots show the real project UI and workflow states, but the LLM, GitHub, and Jira responses are local deterministic fixtures rather than live service responses.
- The PR URL and branch shown in the second screenshot are intentionally fake demo values.
