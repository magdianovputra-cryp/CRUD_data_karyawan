from tabulate import tabulate

karyawan = [
    {
        'Nomor Induk' : 'ID-001', 
        'Nama Pegawai' : 'Alisson Becker', 
        'Divisi' : 'HRD', 
        'Posisi' : 'Kepala Divisi', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '18000000',
        'Email' : 'alisson.becker@perusahaan.com',
        'Domisili' : 'Tangerang'
    },
    {
        'Nomor Induk' : 'ID-002', 
        'Nama Pegawai' : 'Joe Gomez', 
        'Divisi' : 'HRD', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '7000000',
        'Email' : 'joe.gomez@perusahaan.com',
        'Domisili' : 'Depok'
    },
    {
        'Nomor Induk' : 'ID-003', 
        'Nama Pegawai' : 'Wataru Endo', 
        'Divisi' : 'HRD', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Intern',
        'Gaji Pokok' : '3000000',
        'Email' : 'wataru.endo@perusahaan.com',
        'Domisili' : 'Bekasi'
    },
    {
        'Nomor Induk' : 'ID-004', 
        'Nama Pegawai' : 'Van Dijk', 
        'Divisi' : 'Operasional', 
        'Posisi' : 'Kepala Divisi', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '18000000',
        'Email' : 'van.dijk@perusahaan.com',
        'Domisili' : 'Jakarta'
    },
    {
        'Nomor Induk' : 'ID-005', 
        'Nama Pegawai' : 'Ibrahima Konate', 
        'Divisi' : 'Operasional', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '6900000',
        'Email' : 'ibrahima.konate@perusahaan.com',
        'Domisili' : 'Bogor'
    },
    {
        'Nomor Induk' : 'ID-006', 
        'Nama Pegawai' : 'Milos Kerkez', 
        'Divisi' : 'Operasional', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Intern',
        'Gaji Pokok' : '3200000',
        'Email' : 'milos.kerkez@perusahaan.com',
        'Domisili' : 'Bekasi'
    },
    {
        'Nomor Induk' : 'ID-007', 
        'Nama Pegawai' : 'Florian Wirtz', 
        'Divisi' : 'Marketing', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Intern',
        'Gaji Pokok' : '3200000',
        'Email' : 'flo.wirtz@perusahaan.com',
        'Domisili' : 'Bogor'
    },
    {
        'Nomor Induk' : 'ID-008', 
        'Nama Pegawai' : 'Dominik Szoboszlai', 
        'Divisi' : 'Marketing', 
        'Posisi' : 'Kepala Divisi', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '16900000',
        'Email' : 'dom.szoboszlai@perusahaan.com',
        'Domisili' : 'Tangerang'
    },
    {
        'Nomor Induk' : 'ID-009', 
        'Nama Pegawai' : 'Alexander Isak', 
        'Divisi' : 'Marketing', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '7200000',
        'Email' : 'alex.isak@perusahaan.com',
        'Domisili' : 'Jakarta'
    },
    {
        'Nomor Induk' : 'ID-010', 
        'Nama Pegawai' : 'Alexis MacAllister', 
        'Divisi' : 'Finance', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '7200000',
        'Email' : 'alex.macca@perusahaan.com',
        'Domisili' : 'Bekasi'
    },
    {
        'Nomor Induk' : 'ID-011', 
        'Nama Pegawai' : 'Mohammed Salah', 
        'Divisi' : 'Finance', 
        'Posisi' : 'Kepala Divisi', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '19000000',
        'Email' : 'mo.salah@perusahaan.com',
        'Domisili' : 'Depok'
    },
    {
        'Nomor Induk' : 'ID-012', 
        'Nama Pegawai' : 'Conor Bradley', 
        'Divisi' : 'Finance', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Intern',
        'Gaji Pokok' : '3200000',
        'Email' : 'conor.bradley@perusahaan.com',
        'Domisili' : 'Jakarta'
    },
    {
        'Nomor Induk' : 'ID-013', 
        'Nama Pegawai' : 'Curtis Jones', 
        'Divisi' : 'IT', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Intern',
        'Gaji Pokok' : '3200000',
        'Email' : 'curtis.jones@perusahaan.com',
        'Domisili' : 'Jakarta'
    },
    {
        'Nomor Induk' : 'ID-014', 
        'Nama Pegawai' : 'Federico Chiesa', 
        'Divisi' : 'IT', 
        'Posisi' : 'Kepala Divisi', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '17000000',
        'Email' : 'fede.chiesa@perusahaan.com',
        'Domisili' : 'Bogor'
    },
    {
        'Nomor Induk' : 'ID-015', 
        'Nama Pegawai' : 'Giovanni Leoni', 
        'Divisi' : 'IT', 
        'Posisi' : 'Staff', 
        'Status Karyawan' : 'Tetap',
        'Gaji Pokok' : '7000000',
        'Email' : 'gio.leonni@perusahaan.com',
        'Domisili' : 'Depok'
    },
]

def data_karyawan():
    if not karyawan:
        print("Data karyawan kosong.")
        return
    
        # Ubah list of dict jadi list of list
    tabel = []
    for index, item in enumerate(karyawan, start=1):
        tabel.append([
            index,
            item['Nomor Induk'],
            item['Nama Pegawai'],
            item['Divisi'],
            item['Posisi'],
            item['Status Karyawan'],
            item['Gaji Pokok'],
            item['Email'],
            item['Domisili']
        ])
    
    # Header tabel
    headers = ["No", "Nomor Induk", "Nama Pegawai", "Divisi", "Posisi", "Status", "Gaji Pokok", "Email", "Domisili"]
    
    print("=== Data Karyawan ===")
    print(tabulate(tabel, headers=headers, tablefmt="grid"))
    print()

def filter_data():
    if not karyawan:
        print("Data karyawan kosong.")
        return
    while True:
        print("=== FILTER DATA KARYAWAN ===")
        print("Filter berdasarkan:")
        print("1. Divisi")
        print("2. Status Karyawan")
        print("3. Domisili")
        print("4. Kembali ke menu sebelumnya")

        pilihan = input("Pilih filter (1-4): ")

        # Mapping pilihan ke field dictionary
        if pilihan == "1":
            field = "Divisi"
        elif pilihan == "2":
            field = "Status Karyawan"
        elif pilihan == "3":
            field = "Domisili"
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")
            continue

        # List opsi untuk field yang dipilih
        opsi = sorted(set(item[field] for item in karyawan))
        print(f"Opsi {field} yang tersedia: {', '.join(opsi)}")

        # Input nilai filter
        value = input(f"Masukkan {field}: ")
        if value not in opsi:
            print(f"{field} tidak valid, coba lagi.")
            continue

        # Header tabel
        hasil = []
        for index, item in enumerate(karyawan, start=1):
            if item[field].lower() == value.lower():
                hasil.append([
                    index,
                    item['Nomor Induk'],
                    item['Nama Pegawai'],
                    item['Divisi'],
                    item['Posisi'],
                    item['Status Karyawan'],
                    item['Gaji Pokok'],
                    item['Email'],
                    item['Domisili']
                ])
        if hasil:
            headers = ["No", "Nomor Induk", "Nama Pegawai", "Divisi", "Posisi", "Status", "Gaji Pokok", "Email", "Domisili"]
            print(tabulate(hasil, headers=headers, tablefmt="grid"))
        else:
            print(f"Tidak ada data karyawan dengan {field} = {value}.")


def sub_menu_read():
    while True:
        print("=== MENU TAMPILKAN DATA KARYAWAN ===")
        print("1. Tampilkan seluruh data karyawan")
        print("2. Tampilkan data berdasarkan filter tertentu")
        print("3. Kembali ke menu utama")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            data_karyawan()
        elif pilihan == "2":
            filter_data()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")

def tambah_karyawan():
    print("=== TAMBAH KARYAWAN BARU ===")

    # Cek Nomor Induk unik
    while True:
        nomor_induk = input("Masukkan Nomor Induk (ID-xxx): ")
        # Cek format ID (must contain "-")
        if "-" not in nomor_induk:
            print("Format Nomor Induk salah. Harus ID-XXX (contoh: ID-001).")
            continue
        # Cek format ID (must contain "ID" and 3 digits after "-")
        id_split = nomor_induk.split("-")
        if len(id_split) != 2 or id_split[0] != "ID" or not id_split[1].isdigit() or len(id_split[1]) != 3:
            print("Format Nomor Induk salah. Harus ID-XXX (contoh: ID-001).")
            continue
        # Cek duplikat di data
        if any(item['Nomor Induk'].lower() == nomor_induk.lower() for item in karyawan):
            print("Nomor Induk sudah terdaftar. Coba lagi.")
        else:
            break
    nama_pegawai = input("Masukkan Nama Pegawai: ")
    divisi = input("Masukkan Divisi: ")
    posisi = input("Masukkan Posisi (Contoh : Kepala Divisi): ").capitalize()
    status_karyawan = input("Masukkan Status Karyawan (Contoh : Tetap): ").capitalize()


    # Validasi gaji (harus angka)
    while True:
        gaji_pokok = input("Masukkan Gaji Pokok: ")
        if not gaji_pokok.isdigit():
            print("Gaji harus berupa angka.")
        else:
            gaji_pokok = int(gaji_pokok)  #konversi ke integer
            break

    # Validasi email unik dan mengandung @
    while True:
        email = input("Masukkan Email: ")
        if "@" not in email:
            print("Format email tidak valid (harus mengandung @).")
        elif any(item['Email'].lower() == email.lower() for item in karyawan):
            print("Email sudah terdaftar. Gunakan email lain.")
        else:
            break

    domisili = input("Masukkan Domisili: ").capitalize()
    
    karyawan_baru = {
        'Nomor Induk': nomor_induk,
        'Nama Pegawai': nama_pegawai,
        'Divisi': divisi,
        'Posisi': posisi,
        'Status Karyawan': status_karyawan,
        'Gaji Pokok': gaji_pokok,
        'Email': email,
        'Domisili': domisili
    }
    simpan_data = input("Simpan data ini? (y/n): ").lower()
    if simpan_data == "y":
        karyawan.append(karyawan_baru)
        print("==== DATA KARYAWAN BARU BERHASIL DITAMBAHKAN. ====")
    else:
        print("Data tidak jadi ditambahkan, kembali ke submenu")


def sub_menu_tambah():
    while True:
        print("=== MENU MENAMBAH DATA KARYAWAN BARU ===")
        print("1. Tambah data karyawan baru")
        print("2. Kembali ke menu utama")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")

def update_karyawan():
    if not karyawan:
        print("Belum ada data karyawan untuk diupdate.")
        return

    print("=== UPDATE DATA KARYAWAN ===")
    nomor_induk = input(" Masukkan Nomor Induk karyawan yang ingin diupdate (Contoh: ID-001, ID-002, dst): ")
    # Cek data karyawan tersedia atau tidak
    for data in karyawan:
        if data["Nomor Induk"].lower() == nomor_induk.lower():
            print(f"Data ditemukan:{data}")

            # Input nama (boleh kosong kalau tidak mau diubah)
            nama_baru = input(f"Nama Pegawai [{data['Nama Pegawai']}]: ")
            if nama_baru:
                data['Nama Pegawai'] = nama_baru

            # Input divisi 
            divisi_baru = input(f"Divisi [{data['Divisi']}]: ")
            if divisi_baru:
                data['Divisi'] = divisi_baru

            
            posisi_baru = input(f"Posisi [{data['Posisi']}]: ")
            if posisi_baru:
                data['Posisi'] = posisi_baru

            
            status_baru = input(f"Status Karyawan [{data['Status Karyawan']}]: ")
            if status_baru:
                data['Status Karyawan'] = status_baru

            # Validasi gaji
            while True:
                gaji_baru = input(f"Gaji Pokok [{data['Gaji Pokok']}]: ")
                if not gaji_baru:  # kalau kosong, lewati
                    break
                elif gaji_baru.isdigit():
                    data['Gaji Pokok'] = int(gaji_baru)
                    break
                else:
                    print("Gaji harus berupa angka.")

            # Validasi email
            while True:
                email_baru = input(f"Email [{data['Email']}]: ")
                if not email_baru:
                    break
                elif "@" not in email_baru:
                    print("Format email tidak valid.")
                elif any(item['Email'].lower() == email_baru.lower() and item != data for item in karyawan):
                    print("Email sudah digunakan oleh karyawan lain.")
                else:
                    data['Email'] = email_baru
                    break

            # Update domisili 
            domisili_baru = input(f"Domisili [{data['Domisili']}]: ")
            if domisili_baru:
                data['Domisili'] = domisili_baru
            # Konfirmasi simpan perubahan
            simpan_data = input("Simpan data ini? (y/n): ").lower()
            if simpan_data == "y":
                print("=== DATA KARYAWAN BERHASIL DIUPDATE. ===")
                return
            else:
                print("Perubahan dibatalkan.")
                return
            
    print("Data karyawan dengan Nomor Induk tersebut tidak ditemukan.")

def sub_menu_update():
    while True:
        print("=== MENU UPDATE DATA KARYAWAN ===")
        print("1. Update data karyawan")
        print("2. Kembali ke menu utama")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            update_karyawan()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")

def delete_karyawan():
    del_karyawan = input("Masukkan Nomor Induk Karyawan yang ingin dihapus. (Contoh: ID-001, ID-002, dst): ")

    # Cari karyawan berdasarkan Nomor Induk
    for i, item in enumerate(karyawan):
        if item['Nomor Induk'].lower() == del_karyawan.lower():
            # Konfirmasi delete
            print("Data yang akan dihapus: ")
            for key, value in item.items():
                print(f"{key}: {value}")
            konfirmasi = input("Hapus data ini? (y/n): ").lower()
            if konfirmasi == "y":
                terhapus = karyawan.pop(i)
                print(f"=== Data karyawan bernama {terhapus['Nama Pegawai']} berhasil dihapus. ===")
                return
            else:     
                return
    
    print("Data karyawan tidak ditemukan.")

def sub_menu_delete():
    while True:
        print("=== MENU DELETE DATA KARYAWAN ===")
        print("1. Delete data karyawan")
        print("2. Kembali ke menu utama")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            delete_karyawan()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")


def menu():
    while True:
        print('''
=== APLIKASI DATA KARYAWAN ===
=== CV. PERUSAHAAN BERKAH ===
1. Tampilkan Data Karyawan
2. Tambah Data Karyawan
3. Update Data Karyawan
4. Hapus Data Karyawan
5. Keluar
''')
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            sub_menu_read()
        elif pilihan == "2":
            sub_menu_tambah()
        elif pilihan == "3":
            sub_menu_update()
        elif pilihan == "4":
            sub_menu_delete()
        elif pilihan == "5":
            print("Have a nice day.")
            break
        else:
            print("Pilihan tidak valid.")

#=====MENU START=====#
menu()




