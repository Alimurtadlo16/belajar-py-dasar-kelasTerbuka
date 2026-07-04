# Import package dalma python

import time
tStart = time.time()

import packages.Matematika
from packages import Fisika
from packages.Fisika import gaya as physic

hasilTambah = packages.Matematika.tambah(6,7,8,9,0)
print(f"Hasil tambah dari packages adalah: {hasilTambah}")
hasilGaya = Fisika.gaya(99, 10)
print(f"Gaya adalah: {hasilGaya}")
hasilGaya = physic(2025, 10)
print(f"Gaya adalah: {hasilGaya}")

tEnd = time.time()
print(f"Waktu eksekusi adalah: {tEnd - tStart}")