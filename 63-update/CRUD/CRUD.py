# Simpan sebagai CRUD.py (Sejajar dengan Main.py)
import os

def init_console():
    """Memastikan file data.txt tersedia saat program jalan"""
    if not os.path.exists("data.txt"):
        with open("data.txt", "w", encoding="utf-8") as file:
            pass
    print("Database Berhasil Diinisialisasi.")

def read():
    """Membaca seluruh isi file database"""
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def create(judul, penulis, penerbit, tahun):
    """Menambah data baru ke dalam database"""
    data_str = f"{judul},{penulis},{penerbit},{tahun}\n"
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data_str)

def update(nomor, judul, penulis, penerbit, tahun):
    """Mengubah data pada baris tertentu"""
    data = read()
    if 0 < nomor <= len(data):
        data[nomor-1] = f"{judul},{penulis},{penerbit},{tahun}\n"
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(data)

def delete(nomor):
    """Menghapus data pada baris tertentu"""
    data = read()
    if 0 < nomor <= len(data):
        data.pop(nomor-1)
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(data)