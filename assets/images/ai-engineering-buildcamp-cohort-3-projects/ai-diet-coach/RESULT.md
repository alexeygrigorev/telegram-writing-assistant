# AI Diet Coach result

Run command:

```bash
cd /tmp/buildcamp-ws3.xGBGXR/ai-diet-coach
OPENAI_API_KEY=sk-fake-local uv run streamlit run app.py --server.headless true --server.port 8502 --browser.gatherUsageStats false
```

The app was launched locally at `http://127.0.0.1:8502`. A demo profile, seven-day plan, meal and weight logs, and five monitoring traces were seeded under the clone's `data/` directory. The plan uses recipe names from the repository's `data/recipes.json` and `data/asian_recipes.json`. `sk-fake-local` only lets the OpenAI client initialize; no model request was sent.

Screenshots:

- `ai-diet-coach-weekly-plan.png` - the expanded busy-day plan with three meals, tracking state, and nutrition totals.
- `ai-diet-coach-progress.png` - weight trend, on-track status, and current goal metrics.

Limitations:

- The live Streamlit deployment reached its first-run registration page, but I did not create an external account or trigger paid API calls.
- Chat responses, LLM meal-plan generation, USDA nutrition lookup, and Google Maps restaurant lookup were not invoked. The screenshots show the real app UI backed by local recipe data and mock local state.
