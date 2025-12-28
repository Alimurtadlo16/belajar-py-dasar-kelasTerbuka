# Latihan Komparasi dan Logika

# Membandingkan dua nilai dan menggunakan operator logika
inputUser = float(input("Masukkan nilai angka kurang dari 3 lebih besar dari 15: "))
isKurangDari = (inputUser < 3)
isLebihDari  = (inputUser > 15)
print("Kurang dari 3 :",isKurangDari)
print("Lebih dari 15 :",isLebihDari)
isCorrect = isKurangDari or isLebihDari
print("Nilai yang anda masukkan:",isCorrect)

# Kasus irisan 
print("\n",30*"-","\n")
inputUser = float(input("Masukkan nilai angka lebih dari 3 dan kurang dari 15: "))
isLebihDari = inputUser > 3
print("Lebih dari 3 :",isLebihDari)
isKurangDari = inputUser < 15
print("Kurang dari 15 :",isKurangDari)
isCorrect = isLebihDari and isKurangDari
print("Nilai yang anda masukkan:",isCorrect)

# Latihan mandiri
print("\n",30*"-","\n")
Angka = float(input("Masukkan angka : "))
nol = (Angka > 0)
lima = (Angka < 5)
lapan = (Angka > 8)
sebelas = (Angka < 11)
Jawaban = (nol and lima) or (lapan and sebelas)
print("Angka anda :",Jawaban)

print("\n",30*"-","\n")
Angka = float(input("Masukkan angka : "))
nol = (Angka < 0)
lima = (Angka > 5)
lapan = (Angka < 8)
sebelas = (Angka > 11)
Jawaban = (nol or lima) and (lapan or sebelas)
print("Angka anda :",Jawaban)