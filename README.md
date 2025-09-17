# CRUD_data_karyawan
1. Deskripsi
   Simple Phyton-based application untuk mengelola data karyawan, yang terdapat fitur CRUD (Create, Read, Update, dan Delete)      serta filter data berdasarkan kategori tertentu. Data karyawan disimpan sementara di dalam program.
    
2. Fitur
   2.1. Menampilkan Data Karyawan (Read)
         - Melihat seluruh data karyawan dalam bentuk tabel
         - Filter data berdasarkan Divisi, Status Karyawan, atau Domisili
   2.2. Menambah Data Karyawan (Create)
         - Input data karyawan baru dengan beberapa validasi
         - Nomor Induk harus unik dan berformat ID-XXX (XXX = angka 3 digit)
         - Gaji harus diisi dengan angka
         - Email harus valid (must contain '@') dan unik
   2.3. Update Data Karyawan (Update)
         - Memperbaharui sebagian atau seluruh data karyawan dengan validasi yang sama dengan tambah data,
         - Konfirmasi sebelum diupdate
   2.4. Hapus Data Karyawan (Delete)
         - Menghapus data karyawan berdasarkan Nomor Induk dengan konfirmasi sebelum dieksekusi.
   
3. Struktur Data
    3.1. Data karyawan disimpan dalam list of dictionary, contoh:
       {
        'Nomor Induk': 'ID-001',
        'Nama Pegawai': 'Alisson Becker',
        'Divisi': 'HRD',
        'Posisi': 'Kepala Divisi',
        'Status Karyawan': 'Tetap',
        'Gaji Pokok': 18000000,
        'Email': 'alisson.becker@perusahaan.com',
        'Domisili': 'Tangerang'
      }

4. Stakeholder
   Staff HR atau Admin perusahaan sebagai pengguna utama aplikasi
   
5. Limitation
   - Data bersifat sementara dan belum disimpan dalam file. Jika program ditutup, data akan hilang.
   - Bisa diupgrade dengan menyimpan data ke file seperti CSV, JSON, dll.

6. Tampilan Menu Awal Aplikasi
     === APLIKASI DATA KARYAWAN ===
  1. Tampilkan Data Karyawan
  2. Tambah Data Karyawan
  3. Update Data Karyawan
  4. Hapus Data Karyawan
  5. Keluar
