def init_console(): # Sesuaikan nama fungsi dengan yang dipanggil di Main.py
    try:
        with open("data.txt", "r") as file:
            print("Database tersedia, init done")
    except:
        print("Database tidak ditemukan, membuat database baru...")
        # Gunakan nama file yang konsisten (data.txt)
        with open("data.txt", "w", encoding="utf-8") as file:
            penulis = input("Penulis: ")
            judul   = input("Judul: ")
            tahun   = input("Tahun: ")
            dataStr = f"{penulis},{judul},{tahun}"
            # Masukkan dataStr ke dalam write()
            file.write(dataStr)