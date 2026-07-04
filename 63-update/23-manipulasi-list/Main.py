# Manipulasi data list

# Index
data = ["Ahmad","Ali","Murtadlo","Asadillah"]
print(data)
dataPertama = data[0]
print(f"\nData pertama: {dataPertama}")
dataTerakhir = data[-1]
print(f"\nData terakhir: {dataTerakhir}")
dataAli = data[-3]
print(f"\nData ali: {dataAli}")

# Info jumlah list
panjangData = len(data)
print(f"\nPanjang data: {panjangData}")

# Manipulasi data list pertama
data.insert(0,"Dia")
print(f"\nData sesudah ditambah: {data}")

# Manipulasi data list terakhir
data.append("Ganteng")
print(f"\nData sesudah ditambah akhirannya: {data}")

# Menambahkan dua list
dataBaru = ["Joseph","Adam"]
data.extend(dataBaru)
print(f"\nGabungan dua list: {data}")

# Merubah data pada list
data[0] = "Laila"
print(f"\nPerubahan data: {data}")

# Menghapus data sesuai huruf jika tidak sesuai akan eror
data.remove("Laila")
print(f"\nData yang sudah dihapus: {data}")

# Menghapus data akhiran
data = data.pop()
print(f"\nData akhir: {data}")