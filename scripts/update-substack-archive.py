#!/usr/bin/env python3
"""Utilities for updating the local Alexey On Data Substack archive."""

from __future__ import annotations

import argparse
import csv
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
FEED_URL = "https://alexeyondata.substack.com/feed"
POST_URL_RE = re.compile(r"https://alexeyondata\.substack\.com/p/[^ |,\n]+")
USER_AGENT = (
    "Mozilla/5.0 (compatible; telegram-writing-assistant/1.0; "
    "+https://github.com/alexeygrigorev/telegram-writing-assistant)"
)


@dataclass(frozen=True)
class Post:
    date: str
    title: str
    url: str
    description: str


def fetch_feed() -> bytes:
    # Substack blocks Python's default urllib user agent.
    request = Request(
        FEED_URL,
        headers={"User-Agent": USER_AGENT},
    )
    with urlopen(request, timeout=30) as response:
        return response.read()


def clean(text: str | None) -> str:
    return " ".join(unescape(text or "").split())


def feed_posts() -> list[Post]:
    root = ET.fromstring(fetch_feed())
    channel = root.find("channel")
    if channel is None:
        raise SystemExit("No RSS channel found")

    posts: list[Post] = []
    for item in channel.findall("item"):
        pub_date = clean(item.findtext("pubDate"))
        posts.append(
            Post(
                date=parsedate_to_datetime(pub_date).date().isoformat(),
                title=clean(item.findtext("title")),
                url=clean(item.findtext("link")),
                description=clean(item.findtext("description")),
            )
        )
    return posts


def archive_urls() -> list[str]:
    path = ROOT / "articles" / "substack-archive-index.md"
    text = path.read_text(encoding="utf-8")
    return POST_URL_RE.findall(text)


def print_posts(posts: list[Post]) -> None:
    for post in posts:
        print(f"{post.date}\t{post.title}\t{post.url}\t{post.description}")


def cmd_feed(_: argparse.Namespace) -> int:
    print_posts(feed_posts())
    return 0


def cmd_missing(_: argparse.Namespace) -> int:
    known = set(archive_urls())
    missing = [post for post in feed_posts() if post.url not in known]
    print_posts(missing)
    return 0


def cmd_validate(_: argparse.Namespace) -> int:
    csv_path = ROOT / "substack.csv"
    archive_path = ROOT / "articles" / "substack-archive-index.md"

    rows = list(csv.DictReader(csv_path.open(newline="", encoding="utf-8")))
    urls = archive_urls()
    duplicate_urls = sorted({url for url in urls if urls.count(url) > 1})

    print(f"csv_rows={len(rows)}")
    print(f"archive_urls={len(urls)}")
    print(f"duplicate_urls={len(duplicate_urls)}")

    if duplicate_urls:
        print("\n".join(duplicate_urls))
        return 1

    if not archive_path.exists():
        print(f"missing={archive_path}")
        return 1

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    feed = subparsers.add_parser("feed", help="Print current RSS feed posts")
    feed.set_defaults(func=cmd_feed)

    missing = subparsers.add_parser(
        "missing",
        help="Print feed posts not yet present in articles/substack-archive-index.md",
    )
    missing.set_defaults(func=cmd_missing)

    validate = subparsers.add_parser(
        "validate",
        help="Validate substack.csv parsing and duplicate archive URLs",
    )
    validate.set_defaults(func=cmd_validate)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
