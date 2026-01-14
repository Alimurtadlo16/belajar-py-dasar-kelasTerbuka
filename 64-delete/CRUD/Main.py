import os
import CRUD as CRUD

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

daftar_buku = []
CRUD.init_console()

while True:
    clear_screen()
    print(15*"=", " PROGRAM PERPUSTAKAAN ", 15*"=")
    print("1. Lihat Semua Buku")
    print("2. Tambah Buku Baru")
    print("3. Hapus Buku (Memory Style)")
    print("4. Hapus Buku (Database Style)")
    print("5. Keluar")
    
    pilihan = input("\nPilih menu (1-5): ")

    if pilihan == "1":
        clear_screen()
        print(15*"=", " DAFTAR BUKU ", 15*"=")
        if not daftar_buku:
            print("Belum ada data buku di memory.")
        else:
            print(f"{'No':<3} | {'Judul':<20} | {'Penulis':<15} | {'Tahun':<5}")
            print("-" * 55)
            for index, buku in enumerate(daftar_buku, start=1):
                print(f"{index:<3} | {buku['judul']:<20} | {buku['penulis']:<15} | {buku['tahun']:<5}")
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "2":
        while True:
            clear_screen()
            print(15*"=", " INPUT BUKU ", 15*"=")
            judul   = input("Judul   : ")
            penulis = input("Penulis : ")
            penerbit= input("Penerbit: ")
            try:
                tahun = int(input("Tahun   : "))
            except ValueError:
                print("Tahun harus angka! Set ke 0.")
                tahun = 0
            
            daftar_buku.append({"judul": judul, "penulis": penulis, "penerbit": penerbit, "tahun": tahun})
            CRUD.create(judul, penulis, penerbit, tahun)
            
            lagi = input("\nTambah lagi? (y/n): ").lower()
            if lagi != 'y': break

    elif pilihan == "3": # Perbaikan indentasi di sini
        clear_screen()
        print(15*"=", " HAPUS DATA BUKU ", 15*"=")
        data_buku = CRUD.read()
        if not data_buku:
            print("Database kosong!")
        else:
            print(f"{'No':<3} | {'Judul':<20}")
            print("-" * 25)
            for index, baris in enumerate(data_buku, start=1):
                judul = baris.split(',')[0]
                print(f"{index:<3} | {judul:<20}")
            
            try:
                nomor = int(input("\nMasukkan NOMOR buku yang ingin dihapus: "))
                success, data = CRUD.delete(nomor)
                if success:
                    judul_terhapus = data.split(',')[0]
                    print(f"BERHASIL: Buku '{judul_terhapus}' telah dihapus.")
                else:
                    print("GAGAL: Nomor urut tidak ditemukan.")
            except ValueError:
                print("EROR: Masukkan input berupa ANGKA saja!")
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "4":
        while True:
            clear_screen()
            print(15*"=", " HAPUS DATA BUKU (DATABASE) ", 15*"=")
            data_buku = CRUD.read()
            if not data_buku:
                print("Database kosong.")
                input("\nTekan Enter...")
                break
                
            print(f"{'No':<3} | {'Judul':<20} | {'Penulis':<15}")
            print("-" * 45)
            for index, baris in enumerate(data_buku, start=1):
                data = baris.strip().split(',')
                print(f"{index:<3} | {data[0]:<20} | {data[1]:<15}")
            
            try:
                nomor = int(input("\nMasukkan nomor yang ingin dihapus (0 untuk batal): "))
                if nomor == 0: break
                konfirmasi = input(f"Yakin hapus nomor {nomor}? (y/n): ").lower()
                if konfirmasi == 'y':
                    # Pastikan fungsi delete mengembalikan tuple jika ingin menggunakan Menu 3 & 4 bersamaan
                    res = CRUD.delete(nomor)
                    if isinstance(res, tuple): # Proteksi jika return berupa tuple (success, data)
                        success = res[0]
                    else:
                        success = res
                    
                    if success:
                        print("Data Berhasil Dihapus!")
            except ValueError:
                print("Input harus angka!")
                
            if input("\nHapus lagi? (y/n): ").lower() != 'y': break

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break