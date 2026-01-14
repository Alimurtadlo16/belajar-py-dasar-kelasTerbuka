import datetime
from collections import Counter
import io

# 1. Bagian Waktu
dataWaktu = datetime.datetime.now()
print(f"Hari: {dataWaktu.strftime('%A')}")
print(f"Bulan: {dataWaktu.month}")
print(f"Tahun: {dataWaktu.year}")
print(f"Date time now: {dataWaktu}")

print("-" * 20)

# 2. Bagian Counter
data = ["a", "b", "c", "d", "e", "f"]
dataCounter = Counter(data)
print(f"Data count: {dataCounter}")
print(f"Data a: {dataCounter['a']}")
print(f"Data b: {dataCounter['b']}")

print("-" * 20)

# 3. Bagian Membaca File (Gunakan try-except agar tidak crash jika file tidak ada)
# Pastikan file_text.txt berada di folder yang sama dengan script ini
try:
    with open("file_text.txt", "r") as file:
        print(file.read()) # Pastikan ada tanda kurung ()
except Exception as e:
    print(f"Terjadi kesalahan: {e}")