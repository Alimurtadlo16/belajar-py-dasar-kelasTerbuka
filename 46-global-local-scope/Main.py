# Global dan local scope dalam python

namaGlobal = "Ali murtadlo" 

# Akses global dalam fungsi
# Bisa dijalankan dimanapun
def fungsi():
    print(f"Fungsi menampilkan {namaGlobal}")
fungsi()

# Akses global dalam loop
for i in range(0,5):
    print(f"Loop {i} - {namaGlobal}")

# Percabangan
if True:
    print(f"If menampillkan {namaGlobal}")

# Variable lokal scope
# Tidak bisa dijalankan dimanapun
"""def fungsi2():
    namaLocal = "Joseph"
fungsi2()
print(namaLocal)"""

def sayJoseph():
    print(f"Hello {nama}")
nama = "Joseph"
sayJoseph()

# Merubah variable global
angka = 0
nama = "William"
def ubah(nilaiBaru, namaBaru):
    global angka 
    global nama 
    angka = nilaiBaru
    nama = namaBaru
print(f"Sebelum: {angka,nama}")
ubah(99,"John")
print(f"Sesudah: {angka,nama}")

# Looping
angka = 0
angkaDummy = 0
for i in range(0,9):
    angka += 1
    angkaDummy += 1
print(angka)
print(angkaDummy)
if True:
    angka = 5
    angkaDummy = 10
print(angka)
print(angkaDummy)
