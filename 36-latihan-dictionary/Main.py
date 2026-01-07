# Latihan Dictionary - Program Data Mahasiswa

import datetime
import os
import string
import random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

mahasiswaTemplate = {
    'Nama': "nama",
    'NIM': "00000000",
    'SKSLulus': 0,
    'Beasiswa': False,
    'Lahir': datetime.datetime(2000, 1, 1)
}

dataMahasiswa = {}

clear_screen()
print("=" * 50)
print(f"{'SELAMAT DATANG DI PROGRAM DATA MAHASISWA':^50}")
print("=" * 50)
print()

while True:
    # Input data mahasiswa
    mahasiswa = dict.fromkeys(mahasiswaTemplate.keys())
    mahasiswa['Nama'] = input("Nama mahasiswa: ").strip()
    mahasiswa['NIM'] = input("NIM mahasiswa: ").strip()
    mahasiswa['SKSLulus'] = int(input("SKS Lulus: "))
    beasiswa_input = input("Apakah mendapat beasiswa? (y/n): ").strip().lower()
    mahasiswa['Beasiswa'] = beasiswa_input == 'y'

    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (MM): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (DD): "))
    mahasiswa['Lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    # Simpan data dengan NIM sebagai key
    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    dataMahasiswa.update({KEY:mahasiswa})

    print("\n")
    isDone = input("Sudah selesai belum? (y/n) :")
    if isDone.lower() == "y":
        break

    print("\n" + "=" * 50)
    print("DATA MAHASISWA YANG TELAH DIINPUT:")
    print("=" * 50)

# Header tabel
    print(f"{'NIM': <10} {'Nama': <30} {'SKS': <5} {'Beasiswa': <10} {'Lahir': <12}")
    print("-" * 70)

# Tampilkan data
    for nim, data in dataMahasiswa.items():
        nama = data['Nama']
        sks = data['SKSLulus']
        beasiswa = "Ya" if data['Beasiswa'] else "Tidak"
        lahir = data['Lahir'].strftime("%d/%m/%Y")
        print(f"{nim: <10} {nama: <30} {sks: <5} {beasiswa: <10} {lahir: <12}")

        print("\n")
        isDone = input("Ada lagi? (y/n: )")
        if isDone == "n":
            break
print("\nTerima kasih telah menggunakan program ini!")