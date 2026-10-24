# MokaRetail — Prototype Aplikasi Kasir POS, Nota Digital & Booking Retail

Prototype web modern untuk kebutuhan kasir toko/warung/retail terinspirasi dari alur POS profesional seperti Moka POS. Dirancang untuk pemilik toko (admin) dan kasir (karyawan) dengan fokus pencatatan nota transaksi cepat, cetak struk thermal, kirim nota via WhatsApp, serta manajemen booking/jadwal pengambilan barang (pre-order sembako & pesanan toko).

## Fitur Utama

1. **Autentikasi & Multi-Peran (Login / Daftar)**
   - Pilihan peran langsung: **Owner/Admin** (akses penuh ke kasir, stok produk, booking, laporan keuangan, pengaturan nota) dan **Kasir/Karyawan** (fokus kasir transaksi cepat, nota, dan antrean booking).
   - Modal daftar akun staf baru dan switch akun tanpa reload.
   - Ringkasan shift kerja kasir aktif.

2. **Mesin Kasir & Aplikasi Nota (Inspirasi Moka POS)**
   - Grid katalog produk retail terbagi per kategori (Sembako, Minuman, Makanan Ringan, Bumbu & Dapur).
   - Keranjang belanja interaktif: pengaturan kuantitas, diskon transaksi (persen atau nominal), catatan pesanan, dan nama pelanggan/member.
   - Pembayaran fleksibel: Tunai (tombol pecahan uang cepat + hitung otomatis kembalian), QRIS Dinamis, Transfer Bank, dan Debit.
   - **Nota Struk Kasir Thermal (58mm/80mm)**:
     - Nomor nota unik otomatis (`NOTA-YYYYMMDD-XXXX`), tanggal & jam, nama kasir, rincian barang, diskon, total bayar, dan kembalian.
     - **Cetak Nota (Print)**: Format CSS ramah cetak printer thermal struk mini.
     - **Kirim Nota via WhatsApp**: Format teks nota rapi siap dikirim ke nomor pembeli.
     - Simpan riwayat transaksi dan opsi cetak ulang nota kapan saja.

3. **Booking / Jadwal Pengambilan (Pre-Order & Titip Ambil)**
   - Solusi untuk toko retail/sembako yang melayani pesanan partai besar, paket arisan/hajatan, atau titip ambil terjadwal.
   - Kalender & slot jadwal pengambilan pesanan (Hari ini, Besok, Mendatang).
   - Form booking dengan estimasi total belanja, uang muka (DP), dan rincian item.
   - Status pesanan: *Menunggu*, *Sedang Disiapkan*, *Siap Ambil*, *Selesai*.
   - Tombol **Kirim Pengingat WA** ke pembeli.
   - Tombol **Konversi ke Nota POS** (pesanan booking langsung ditarik ke kasir untuk proses pelunasan dan cetak nota instan).

4. **Inventaris & Manajemen Stok**
   - Tambah dan edit produk retail, penetapan harga jual, SKU/barcode simulasi, dan jumlah stok.
   - Peringatan stok menipis otomatis.

5. **Laporan & Dashboard Analytics**
   - Ringkasan penjualan harian: Omzet, total nota, barang terjual, dan booking aktif.
   - Grafik tren penjualan 7 hari terakhir (Canvas 2D interaktif tanpa dependensi eksternal berat).
   - Ekspor laporan penjualan ke format CSV.

6. **Pengaturan Toko**
   - Kustomisasi identitas toko: Nama Toko, Alamat, Nomor WhatsApp, dan Pesan Footer Nota.
   - Seluruh data tersimpan secara persisten di `localStorage` peramban (client-side prototype siap demo).

## Teknologi
- HTML5 & CSS3
- Tailwind CSS CDN
- Font Awesome 6.5
- Inter & Plus Jakarta Sans Google Fonts
- Vanilla JavaScript (Responsive Desktop & Mobile Android View)
