# Di dalam file CRUD.py

def init_console():
    try:
        with open("data.txt", "r") as file:
            pass
    except:
        with open("data.txt", "w", encoding="utf-8") as file:
            pass

def create(judul, penulis, penerbit, tahun):
    data_str = f"{judul},{penulis},{penerbit},{tahun}\n"
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data_str)
    print("Data berhasil ditambahkan ke database!")