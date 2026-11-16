# Kael Cover

A clean-room, topic-led cover workflow for Chinese article and social-media covers.

This project is independently implemented from the MIT-era Punk-Skill baseline. It is not an upstream Punk-Skill release and does not include later proprietary Punk-Skill v2 code, templates, or assets.

## What it does

- Converts an article topic into a focused cover brief.
- Chooses one visual style from a small local registry.
- Compiles an integrated prompt instead of concatenating generic instructions.
- Separates landscape WeChat/site covers from portrait Xiaohongshu covers.
- Keeps exact titles, topic summaries, negative constraints, and generation metadata.
- Supports later image-provider adapters without coupling the workflow to one vendor.

## Layout

- `SKILL.md` — Hermes skill instructions.
- `scripts/compile_prompt.py` — deterministic prompt compiler.
- `styles/registry.json` — original local style descriptors.
- `PROVENANCE.md` — licensing and clean-room boundary.
- `LICENSE` — retained MIT notice from the V1 baseline.

## Example

```bash
python3 scripts/compile_prompt.py \
  --topic "AI freelance work rebundling" \
  --title "项目变大，时薪没涨" \
  --summary "Larger bundled projects do not automatically produce higher hourly pay." \
  --platform wechat \
  --ratio 2.35:1 \
  --out /tmp/cover-prompt.md
```

## License

MIT for the retained baseline notice and this project’s original implementation, subject to the provenance and third-party notices in the repository. This project does not grant rights to third-party upstream materials beyond their applicable licenses.

## Status

Version 2.0.0. The deterministic compiler and regression cases are working. Image-provider adapters are intentionally separate because provider availability and licensing vary.
