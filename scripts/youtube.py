#!/usr/bin/env python3
"""Fetch YouTube video transcripts as timestamped subtitles, with optional proxy support."""

import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig


def extract_video_id(url_or_id: str) -> str:
    """Extract YouTube video ID from a URL or return as-is if already an ID."""
    patterns = [
        r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id


def format_timestamp(seconds: float) -> str:
    """Convert seconds to H:MM:SS if > 1 hour, else M:SS."""
    total_seconds = int(seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)

    if hours > 0:
        return f"{hours}:{minutes:02}:{secs:02}"
    else:
        return f"{minutes}:{secs:02}"


def make_subtitles(transcript) -> str:
    """Format transcript entries into timestamped subtitle text."""
    lines = []
    for entry in transcript:
        ts = format_timestamp(entry.start)
        text = entry.text.replace("\n", " ")
        lines.append(ts + " " + text)
    return "\n".join(lines)


def _build_proxy_url() -> str | None:
    """Build Oxylabs proxy URL from user, endpoint, and password. Uses one-time sessions (random IP each request)."""
    user = os.environ.get("OXYLABS_USER")
    endpoint = os.environ.get("OXYLABS_ENDPOINT")
    password = os.environ.get("OXYLABS_PASSWORD")
    if not user or not endpoint or not password:
        return None
    username = f"customer-{user}"
    return f"http://{username}:{quote(password, safe='')}@{endpoint}"


def create_api() -> YouTubeTranscriptApi:
    """Create YouTubeTranscriptApi instance, with proxy if Oxylabs credentials are set."""
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    proxy_url = _build_proxy_url()

    if proxy_url:
        proxy_config = GenericProxyConfig(
            http_url=proxy_url,
            https_url=proxy_url,
        )
        return YouTubeTranscriptApi(proxy_config=proxy_config)

    return YouTubeTranscriptApi()


def fetch_transcript_text(video_id: str, retries: int = 3) -> str:
    """Fetch transcript and return as formatted subtitle text. Retries on failure."""
    for attempt in range(retries):
        try:
            api = create_api()
            transcript = api.fetch(video_id)
            return make_subtitles(transcript)
        except Exception as e:
            if attempt < retries - 1:
                wait = 2 ** attempt
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                raise


def fetch_transcript_cached(video_id: str) -> str:
    """Fetch transcript with local file caching."""
    cache_dir = Path.home() / ".cache" / "youtube_transcripts"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{video_id}.txt"

    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")

    subtitles = fetch_transcript_text(video_id)
    cache_file.write_text(subtitles, encoding="utf-8")
    return subtitles


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube.py <video-url-or-id>", file=sys.stderr)
        sys.exit(1)

    video_id = extract_video_id(sys.argv[1])
    print(fetch_transcript_cached(video_id))
