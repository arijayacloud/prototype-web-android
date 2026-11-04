# Flipbook — E-paper / E-book dari Gambar

Aplikasi web statis (satu file `flipbook.html`, tanpa backend) untuk mengubah kumpulan gambar menjadi buku digital dengan efek halaman yang bisa dibolak-balik, musik latar, dan link yang bisa dibagikan.

Live: https://arijayacloud.github.io/prototype-web-android/flipbook.html

## Fitur
- Upload banyak gambar sekaligus, urutkan (◀ ▶) dan hapus per halaman
- Gambar dikompres otomatis di browser (maks. lebar 900px, JPEG q72)
- Efek balik halaman 3D (CSS transform), navigasi: klik sisi kanan/kiri, tombol ‹ ›, panah keyboard, geser di layar sentuh
- Musik latar dari URL mp3 — tombol putar/jeda, playlist berurutan, loop
- Share link: seluruh buku (judul, penulis, halaman, musik) dipak ke hash URL dengan deflate-raw + base64 — bisa dibuka siapa saja, tanpa server
- Draft tersimpan otomatis di `localStorage`

## Batasan
- Data buku ada di dalam URL. Batas praktis ±1.5 MB; kalau lebih, kurangi halaman atau kecilkan gambar.
- File musik lokal tidak bisa dibagikan — pakai URL publik.
- `CompressionStream` dibutuhkan untuk kompresi; browser lama pakai base64 mentah (link lebih panjang).

## Struktur
- `flipbook.html` — seluruh aplikasi (editor + reader + share)
- `index.html` — daftar project; kartu Flipbook ada di sini
4. Bagikan link dengan teman, keluarga, atau publik
5. Klik link untuk membuka buku di peramban web (desktop/mobile)

## Struktur Proyek
- `index.html` - Halaman utama (login + dashboard)
- `flipbook.html` - Aplikasi flipbook (halaman utama)
- `admin.html` - Dashboard admin untuk mengelola buku
- `assets/` - Penyimpanan gambar buku
- `music/` - File musik background
- `styles/` - CSS untuk semua halaman
- `scripts/` - JavaScript untuk logika flipbook dan admin

## Versi API
- `v1` - Versi stabil saat ini

## Cara Menggunakan
1. Kloning repositori
2. Buka `index.html` di peramban web
3. Daftar/masuk
4. Klik "Buat Buku Baru" atau pilih buku dari daftar
5. Ikuti proses upload gambar
6. Preview dan publikasikan
7. Bagikan link dengan orang lain

## Teknologi Stack
- HTML5
- CSS3 (Tailwind CSS)
- JavaScript (Vanilla)
- Canvas API (untuk efek halaman)
- Web Audio API (untuk pemutar musik)

## Masalah yang Dikenal
- Efek halaman mungkin lambat pada perangkat dengan spesifikasi rendah
- Upload gambar > 100 halaman mungkin menyebabkan masalah performa
- Beberapa browser mungkin memiliki masalah dengan audio autostart

## License
MIT License - Hak cipta © 2024 Flipbook Project