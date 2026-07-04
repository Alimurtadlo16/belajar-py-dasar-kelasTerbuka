# Looping dari list dalam python

# For loop
kumpulanAngka = [4,3,2,6,5,7]
for angka in kumpulanAngka:
    print(f"Angka: {angka}")

print(f"\n")
peserta = ["Ali", "Joseph", "Steven", "Adam"]
for nama in peserta:
    print(f"Nama: {nama}")
    
# For loop and range
print(f"\n")
angkaAngka = [10,5,6,3,2,7]
panjang = len(angkaAngka)
for i in range (panjang):
    print(f"Angka : {angkaAngka[i]}")

# While
angkaAngka = [10,5,6,3,2,7]
panjang = len(angkaAngka)
while i < panjang:
    print(f"Angka : {angkaAngka[i]}")
    i += 1

# List comprehension
print(f"\n")
peserta = ["Ali", "Joseph", "Steven", "Adam"]
[print(f"Data: {i}") for i in peserta]
kumpulanAngka = [4,3,2,6,5,7]
angkaKuadrat = [i**2 for i in kumpulanAngka]
print(angkaKuadrat)

# Enumerate 
print(f"\n")
listPeserta = ["Ali",1,2,3,4,5, "Joseph", "Steven", "Adam"]
for index,data in enumerate(listPeserta):
    print(f"Index: {index}, Data: {data}")