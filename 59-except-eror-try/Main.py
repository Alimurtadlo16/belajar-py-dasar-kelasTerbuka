dataInput = int(input("Masukkan angka: "))
hasil = 10/dataInput
print(hasil)

# Exception
# Eror saat dijalankan
from math import nan

inputUser = int(input("Masukkan angka: "))
hasil = nan
try:
    hasil = 10/inputUser
except:
    print("Input tidak boleh 0")
print(f"Hasil: {hasil}")

# ... (kode pembagian sebelumnya)

# Contoh diaplikasi
while(True):
    try:
        # Masukkan input DI DALAM try agar jika user memasukkan huruf, tidak error
        angka = int(input("Masukkan angka pembagi: "))
        hasil = 10/angka
        print(f"Hasil: {hasil}")
        isDone = input("Lanjutkan (y/n): ")
        if isDone == "n":
            break
    except ZeroDivisionError:
        print("Pembagian nol, silahkan masukkan input lain")
    except ValueError:
        print("Input harus berupa angka!")

print("Akhir dari program")

# Bagian File yang looping terus
while (True):
    try:
        with open("data.txt", 'r') as file:
            print(file.read())
        break # TAMBAHKAN INI agar berhenti setelah berhasil membaca
    except:
        print("File data.txt tidak ditemukan, membuat file baru...")
        with open("data.txt", 'w', encoding='utf-8') as file:
            file.write("file baru")
        # Tidak perlu break di sini jika ingin langsung mencoba baca lagi, 
        # tapi biasanya ditambahkan break agar tidak looping.
        break 

print(f"Akhir dari program")