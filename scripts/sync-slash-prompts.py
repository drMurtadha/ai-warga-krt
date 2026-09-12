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
entries = {}
for name, block in re.findall(r'^### `(/[^`]+)`\n(.*?)(?=^#{2,3} |\Z)', source, re.S | re.M):
    purpose = block.strip().splitlines()[0]
    examples = re.findall(r'```text\n(.*?)\n```', block, re.S)
    assert examples, f'Missing example for {name}'
    assert name not in entries, f'Duplicate slash prompt: {name}'
    entries[name] = (purpose, examples)
cards = []
for name in SELECTED:
    purpose, examples = entries[name]
    prompt = examples[0]
    cards.append(
        '<article class="card prompt-card slash-card">'
        f'<h3>{escape(name)}</h3><p>{escape(purpose)}</p>'
        f'<p class="prompt-text">{escape(prompt)}</p>'
        f'<button class="copy-btn" data-prompt="{escape(prompt, quote=True)}">Copy Prompt</button>'
        '</article>'
    )
creative_cards = []
product_cards = []
for name in ('/magazinecover', '/adcreative', '/animated', '/productexplosion', '/productspin', '/360gif'):
    purpose, examples = entries[name]
    assert len(examples) == 2, f'Expected Malay and English examples for {name}'
    content = f'<article class="card prompt-card slash-card creative-card"><h3>{escape(name)}</h3><p>{escape(purpose)}</p>'
    for language, prompt in zip(('Bahasa Melayu', 'English'), examples):
        content += (
            f'<div class="prompt-example"><h4>{language}</h4>'
            f'<p class="prompt-text">{escape(prompt)}</p>'
            f'<button class="copy-btn" aria-label="Copy Prompt {escape(name)} — {language}" '
            f'data-prompt="{escape(prompt, quote=True)}">Copy Prompt</button></div>'
        )
    (product_cards if name in ('/productexplosion', '/productspin', '/360gif') else creative_cards).append(content + '</article>')
creative_section = (
    '<section id="slash-visual" aria-labelledby="visual-title">'
    '<h3 id="visual-title" class="visual-title">Slash Prompt Visual Kreatif</h3>'
    '<p>Pilih contoh Bahasa Melayu atau English untuk mencuba idea visual. Salin satu contoh dan ubah mengikut aktiviti komuniti anda.</p>'
    '<div class="grid two">' + '\n'.join(creative_cards) + '</div></section>'
)
product_section = (
    '<section id="slash-produk" aria-labelledby="product-title">'
    '<h3 id="product-title" class="visual-title">Slash Prompt Visual Produk</h3>'
    '<p>Cuba dengan gambar makanan, kraftangan atau produk jualan warga KRT. Lampirkan gambar dalam alat AI pilihan anda, kemudian tampal satu prompt lengkap.</p>'
    '<p><strong>Untuk putaran:</strong> gambar produk → /productspin → helaian 8 sudut → /360gif → fail GIF.</p>'
    '<p><strong>Untuk lapisan produk:</strong> gambar produk → /productexplosion → visual komponen berasingan.</p>'
    '<p>Gunakan alat yang menyokong imej dan eksport GIF. Sudut yang tidak kelihatan ialah anggaran; semak rupa produk sebelum membuat hebahan.</p>'
    '<p><a class="button secondary" href="product_visual_commands.md" download>Muat Turun Panduan Visual Produk</a></p>'
    '<div class="grid two">' + '\n'.join(product_cards) + '</div></section>'
)
section = '''<section class="shell section" id="slash-prompt" aria-labelledby="slash-title">
<p class="eyebrow">ARAHAN CEPAT UNTUK AI</p><h2 id="slash-title">Slash Prompt</h2>
<p class="intro">Mulakan arahan dengan kata kunci seperti <strong>/poster</strong> atau <strong>/resepi</strong>. Pilih kad, salin keseluruhan prompt dan tampal dalam alat AI pilihan anda. Tukar maklumat mengikut keperluan, kemudian semak jawapannya.</p>
<p>Simbol <strong>/</strong> ialah cara ringkas melabel arahan. Ia bukan arahan rasmi dalam semua aplikasi AI; salin juga ayat penerangan selepasnya.</p>
<p><a class="button secondary" href="slash-prompts.md" download>Lihat / Muat Turun Semua Slash Prompt</a></p>
<div class="grid two">''' + '\n'.join(cards) + '</div>' + creative_section + product_section + '</section>'
path = ROOT / 'index.html'
html = path.read_text(encoding='utf-8')
start, end = '<!-- SLASH_PROMPTS_START -->', '<!-- SLASH_PROMPTS_END -->'
assert html.count(start) == html.count(end) == 1, 'Expected one generated section'
before, rest = html.split(start)
_, after = rest.split(end)
path.write_text(before + start + '\n' + section + '\n' + end + after, encoding='utf-8')
print(f'Synced {len(cards) + len(creative_cards) + len(product_cards)} selected cards from {len(entries)} slash prompts.')
