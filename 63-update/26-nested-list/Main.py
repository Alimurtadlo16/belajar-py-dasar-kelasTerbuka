# Nested list dalam python

# Contoh 1
data1 = [1,2]
data2 = [3,4,5]
dataList = [1,2,3,4,5]
print(f"Data list biasa: {dataList}\n")

# Contoh 2
list2D = [data1,data2]
print(f"Data list dalam list: {list2D}\n")

# Contoh 3
peserta1 = ["Ali", 18, "Laki laki"]
peserta2 = ["Steven",19, "Laki laki"]
peserta3 = ["Joseph",20, "Laki laki"]
semuaPeserta = [peserta1,peserta2,peserta3]
print(f"Semua data peserta: {semuaPeserta}")
for peserta in semuaPeserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Kelamin\t: {peserta[2]}\n")

# Contoh 4
copyList = semuaPeserta.copy();
print(f"Semua data peserta: {copyList}\n")
peserta1[0] = "Michael"
print(f"Semua data peserta: {copyList}\n")
print(f"Semua data peserta: {semuaPeserta}\n")