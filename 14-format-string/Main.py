# Format String Example

# Contoh generic
nama = "Ahmad Ali Murtadlo Asadillah"
str  =  f"Nama saya adalah: {nama}"
print(str)  

# Contoh angka
angka = 1500.5
str   = f"Harga barang tersebut adalah: {angka}"
print(str)

# Contoh boolean
status = True
str    = f"Status keanggotaan Anda adalah: {status}"
print(str)

# Bilangan bulat
angka = 1000.5
str   = f"Nilai bilangan bulatnya adalah: {int(angka)}"
print(str)

# Bilangan ribuan
angka = 1000000
str   = f"Nilai bilangan ribuannya adalah: {angka:,}"
print(str)

# Bilangan desimal
angka = 1500.56789
str   = f"Nilai bilangan desimalnya adalah: {angka:.2f}"
print(str)

# Bilangan persen
angka = 0.75
str   = f"Nilai bilangan persennya adalah: {angka:.2%}"
print(str)

# Loading zero
angka = 1500000.77777
str   = f"Nilai dengan loading zero adalah: {angka:9.2f}"
print(str)

# Tanda plus dan minus
angka_pos = 1500
angka_neg = -1500
str_pos   = f"Nilai dengan tanda plus adalah: {angka_pos:}"
str_neg   = f"Nilai dengan tanda minus adalah: {angka_neg:}"
print(str_pos)
print(str_neg)

# Operasi aritmatika dalam placeholder
angka1 = 10000
jumlah = 500
str    = f"Jumlah dari {angka1} + {jumlah} adalah: {angka1 + jumlah}"
print(str)

# Format lain (biner, oktal, heksadesimal)
angka = 255
biner = f"Nilai biner dari {angka} adalah: {angka:b}"
oktal = f"Nilai oktal dari {angka} adalah: {angka:o}"
heksa = f"Nilai heksadesimal dari {angka} adalah: {angka:x}"
print(biner)
print(oktal)
print(heksa)