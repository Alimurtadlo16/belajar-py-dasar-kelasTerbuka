import os

def init_console():
    if not os.path.exists("data.txt"):
        with open("data.txt", "w", encoding="utf-8") as file:
            pass

def read():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except:
        return []

def create(judul, penulis, penerbit, tahun):
    data_str = f"{judul},{penulis},{penerbit},{tahun}\n"
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data_str)

def update(nomor, judul, penulis, penerbit, tahun):
    data = read()
    if 0 < nomor <= len(data):
        data[nomor-1] = f"{judul},{penulis},{penerbit},{tahun}\n"
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(data)
        return True
    return False

def delete(nomor):
    data = read()
    if 0 < nomor <= len(data):
        data_terhapus = data.pop(nomor-1)
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(data)
        return True, data_terhapus # Ini penting agar "split" di Main.py tidak error
    return False, None