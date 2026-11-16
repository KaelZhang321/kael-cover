import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = json.loads((ROOT / 'styles' / 'registry.json').read_text())

def compile_prompt(topic, title, summary, platform, ratio, style_id=None, subtitle='', banned='generic presentation-slide layout, fake charts, clutter, watermark'):
    styles = REG['styles']
    if style_id is None:
        if any(x in (topic + ' ' + summary).lower() for x in ('security', 'leak', 'exposure', 'attack')):
            style_id = 'black-red-editorial'
        elif any(x in (topic + ' ' + summary).lower() for x in ('code', 'github', 'api', 'model', 'technical')):
            style_id = 'research-paper'
        elif any(x in (topic + ' ' + summary).lower() for x in ('career', 'freelance', 'work', 'job')):
            style_id = 'midcentury-editorial'
        else:
            style_id = 'editorial-grid'
    if style_id not in styles:
        raise ValueError(f'unknown style: {style_id}')
    s = styles[style_id]
    return f'''Create one editorial cover for {platform}, aspect ratio {ratio}.

Topic: {topic}
Exact title: {title}
Short subtitle: {subtitle}
Context: {summary}

Visual subject: one clear subject that explains the topic at first glance.
Visual metaphor: express the central mechanism or contradiction through one physical visual metaphor, not a collage of unrelated symbols.
Audience and mood: technically literate readers; clear, restrained, curious, editorial.

Style: {style_id}. Material: {s['material']}. Palette: {s['palette']}. Composition: {s['composition']}.
Integrate the style into the entire cover: background, subject, title treatment, texture, spacing, and contrast must belong to one visual system. Keep one dominant focal point and reserve a clean title-safe area. Render the exact title accurately and completely, with high contrast and no clipping. Use the subtitle only if it remains legible.

Do not use: {banned}. No stock-photo montage, no generic SaaS dashboard, no PPT/course cover, no tiny unreadable paragraph text, no invented statistics, no extra logos, no multiple competing subjects.

Final standard: deliberate magazine cover, topic recognizable in one second, metaphor discoverable in a second glance, readable title, balanced negative space, platform-safe composition.''' 

if __name__ == '__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--topic',required=True); ap.add_argument('--title',required=True); ap.add_argument('--summary',required=True); ap.add_argument('--platform',required=True); ap.add_argument('--ratio',required=True); ap.add_argument('--style'); ap.add_argument('--subtitle',default=''); ap.add_argument('--out',required=True)
    a=ap.parse_args(); p=compile_prompt(a.topic,a.title,a.summary,a.platform,a.ratio,a.style,a.subtitle); Path(a.out).write_text(p)
