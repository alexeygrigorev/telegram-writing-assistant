#!/usr/bin/env python3
"""Utilities for updating the local Alexey On Data Substack archive."""

from __future__ import annotations

import argparse
import csv
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter


ROOT = Path(__file__).resolve().parent.parent
FEED_URL = "https://aishippingblog.com/feed"
# Matches both the current domain and the older alexeyondata.substack.com
# links that may still linger in older archive rows.
POST_URL_RE = re.compile(
    r"https://(?:aishippingblog\.com|alexeyondata\.substack\.com)/p/[^ |,\n\]]+"
)
ARCHIVE_ROW_RE = re.compile(
    r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(https://\S+?)\s*\|", re.M
)
REFERENCE_DIR = ROOT / "reference" / "substack"
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
    path = ROOT / "articles" / "_substack-archive-index.md"
    text = path.read_text(encoding="utf-8")
    return POST_URL_RE.findall(text)


def archive_rows() -> list[tuple[str, str, str]]:
    """Return (date, title, url) for every row in the archive index table."""
    path = ROOT / "articles" / "_substack-archive-index.md"
    text = path.read_text(encoding="utf-8")
    return ARCHIVE_ROW_RE.findall(text)


def print_posts(posts: list[Post]) -> None:
    for post in posts:
        print(f"{post.date}\t{post.title}\t{post.url}\t{post.description}")


# --- Full-text reference conversion -----------------------------------

NOISE_SELECTORS = [
    ".header-anchor-parent",
    ".subscription-widget-wrap",
    "[data-component-name='SubscribeWidget']",
    "form",
    "button",
    "hr",
    "script",
    "style",
]
# Embed cards (recommended-post previews etc.) wrap an <a> around nested
# headings/images/another <a>, which markdownify mangles. Flatten them into
# a single clean link before conversion.
EMBED_CARD_SELECTOR = "[data-component-name]"


def fetch_html(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


class _PostConverter(MarkdownConverter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_count = 0

    def convert_img(self, el, text, parent_tags):
        src = el.get("src") or el.get("data-src") or ""
        if not src:
            return ""
        self.image_count += 1
        alt = el.get("alt") or f"Image {self.image_count}"
        return f"![{alt}]({src})"

    def convert_h1(self, el, text, parent_tags):
        return ""  # title is carried in frontmatter, not the body


def _flatten_embed_cards(content) -> None:
    for card in content.select(EMBED_CARD_SELECTOR):
        link = card.find("a", href=True)
        if link is None:
            continue
        heading = card.find(["h3", "h4"])
        title = heading.get_text(strip=True) if heading else link.get_text(strip=True)
        if not title:
            continue
        replacement = BeautifulSoup("", "html.parser").new_tag("p")
        new_a = BeautifulSoup("", "html.parser").new_tag("a", href=link["href"])
        new_a.string = title
        replacement.append(new_a)
        card.replace_with(replacement)


def extract_title(soup: BeautifulSoup) -> str:
    h1 = soup.select_one("h1.post-title")
    return h1.get_text(strip=True) if h1 else ""


def extract_content(soup: BeautifulSoup):
    content = soup.select_one("div.available-content")
    if content is None:
        raise SystemExit("available-content div not found")
    for selector in NOISE_SELECTORS:
        for tag in content.select(selector):
            tag.decompose()
    _flatten_embed_cards(content)
    return content


def to_markdown(content) -> str:
    converter = _PostConverter(heading_style="ATX", bullets="*", strong_em_symbol="*")
    md = converter.convert_soup(content)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def fetch_reference_post(url: str) -> tuple[str, str]:
    """Fetch one post and return (title, markdown_body)."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")
    title = extract_title(soup)
    content = extract_content(soup)
    body = to_markdown(content)
    return title, body


def reference_path(date: str, url: str) -> Path:
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    return REFERENCE_DIR / f"{date}-{slug}.md"


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
    archive_path = ROOT / "articles" / "_substack-archive-index.md"

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


def cmd_reference_sync(args: argparse.Namespace) -> int:
    REFERENCE_DIR.mkdir(parents=True, exist_ok=True)
    rows = archive_rows()
    if not rows:
        print("No rows found in articles/_substack-archive-index.md")
        return 1

    todo = []
    for date, _title, url in rows:
        path = reference_path(date, url)
        if path.exists() and not args.force:
            continue
        todo.append((date, url, path))

    if not todo:
        print("Reference archive is already up to date.")
        return 0

    print(f"Fetching {len(todo)} post(s)...")
    failures = []
    for i, (date, url, path) in enumerate(todo, 1):
        try:
            title, body = fetch_reference_post(url)
        except (HTTPError, URLError, SystemExit) as e:
            print(f"[{i}/{len(todo)}] FAIL {path.name}: {e}")
            failures.append(path.name)
            time.sleep(1)
            continue

        frontmatter = f'---\ntitle: "{title}"\ndate: {date}\nurl: {url}\n---\n\n'
        path.write_text(frontmatter + body, encoding="utf-8")
        heading_count = len(re.findall(r"^#{2,6} ", body, re.M))
        print(f"[{i}/{len(todo)}] OK {path.name} ({heading_count} headings)")
        time.sleep(0.5)

    if failures:
        print("\nFailures:")
        for name in failures:
            print(f" - {name}")
        return 1

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    feed = subparsers.add_parser("feed", help="Print current RSS feed posts")
    feed.set_defaults(func=cmd_feed)

    missing = subparsers.add_parser(
        "missing",
        help="Print feed posts not yet present in articles/_substack-archive-index.md",
    )
    missing.set_defaults(func=cmd_missing)

    validate = subparsers.add_parser(
        "validate",
        help="Validate substack.csv parsing and duplicate archive URLs",
    )
    validate.set_defaults(func=cmd_validate)

    reference_sync = subparsers.add_parser(
        "reference-sync",
        help=(
            "Fetch full post text for every archive-index row missing a "
            "reference/substack/*.md file, converting real headings from the "
            "post HTML"
        ),
    )
    reference_sync.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch and overwrite files that already exist",
    )
    reference_sync.set_defaults(func=cmd_reference_sync)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
