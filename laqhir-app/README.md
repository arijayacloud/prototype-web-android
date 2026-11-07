# Aplikasi Laqhir

Aplikasi web single-page interaktif untuk metode Laqhir (menebalkan, mengurut, membaca, mengulang) dengan gamifikasi, lock system, dan dasbor monitoring.

## Fitur

- **Sesi Laqhir – Lauh**
  - Menebalkan (menebalkan) dengan sentuhan jari di layar.
  - Drag & Drop puzzle untuk menyusun ulang ayat acak.
  - Validasi garis, bantu ulangi secara halus jika keluar jalur.

- **Sesi Qiroah – Membaca Terpandu**
  - Karaoke highlight: audio diputar, teks menyala kata per kata.
  - Tajwid pop-up: ketuk kata untuk animasi singkat.

- **Sesi Takrir – Mengulang dengan Gamifikasi**
  - Pohon progress visual (tunas → daun → bunga).
  - Rekam & cek mandiri: record audio -> diputar sendiri.
  - Progress tersimpan secara lokal (localStorage).

- **Dasbor Monitoring Guru**
  - Lock system: tidak bisa Takrir sebelum Lauh & Qiroah.
  - Rapor real-time: statistik per siswa, progress per tahap.

## Alur Kerja

1. Load → verifikasi storage ID per anak (qris code? default), inisialisasi progres.
2. Lauh → render canvas + watermark; touch event validasi -> localStorage.
3. Qiroah → audio URL dipanggil; audio diputar; teks highlight otomatis; pop-up on tap.
4. Takrir → record audio via MediaRecorder → simpan -> tampilkan snapshot + grow pohon.
5. Lock system cek -> blok Tahap Takrir.

## Browser Kompatibilitas

- Bekerja di smartphone/Android (touch, gesture, audio). Direkomendasikan Chrome/Edge.

## Instruksi Penggunaan

- Buka `index.html` (atau `https://arijayacloud.github.io/prototype-web-android/laqhir-app/`).
- Ikuti alur (Lauh → Qiroah → Takrir).
- Guru dapat membuka `dashboard.html` untuk statistik.

## Bagaimana Kerjanya

- **Canvas tracing**: HTML5 canvas dengan gambar ayat; event `touchstart` → koordinat → gambar garis tebal -> validasi akurasi via tolerance Euclidean sederhana.
- **Drag & Drop**: potongan kata HTML (`div.draggable`) -> `position: absolute`; `ontouchstart` -> `mousemove` analog; drop validasi posisi.
- **Karaoke**: audio (`audio` tag) dengan `ontimeupdate` -> synchronized highlight span; `pointerdown` on span -> tajwid animasi (canvas konfeti).
- **Audio record**: `navigator.mediaDevices.getUserMedia({audio:true})` -> MediaRecorder -> simpan ke IndexedDB (blob) -> putar kembali.
- **Progress tree**: hitung episode -> peta -> SVG tree grow di dashboard.
- **Lock system**: field `progress.locked` di localStorage; cek sebelum akses Tahap Takrir.
- **Dashboard**: simple HTML + JS membaca localStorage per session (bisa disaring by childId) -> hitung total aksi -> tampilkan list.

## Catatan Teknis

- Semua state disimpankan secara lokal (no server).
- Audio recording disimpan di IndexedDB; bisa di-playback.
- Visual efek minimal: canvas, SVG, pure JS.
- Mendukung offline: data tersimpan di browser.
- Git push di branch `laqhir-app`.

## Test & Debugging

- Buka devtools → console log event (misal: `trace`).
- Jika audio record gagal, periksa izin mikrofon browser.
- Trace Lauh: pastikan tolerance and tolerance mapping.

## Lisensi

Open source, bebas dimodifikasi.