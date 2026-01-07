# Fungsi dengan input dalam python

def hello_world(nama):
    print(f"Selamat datang di dunia {nama}")

hello_world("Ali murtadlo")

def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,6)

def say_Hi(namaMahasiswa):
    namaMahasiswa = namaMahasiswa.copy()
    for mahasiswa in namaMahasiswa:
        print(f"Yang terhormat {mahasiswa}")

mahasiswa = ["Ali murtadlo"]
say_Hi(mahasiswa)