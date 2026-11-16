---
name: kael-cover
description: Use when generating branded article and social covers. Build one topic-led prompt, choose a style, render, validate, and save platform-specific assets.
---

# Kael Cover V2

A clean-room cover workflow rebuilt from the MIT-era Punk Cover baseline. It uses a local style registry and an explicit compiler instead of copying later proprietary prompt text.

## Operating rules

- Analyze the article before choosing a visual metaphor.
- Use exactly one style per image.
- Prefer one strong subject and one readable title hierarchy.
- Generate independently for each platform ratio; never stretch a landscape cover into a portrait cover.
- Keep title text short enough for reliable image rendering; preserve the full title in metadata and prompt files.
- Save the compiled prompt and generation metadata beside the output.
- Never claim an image was saved unless the generator returned a current-run file path or URL.

## Supported targets

- WeChat/site: landscape; current generator maps this to `landscape`.
- Xiaohongshu: portrait; current generator maps this to `portrait`.
- Weibo/X: landscape or square according to the post template.

## Pipeline

1. Read `article.json` or the source Markdown.
2. Derive title, short subtitle, subject, audience, mood, metaphor, and forbidden elements.
3. Choose one style from `styles/registry.json` using the topic-to-style rules.
4. Compile a single prompt with `scripts/compile_prompt.py`.
5. Generate one image with the image tool.
6. Copy only the explicit returned artifact into the requested output path.
7. Validate dimensions, title-safe area, file type, and non-empty image content.
8. Derive platform files with `sips`; keep the original PNG.

## Style selection

- research, code, engineering: `etching-editorial` or `research-paper`
- products, startups, AI tools: `editorial-grid` or `retro-future`
- social criticism or security incidents: `black-red-editorial` or `etching-editorial`
- career and work: `midcentury-editorial` or `paper-relief`
- abstract mechanisms: `paper-relief` or `pixel-mechanism`

When no style is specified, select one automatically and record the reason in `generation.json`.

## Quality gate

Reject and regenerate if the title is missing, severely misspelled, clipped, the subject is unrelated, the image is a generic presentation slide, or the composition has multiple competing focal points. Text in generated images is not trusted automatically: inspect the image and retain the exact title in the prompt metadata.
