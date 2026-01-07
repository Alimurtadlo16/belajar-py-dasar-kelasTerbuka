# Fungsi dengan return dalam python

# Fungsi kuadrat
def kuadrat(inputAngka):
    outputKuadrat = inputAngka**2
    return outputKuadrat
y = kuadrat(8)
print(y)
print(kuadrat(6))
z = 10 + kuadrat(7)
print(z)

# Fungsi tambah
def fungsiTambah(angka1,angka2):
    return angka1 + angka2

a = fungsiTambah(20,99)
print(a)

# Fungsi dengan return banyak
def operasiMatematika(angka1,angka2):
    kali = angka1 * angka2
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    bagi = angka1 / angka2
    return kali,tambah,kurang,bagi
k,l,m,n = operasiMatematika(99,25)
print(f"Hasil kali: {k}")
print(f"Hasil tambah: {l}")
print(f"Hasil kurang: {m}")
print(f"Hasil bagi: {n}")