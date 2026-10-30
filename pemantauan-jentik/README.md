# Si-Jentik Kelurahan — Sistem Pemantauan Jentik Nyamuk (ABJ & Jumantik)

Aplikasi pemantauan jentik nyamuk (Pemeriksaan Jentik Berkala / PJB) tingkat kelurahan/desa berbasis digital untuk kader Jumantik (Juru Pemantau Jentik), Puskesmas, dan Kelurahan.

## Fitur Utama

1. **Dashboard & Indikator Angka Bebas Jentik (ABJ):**
   - Perhitungan otomatis persentase Angka Bebas Jentik (ABJ = Jumlah Rumah Bebas Jentik / Total Rumah Diperiksa * 100%).
   - Indikator standar Kemenkes RI: Target ABJ ≥ 95% (Zona Hijau/Aman), 85-94% (Zona Kuning/Waspada DBD), < 85% (Zona Merah/Rawan Kejadian Luar Biasa DBD).
   - Indeks House Index (HI), Container Index (CI), dan Breteau Index (BI).

2. **Formulir Input Pemeriksaan Lapangan Kader Jumantik:**
   - Data kepala keluarga (nama KK, NIK/No. Telepon, RT, RW, alamat rumah).
   - Checklist kontainer penampungan air dalam rumah (bak mandi, drum air, ember, tempayan) dan luar rumah (talang air, ban bekas, pot bunga, dispenser).
   - Hasil deteksi per kontainer: Positif Jentik / Negatif.
   - Tindakan intervensi langsung: Pemberian bubuk abate/larvasida, pengurasan, penutupan kontainer (PSN 3M Plus).
   - Catatan kondisi lingkungan & foto dokumentasi.

3. **Peta & Rekapitulasi Wilayah RW/RT Kelurahan:**
   - Rekap status jentik per RW/RT untuk pemetaan area prioritas fogging atau kerja bakti serentak.
   - Filter data berdasarkan tanggal pemeriksaan, RW, dan status hasil (Bebas / Ditemukan Jentik).

4. **Laporan & Ekspor Laporan Jumantik:**
   - Tabel laporan rekapitulasi data pemeriksaan real-time.
   - Fitur cetak laporan format rekap bulanan Puskesmas / Kelurahan dan kirim ringkasan ke grup WhatsApp RW/RT.
   - Data persisten tersimpan di `localStorage`.
