# Research Radar result

Run command:

```bash
cd /tmp/buildcamp-ws3.xGBGXR/research-radar
/usr/bin/python3 dashboard.py
```

The dashboard was launched locally at `http://127.0.0.1:5000`. It was given three local fixture runs in `logs/runs.jsonl`, using paper titles and ratings from the repository's `data/ground_truth_papers.csv`. No ArXiv, LLM, Resend, or paid API call was made.

Screenshots:

- `research-radar-pipeline-runs.png` - pipeline metrics, relevance trend, recent recommendations, and run history.
- `research-radar-ratings.png` - rating distribution and saved-for-later papers from the repository ground truth.

Limitations:

- The full `pipeline.py` was not run because it would fetch live ArXiv data and can call an LLM and Resend. The screenshots show the project's real dashboard rendering with local, clearly synthetic run events.
- The repository's `demo_ranker.py` references a root-level `ground_truth_papers.csv`, while the checked-in dataset is under `data/`; it was not used for the capture.
