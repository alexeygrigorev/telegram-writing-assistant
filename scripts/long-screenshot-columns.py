"""Cut one long screenshot into equal slices and place them side by side.

From an existing long image:

    uv run --with pillow scripts/long-screenshot-columns.py \
      --input long.png --output columns.png --columns 10

Capture a page first, then cut it:

    uv run --with pillow --with playwright scripts/long-screenshot-columns.py \
      --url https://example.com/article --output columns.png --columns 10

Each column is one uninterrupted, consecutive slice of the original image.
There are no rows, labels, borders, or gaps. A short final slice is padded
with white so every column has the same height.
"""

from __future__ import annotations

import argparse
from io import BytesIO
from math import ceil
from pathlib import Path

from PIL import Image


def capture_page(url: str, viewport_width: int, viewport_height: int) -> Image.Image:
    """Capture viewport sections and stitch them into one page without repeats."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = playwright.chromium.launch(headless=True)

        page = browser.new_page(
            viewport={"width": viewport_width, "height": viewport_height},
            device_scale_factor=1,
        )
        response = page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        if response is None or response.status >= 400:
            status = response.status if response else "no response"
            raise RuntimeError(f"Could not load {url}: {status}")

        page.evaluate(
            """async () => {
                for (const img of document.images) img.loading = 'eager';
                await Promise.race([
                    Promise.allSettled(Array.from(document.images,
                        img => img.decode().catch(() => {}))),
                    new Promise(resolve => setTimeout(resolve, 12000))
                ]);
                await document.fonts.ready;
            }"""
        )

        # Sticky toolbars otherwise appear once in every captured section.
        page.evaluate(
            """() => {
                for (const el of document.querySelectorAll('*')) {
                    const position = getComputedStyle(el).position;
                    if (position === 'sticky' || position === 'fixed') {
                        el.style.setProperty('visibility', 'hidden', 'important');
                    }
                }
            }"""
        )

        page_height = page.evaluate("document.documentElement.scrollHeight")
        long_image = Image.new("RGB", (viewport_width, page_height), "white")
        step = viewport_height - 200
        for top in range(0, page_height, step):
            page.evaluate("y => window.scrollTo(0, y)", top)
            actual_scroll = page.evaluate("window.scrollY")
            screenshot = Image.open(BytesIO(page.screenshot(animations="disabled")))
            visible_top = top - actual_scroll
            section_height = min(step, page_height - top, viewport_height - visible_top)
            if section_height <= 0:
                raise RuntimeError(f"Could not capture page at pixel {top}")
            section = screenshot.crop(
                (0, visible_top, viewport_width, visible_top + section_height)
            ).convert("RGB")
            long_image.paste(section, (0, top))

        browser.close()
        return long_image


def arrange_columns(image: Image.Image, columns: int) -> Image.Image:
    """Place consecutive equal-height slices left to right, one per column."""
    width, height = image.size
    slice_height = ceil(height / columns)
    result = Image.new("RGB", (width * columns, slice_height), "white")
    for column in range(columns):
        top = column * slice_height
        section = image.crop((0, top, width, min(top + slice_height, height)))
        result.paste(section, (column * width, 0))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="Existing long screenshot")
    source.add_argument("--url", help="Web page to capture before cutting")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--columns", type=int, default=10)
    parser.add_argument("--crop-left", type=int, default=0)
    parser.add_argument("--crop-right", type=int, default=0)
    parser.add_argument("--viewport-width", type=int, default=1280)
    parser.add_argument("--viewport-height", type=int, default=900)
    args = parser.parse_args()

    if args.columns < 1:
        parser.error("--columns must be at least 1")
    if args.crop_left < 0 or args.crop_right < 0:
        parser.error("crop values cannot be negative")

    if args.input:
        with Image.open(args.input) as source_image:
            long_image = source_image.convert("RGB")
    else:
        long_image = capture_page(args.url, args.viewport_width, args.viewport_height)
        long_path = args.output.with_name(args.output.stem + "-long.png")
        long_path.parent.mkdir(parents=True, exist_ok=True)
        long_image.save(long_path, optimize=True)
        print(f"Long screenshot: {long_path}")

    width, height = long_image.size
    if args.crop_left + args.crop_right >= width:
        parser.error("the crop removes the entire image width")
    cropped = long_image.crop((args.crop_left, 0, width - args.crop_right, height))
    columns_image = arrange_columns(cropped, args.columns)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    columns_image.save(args.output, optimize=True)
    print(f"Columns: {args.output} ({columns_image.width} x {columns_image.height})")


if __name__ == "__main__":
    main()
