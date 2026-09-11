"""Generate selected static cards from slash-prompts.md; no runtime dependencies."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent.parent
SELECTED = (
    '/poster', '/whatsappposter', '/resepi', '/itinerary', '/jadualkrt',
    '/whatsapp', '/kemaskanmesej', '/kuizjajan', '/apaaituai', '/tipai',
)
source = (ROOT / 'slash-prompts.md').read_text(encoding='utf-8')
entries = {
    name: (purpose.strip(), prompt.strip())
    for name, purpose, prompt in re.findall(
        r'### `(/[^`]+)`\s+([^\n]+)\s+```text\n(.*?)\n```', source, re.S
    )
}
cards = []
for name in SELECTED:
    purpose, prompt = entries[name]
    cards.append(
        '<article class="card prompt-card slash-card">'
        f'<h3>{escape(name)}</h3><p>{escape(purpose)}</p>'
        f'<p class="prompt-text">{escape(prompt)}</p>'
        f'<button class="copy-btn" data-prompt="{escape(prompt, quote=True)}">Copy Prompt</button>'
        '</article>'
    )
section = '''<section class="shell section" id="slash-prompt" aria-labelledby="slash-title">
<p class="eyebrow">ARAHAN CEPAT UNTUK AI</p><h2 id="slash-title">Slash Prompt</h2>
<p class="intro">Mulakan arahan dengan kata kunci seperti <strong>/poster</strong> atau <strong>/resepi</strong>. Pilih kad, salin keseluruhan prompt dan tampal dalam alat AI pilihan anda. Tukar maklumat mengikut keperluan, kemudian semak jawapannya.</p>
<p>Simbol <strong>/</strong> ialah cara ringkas melabel arahan. Ia bukan arahan rasmi dalam semua aplikasi AI; salin juga ayat penerangan selepasnya.</p>
<p><a class="button secondary" href="slash-prompts.md" download>Lihat / Muat Turun Semua Slash Prompt</a></p>
<div class="grid two">''' + '\n'.join(cards) + '</div></section>'
path = ROOT / 'index.html'
html = path.read_text(encoding='utf-8')
start, end = '<!-- SLASH_PROMPTS_START -->', '<!-- SLASH_PROMPTS_END -->'
assert html.count(start) == html.count(end) == 1, 'Expected one generated section'
before, rest = html.split(start)
_, after = rest.split(end)
path.write_text(before + start + '\n' + section + '\n' + end + after, encoding='utf-8')
print(f'Synced {len(cards)} selected cards from {len(entries)} slash prompts.')
