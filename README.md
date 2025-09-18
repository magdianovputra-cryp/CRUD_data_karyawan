# CRUD Data Karyawan

## Deskripsi
Simple Phyton-based application untuk mengelola data karyawan, yang terdapat fitur CRUD (Create, Read, Update, dan Delete) serta filter data berdasarkan kategori tertentu. Data karyawan disimpan sementara di dalam program.

---

## Fitur
### Menampilkan Data Karyawan (Read)
- Menampilkan seluruh data karyawan dalam bentuk tabel
- Filter data berdasarkan Divisi, Status Karyawan, atau Domisili

### Menambah Data Karyawan (Create)
- Menambah data karyawan baru dengan validasi:
  - Nomor Induk unik dengan format `ID-XXX` (XXX = angka 3 digit)
  - Gaji harus berupa angka
  - Email harus valid (mengandung `@`) dan unik

### Update Data Karyawan (Update)
- Memperbarui sebagian atau seluruh data karyawan dengan validasi yang sama seperti saat menambah data
- Konfirmasi sebelum data disimpan

### Hapus Data Karyawan (Delete)
- Menghapus data karyawan berdasarkan Nomor Induk
- Konfirmasi sebelum data benar-benar dihapus

---

## Struktur Data
Data karyawan disimpan dalam list of dictionary. Contoh:

```python
[
{
  "Nomor Induk": "ID-001",
  "Nama Pegawai": "Alisson Becker",
  "Divisi": "HRD",
  "Posisi": "Kepala Divisi",
  "Status Karyawan": "Tetap",
  "Gaji Pokok": 18000000,
  "Email": "alisson.becker@perusahaan.com",
  "Domisili": "Tangerang"
}
]

```
## Stakeholder
Staff HR atau Admin perusahaan sebagai pengguna utama aplikasi

## Limitation
- Data bersifat sementara dan belum disimpan dalam file. Jika program ditutup, data akan hilang.
- Bisa diupgrade dengan menyimpan data ke file seperti CSV, JSON, dll.

## Tampilan Menu Awal
```python
=== APLIKASI DATA KARYAWAN ===
1. Tampilkan Data Karyawan
2. Tambah Data Karyawan
3. Update Data Karyawan
4. Hapus Data Karyawan
5. Keluar
```
