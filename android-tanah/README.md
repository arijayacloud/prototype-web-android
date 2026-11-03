# Aplikasi Android — Manajemen Properti Tanah

Aplikasi mobile Android untuk **manajemen dan pemantauan progres akad dan transaksi properti** (AJB/PPJB), dilengkapi fitur CRM, notifikasi timeline, jatuh tempo otomatis, dan dashboard analitik.

## 🎯 Masalah
Proyek properti seringkali **terlambat**, **tidak terstruktur**, dan **kurang transparan**:
- Progres akad (surat, tandatangan, notaris) tidak terpantau
- Jatuh tempo pembayaran tidak ada notifikasi
- Timeline progress tidak terlihat jelas
- Data notaris, pembayaran, dokumen terpencar di WhatsApp/spreadsheets

## ✅ Solusi
Aplikasi Android ini memberikan **secara end-to-end**:
- **CRM & Catatan Akad** (bukti servey, surat, kesediaan, dll.)
- **Timeline Progress** (AKAD, AJB/PPJB, Serah Terima, Lunas)
- **Jatuh Tempo & Notifikasi** (SMS WhatsApp), reminder otomatis
- **Dashboard Analitik & Laporan** (per Realtors, jumlah transaksi, omzet, progress aset)
- **Booking / Jadwal** (offline first + sync cloud)
- **Absensi & Catatan** (pemeriksaan lapangan, peninjauan)
- **Aplikasi Login / Daftar** (SMS/OTP, autentikasi biometrik)

## 🌟 Fitur Utama

### 📋 Catatan Akad & Data Transaksi
- **Laporan Pemesanan**: Cetak faktur & bukti pembayaran (PDF/Excel)
- **Tracking Progres Akad**: Pertahankan bukti sukses + bukti timeline
- **Manajemen Notaris**: Contact list, tagihan, catatan progres
- **Dokumentasi Lengkap**: Upload/upload, tanda tangan digital, pembuktian (bukti servey, surat, kesediaan, dll.)

### 🔔 Notifikasi & Timeline
- **Jatuh Tempo**: Booking, PPJB, progres, AJB, pembayaran, review
- **Timeline Akad**: Pemantauan progres awal & akurat
- **Progress Dashboard**: Tingkatkan kontrol proses property
- **Kepatuhan**: Pastikan deadline & timeline terpenuhi

### 📊 Dashboard & Analitik
- **Widget Dashboard**: Pengeluaran tunai, tagihan, timeline, belanja klien
- **Analitik Per Realtors**: Metrik performa per cabang / per orang
- **Laporan Bulanan**: Koreksi potensi masalah, penjadwalan
- **Notifikasi**: Progress akad klien baru, alert progres, reminder follow-up

### 📅 Booking / Jadwal
- **List Properti**: Pilih berdasarkan kode, harga, tipe
- **Pemesanan**: Simpan data, bukti transaksi, cek riwayat pemesanan, booking kalender
- **Timeline Booking**: Booking, intinya, update, pembayaran
- **Offline First**: Sync otomatis setelah konektivitas
- **Calender View**: Booking, update, timeline, notification dengan event yang relevan

### 🧾 Absensi & Catatan Progres
- **Absensi Pemeriksaan Lapangan**: User verifikasi di lokasi
- **Catatan Progres**: Verifikasi progres, dokumen, catatan (foto/voice/video)
- **Laporan Bulanan**: PDF data progres per cabang
- **Catatan Kunjungan**: Pencatatan, data pengukur lahan

### 🔐 Autentikasi & Keamanan
- **Login / Daftar**: OTP via SMS, Email, Google, Facebook
- **Autentikasi Biometrik**: Face ID, Fingerprint
- **Keamanan Password**: Enkripsi dari metadata
- **Peran**: Owner, Admin Cabang, Sales, Notaris

## 🗂️ Struktur File

```
/android-tanah
├── app/src/main/java/com/example/androidtanah
│   ├── ui/login/login_screen.java
│   ├── ui/dashboard/dashboard_activity.java
│   ├── ui/katalog/katalog_aktivitas.java
│   ├── ui/akad/akad_aktivitas.java
│   ├── ui/progress/timeline_aktivitas.java
│   ├── ui/absensi/absensi_aktivitas.java
│   └── ui/laporan/laporan_aktivitas.java
├── app/src/main/res
│   ├── navigation
│   ├── layouts
│   └── values/strings.xml
├── data/database
│   ├── retrofit_client.java
│   ├── api/endpoints.java
│   └── local/keystore_app.db
├── build.gradle
└── gradle.properties
```

## ⚙️ Stack Teknologi

- **Android SDK**: Jetpack Compose + Activity/Fragment
- **Networking**: Retrofit, OkHttp
- **Database**: Room (SQLite + offline)
- **Security**: BiometricAuthenticator, AES256
- **Auth**: OTP via Firebase / Firebase Auth
- **UI**: Material Design, Dark Theme, Typography
- **Push Notification**: Firebase Cloud Messaging
- **Lokal Storage**: SharedPreferences, EncryptedSharedPreferences
- **Sync**: WorkManager (background sync)
- **Local Maps**: Google Maps API (lokasi) atau OpenStreetMap
- **Export**: MPDF / PDFBox (export report)
- **FontAwesome**: Icon dalam UI
- **Font**: Google Fonts (Inter / Open Sans)

## 🧪 State App

**In Progress:**
- Pemantauan progres awal proyek prootperti
- Implementasi autentikasi SMS OTP + biometrik
- Offline-first penyimpanan data lokal
- Timeline UI dan notifikasi jatuh tempo
- Integrasi WhatsApp untuk sync cepat

**Roadmap (minggu depan):**
- Complete Flutter Android release
- Implement payment gateway + QRIS
- Build isobar adlescent screen & agent display
- Test deploy to Play Store