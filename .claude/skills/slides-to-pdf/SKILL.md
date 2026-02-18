---
name: slides-to-pdf
description: Convert reveal.js slide decks to PDF. Use when the user asks to export slides to PDF, create a PDF from slides, or make a shareable version of a presentation.
---

# Convert Slides to PDF

Convert a reveal.js HTML slide deck to a PDF file, preserving all styles and images.

## Steps

Use Playwright to open the slides, navigate through each slide, capture a screenshot, and combine them into a PDF using Pillow.

```python
from playwright.sync_api import sync_playwright
from PIL import Image
import os, time

html_path = 'INPUT_HTML_PATH'
pdf_path = html_path.replace('.html', '.pdf')
file_url = 'file:///' + os.path.abspath(html_path).replace(os.sep, '/')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 720})

    page.goto(file_url, wait_until='networkidle')
    time.sleep(2)

    total = page.evaluate('Reveal.getTotalSlides()')
    print(f'Total slides: {total}')

    screenshots = []
    for i in range(total):
        page.evaluate(f'Reveal.slide({i})')
        time.sleep(0.3)
        ss_path = f'.tmp/slide_{i:03d}.png'
        page.screenshot(path=ss_path)
        screenshots.append(ss_path)

    browser.close()

# Combine into PDF
images = [Image.open(ss).convert('RGB') for ss in screenshots]
images[0].save(pdf_path, save_all=True, append_images=images[1:], resolution=150)

# Cleanup screenshots
for ss in screenshots:
    os.remove(ss)

print(f'Done! {pdf_path} ({os.path.getsize(pdf_path) // 1024}KB)')
```

## Requirements

- `playwright` Python package with Chromium browser installed
- `Pillow` (PIL) for image-to-PDF conversion

Ensure `.tmp/` directory exists before running (create it if not).

## Notes

- The PDF goes in the same directory as the source slides (typically `wip/`)
- The PDF preserves the exact visual appearance including dark backgrounds, fonts, and image layouts
- Resolution is set to 150 DPI which balances quality and file size
