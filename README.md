# AI untuk Warga KRT — KRT Meranti

Laman web mobile-first untuk aktiviti hands-on AI komuniti KRT Meranti pada 12 September 2026.

## Tujuan
Membantu peserta menggunakan AI melalui telefon pintar untuk mencari idea resepi, membuat itinerary, menyusun jadual bertugas KRT, menyediakan poster aktiviti dan menjawab kuiz santai. Slot praktikal berlangsung 50 minit dalam program 9.00–11.00 pagi.

## Teknologi
HTML, CSS dan Vanilla JavaScript sahaja. Hosting menggunakan GitHub Pages. Tiada pemasangan kebergantungan atau proses build diperlukan.

## Cara deploy ke GitHub Pages
1. Muat naik semua fail dalam folder projek ke repo `drMurtadha/ai-warga-krt`.
2. Buka **Settings → Pages**.
3. Pilih **Deploy from a branch**.
4. Pilih branch **main**, folder **/ (root)**, kemudian **Save**.
5. Tunggu deployment selesai. Laman: https://drMurtadha.github.io/ai-warga-krt/

## Penggunaan
Buka laman melalui telefon. Baca prompt dan tekan **Copy Prompt**, buka alat AI pilihan anda, tampal teks dan hantar. Mesej kejayaan hanya dipaparkan selepas salinan berjaya. Jika akses clipboard ditolak, laman cuba kaedah salinan alternatif dan memaparkan arahan manual jika masih gagal.

Kuiz menyediakan pilihan jawapan dan butang untuk membuka/menutup jawapan. Poster boleh dibuka dalam dialog untuk tangkap layar. **Cetak / Save as PDF** mencetak poster sahaja.

## Pratonton tempatan
Jalankan `python3 -m http.server 8000` dalam folder ini, kemudian buka http://localhost:8000. Clipboard berfungsi pada HTTPS atau localhost, bergantung pada kebenaran pelayar.

## Tambah atau ubah prompt
1. Dalam `index.html`, salin satu elemen `article.prompt-card` dalam seksyen `id="prompt"`.
2. Ubah tajuk, tujuan, teks `.prompt-text` dan nilai `data-prompt` pada butang kepada teks yang sama. Escape petikan berganda sebagai `&quot;` dan ampersand sebagai `&amp;` dalam atribut HTML.
3. Kemas kini `prompts.md` supaya salinan rujukan sepadan. Fail Markdown ini ialah rujukan penyunting; laman membaca kandungan daripada HTML.
4. Jika prompt digunakan dalam aktiviti, kemas kini salinannya di seksyen aktiviti juga.

## Poster dan gambar
Poster utama ialah HTML/CSS dalam `#poster-content`, bukan imej. Ubah teks di situ dan nilai `data-prompt` butang **Salin Teks Poster** bersama-sama. Dialog menyalin poster HTML secara automatik.

`assets/poster-placeholder.jpg`, `assets/dr-murtadha.jpg` dan `assets/krt-meranti.jpg` ialah placeholder yang disediakan untuk diganti kemudian. Gambar ini belum dipaparkan agar laman tidak menunjukkan gambar pengajar atau lokasi rekaan. Ganti fail pada nama sama dengan imej sebenar; untuk memaparkannya, tambah `<img src="assets/dr-murtadha.jpg" alt="Dr Murtadha, pengajar program" width="1000" height="700" loading="lazy">` pada seksyen pilihan. Untuk poster imej, letakkan elemen imej dalam `#poster-content` supaya paparan dan cetakan menggunakannya. Laraskan saiz dan alt mengikut gambar sebenar.

## Fail
- `index.html`: semua kandungan, prompt, kuiz dan poster.
- `styles.css`: paparan responsive, navigasi telefon dan gaya cetakan.
- `script.js`: clipboard, jawapan kuiz dan dialog poster.
- `prompts.md`: semua teks untuk disalin termasuk prompt latihan dan teks poster.
- `assets/`: placeholder imej dan ruang ikon.
- `.nojekyll`: membolehkan hosting statik terus.

## Aksesibiliti
Bahasa laman Melayu, teks minimum 16px, sasaran sentuhan minimum 44px, fokus papan kekunci, pautan langkau, status salinan untuk pembaca skrin, accordion asli, dialog dengan kekunci Escape dan sokongan reduced motion. Kandungan utama kekal boleh dibaca tanpa JavaScript; fungsi interaktif memerlukan JavaScript.

## Slash Prompt
`slash-prompts.md` mengandungi 31 slash prompt dan panduan penggunaan dalam Bahasa Melayu untuk warga KRT. Sepuluh pilihan asas dan tiga pilihan visual kreatif dan tiga pilihan visual produk dipaparkan sebagai kad dalam seksyen **Slash Prompt**, lengkap dengan tujuan, teks penuh dan butang salin. Pautan ke seksyen tersedia pada navigasi desktop dan sebelum senarai prompt biasa pada semua saiz skrin.

Untuk mengemas kini kad:
1. Edit tajuk slash prompt, tujuan atau blok `text` dalam `slash-prompts.md`.
2. Untuk menukar pilihan kad, edit `SELECTED` dalam `scripts/sync-slash-prompts.py`.
3. Jalankan `python3 scripts/sync-slash-prompts.py` dari folder projek.
4. Commit `slash-prompts.md` dan `index.html` yang dikemas kini bersama-sama.

Kad dijana sebagai HTML statik supaya boleh dibaca tanpa JavaScript dan semasa membuka fail setempat. Tiada proses build diperlukan pada GitHub Pages. Butang salin menggunakan fungsi clipboard sedia ada. Simbol `/` ialah gaya arahan, bukan arahan rasmi yang disokong oleh semua alat AI.

Kad **Slash Prompt Visual Kreatif** dan **Slash Prompt Visual Produk** menyediakan contoh Bahasa Melayu dan English, masing-masing dengan butang salin sendiri. Edit kedua-dua blok `text` di bawah prompt berkaitan dalam `slash-prompts.md`, kemudian jalankan skrip penyegerakan di atas.

## Visual Produk
`product_visual_commands.md` menyimpan panduan terperinci yang disesuaikan untuk warga KRT. Seksyen `#slash-produk` mempunyai `/productexplosion`, `/productspin` dan `/360gif`, dengan contoh Bahasa Melayu dan English dalam `slash-prompts.md`. `/productexplosion` dipindahkan dari visual kreatif supaya tidak berulang. Laman menyediakan prompt untuk disalin; imej dan GIF dihasilkan melalui alat pilihan peserta yang menyokong fungsi tersebut.
