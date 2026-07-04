# Latihan fungsi dalam python

import os

def header():
    '''Header'''
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print("-" * 60)

def menu():
    print("Pilih opsi perhitungan:")
    print("1. Hitung Luas saja")
    print("2. Hitung Keliling saja")
    print("3. Hitung Luas dan Keliling")
    return input("Masukkan pilihan (1/2/3): ").strip()

def inputUser():
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar, panjang

def hitungLuasKeliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hitungLuas(lebar, panjang):
    return lebar * panjang

def hitungKeliling(lebar, panjang):
    return 2 * (lebar + panjang)

def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")

while True:
    header()
    opsi = menu()
    lebar, panjang = inputUser()

    if opsi == "1":
        luas = hitungLuas(lebar, panjang)
        display("luas", luas)
    elif opsi == "2":
        keliling = hitungKeliling(lebar, panjang)
        display("keliling", keliling)
    elif opsi == "3":
        luas = hitungLuas(lebar, panjang)
        keliling = hitungKeliling(lebar, panjang)
        display("luas", luas)
        display("keliling", keliling)
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        continue

    print()
    isContinue = input("Apakah mau lanjut? (y/n): ").lower()
    if isContinue == "n":
        break

print("PROGRAM SELESAI TERIMA KASIH")