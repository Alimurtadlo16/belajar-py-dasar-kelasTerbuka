import os

def init_console():
    if not os.name == "posix":
        os.system("cls")
    else:
        os.system("clear")
    
    if not os.path.exists("data.txt"):
        with open("data.txt", "w", encoding="utf-8") as file:
            pass

def read():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
    except:
        return []

def create(judul, penulis, penerbit, tahun):
    data_str = f"{judul},{penulis},{penerbit},{tahun}\n"
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data_str)

def update(nomor_buku, judul, penulis, penerbit, tahun):
    data_buku = read()
    if 0 < nomor_buku <= len(data_buku):
        data_buku[nomor_buku - 1] = f"{judul},{penulis},{penerbit},{tahun}\n"
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(data_buku)

def delete(nomor_buku):
    """Fungsi khusus untuk menghapus data buku berdasarkan nomor urut"""
    data_buku = read()
    if 0 < nomor_buku <= len(data_buku):
        # Menghapus data dari list berdasarkan index
        data_buku.pop(nomor_buku - 1)
        # Menulis ulang file dengan data yang sudah dikurangi
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(data_buku)
        return True
    return False