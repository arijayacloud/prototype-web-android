# Desain Elegan Rumah Kekinian — konsep 8 × 18 m

Paket ini memuat denah konseptual dua lantai, model 3D yang dapat dibuka di Blender, halaman web untuk memutar model, dan presentasi PowerPoint.

## Buka halaman web

Jalankan `run-viewer.ps1` dari PowerShell, lalu buka <http://127.0.0.1:8080>.
Model GLB dimuat melalui server lokal karena browser membatasi pembacaan file 3D langsung dari `file://`. Internet diperlukan untuk memuat pustaka Three.js dari CDN.

Di halaman tersedia tiga tampilan:

- **Rumah utuh**: kedua lantai dan atap.
- **Lantai 1**: denah dan model lantai 1 dengan bidang atas disembunyikan.
- **Lantai 2**: model lantai atas secara terpisah.

Seret model untuk memutar. Roda mouse atau cubit layar untuk zoom. Tombol tengah / dua jari menggeser model.

## File utama

- `index.html` — halaman model 3D dan denah.
- `plan_data.json` — ukuran tapak, ruang, dan perlengkapan bersama yang menjadi acuan denah dan model.
- `assets/floor-1.svg`, `assets/floor-2.svg` — denah vektor.
- `assets/house.glb`, `assets/floor-1.glb`, `assets/floor-2.glb` — model web GLB.
- `assets/house.blend` — scene Blender yang dapat diedit. Koleksi bernama `Floor_1`, `Floor_2`, `Roof`, `Furniture`, dan `Site`.
- `assets/renders/` — render model untuk halaman web dan presentasi.
- `output/presentasi-desain-elegan-8x18.pptx` — presentasi 6 slide.
- `blender/build_house.py` — pembangun scene untuk dijalankan dari Blender atau Blender MCP.
- `scripts/generate_plans.py` — pembuat ulang gambar denah SVG.
- `scripts/build_presentation.mjs` — sumber presentasi berbasis Artifact Tool.

## Membuat ulang berkas

Dari folder ini:

```powershell
python scripts/generate_plans.py
python scripts/validate_assets.py --all
```

Untuk model Blender, jalankan `blender/build_house.py` dari Blender Python Console atau melalui MCP yang terhubung ke Blender. Script menyimpan `house.blend` dan render ke `assets/`; ekspor tiga GLB terpisah melalui menu **File → Export → glTF 2.0** dengan pilihan object sesuai koleksi `Floor_1`, `Floor_2`, `Roof`, dan furnitur.

## Catatan desain

Denah lantai 1 merupakan interpretasi dari sketsa yang diberikan. Tulisan sebagian ruang servis pada sketsa kurang jelas. Denah lantai 2 mengikuti daftar ruang yang diberikan dan merupakan susunan awal untuk mengakomodasi kebutuhan tersebut. Posisi, dimensi ruang, bukaan, struktur, dan jalur instalasi belum diverifikasi di lokasi. Berkas ini adalah studi konsep, bukan gambar kerja konstruksi.
