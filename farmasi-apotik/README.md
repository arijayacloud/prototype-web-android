# Apotikku — Manajemen Obat & Farmasi

Aplikasi web dan Android untuk **apotik / manajemen farmasi**, dengan fokus pada:
- **Inventaris obat**: input, barcode generator, harga, stok.
- **Penjualan**: transaksi, cetak struk, update stok, piutang.
- **Laporan**: harian, mingguan, bulanan, tahunan.
- **Manajemen**: penyedia, pengeluaran, barcode otomatis.

## 🎯 Masala
Apotik menghadapi tantangan:
- **Stok hilang**: Pencatatan manual menyebabkan mismatched & kehilangan stok.
- **Penjualan tidak tercatat**: Struk manual, sulit lacak piutang.
- **Laporan tidak terstruktur**: Data end-of-day (EOD) manual, sulit analisis.
- **Barcode manual**: Label cetak manual, error input & alur kerja lambat.
- **Transparansi**: Pelanggan sulit lacak stok & harga.

## ✅ Solusi
**Apotikku** mengotomatisasi:
- **Input obat**: Formulir serbaguna + barcode otomatis per item.
- **Penjualan & Transaksi**: Kasir digital, cetak struk, update stok real-time.
- **Piutang & Kliring**: Catat piutang, reminder, notifikasi.
- **Laporan & Analitik**: dashboard EOD, filter cepat (hari, minggu, bulan, tahunan).
- **Manajemen Stok & Pembelian**: Tracking stok per unit, pembelian & pembelian ulang otomatis.
- **Mobile-First**: PWA (Progressive Web App) untuk Android & iOS, offline-first.

## 🌟 Fitur Utama

### 📱 Interface Kasir
- **Input Produk**: Form pencarian, barcode generation, capture harga.
- **Keranjang Belanja**: Tambah item, hitung otomatis total & harga satuan.
- **Pembayaran**: Tunai, transfer, qris, split payment, kembalian otomatis.
- **Cetak Struk**: Thermal printer, WhatsApp, atau PDF.
- **Piutang**: Input jumlah & jatuh tempo, reminder push.

### 📊 Dashboard Manajemen
- **Ringkasan EOD**: Overview harian: penjualan, stok, profit, piutang.
- **Filter Periode**: Hari, minggu, bulan, tahun.
- **Grafis**: Chart penjualan per hari, profit & stok menurun.
- **Pembuatan Laporan**: Export CSV & PDF.

### ⚙️ Fitur Teknis
- **Frontend**: React + Tailwind (desktop + mobile responsive).
- **Backend**: Node.js + Express + PostgreSQL (lokal/awan).
- **Barcode**: Code128, QR code generator.
- **Integrasi**: WhatsApp push untuk reminder & struk.
- **Offline-First**: IndexedDB lokal, sync background.
- **Keamanan**: Role-based access (Admin, Apoteker, Kasir).

## 🏗️ Struktur File

```
/farmasi-apotik
├── app/ (React Native + Expo + Tailwind)
│   ├── src/
│   │   ├── features/
│   │   │   ├── obat/ (input, barcode, edit)
│   │   │   ├── penjualan/ (kasir, keranjang, pembayaran)
│   │   │   ├── laporan/ (dashboard EOD, filter & export)
│   │   │   ├── piutang/ (form, reminder, kliring)
│   │   │   ├── provider/ (master data supplier)
│   │   │   └── pengeluaran/ (transaksi pembelian)
│   │   ├── core/
│   │   │   ├── api/ (REST endpoints)
│   │   │   ├── store/ (Redux + RTK)
│   │   │   └── utils/ (barcode, crypto, validators)
│   │   ├── hooks/ (custom hooks)
│   │   └── shared/ (komponen UI, tema)
│   ├── android/ (gradle, gradle.properties)
│   ├── ios/ (project.pbxproj)
│   └── package.json (react-native, expo)
├── web/ (Next.js 14 + TypeScript + Tailwind)
│   ├── pages/
│   │   ├── login.tsx, register.tsx, forgot.tsx
│   │   ├── dashboard/ (overview, grafik, filter period)
│   │   ├── obat/ (list, input, barcode)
│   │   ├── penjualan/ (kasir, keranjang)
│   │   ├── piutang/ (list, form)
│   │   └── export/ (pdf & csv)
│   ├── public/ (favicon, assets)
│   ├── next.config.js
│   └── tailwind.config.js
├── docs/ (API spec, diagram alir)
└── scripts/ (backup, sync, deploy)
```

## 🛠️ Tech Stack

- **Mobile**: React Native (Expo) + Tailwind CSS Native + React Navigation + Expo Secure Store
- **Web**: Next.js 14 (App Router) + TypeScript + Tailwind CSS + SWR + Headless UI
- **Backend**: Node.js (Express) + PostgreSQL (realtime sync) / MongoDB
- **Auth**: JWT + OAuth2 + Passkey + WebAuthn + Firebase Auth (fallback)
- **Barcode**: Code128 / QR code generator
- **Payments**: Midtrans + QRIS + transfer bank
- **Storage**: Cloudinary (upload), AWS S3 (backup), Supabase (Edge Functions)
- **Analytics**: Segment + Mixpanel
- **WhatsApp**: Cloud API + Business SDK
- **CI/CD**: GitHub Actions (build, test, deploy), Vercel (web), EAS (mobile)
- **Monitoring**: Sentry + LogRocket
- **FontAwesome**: Icon
- **Font**: Google Fonts (Inter)

## 🚀 State App

**In Progress:**
- Implementasi React Native + Expo (Android/iOS)
- Fitur input obat & barcode otomatis
- Alur kasir: keranjang, pembayaran, cetak struk
- Piutang & reminder WhatsApp
- Dashboard EOD & export PDF/CSV
- Role-based access (Admin, Apoteker, Kasir)

**Roadmap (minggu depan):**
- Selesaikan web dashboard (Next.js)
- Integrasi barcode API & cetak barcode PDF
- Analisis stok + purchase order otomatis
- Notifikasi stok habis & penurunan harga
- Uji A/B dashboard analitik & alur kasir
- Deploy ke Play Store & App Store
