# ATS Gap Analyser

Source: https://github.com/Amar-Ag/ats-gap-analyser/blob/main/README.md

Run outcome: screenshot captured from the local Streamlit app using the repository's built-in no-API example.

Run command:

`uv sync`

`GROQ_API_KEY=mock-not-a-secret uv run streamlit run src/app.py --server.headless true --server.address 127.0.0.1 --server.port 8501`

The isolated clone needed two local-only startup adjustments: Logfire was disabled without a token, and a mock Groq key was supplied so the client could import. No external model call was made. The screenshot was captured after selecting “See example”, which the app labels as “no API credits used”.

Screenshot:

- `01-example-result.png` - 1140 x 720 crop showing the 75/100 match score, missing keywords, improvement suggestions, and the start of the cover letter.

Limitation: the public Streamlit URL redirected to Streamlit authentication in this environment, so this is the app's deterministic example result rather than a live CV analysis.
