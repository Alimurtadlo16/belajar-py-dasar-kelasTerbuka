# Anonymous dan Lambda Function dalam python

def kuadrat(angka):
    return angka**2
print(f"Hasil dari kuadrat: {kuadrat(99)}")

# Menggunakan lambda
# output = lambda arguments: expression
kuadrat = lambda angka:angka**2
print(kuadrat(99))
pangkat = lambda num,pow: num**pow
print(f"Hasil dari pangkat = {pangkat(6, 2)}")  # Diperbaiki: Tambahkan argumen kedua (misalnya, 6^2)

# Kegunaan lambda
# Sorting list
dataList = ["Ali","Joseph","William"]
print(f"Original list = {dataList}")

# Sorting berdasarkan panjang nama
def panjangNama(nama):
    return len(nama)
sorted_by_len = sorted(dataList, key=len)
print(f"Sorted by length: {sorted_by_len}")

# Sorting alphabetical
sorted_alpha = sorted(dataList)
print(f"Sorted alphabetical: {sorted_alpha}")

# Analisa panjang nama
for nama in dataList:
    print(f"Panjang nama {nama}: {len(nama)} huruf")

# Sort lambda
dataList = ["Ali","Joseph","William"]
dataList.sort(key=lambda nama:len(nama))
print(f"Sorted by lambda: {dataList}")

# Filter
dataAngka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurangDariLima(angka):
    return angka < 5
dataAngkaBaru = list(filter(kurangDariLima,dataAngka))
dataAngkaBaru = list(filter(lambda x:x<8,dataAngka))
print(dataAngkaBaru)

# Data genap
dataGenap = list(filter(lambda x:(x%2==0),dataAngka))
print(dataGenap)

# Data ganjil
dataGanjil = list(filter(lambda x:(x%2!=0),dataAngka))
print(dataGanjil)

# Data kelipatan 3
dataKelipatan = list(filter(lambda x:(x%3==0),dataAngka))
print(dataKelipatan)

# Anonymous function
# Currying <- Haskell curry
def pangkat(n):
    return lambda angka:angka**n
pangkat2 = pangkat(99)
print(pangkat2(2))  # Diperbaiki: Cetak hasil pangkat2(2), yaitu 2^99, bukan objek fungsi