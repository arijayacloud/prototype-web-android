# Majelis Muhyin Nufuus — Aplikasi Manajemen Komunitas Islami

Aplikasi web & Android untuk **organisasi majelis Islam** (PII — Persatuan Islampos), menghubungkan Jemaah (anggota) dan Pengurus (admin) dalam satu ekosistem terpadu. Desain hijau berdasarkan gambar yang disediakan, fitur streaming, buku digital, donasi, manajemen anggota, dan dashboard analitik.

## 🎯 Masalah
Komunitas majelis menghadapi tantangan:
- **Jadwal & lokasi tidak terpantau**: Anggota bingung mencari waktu/kegiatan majelis terdekat
- **Konten dakwah terpencar**: Tausiyah di berbagai platform (YouTube, Facebook, TikTok)
- **Buku & panduan offline hilang**: Ribuan kitab penting & panduan praktik tidak tersedia digital
- **Donasi tidak transparan**: Celengan masjid tidak terdata & sulit dilacak
- **Manajemen anggota tidak efisien**: Data anggota tersebar di WhatsApp/spreadsheets

## ✅ Solusi
Majelis Muhyin Nufuus memberikan **lengkap**:
- **Panel Jemaah**: Kalender terintegrasi Google Maps, streaming konten dakwah, buku digital library, pendaftaran anggota, donasi digital
- **Panel Pengurus**: Dashboard analitik, manajemen anggota & QR code, broadcast massal, POS (Toko Majelis)
- **Cross-platform**: Web, Android, iOS — sinkronisasi real-time
- **Keamanan**: Role-based access (Jemaah vs Pengurus), QR check-in
- **Fitur**: Live streaming, donation manager, digital library, kalender interaktif

## 🌟 Fitur Utama

### 📱 Panel Jemaah (Mobile-First)

#### 1. Kalender & Lokasi
- **Google Maps Integration**: Daftar jadwal majelis per daerah, map interaktif
- **Notifikasi Jadwal**: Pengingat otomatis H-1 & H-1.5 untuk setiap kegiatan
- **Filter Lokasi**: Cari berdasarkan kota/provinsi/kategori kegiatan

#### 2. Streaming & Konten Dakwah
- **Live Streaming**: Siaran langsung kajian rutin, khotbah Jumat
- **Video Library**: Terintegrasi YouTube, Facebook, TikTok
- **Categories**: Kajian Rutin, Tarawih, Quran Akhad, Hafidz, dan lainnya

#### 3. Kitab Digital
- **Digital Library**: Ribuan judul buku Islami (Fiqh, Akidah, Tafsir, Sirah)
- **Search & Filter**: Akses berdasarkan tema, penulis, kategori
- **Offline Access**: Download buku untuk dibaca tanpa internet

#### 4. Pendaftaran Anggota
- **Online Form**: Nama, email, telepon, wilayah
- **Digital Membership Card**: QR code otomatis setelah pendaftaran
- **Verification**: Email/SMS OTP, login biometrik

#### 5. Celengan Digital
- **Donation Platform**: QRIS, e-wallet, transfer bank
- **Kategori Donasi**: Infak, Zakat, Donasi Khusus, Sedekah
- **Tracking**: Riwayat donasi, bukti transfer, laporan pajak

#### 6. Profil & Struktur
- **Struktur Organisasi**: Vizualisasi hierarki (Pusat, Wilayah, Cabang, Ranting)
- **Profil Pengurus**: Bio, kontak, sejarah jabatan

### 🖥️ Panel Pengurus (Web Admin)

#### 1. Dashboard Analitik
- **Statistik**: Jumlah anggota, pertumbuhan donasi, kegiatan bulanan
- **Visual Charts**: Grafik donasi, pertumbuhan anggota, kalender kegiatan
- **Key Metrics**: Target vs realisasi, performa daerah

#### 2. Manajemen Anggota
- **Database**: CRUD anggota, upload massal
- **QR Code Check-in**: Absensi otomatis via scan QR
- **Regional Management**: Kelola cabang/wilayah
- **Export Data**: CSV/Excel, backup harian

#### 3. Broadcast & Notifikasi
- **Mass Message**: Kirim ke seluruh anggota atau kelompok
- **Template**: Predefined message, personalization tags
- **Schedule**: Kirim nanti, target segmentasi

#### 4. Toko Majelis (POS)
- **Inventory**: Jual buku, minyak wangi, dupa, tasbih
- **Payment**: QRIS, cash, transfer bank
- **Laporan Transaksi**: Harian, bulanan, per produk
- **Kupon & Diskon**: Kupon global, periode, jumlah

## 🏗️ Struktur File

```
/majelis-muhyin
├── app/src/main/java/com/example/majelismuhyin
│   ├── ui/jemaah/
│   │   ├── beranda (home)
│   │   ├── jadwal (calendar & maps)
│   │   ├── streaming (live & video)
│   │   ├── buku (digital library)
│   │   ├── daftar (registration)
│   │   ├── donasi (donation)
│   │   └── profil (profile)
│   ├── ui/pengurus/
│   │   ├── dashboard (analytics)
│   │   ├── anggota (member management)
│   │   ├── broadcast (notifications)
│   │   ├── toko (POS & inventory)
│   │   └── laporan (reports)
│   ├── auth/ (login, register, OTP)
│   ├── data/
│   │   ├── database (Room)
│   │   ├── api/ (Retrofit)
│   │   └── local (SecureStorage)
│   └── utils/ (QR scanner, maps, upload)
├── build.gradle
└── gradle.properties
```

## 🛠️ Stack Teknologi

- **Frontend**: Jetpack Compose (Android), Tailwind CSS (Web), Flutter (iOS)
- **Backend**: Spring Boot (REST API), Firebase Auth, Cloudinary (storage)
- **Database**: Room (Android), PostgreSQL (Web), Supabase (cross-platform sync)
- **Security**: JWT + OAuth2, Biometrics (Face ID/Fingerprint)
- **Maps**: Google Maps SDK (Android/iOS), Leaflet (Web)
- **Payments**: Midtrans (QRIS), Bank transfer integration
- **Streaming**: YouTube API, Facebook Graph, TikTok API
- **Push Notification**: Firebase Cloud Messaging
- **Export**: Apache POI (Excel), MPDF (PDF)
- **FontAwesome**: Icon dalam UI
- **Font**: Google Fonts (Open Sans / Lato)

## 🧪 State App

**In Progress:**
- Implementasi Flutter Android release
- Autentikasi SMS OTP + biometrik
- Offline-first data penyimpanan + sync cloud
- Integrasi Google Maps + kalender interaktif
- Digital library + streaming API integration
- POS & donation flow dengan QRIS

**Roadmap (minggu depan):**
- Complete Web-responsive UI
- Implement payment gateway + QRIS
- Build isobar admin dashboard & analytics
- Test deploy to Play Store & App Store