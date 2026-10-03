# Design Spec: Rumah Dua Lantai 8 × 18 m

Tanggal: 2026-10-02
Status: Disetujui untuk implementasi.

## Tujuan

Membuat presentasi konsep rumah dua lantai yang mudah dipahami dan ditinjau: denah 2D kedua lantai, model 3D dengan beberapa cara pandang, dan proyek Blender yang dapat diedit. Hasil akhir disimpan di `C:\Users\Arifiansyah\OneDrive\Documents\ChatGPT\audit\project-housing`.

## Brief yang disepakati

- Tapak acuan berukuran 8 m lebar muka × 18 m panjang ke belakang.
- Sketsa yang dilampirkan menjadi acuan pembagian ruang lantai 1.
- Daftar teks pengguna menjadi acuan ruang lantai 2.
- Denah merupakan rancangan konsep berproporsi. Ukuran tiap ruang, struktur, bukaan, dan posisi tangga belum ditentukan sebagai gambar kerja konstruksi.
- Halaman harus menampilkan tiga model yang bisa dipilih:
  1. Bentuk rumah lengkap dengan atap.
  2. Lantai 1 saja dengan bagian atas/atap dibuka agar interior terlihat.
  3. Lantai 2 saja.
- Buat presentasi PowerPoint (`.pptx`) yang merangkum konsep, denah, serta tiga mode model untuk dibagikan atau dipresentasikan.

## Pembagian ruang

### Lantai 1 — interpretasi sketsa

Gunakan susunan pada sketsa sebagai panduan, dengan sisi 8 m dianggap sisi depan. Pertahankan hubungan ruang dan nama ruang yang terbaca, termasuk teras, ruang tamu/keluarga, kamar-kamar, kamar utama dan toilet dalam, kamar ART/area servis, pantry atau dapur, toilet, serta area makan/laundry bila terbaca. Tulisan yang tidak jelas tidak boleh diperlakukan sebagai ukuran atau spesifikasi pasti; tandai interpretasinya di halaman sebagai rancangan awal.

### Lantai 2 — daftar pengguna

- Balkon.
- Ruang tamu.
- Area meja kerja dan lemari sepatu.
- Kamar utama dengan toilet dalam.
- Kamar anak perempuan dengan ranjang tingkat.
- Kamar anak laki-laki.
- Satu toilet bersama.
- Meja makan dan pantry.

Susun area bersama dekat balkon dan akses tangga. Tempatkan kamar sebagai zona lebih privat; kamar utama memiliki toilet dalam, sementara toilet bersama mudah dicapai dari ruang bersama dan kamar anak. Posisi final mengikuti proporsi tapak dan tetap dapat direvisi.

## Pengalaman web

- Satu halaman HTML yang dibuka sebagai presentasi lokal.
- Kontrol tiga mode model dengan label “Rumah lengkap”, “Lantai 1”, dan “Lantai 2”.
- Model dapat diputar, diperbesar, diperkecil, dan digeser; kamera awal menunjukkan sudut isometrik yang mudah dibaca.
- Denah 2D lantai 1 dan lantai 2 ditampilkan sebagai gambar terpisah dengan label, skala grafis, dan penanda orientasi depan.
- Tampilkan ringkasan luas tapak dan catatan bahwa ukuran ruang masih konseptual.
- Sediakan tampilan elevasi/atap untuk rumah lengkap; pada mode lantai 1 sembunyikan atap dan lantai 2; pada mode lantai 2 tampilkan lantai 2 sebagai objek fokus.
- Optimalkan agar tetap nyaman di desktop serta dapat digunakan di layar ponsel.

## Model dan aset

- Script Python untuk Blender membuat geometri dua lantai yang konsisten dengan denah dan menambahkan atap sebagai koleksi terpisah agar dapat disembunyikan per mode.
- Hasil yang dituju: file `.blend`, ekspor `.glb` untuk web, dan render gambar utama.
- Denah digital disimpan sebagai SVG supaya label tetap tajam saat diperbesar; sediakan PNG untuk pratinjau cepat.
- Halaman web memuat model dari aset proyek, dengan Three.js sebagai viewer. Jika Blender tidak tersedia di mesin, script tetap disertakan dan keterbatasan pembuatan `.blend`/`.glb` dilaporkan secara jelas.
- Web dan aset disimpan bersama dalam subfolder `project-housing`; README berisi cara membuka halaman dan membuat ulang model di Blender.
- Presentasi PowerPoint disimpan pada folder hasil yang sama dan menggunakan bahasa Indonesia, gambar denah, serta gambar model/render yang konsisten dengan halaman web.

## Batasan dan asumsi

- 8 × 18 m dipakai sebagai jejak bangunan konseptual untuk kedua lantai, bukan survei batas tanah.
- Tebal dinding, ukuran pintu/jendela, tinggi lantai, struktur, dan detail MEP belum diberikan; gunakan nilai visual yang wajar dan konsisten, jangan menyebutnya sebagai spesifikasi konstruksi.
- Tidak mengarang ukuran ruang presisi; dimensi yang muncul sebagai angka di denah harus ditandai sebagai perkiraan konsep.
- Sketsa lantai 1 tidak sepenuhnya jelas pada semua tulisan; hubungan ruang yang terbaca diprioritaskan dan label yang meragukan diberi catatan.
- Tidak ada perubahan pada proyek contoh `akad.in`; proyek itu hanya referensi pola aset.

## Kriteria penerimaan

- Halaman web menampilkan denah kedua lantai serta tiga mode model sesuai brief.
- Mode lantai 1 benar-benar menyembunyikan lantai 2 dan atap; mode lantai 2 memusatkan tampilan pada lantai 2; mode rumah lengkap menunjukkan atap.
- Kamar anak perempuan menampilkan ranjang tingkat dan kamar utama memiliki toilet dalam pada model/denah lantai 2.
- File sumber Blender dan dokumentasi pembuatan tersedia di folder hasil.
- File `.pptx` menyajikan kebutuhan, pembagian ruang dua lantai, dan tiga mode model dengan gambar yang berasal dari aset proyek.
- Denah menampilkan label ruang dengan jelas dan mengikuti orientasi muka 8 m.
- Catatan konseptual dan semua asumsi ukuran terlihat pada halaman atau README.
