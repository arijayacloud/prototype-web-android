# NihonGo! — Prototype Aplikasi Latihan Soal Bahasa Jepang (JLPT N5 - N1)

Aplikasi latihan soal interaktif Bahasa Jepang berbasis standar JLPT (Japanese-Language Proficiency Test) dengan 5 level kesulitan lengkap (N5 hingga N1) dan 4 kategori tes per level, dilengkapi fitur penyimpanan histori nilai dan analisis kelemahan siswa.

## Fitur Utama

1. **5 Tingkat Kesulitan Lengkap (JLPT N5 s/d N1):**
   - **N5 (Dasar Pemula):** Kosakata harian, partikel dasar (は, が, を, に, で), kanji dasar.
   - **N4 (Pra-Menengah):** Pola kalimat dasar (て-form, keharusan, pengandaian), kanji ~300.
   - **N3 (Menengah):** Transisi bahasa formal & percakapan, partikel ganda, pola kalimat ~150.
   - **N2 (Menengah Atas):** Bahasa bisnis & berita, pola kalimat idiomatis, dokkai/soal cerita analitis.
   - **N1 (Tingkat Mahir):** Bahasa resmi, surat kabar, sastra, kanji rumit ~2000, ekspresi akademik.

2. **4 Kategori Soal di Setiap Level:**
   - **Latihan Kanji (漢字):** Cara baca (Onyomi/Kunyomi) dan arti kanji dalam kalimat.
   - **Latihan Partikel (助詞):** Pemilihan partikel yang tepat sesuai konteks kalimat.
   - **Latihan Pola Kalimat / Tata Bahasa (文法):** Struktur tata bahasa khas per level JLPT.
   - **Soal Cerita / Membaca (読解 Dokkai):** Paragraf pendek/sedang dengan pertanyaan pemahaman bacaan.

3. **Interaktif & Penilaian Real-Time:**
   - Soal pilihan ganda 4 opsi dengan penjelasan jawaban (furigana & arti bahasa Indonesia).
   - Pengatur waktu latihan (timer kuis).
   - Skor otomatis di akhir sesi dengan rincian benar/salah.

4. **Penyimpanan Histori Siswa (Persistent via localStorage):**
   - Catatan setiap sesi latihan (tanggal, level N, kategori, skor/persentase, durasi).
   - Statistik kumulatif: Total latihan, rata-rata skor, kategori terkuat dan kategori yang perlu ditingkatkan.
   - Tombol reset/ekspor riwayat jika siswa ingin mengulang dari awal.
