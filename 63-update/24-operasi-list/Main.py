# Operasi pada list dalam python

dataAngka = [1,2,3,4,5,6,7,8,9,2,3,5]
print(dataAngka)

# Count data
jumlahData = dataAngka.count(2)
jumlahData1 = dataAngka.count(3)
jumlahData2 = dataAngka.count(5)
print(f"Jumlah data 2: {jumlahData}")
print(f"Jumlah data 3: {jumlahData1}")
print(f"Jumlah data 5: {jumlahData2}")

# Cara mengambil index
index5 = dataAngka.index(6)
print(f"Index ke 4: {index5}")

# Mengurutkan list 
dataAngka.sort()
print(f"\nData angka setelah sort: {dataAngka}")

# Balik list
dataAngka.reverse()
print(f"Data di reverse: {dataAngka} ")