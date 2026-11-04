# Tahfidz Pembinaan — Aplikasi Manajemen Setoran & Koreksi Tahfidz Al-Quran

Aplikasi web khusus untuk **program tahfidz** (pesantren, madrasah, atau komunitas internal) yang mengelola setoran hafalan dan koreksi otomatis oleh guru, dengan pencapaian siswa terukur per minggu & bulan, beserta rekap final bulanan.

## 🎯 Masalah
Pesantren / Tahfidz Center menghadapi tantangan:
- **Setoran tidak terdata**: Guru input hafalan siswa tidak terstruktur dan sulit dilacak progresnya.
- **Koreksi manual**: Proses manual rentan kesalahan, tidak ada penyimpanan bukti koreksi (tajwid, makhraj, kelancaran, hafalan, adab).
- **Keterlambatan rekapitulasi**: Data tidak dikonsolidasikan per minggu; rekap bulanan baru ada di akhir periode.
- **Kehilangan transparansi**: Orang tua kesulitan memantau perkembangan actual siswa.
- **Penumpukan data**: Data tidak terstruktur hingga membebani penyimpanan & analisis.

## ✅ Solusi
**Tahfidz Pembinaan** memberikan end-to-end:
- **Input Setoran & Koreksi**: Guru input setoran per siswa, lalu koreksi detil (tajwid, makhraj, lancar, hafalan, adab) langsung pada UI interaktif.
- **Auto Perhitungan**: Penetapan skor otomatis per kriteria (0–10) dan total skor mingguan/bulanan.
- **Dashboard Analitik**: Real-time progress per kelas, tingkat keberhasilan, heatmap kesalahaan, pencapaian per semester.
- **Laporan & Export**: PDF rekap per periode, Excel untuk gudang data, CSV untuk integrasi absensi sekolah.
- **Akses Multi-Role**: Guru (input koreksi), Kepala Sekolah (kontrol & approval), Wali Murid (riwayat progres).
- **Akses Offline-First**: Sinkronisasi lokal + API endpoint untuk upload data.

## 🌟 Fitur Utama

### 📱 Panel Guru
- **Input Setoran**: Pilih siswa, tanggal, juz/halaman, jenis setoran (tilawah, murottal, sabq, musytarak).
- **Koreksi Interaktif**: Klik/tap kotak cek untuk setiap item: Tajwid, Makhraj, Lancar, Hafalan, Adab. Catatan opsional.
- **Auto Skor**: Sistem menghitung total otomatis setelah koreksi selesai.
- **Riwayat Koreksi**: Melihat semua data input guru sebelumnya.
- **Filter & Pencarian**: Filter per siswa/kelas, pencarian cepat oleh nama.

### 🖥️ Panel Kepala Sekolah
- **Akses Kontrol**: Review & approve/reject setiap koreksi sebelum finalisasi.
- **Dashboard**: Grafis progres kelas, rata-rata skor, heatmap kesalahan, pencapaian per semester.
- **Export**: PDF per siswa, Excel per kelas, CSV sinkronisasi ke sistem absensi eksternal.
- **Jadwal Kegiatan**: Atur periode koreksi (mingguan, bulanan, semesteran).
- **Manajemen Kelas**: Buat/edit kelas, tambahkan siswa, duplicate periode.

### 👨‍👩‍👧‍👦 Panel Orang Tua (Mobile)
- **Login Siswa**: QR code scan atau nomor induk.
- **Dashboard**: Persentase pencapaian bulanan, rekap siklus mingguan.
- **Progress Chart**: Histogram skor per bulan, perbandingan dengan target sekolah.
- **Notifikasi**: Auto push via WhatsApp ketika guru approve koreksi baru.
- **Download PDF**: Unduh laporan bulanan satu kali sentuh.

### ⚙️ Fitur Teknis
- **Offline-First**: IndexedDB lokal + background sync API.
- **Auto Backup**: Backup harian ke remote (AWS S3/Cloudinary).
- **Responsive**: UI native Android + Web + iOS (React Native + Tailwind).
- **Integrasi WhatsApp**: Notifikasi otomatis ke wali murid.
- **Grafis Analitik**: Chart.js + real-time updates via WebSocket.
- **Role-Based Access**: JWT + OAuth2 (Google/Apple ID)
- **Keamanan**: Enkripsi AES-256 di penyimpanan, 2FA, rate-limiting per role.

## 🏗️ Struktur File

```
/tahfidz-pembinaan
├── app/ (React Native + Native Base)
│   ├── src/
│   │   ├── features/
│   │   │   ├── input-setoran/ (form, koreksi, preview)
│   │   │   ├── koreksi-uang/ (dashboard guru)
│   │   │   ├── review-approval/ (Kepala Sekolah)
│   │   │   ├── parent/ (Dashboard wali murid)
│   │   ├── core/
│   │   │   ├── auth/ (login, register, 2FA)
│   │   │   ├── api/ (REST endpoints)
│   │   │   ├── store/ (Redux + RTK)
│   │   │   └── utils/ (crypto, storage, validators)
│   │   ├── hooks/ (custom hooks)
│   │   └── shared/ (komponen UI, tema)
│   ├── android/ (gradle, gradle.properties)
│   ├── ios/ (project.pbxproj)
│   └── package.json (react-native, expo, dependencies)
├── web/ (Next.js 14 + TypeScript + Tailwind)
│   ├── pages/
│   │   ├── login.tsx, register.tsx, forgot.tsx
│   │   ├── guru/ (dashboard, form, list)
│   │   ├── kepala-sekolah/ (overview, export, kelas)
│   │   └── orangtua/ (login, progress, download)
│   ├── public/ (favicon, assets)
│   ├── next.config.js
│   └── tailwind.config.js
├── docs/ (API spec, diagram alir)
├── docs/monitoring/
│   ├── logs.json
│   └── performance.html
└── scripts/ (backup, sync, deploy)
```

## 🛠️ Tech Stack

- **Mobile**: React Native (Expo) + Tailwind CSS Native + Native Base + React Navigation
- **Web**: Next.js 14 (App Router) + TypeScript + Tailwind CSS + Headless UI + SWR
- **Backend**: Node.js (Express) + MongoDB (realtime sync) / PostgreSQL + Redis
- **Auth**: JWT + OAuth2 + Passkey + WebAuthn + Firebase Auth (fallback)
- **Payments**: Midtrans (untuk upgrade premium), QRIS, transfer bank
- **Storage**: AWS S3 (backup), Cloudinary (upload gambar koreksi), Supabase (Edge Functions)
- **Analytics**: Segment + Mixpanel + custom event tracking
- **Notifications**: Firebase Cloud Messaging + WhatsApp Cloud API
- **CI/CD**: GitHub Actions (build, test, deploy), Vercel (web), EAS (mobile)
- **Monitoring**: Sentry + LogRocket + Custom error tracking
- **FontAwesome**: Icon dalam UI
- **Font**: Google Fonts (Open Sans / Lato)

## 🚀 State App

**In Progress:**
- Implementasi React Native + Expo (Android/iOS)
- Fitur koreksi interaktif & auto-perhitungan
- Auto backup ke cloud & indexedDB
- Panel admin & kepala sekolah (real-time)
- Export PDF/Excel
- Integrasi WhatsApp (notifikasi)

**Roadmap (minggu depan):**
- Selesaikan Web dashboard (Next.js)
- Integrasi Google Maps (kelas & siswa) & QR code scan
- Implementasi pembayaran & manajemen kuota siswa
- Uji A/B fitur analytics & UI/UX
- Deploy ke Play Store & App Store