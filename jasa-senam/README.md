# SenamPro — Sistem Pemesanan Paket Senam Online

Aplikasi booking dan manajemen kelas senam online interaktif dengan alur lengkap pemesanan senam: **Pelanggan Pilih Paket → Pilih Jadwal & Instruktur → Bayar Online → Admin Konfirmasi → Instruktur Terima Jadwal → Selesai**.

## Fitur Utama

1. **Katalog Paket Senam (6 Jenis Kelas):**
   - Zumba Dance (Rp 150.000)
   - Aerobik Low Impact (Rp 120.000)
   - Yoga & Stretching (Rp 100.000)
   - Body Combat (Rp 180.000)
   - Personal Trainer (Rp 350.000)
   - Family Fitness (Rp 250.000)

2. **Alur Pemesanan Multi-Step (3 Tahap):**
   - **Langkah 1: Pilih Paket Senam** — Pelanggan memilih dari 6 paket kelas dengan icon, deskripsi, dan harga.
   - **Langkah 2: Pilih Jadwal & Instruktur** — Pemilihan hari/jam kelas, instruktur berlisensi, data pelanggan (nama, WhatsApp).
   - **Langkah 3: Konfirmasi & Bayar** — Ringkasan pesanan, metode pembayaran (QRIS/Transfer/E-Wallet/Kartu Kredit), bukti transfer.

3. **Manajemen Pembayaran & Status Pesanan:**
   - Metode pembayaran: QRIS, Transfer Bank (BCA/Mandiri/BNI), E-Wallet (OVO/GoPay/DANA), Kartu Kredit.
   - Status otomatis: "MENUNGGU KONFIRMASI ADMIN" → Admin verifikasi → "DIKONFIRMASI" → Instruktur terima jadwal di aplikasi admin.
   - Integrasi WhatsApp otomatis untuk notifikasi pesanan & konfirmasi ke pelanggan.

4. **Riwayat Pesanan Pelanggan:**
   - Tabel riwayat semua booking dengan status real-time.
   - Kode booking unik untuk setiap pesanan (SEN-XXXX).
   - Tombol "Hubungi Admin via WhatsApp" untuk follow-up & pertanyaan.

5. **Promo & Diskon:**
   - Banner promo otomatis: "DISKON 20%" dengan kode SENAMPRO.
   - Hitung harga otomatis per paket.

6. **Penyimpanan Data Lokal:**
   - Semua booking tersimpan di `localStorage` browser.
   - Data persisten tanpa perlu backend/database.

## Alur Bisnis (User Journey)

```
[Pelanggan Buka Aplikasi]
         ↓
   [Lihat Katalog Paket 6 Jenis Senam]
         ↓
   [Pilih 1 Paket → Klik "Pesan"]
         ↓
   [Step 1: Paket Senam Dipilih → Klik "Lanjut"]
         ↓
   [Step 2: Input Jadwal, Instruktur, Data Diri → Klik "Lanjut"]
         ↓
   [Step 3: Lihat Ringkasan, Pilih Metode Bayar, Upload Bukti → Klik "Kirim ke Admin"]
         ↓
   [Pesanan Dikirim ke Admin]
         ↓
   [Status: "MENUNGGU KONFIRMASI ADMIN"]
         ↓
   [Admin Verifikasi Pembayaran di Aplikasi Admin Panel]
         ↓
   [Status Berubah Menjadi "DIKONFIRMASI"]
         ↓
   [Instruktur Menerima Jadwal Kelas Baru di Dashboard]
         ↓
   [Pelanggan Dapat Notifikasi WhatsApp Konfirmasi]
         ↓
   [Selesai — Kelas Dimulai Sesuai Jadwal]
```

## Stack Teknologi

- **Frontend:** HTML5, Tailwind CSS (CDN), Font Awesome (Icon), Vanilla JavaScript
- **Database:** LocalStorage (Penyimpanan Lokal Browser)
- **Integrasi:** WhatsApp API (Simulasi Chat ke Admin)
- **Responsif:** Mobile-first, support semua ukuran layar
