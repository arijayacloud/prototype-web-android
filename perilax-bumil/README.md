# Perilax — Prototype Aplikasi Kehamilan & Persalinan Minim Trauma

Prototype web mobile (Android UI) untuk aplikasi kesehatan ibu hamil **Perilax** (*"Perineum Relax, Bumil Siap Bersalin Minim Trauma"*). Didesain berdasarkan mockup 10 layar perjalanan ibu hamil: mulai dari onboarding edukatif, pemantauan usia kehamilan, panduan pijat perineum, pencegahan trauma jalan lahir, artikel edukasi, tombol bantuan darurat, hingga jadwal & riwayat pemeriksaan medis (ANC).

## 10 Layar Utama yang Diimplementasikan

1. **Layar 1 — Splash Screen:**
   - Visual identitas Perilax (nuansa *Rose Magenta & Blush Pink*), tagline inspiratif, dan indikator loading otomatis.
2. **Layar 2 — Onboarding 1 (Pendamping Setia Kehamilanmu):**
   - Ilustrasi ibu hamil & penjelasan misi pendampingan kehamilan aman & nyaman.
3. **Layar 3 — Onboarding 2 (Pantau Tumbuh Kembang & Kesehatan):**
   - Poin pemantauan janin, pengingat ANC, dan catatan rekam medis kehamilan.
4. **Layar 4 — Onboarding 3 (Persiapan Persalinan Minim Trauma):**
   - 4 pilar pencegahan robekan perineum: pijat perineum (35+ minggu), senam Kegel dasar panggul, teknik napas, dan kompres hangat.
5. **Layar 10 — Penutup & Motivasi:**
   - Karangan bunga visual, kutipan *"Persiapan hari ini, untuk kelahiran yang lebih baik esok hari"*, serta CTA **"Mulai Sekarang →"**.
6. **Layar 5 — Beranda / Dashboard Utama:**
   - Kartu tracker kehamilan interaktif: Usia 28 Minggu (Trimester 2), hitung mundur HPL, ukuran janin, dan denyut jantung janin simulasi.
   - 6 Menu Cepat: Perkembangan Janin, Jadwal ANC, Info Kesehatan, Latihan & Relaksasi, Persiapan Persalinan, dan Konsultasi Bidan.
   - Banner tombol cepat siaga darurat.
7. **Layar 6 — Panduan Persalinan:**
   - Tab filter: *Sebelum*, *Saat Persalinan*, dan *Setelah*.
   - Modul Pijat Perineum (panduan langkah demi langkah & timer), Latihan Otot Dasar Panggul (Kegel timer interaktif), Kompres Hangat, dan Teknik Napas Mengejan.
8. **Layar 7 — Edukasi & Informasi:**
   - Kolom pencarian topik & filter kategori: *Janin*, *Ibu*, *Nutrisi*, *Tanda Bahaya*.
   - Artikel lengkap dengan modal baca (nutrisi bumil, perkembangan janin, tanda bahaya).
9. **Layar 8 — Fitur Darurat & Kontak Tenaga Medis:**
   - Tombol panggil cepat Ambulans 118 / 119, Bidan Desa, Puskesmas, RSIA, dan Kontak Suami/Keluarga via telepon / WhatsApp darurat.
   - Kotak peringatan tanda bahaya kehamilan (perdarahan, ketuban pecah, sakit kepala berat).
10. **Layar 9 — Jadwal & Riwayat Medis (ANC):**
    - Tab *Jadwal ANC* dan *Riwayat Pemeriksaan*.
    - Kartu kunjungan ANC mendatang, hasil USG, lab darah/Hb, serta tracker harian minum Tablet Tambah Darah (TTD) yang bisa dicentang langsung.

## Fitur Interaktif Tambahan
- **Screen Navigator Panel (Desktop Mode):** Pemilih 10 layar instan untuk kemudahan demo klien / reviewer.
- **Responsive Phone Frame:** Frame Android realistis lengkap dengan status bar waktu/sinyal dan bottom navigation bar yang aktif berpindah antar menu.
- **LocalStorage Persistence:** Data tracker TTD, catatan ANC, dan preferensi tersimpan di peramban.

## Teknologi
- HTML5, CSS3 & Tailwind CSS CDN
- Font: Google Fonts (*Plus Jakarta Sans*, *Inter*, *Playfair / Dancing Script accents*)
- Font Awesome 6.5 Icons
- Vanilla JavaScript tanpa dependensi eksternal berat
