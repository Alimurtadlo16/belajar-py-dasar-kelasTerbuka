import os
import CRUD as CRUD

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

CRUD.init_console()

while True:
    clear_screen()
    print(15*"=", " DATABASE PERPUSTAKAAN ", 15*"=")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Ubah Data (Update)")
    print("4. Hapus Data (Delete)")
    print("5. Keluar")
    
    pilihan = input("\nPilih menu (1-5): ")

    if pilihan == "1":
        clear_screen()
        data = CRUD.read()
        print(f"{'No':<3} | {'Judul':<20} | {'Penulis':<15} | {'Tahun':<5}")
        print("-" * 55)
        for index, baris in enumerate(data, start=1):
            j, p, pb, t = baris.strip().split(',')
            print(f"{index:<3} | {j:<20} | {p:<15} | {t:<5}")
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "2":
        judul = input("Judul   : ")
        penulis = input("Penulis : ")
        penerbit = input("Penerbit: ")
        tahun = input("Tahun   : ")
        CRUD.create(judul, penulis, penerbit, tahun)

    elif pilihan == "3":
        # Fitur Update
        clear_screen()
        data = CRUD.read()
        for index, baris in enumerate(data, start=1):
            print(f"{index}. {baris.strip()}")
        
        nomor = int(input("\nNomor buku yang akan diubah: "))
        print("--- Masukkan Data Baru ---")
        judul = input("Judul baru   : ")
        penulis = input("Penulis baru : ")
        penerbit = input("Penerbit baru: ")
        tahun = input("Tahun baru   : ")
        CRUD.update(nomor, judul, penulis, penerbit, tahun)

    elif pilihan == "4":
        # Fitur Delete
        clear_screen()
        data = CRUD.read()
        for index, baris in enumerate(data, start=1):
            print(f"{index}. {baris.strip()}")
        
        nomor = int(input("\nNomor buku yang akan dihapus: "))
        CRUD.delete(nomor)
        print("Data berhasil dihapus!")
        input("\nTekan Enter...")

    elif pilihan == "5":
        break