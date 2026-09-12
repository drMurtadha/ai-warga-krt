# Visual Product Commands

Panduan visual produk untuk warga KRT, termasuk makanan, kraftangan dan produk jualan komuniti. Lampirkan imej rujukan dan salin arahan lengkap. Simbol `/` ialah label arahan, bukan fungsi rasmi semua aplikasi AI. Gunakan alat yang menyokong imej; eksport GIF memerlukan sokongan pemprosesan fail.

Semak hasil AI sebelum digunakan untuk promosi. Sudut yang tidak kelihatan dalam gambar ialah anggaran, bukan bukti rupa sebenar produk.

---

## `/productexplosion`

### Tujuan
Menghasilkan visual **exploded view** produk dengan komponen atau lapisan produk dipisahkan secara menegak atau mengikut paksi struktur asal.

### Arahan
Gunakan imej produk yang diberikan sebagai rujukan utama.

Hasilkan **exploded product view** yang profesional dan fotorealistik. Pisahkan komponen, bahan, atau lapisan utama produk supaya setiap bahagian kelihatan terapung secara tersusun tetapi masih jelas menunjukkan bagaimana semuanya membentuk produk asal.

### Keperluan
- Kekalkan identiti, bentuk, warna, bahan, tekstur, dan proporsi produk asal semaksimum mungkin.
- Jangan menukar produk kepada reka bentuk baharu.
- Jangan menambah komponen yang tidak wujud atau tidak munasabah.
- Susun komponen mengikut struktur sebenar atau logik produk.
- Pastikan semua komponen sejajar pada paksi yang sesuai.
- Gunakan jarak yang mencukupi antara komponen supaya setiap bahagian mudah dikenal pasti.
- Gunakan perspektif produk komersial/professional product photography.
- Gunakan pencahayaan studio yang bersih dan konsisten.
- Gunakan latar neutral atau putih kecuali konteks imej memerlukan latar lain.
- Elakkan teks, label, anak panah, atau anotasi kecuali diminta.
- Untuk makanan, asingkan setiap lapisan bahan mengikut susunan sebenar dari atas ke bawah.
- Untuk produk mekanikal/elektronik, paparkan casing dan komponen dalaman secara logik tanpa mereka-reka struktur yang tidak dapat disimpulkan daripada imej.

### Output
Satu visual **exploded view** berkualiti tinggi yang masih jelas merupakan produk yang sama seperti imej rujukan.

---

## `/productspin`

### Tujuan
Menghasilkan **multi-angle product spin sheet** yang menunjukkan produk daripada beberapa sudut mengelilingi paksi menegaknya.

### Arahan
Gunakan imej produk yang diberikan sebagai rujukan utama.

Hasilkan **8 pandangan konsisten** bagi produk yang sama pada sudut:

**0° → 45° → 90° → 135° → 180° → 225° → 270° → 315°**

Anggap kamera berada pada ketinggian dan jarak yang sama sementara produk berputar pada paksi menegaknya.

### Keperluan
- Produk mestilah kelihatan sebagai **objek yang sama dalam semua frame**.
- Kekalkan bentuk, dimensi, proporsi, warna, bahan, tekstur, logo, corak, dan ciri unik produk semaksimum mungkin.
- Jangan mengubah reka bentuk produk antara sudut.
- Jangan sekadar mirror atau distort imej asal.
- Perubahan perspektif mesti konsisten dengan putaran fizikal objek.
- Kekalkan saiz produk yang hampir sama dalam setiap frame.
- Pusatkan produk pada kedudukan yang konsisten.
- Gunakan kamera, focal length, horizon, pencahayaan, bayang, dan latar yang konsisten.
- Gunakan latar studio putih atau neutral yang bersih.
- Jika bahagian belakang atau sisi tidak kelihatan dalam imej rujukan, hasilkan anggaran visual yang konservatif dan konsisten; jangan menambah butiran kompleks tanpa asas.
- Susun semua pandangan dalam grid yang kemas.
- Labelkan sudut dengan tepat jika label diperlukan.

### Output
Satu **8-angle product spin sheet** yang boleh digunakan sebagai sumber untuk animasi 360°.

---

## `/360gif`

### Tujuan
Menukarkan siri pandangan produk kepada **animated GIF 360° looping**.

### Input yang digalakkan
Gunakan:
1. product spin sheet yang mempunyai 8 pandangan; atau
2. 8–16 imej produk berasingan yang telah disusun mengikut sudut putaran.

### Arahan
Kenal pasti dan asingkan setiap pandangan produk daripada input.

Susun frame mengikut turutan putaran fizikal yang betul. Untuk set 8 frame, gunakan:

**0° → 45° → 90° → 135° → 180° → 225° → 270° → 315° → kembali ke 0°**

Kemudian bina **animated GIF** yang berulang tanpa henti.

### Keperluan pemprosesan
- Gunakan frame sebenar daripada input; jangan sekadar menggerakkan, memicit, warp, atau rotate imej 2D yang sama.
- Crop setiap frame secara konsisten.
- Samakan canvas, skala, dan kedudukan pusat produk.
- Kekalkan aspect ratio produk.
- Gunakan latar yang konsisten.
- Elakkan perubahan saiz atau kedudukan yang menyebabkan produk kelihatan melompat antara frame.
- Kekalkan urutan sudut yang betul.
- Gunakan sekitar **350–450 ms per frame** sebagai default untuk 8 frame.
- Gunakan **infinite loop**.
- Jangan masukkan UI simulator, slider, butang, atau mock-up interactive viewer.
- Output mestilah fail `.gif` sebenar.
- Jika input mempunyai 16 frame, gunakan semua frame untuk menghasilkan putaran yang lebih lancar.

### Output
Hasilkan fail:

`product_360_spin.gif`

dan berikan pautan untuk memuat turun fail tersebut.

---

## Workflow Disyorkan

```text
Imej produk
    ↓
/productspin
    ↓
8-angle product spin sheet
    ↓
/360gif
    ↓
Animated 360° GIF
```

Untuk visual struktur produk:

```text
Imej produk
    ↓
/productexplosion
    ↓
Exploded product view
```

---

## Contoh Penggunaan

```text
[Upload imej produk]
/productexplosion
```

```text
[Upload imej produk]
/productspin
```

```text
[Upload 8-angle product spin sheet]
/360gif
```
