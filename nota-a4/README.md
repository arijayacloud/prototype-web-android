# NotaKilat A4 — Pembuat Nota & Invoice Cepat Kertas A4 (Tanpa Data Master)

Aplikasi web modern untuk pembuatan nota penjualan dan invoice langsung jadi yang dioptimalkan khusus untuk pencetakan ke kertas A4, penyimpanan data pelanggan otomatis, dan riwayat nota tanpa repot menginput data master barang.

## Fitur Utama

1. **Tanpa Input Data Master (Fast-Entry)**:
   - Pengguna dapat langsung mengetik nama barang, jumlah (qty), dan harga satuan secara dinamis on-the-fly.
   - Tambah baris barang bebas (`+ Tambah Baris Barang`) dan hapus baris dalam satu klik.
   - Subtotal per item dan Grand Total langsung terhitung otomatis secara real-time.

2. **Format Print Kertas A4 Presisi**:
   - Styling cetak `@page { size: A4 portrait; margin: 10mm 12mm; }` dan `@media print`.
   - Layout formal nota profesional: Kop Toko/Usaha, Nomor Nota, Tanggal, Kepada Yth Pelanggan, Tabel Rincian Barang (No, Uraian, Qty, Harga, Subtotal), Terbilang Bahasa Indonesia otomatis, Catatan, Ringkasan Pembayaran, serta Kolom Tanda Tangan (Pelanggan, Gudang, Kasir/Hormat Kami).
   - Watermark status otomatis (LUNAS / TEMPO / DP).

3. **Penyimpanan Nota & Buku Pelanggan**:
   - Riwayat nota tersimpan aman di `localStorage` peramban.
   - Setiap kali nota disimpan, nama dan alamat pelanggan otomatis tersimpan ke buku pelanggan (bisa dipilih kembali pada pembuatan nota berikutnya).
   - Pencarian riwayat nota berdasarkan nama pelanggan atau nomor nota.
   - Buka, edit, cetak ulang, atau duplikasi nota lama.
   - Ekspor dan impor data nota ke format JSON untuk backup data.

4. **Kirim via WhatsApp**:
   - Satu klik untuk mengirimkan format ringkasan nota langsung ke WhatsApp pelanggan.

5. **Pengaturan Kop Toko Fleksibel**:
   - Dapat mengubah nama toko, slogan, alamat toko, nomor telepon/WhatsApp, dan rekening pembayaran.

## Tech Stack
- HTML5 & CSS3 (Tailwind CSS CDN)
- Font Awesome 6.5.1
- Google Fonts (Inter, Plus Jakarta Sans, JetBrains Mono)
- Vanilla JavaScript (Local Storage persistence & responsive view)
