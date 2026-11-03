# LaundryApp — Aplikasi Laundry Mobile & Web

Aplikasi laundry laundry lengkap untuk layanan cuci, setrika, dan pemesanan laundry kilat online. Dilengkapi fitur CRM, katalog produk, keranjang belanja, checkout terintegrasi, chat WhatsApp, kupon & promo, absensi laundry, dan laporan analitik.

## 🎯 Masalah
Bisnis laundry seringkali menghadapi tantangan:
- **Pelanggan bingung** menentukan berat cucian & harga
- **Proses pemesanan lama** & konfirmasi manual
- **Promo tidak terdata** & kadang diberikan sembarangan
- **Tidak ada laporan** tentang pesanan, pemasukan, & performa staff
- **Pelanggan sulit** menghubungi admin untuk konsultasi

## ✅ Solusi
Aplikasi LaundryApp memberikan **lengkap**:
- **Login / Daftar** (OTP & biometrik) + RBAC (Pelanggan, Karyawan, Admin)
- **Katalog Produk**: Paket laundry, harga, durasi, kapasitas
- **Keranjang & Checkout**: Pilih layanan & berat cucian otomatis, kalkulasi harga
- **Chat Admin**: WhatsApp cepat untuk konsultasi & pemesanan
- **Kupon & Promo**: Kupon progresif, diskon, kode referral
- **Laporan & Analitik**: Pemasukan harian, produk populer, profitabilitas, pelanggan
- **Booking / Jadwal**: Pesan laundry sesuai jadwal & tracking progres

## 🌟 Fitur Utama

### 🔐 Autentikasi & Keamanan
- **Login / Daftar**: OTP via SMS, Email, Google, Facebook
- **Autentikasi Biometrik**: Face ID, Fingerprint (Android)
- **Role-Based Access Control**:
  - **Pelanggan**: Pesan, tracking, upload bukti pembayaran
  - **Karyawan**: Absensi, status pesanan, cek cucian
  - **Admin**: Kelola produk, kupon, chat pelanggan, laporan

### 📦 Katalog & Pemesanan
- **Paket Laundry**:
  - **Reguler**: Cuci saja (2 jam), Setrika saja (1 jam), Cuci + Setrika (3 jam)
  - **Kilat**: Express 2 jam, Express 4 jam, Express 6 jam
  - **Keluarga**: Paket 3kg, 5kg, 10kg, VIP 24 jam
- **Harga Otomatis**: Berat cucian terdeteksi, kalkulasi biaya real-time
- **Keranjang Belanja**: Pilih layanan, berat, frekuensi, estimasi biaya
- **Checkout**: Pilihan pembayaran (QRIS, Transfer, Tunai), upload bukti

### 📞 Chat & Notifikasi WhatsApp
- **WhatsApp Direct**: Konsultasi, pertanyaan layanan, fast order
- **Real-time Notifikasi**:
  - Status pesanan: Diterima, Proses, Cuci, Setrika, Siap, Selesai
  - Jatuh tempo, promo, reminder laundry
  - Konfirmasi pembayaran
- **Web Widget**: Chat admin langsung di website

### 💰 Kupon & Promo
- **Kupon**: Kupon progresif, diskon 10% - 50%, berlaku, jumlah terbatas
- **Referral**: Kode referral, bonus poin untuk referensi
- **Diskon**: Paket bundling, promo musim, diskon volume
- **Kelola Kupon**: Buat, edit, batas waktu, statistik penggunaan

### 📊 Laporan & Analitik
- **Dashboard**: Pemasukan harian & bulanan, pesanan hari ini
- **Analitik Produk**: Layanan terlaris, profit margin, rating pelanggan
- **Pelanggan**: Loyalitas, riwayat pemesanan, total belanja
- **Stok & Inventaris**: Pelacakan deterjen, chemical, kapasitas mesin
- **Laporan Bulanan**: PDF & Excel, export data, segmentasi data

### 📅 Booking / Jadwal
- **Jadwal Pesan**: Pilih tanggal & jam layanan
- **Tracking Progress**: Status pesanan real-time
- **Kalender**: Lihat & kelola semua pemesanan
- **Kustomisasi**: Tambah layanan tambahan, instruksi khusus

## 🏗️ Struktur File

```
/laundry-app
├── app/src/main/java/com/example/laundryapp
│   ├── ui/login/login_aktivitas.java
│   ├── ui/katalog/katalog_aktivitas.java
│   ├── ui/keranjang/keranjang_aktivitas.java
│   ├── ui/checkout/checkout_aktivitas.java
│   ├── ui/chat/chat_aktivitas.java
│   ├── ui/kupon/kupon_aktivitas.java
│   ├── ui/laporan/laporan_aktivitas.java
│   ├── ui/absensi/absensi_aktivitas.java
│   └── ui/riwayat/riwayat_aktivitas.java
├── app/src/main/res
│   ├── navigation
│   ├── layouts
│   └── values/strings.xml
├── data/database
│   ├── retrofit_client.java
│   ├── api/endpoints.java
│   └── local/laundry_db.sqlite
├── build.gradle
└── gradle.properties
```

## 🛠️ Stack Teknologi

- **Android SDK**: Jetpack Compose + MVVM + LiveData
- **Networking**: Retrofit, OkHttp
- **Database**: Room (SQLite + offline)
- **Security**: BiometricAuthenticator, AES256
- **Auth**: OTP via Firebase / Google Sign-In
- **UI**: Material 3, Dark Theme, Dynamic Colors
- **Push Notification**: Firebase Cloud Messaging
- **Lokal Storage**: SharedPreferences, EncryptedSharedPreferences
- **PDF/Excel**: MPDF / Apache POI untuk export laporan
- **FontAwesome**: Icon dalam UI
- **Font**: Google Fonts (Inter)

## 🧪 State App

**In Progress:**
- Implementasi Flutter Android release
- Autentikasi SMS OTP + biometrik
- Offline-first data penyimpanan
- Katalog produk dengan pricing dinamis
- Keranjang & checkout workflow
- Notifikasi WhatsApp & real-time

**Roadmap (minggu depan):**
- Complete Web-responsive UI
- Implement payment gateway + QRIS
- Build isobar admin dashboard & analytics
- Test deploy to Play Store & Web