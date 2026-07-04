import os
import CRUD as CRUD

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

# Inisialisasi list untuk menampung data
daftar_buku = []

CRUD.init_console()
while True:
    clear_screen()
    print(15*"=", " PROGRAM PERPUSTAKAAN ", 15*"=")
    print("1. Lihat Semua Buku")
    print("2. Tambah Buku Baru")
    print("3. Hapus Buku")
    print("4. Cari Buku")
    print("5. Keluar")
    
    pilihan = input("\nPilih menu (1-5): ")

    if pilihan == "1":
        # MENU LIHAT DATA
        clear_screen()
        print(15*"=", " DAFTAR BUKU ", 15*"=")
        if not daftar_buku:
            print("Belum ada data buku.")
        else:
            print(f"{'No':<3} | {'Judul':<20} | {'Penulis':<15} | {'Tahun':<5}")
            print("-" * 55)
            for index, buku in enumerate(daftar_buku, start=1):
                print(f"{index:<3} | {buku['judul']:<20} | {buku['penulis']:<15} | {buku['tahun']:<5}")
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "2":
        # MENU TAMBAH DATA
        while True:
            clear_screen()
            print(15*"=", " INPUT BUKU ", 15*"=")
            judul = input("Judul   : ")
            penulis = input("Penulis : ")
            penerbit = input("Penerbit: ")
            try:
                tahun = int(input("Tahun   : "))
            except ValueError:
                print("Tahun harus angka! Set ke 0.")
                tahun = 0
            
            daftar_buku.append({
                "judul": judul,
                "penulis": penulis,
                "penerbit": penerbit,
                "tahun": tahun
            })
            
            lagi = input("\nTambah lagi? (y/n): ").lower()
            if lagi != 'y': break

    elif pilihan == "3":
        # MENU HAPUS DATA
        clear_screen()
        print(15*"=", " HAPUS BUKU ", 15*"=")
        for index, buku in enumerate(daftar_buku, start=1):
            print(f"{index}. {buku['judul']}")
        
        try:
            nomor = int(input("\nMasukkan nomor buku yang ingin dihapus: "))
            if 0 < nomor <= len(daftar_buku):
                dihapus = daftar_buku.pop(nomor-1)
                print(f"Buku '{dihapus['judul']}' berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus angka.")
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "4":
        # MENU CARI BUKU
        clear_screen()
        print(15*"=", " CARI BUKU ", 15*"=")
        keyword = input("Masukkan judul buku yang dicari: ").lower()
        print("\nHasil Pencarian:")
        ditemukan = False
        for buku in daftar_buku:
            if keyword in buku['judul'].lower():
                print(f"- {buku['judul']} (Penulis: {buku['penulis']})")
                ditemukan = True
        if not ditemukan:
            print("Buku tidak ditemukan.")
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")
        input("Tekan Enter untuk coba lagi...")