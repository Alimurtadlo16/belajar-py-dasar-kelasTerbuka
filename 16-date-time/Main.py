# latihan Date and Time di Python

# Contoh 1
import datetime as dt
hari_ini = dt.date.today()
print("Sekarang tanggal:", hari_ini)
print(f"Hari ini:  {hari_ini:%A}\n")

# Contoh 2
tanggal = dt.date(2007,11,16)
print("Tanggal lahirku:", tanggal)
print(f"Hari lahirku:  {tanggal:%A}")

# Contoh 3
print("\nSilahkan masukkan: tanggal,bulan,tahun lahirmu: ")
tanggal = int(input("Tanggal \t:"))
bulan   = int(input("bulan \t\t:"))
tahun   = int(input("tahun \t\t:"))
tanggalLahir = dt.date(tahun,bulan,tanggal)
print("Tanggal lahirmu: ", tanggalLahir)
print(f"Hari lahirmu:  {tanggalLahir:%A}")

# Contoh 4
hari_ini = dt.date.today()
print(f"\nHari ini tanggal:  {hari_ini}")
umur =  hari_ini - tanggalLahir
umurTahun = umur.days // 365
umurSisaBulan = (umur.days % 365) // 30
print(f"Umur anda adalah: {umur}Hari")
print(f"Umur anda adalah: {umurTahun} Tahun, {umurSisaBulan} Bulan")