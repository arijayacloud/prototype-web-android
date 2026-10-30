# Aquafit & SwimPro — Prototype Aplikasi Jasa & Kursus Renang

Prototype web aplikasi pemesanan jasa kursus dan pelatihan renang privat/reguler dengan alur end-to-end terintegrasi multi-peran:
**Pelanggan Pilih Paket → Pilih Jadwal → Pilih Instruktur → Pembayaran → Admin Konfirmasi → Instruktur Menerima Jadwal → Sesi Selesai**.

## Fitur Utama & Alur Sistem

1. **Alur Pelanggan (Booking Wizard 4 Tahap):**
   - **Tahap 1: Pilih Paket Kursus**
     - Paket Balita/Kids Water Safety (4 sesi)
     - Paket Pemula Dewasa (Gaya Dada & Pernapasan - 6 sesi)
     - Paket Private VIP 1-on-1 (Eksklusif - 8 sesi)
     - Paket Terapi Renang / Skoliosis & Lansia (4 sesi)
     - Paket Intensif Prestasi & Koreksi Gaya (10 sesi)
   - **Tahap 2: Atur Jadwal & Lokasi Kolam**
     - Pilihan tanggal latihan dan slot jam (Pagi 07:00-09:00, Siang 10:00-12:00, Sore 15:30-17:30, Malam 18:30-20:30)
     - Pilihan venue kolam (Kolam Renang Mitra Terdekat / Kolam Pribadi Rumah)
   - **Tahap 3: Pilih Instruktur Renang Bersertifikasi**
     - Profil pelatih (lisensi PRSI, pengalaman, rating siswa, spesialisasi pria/wanita hijab-friendly)
   - **Tahap 4: Pembayaran & Terbitkan Pesanan**
     - Metode QRIS instan, Transfer BCA/Mandiri, Debit
     - Simulasi upload bukti bayar
     - Status booking realtime: *Menunggu Verifikasi Admin*

2. **Alur Admin (Verifikasi & Manajemen Booking):**
   - Dashboard ringkasan booking aktif, verifikasi bukti bayar dalam satu klik
   - Konfirmasi pemesanan sehingga status berganti menjadi *Terkonfirmasi* dan jadwal otomatis ditugaskan ke dashboard instruktur terkait
   - Laporan omzet dan status seluruh pemesanan

3. **Alur Instruktur (Jadwal Mengajar & Penyelesaian Sesi):**
   - Kalender jadwal mengajar instruktur yang disetujui admin
   - Rincian murid: level kemampuan, target gaya renang, lokasi kolam, kontak WA murid
   - Aksi: Tombol *Mulai Sesi* dan *Tandai Selesai* setelah latihan berakhir
   - Feedback evaluasi capaian teknik murid

4. **Multi-Role Switcher:**
   - Bar kontrol di bagian atas memungkinkan penguji beralih instan antara peran Pelanggan, Admin, dan Instruktur tanpa login ulang.
   - Data tersimpan persisten di `localStorage`.
