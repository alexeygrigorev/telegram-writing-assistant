---
name: create-slides
description: Create reveal.js slide decks from articles. Use when the user asks to create slides, a presentation, or a deck from an article or markdown file.
---

# Create Slides from Article

Create a reveal.js HTML slide deck from an article markdown file. Output goes to `wip/`.

## Steps

1. Read the article the user wants to turn into slides
2. Ask the user for the talk title, speaker name, date, and event name (if not already clear from the article)
3. Create the HTML slide deck in `wip/<article-name>-slides.html`

## HTML Template

Use this exact template structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TALK TITLE</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css">
<style>
  .reveal { font-size: 40px; }
  .reveal h1 { font-size: 1.8em; }
  .reveal h2 { font-size: 1.4em; }
  .reveal h3 { font-size: 1.1em; }
  .reveal ul { text-align: left; }
  .reveal li { margin-bottom: 0.3em; }
  .reveal img { max-height: 85vh; max-width: 95%; border: none !important; box-shadow: none !important; }
  .reveal .small { font-size: 0.6em; color: #888; }
  .reveal .subtitle { font-size: 0.7em; color: #aaa; margin-top: 0.5em; }
  .reveal .slides section { text-align: center; }
  .reveal .slides > section { top: 0 !important; }
  .reveal .center { text-align: center; }
  .reveal code { color: #7ec8e3; }
  .reveal .slides section h2 { position: relative; top: 0; margin-top: 0; margin-bottom: 0.4em; }
  .reveal .slides section.vcenter { display: flex !important; flex-direction: column; justify-content: center; height: 100%; }
</style>
</head>
<body>
<div class="reveal">
<div class="slides">

<!-- slides go here -->

</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script>
Reveal.initialize({
  hash: true,
  slideNumber: true,
  width: 1280,
  height: 720,
  margin: 0.1,
  transition: 'none',
  center: false
});
</script>
</body>
</html>
```

## Slide Types

### Title slide

Vertically centered with dark background:

```html
<section class="vcenter" data-background-color="#1a1a2e">
  <h1>Talk Title</h1>
  <p class="subtitle">Subtitle if needed</p>
  <p class="small">Speaker Name &middot; Event &middot; Date</p>
</section>
```

### Section divider slide

Vertically centered with dark background. Use to introduce major sections:

```html
<section class="vcenter" data-background-color="#1a1a2e">
  <h1>Section Title</h1>
</section>
```

### Content slide (text with bullet points)

Title at top, bullet list below. This is the most common slide type:

```html
<section>
  <h2>Slide Title</h2>
  <ul>
    <li>Point one</li>
    <li>Point two</li>
    <li>Point three</li>
  </ul>
</section>
```

### Image-only slide

Full-screen image, no title:

```html
<section>
  <div class="center">
    <img src="../assets/images/folder/image.png">
  </div>
</section>
```

### Thank you slide

```html
<section class="vcenter" data-background-color="#1a1a2e">
  <h1>Thank you!</h1>
  <p>Questions?</p>
  <p class="small">Speaker Name &middot; Event</p>
</section>
```

## Slide Design Principles

- Keep slides simple and minimal - just key points, not full sentences
- For topics with images: show the image first on its own slide, then have a separate text slide with the description
- Section dividers use `class="vcenter"` for vertical centering; content slides use top-aligned layout (handled by `center: false` in config)
- Limit bullet points to 5-6 per slide maximum
- Use `<code>` tags for code/command references inline
- Use `<p class="small">` for attribution or small notes
- Images reference paths relative to `wip/` directory (typically `../assets/images/...`)
- Plan slide near the beginning with the talk outline
- Resources slide near the end with links (plain text, no hyperlinks needed for presentation)
