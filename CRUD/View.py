import os

def init_console():
    if not os.path.exists("data.txt"):
        with open("data.txt", "w", encoding="utf-8") as file:
            pass

def create(judul, penulis, penerbit, tahun):
    data_str = f"{judul},{penulis},{penerbit},{tahun}\n"
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data_str)

def read():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
    except:
        return []

def update(nomor_buku, judul, penulis, penerbit, tahun):
    data_buku = read()
    # Mengganti baris sesuai nomor (index dimulai dari 0)
    data_buku[nomor_buku - 1] = f"{judul},{penulis},{penerbit},{tahun}\n"
    
    with open("data.txt", "w", encoding="utf-8") as file:
        file.writelines(data_buku)

def delete(nomor_buku):
    data_buku = read()
    # Menghapus baris berdasarkan index
    data_buku.pop(nomor_buku - 1)
    
    with open("data.txt", "w", encoding="utf-8") as file:
        file.writelines(data_buku)