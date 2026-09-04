# Chess Coach Agent result

Repository: https://github.com/leo-cabibihan/chess-coach-agent

Run path

- Installed backend dependencies with `uv sync --extra dev` in an isolated clone.
- Downloaded the Ubuntu `stockfish` package into the temporary clone and ran Stockfish 16 at depth 10.
- Started FastAPI with SQLite using `DATABASE_URL=sqlite:////tmp/twa-ws2-chess-M18sdB/repo/backend/data/chess_coach.db`, an empty `OPENROUTER_API_KEY`, and the temporary `STOCKFISH_PATH`.
- Installed and started the Vite frontend with `npm ci` and `npm run dev -- --host 127.0.0.1 --port 5173`.
- Posted the included `backend/data/sample_games/kfctofu_sample.pgn` to `POST /api/analyze` for player `kfctofu` and platform `chess.com`.
- Opened the real Games, review, and practice routes in a headless browser.

Screenshots

- `chess-coach-agent-review.png` - review of the imported game, with four engine-detected coachable moments, the selected blunder, recommended move, explanation, and board.
- `chess-coach-agent-practice.png` - the generated one-position practice session after the correct `Qh5+` answer, including engine feedback and the next review date.

Limitations

- The Render deployment timed out, so the capture uses the documented local path and the repository sample PGN instead of a public deployment or remote account sync.
- No OpenRouter key was used. The practice agent therefore used the project deterministic fallback; Stockfish analysis and grading still ran locally.
- The existing frontend displays the move number with `...` for both colors. This is visible in the review card but does not change the underlying PGN or engine result.
