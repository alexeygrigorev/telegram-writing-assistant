# Applied ML Teaching Copilot

Source: https://github.com/marcoteran/applied-ml-teaching-copilot/blob/main/README.md

Run outcome: screenshot captured from a local Streamlit app with the local course-material search tools and a deterministic mock model response.

Run command:

`uv sync`

`uv run streamlit run app.py --server.headless true --server.address 127.0.0.1 --server.port 8523`

For the isolated screenshot clone, the external OpenAI call was replaced with a local function that runs `CourseMaterialTools` against `data/course_materials.json`, fetches `aml-001`, and returns a grounded MAE-versus-MSE answer. This keeps the real UI, tool-call history, fetched ids, and citation behavior visible without a key or paid request.

Screenshot:

- `01-grounded-answer.png` - 1140 x 650 crop showing the question, grounded answer citing `aml-001`, and the Tool calls panel.

Limitation: the answer is deterministic local mock output, not an OpenAI response. The public Streamlit URL redirected to Streamlit authentication in this environment.
