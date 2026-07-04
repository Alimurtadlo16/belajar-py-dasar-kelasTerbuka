# Module matematika dengan import alias

from Matematika import tambah as add
from Matematika import kali as other
from Matematika import pangkat as noken
from Matematika import *
import Matematika as math

hasilTambah = add(6,7,8,9,99)
print(f"Hasil tambah: {hasilTambah}")
hasilKali = math.kali(6,7,8,9,99)
print(f"Hasil kali: {hasilKali}")
pangkat3 = noken(3)
print(f"Hasil pangkat: {pangkat3(3)}")