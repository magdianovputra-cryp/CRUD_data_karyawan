# Flowcharts

Folder ini menyimpan sumber diagram Mermaid (.mmd) untuk alur program CRUD Data Karyawan.

## Struktur
- `docs/flowcharts/*.mmd` — sumber diagram Mermaid.
- `docs/images/png/*.png` — hasil render PNG (dibuat otomatis oleh GitHub Actions).
- `docs/images/svg/*.svg` — hasil render SVG (dibuat otomatis oleh GitHub Actions).

## Cara mengubah diagram
1. Edit file `.mmd` yang relevan di `docs/flowcharts/`.
2. Commit dan push perubahan ke branch Anda.
3. GitHub Actions akan otomatis merender ulang PNG/SVG dan commit hasilnya ke branch yang sama.

## Menjalankan ulang render manual
- Buka tab Actions > pilih workflow "Render Mermaid diagrams" > Run workflow.

## Catatan
- Workflow membutuhkan izin menulis (contents: write) untuk bisa commit hasil render. Izin ini sudah dideklarasikan di file workflow.
- Semua file tetap privat karena repo ini privat.