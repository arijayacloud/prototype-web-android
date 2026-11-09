# SMART (Sistem Manajemen Data)

Aplikasi manajemen data terintegrasi untuk toko atau bisnis dengan fitur lengkap:
- **Login / Daftar** — autentikasi aman (JWT + OAuth2)
- **Katalog Produk / Jasa** — CRUD lengkap, barcode, SKU, harga, kategori
- **Chat ke Admin (WA)** — WhatsApp Business API terintegrasi, real-time messaging
- **Notifikasi** — push notification, email, in-app, dan desktop
- **Laporan & Grafik** — dashboard analitik, grafik penjualan, KPI, export CSV/PDF
- **Kelola Stok** — manajemen stok multi-g gudang, reorder point, tracking expiration

## 🎯 Masala
Bisnis menghadapi tantangan:
- **Data terpisah**: Excel manual, silo informasi
- **Pelacakan stok**: Stock opname manual, error input
- **Pelanggan terputus**: Chat terpisah, tidak ada notifikasi
- **Laporan tidak real-time**: Bulanan, tidak ada insight cepat
- **Error manusia**: Input data manual, sulit audit trail

## ✅ Solusi
**SMART** menyatukan semuanya:
- **Autentikasi centralized** (multi-pass + MFA)
- **Katalog unified** (produk + jasa, barcode + SKU)
- **Chat terintegrasi** (WhatsApp + dashboard admin)
- **Notifikasi real-time** (push, email, in-app)
- **Dashboard analitik** (grafik waktu nyata, export)
- **Manajemen stok cerdas** (expire alerts, multi-g warehouse, reorder)

## 🌟 Fitur Utama

### 🔐 Sistem Autentikasi
- Login dengan email, Google, GitHub, WhatsApp
- Multi-role (Admin, Staff, User)
- Enkripsi JWT + Passkey + WebAuthn
- MFA dan password policy

### 📦 Katalog Produk / Jasa
- Input, edit, delete (CRUD)
- Generate barcode & QR code
- SKU, SKU kategori, cost & selling price
- Batch management & serial tracking
- Multi-image uploads + PDF dokumentasi

### 📧 Chat & Notifikasi
- Real-time chat with admin via WhatsApp
- In-app messaging dashboard
- Notifikasi push (web, mobile)
- Email notifikasi (faktur, stok habis)
- Desktop notification (desktop native)

### 📊 Laporan & Analitik
- Dashboard overview (penjualan, stok, pelanggan)
- Filter dinamis (periode, produk, staff)
- Grafik: penjualan per hari/minggu/bulan
- KPI: ROI, omzet, stok turnover
- Export: CSV, PDF, Excel

### ⚙️ Manajemen Stok
- Multi-g warehouse
- Auto reorder point
- Stock opname scan
- Expiration alerts
- Transfer antar gudang

## 🏗️ Struktur File

```
/prototype-web-android/smart/
├── app/ (React + TypeScript + Tailwind)
│   ├── src/
│   │   ├── auth/ (login, register, reset, mfa)
│   │   ├── katalog/ (produk, jasa, barcode, sku)
│   │   ├── stok/ (warehouse, quantity, transfer, opname)
│   │   ├── chat/ (whatsapp, real-time, admin panel)
│   │   ├── notif/ (push, email, in-app)
│   │   ├── laporan/ (dashboard, grafik, export)
│   │   ├── setting/ (profile, role, theme)
│   │   └── api/ (REST endpoints)
│   ├── components/ (shared UI)
│   ├── hooks/ (custom hooks)
│   └── utils/ (barcode, crypto, validators)
├── public/ (favicon, assets)
├── package.json (deps, scripts)
├── next.config.js
└── tailwind.config.js
```

## 🛠️ Tech Stack

- **Frontend**: React 18 + TypeScript + Tailwind CSS + Zustand + SWR
- **Auth**: Clerk + OAuth2 + Passkey + WebAuthn
- **Backend**: Node.js (Express) + PostgreSQL + Redis + WebSocket
- **Barcode**: QR code generator, Code128, EAN-13
- **Chat**: WhatsApp Business API + Socket.IO
- **Notifikasi**: Pusher + EmailJS + Web Push (Web Push API)
- **Grafik**: Chart.js + ApexCharts
- **CI/CD**: GitHub Actions + Vercel (web), EAS (mobile)
- **Deployment**: Vercel (web), EAS (Android/iOS)
- **Database**: PostgreSQL + Supabase (Edge Functions)
- **Storage**: Cloudinary (upload), AWS S3 (backup)
- **Monitoring**: Sentry + LogRocket
- **FontAwesome**: Icon
- **Font**: Google Fonts (Inter)

## 🚀 State App

**In Progress:**
- Autentikasi (login/register/mfa)
- Katalog produk & barcode generator
- Manajemen stok multi-g warehouse
- Chat WhatsApp + dashboard admin
- Notifikasi real-time
- Dashboard laporan & grafik

**Roadmap (minggu depan):**
- Web app deployment (Next.js)
- Mobile app (React Native + Expo)
- Mobile push notifications
- Advanced analitik (prediksi stok)
- Payment gateway (Midtrans + QRIS)
- Multi-language support
- API untuk integrasi (POS, accounting)
