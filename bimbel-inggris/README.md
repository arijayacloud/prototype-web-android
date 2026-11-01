# Briton & Oxford Academy — Prototype Sistem Manajemen Bimbel Bahasa Inggris Multi-Cabang

Aplikasi manajemen dan portal bimbingan belajar Bahasa Inggris multi-cabang terintegrasi dengan pembedaan hak akses berbasis peran (Role-Based Access Control): **Owner, Admin Pusat, Admin Cabang, Tutor, dan Orang Tua / Siswa**.

## Hak Akses & Fitur Khusus Peran

1. **Owner (Eksekutif & Analitik Bisnis):**
   - KPI Utama: Total seluruh siswa aktif lintas cabang, total pemasukan SPP, tagihan belum dibayar (tunggakan).
   - Tutor Metrics: Jumlah tutor aktif, tingkat kehadiran tutor, dan total pengeluaran honor/payroll.
   - Analitik Performa: Grafik pertumbuhan siswa baru vs siswa keluar, rekap siswa per cabang, serta performa kelas.

2. **Admin Pusat (Super Admin):**
   - Mengelola data master seluruh cabang (Pusat, Selatan, Surabaya, Bandung).
   - Manajemen siswa, tutor, dan kelas lintas cabang.
   - Pengaturan paket kursus & katalog modul/buku (stok).
   - Manajemen billing/invoice SPP otomatis & broadcast pengumuman resmi ke seluruh cabang.

3. **Admin Cabang:**
   - Akses terfilter khusus cabang yang dipimpin (misal: Cabang Jakarta Selatan).
   - Verifikasi kehadiran siswa/tutor cabang, penagihan SPP siswa cabang via WhatsApp, dan koordinasi jadwal lokal.

4. **Tutor (Instruktur / Pengajar):**
   - Check-in/Check-out absensi mandiri dengan jam masuk & status keterlambatan.
   - Jadwal mengajar harian & mingguan.
   - Input materi pertemuan harian & upload learning progress (nilai tugas, kuis, dan radar perkembangan speaking/pronunciation).

5. **Orang Tua / Siswa (Student & Parent Portal):**
   - Bayar SPP online (QRIS / Transfer Bank) dengan unduh kuitansi resmi.
   - Pantau rapor perkembangan belajar anak (materi pertemuan terakhir, speaking progress score).
   - Pantau persentase kehadiran dan perkiraan tanggal wisuda / kelulusan level (Graduation Forecast).
   - Notifikasi pengumuman libur, surat edaran, dan tombol direct chat WhatsApp ke Admin/Tutor.

## Cara Mencoba

Buka `index.html`, lalu klik salah satu akun demo di halaman login (password semua akun: `demo123`). Data tersimpan di `localStorage` dan bisa direset dari halaman login.

Tanggal demo dikunci pada Senin, 2 Nov 2026 supaya jadwal, tunggakan, dan payroll konsisten.
