# Fetch YouTube Transcript

Fetch the transcript/subtitles of a YouTube video and return it as timestamped text.

## Instructions

Run the fetch script:

```bash
uv run python scripts/youtube.py $ARGUMENTS
```

The script accepts a video ID (`dQw4w9WgXcQ`), full URL (`https://www.youtube.com/watch?v=dQw4w9WgXcQ`), or short URL (`https://youtu.be/dQw4w9WgXcQ`).

Transcripts are cached in `~/.cache/youtube_transcripts/`. If `OXYLABS_PROXY_URL` is set in `.env`, requests are routed through the proxy.

After fetching the transcript, ask the user what they'd like to do with it (summarize, extract key points, answer questions, etc.).
