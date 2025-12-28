# Operasi dan manipulasi string dalam Python
# Menyambung string (concatenation)

# Contoh 1
nama_depan = "Ahmad"
nama_tengah = "Ali Murtadlo"
nama_belakang = "Asadillah"
nama_lengkap = nama_depan +" "+ nama_tengah +" "+ nama_belakang
print("Nama lengkap saya adalah: " + nama_lengkap)

# Contoh 2
# Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang nama lengkap saya adalah: " + str(panjang) + " karakter")

# Contoh 3
# Operator untuk string
# Mengecek apakah sebuah substring ada di dalam string
status = "Ali" in nama_lengkap
print("Apakah 'Ali' ada di dalam nama lengkap saya? " + str(status))
status = "Umar" in nama_lengkap
print("Apakah 'Umar' ada di dalam nama lengkap saya? " + str(status))
status = "Umar" not in nama_lengkap
print("Apakah 'Umar' tidak ada di dalam nama lengkap saya? " + str(status))

# Contoh 4
# Mengulang string
print("Wkwkwk" * 10)
print(10 *"Wkwkwk")

# Contoh 5
# Indexing dan Slicing
print("Index ke-0: " + nama_lengkap[0])
print("Index ke-1: " + nama_lengkap[1])
print("Index ke-(-1): " + nama_lengkap[-1])
print("Index ke-(-2): " + nama_lengkap[-2])
print("Index 0 sampai 4: " + nama_lengkap[0:5])
print("Index 5 sampai 10: " + nama_lengkap[5:11])
print("Index 0 sampai akhir: " + nama_lengkap[0:])
print("Index 10 sampai akhir: " + nama_lengkap[10:])

# Contoh 6
# Item paling kecil dan paling besar
print("Item paling kecil: " + min(nama_lengkap))
print("Item paling besar: " + max(nama_lengkap))
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah: " + str(ascii_code))
data = 117
print("Character untuk ASCII code 117 adalah: " + chr(data))

# Contoh 7
# Operator dalam bentuk method
data = "Ahmad Ali Murtadlo Asadillah"
jumlah = data.count("A")
print("Jumlah huruf A pada variable data adalah: " + str(jumlah))

# Contoh 8
# Mengubah case string uppercase, lowercase, titlecase
data = "Ahmad Ali Murtadlo Asadillah"
print("Lower case: " + data.lower())
print("Upper case: " + data.upper())
print("Title case: " + data.title())

# Contoh 9
# Mengecek dengan isx method, lower, upper, title, space, alpha, numeric
data = "AhmadAliMurtadloAsadillah"
print("Apakah semua karakter adalah huruf? " + str(data.isalpha()))
data = "1234567890"
print("Apakah semua karakter adalah angka? " + str(data.isnumeric()))
data = "   "
print("Apakah semua karakter adalah spasi? " + str(data.isspace()))
data = "ahmad"
print("Apakah semua karakter adalah huruf kecil? " + str(data.islower()))
data = "AHMAD"
print("Apakah semua karakter adalah huruf besar? " + str(data.isupper()))
data = "Ahmad Ali Murtadlo Asadillah"
print("Apakah setiap kata diawali dengan huruf besar? " + str(data.istitle()))

# Contoh 10
# isalpha, isalnum, isdecimal, isspace, islower, isupper
# Mengecek semua string
data = "AhmadAliMurtadloAsadillah123"
print("Apakah semua karakter adalah huruf atau angka? " + str(data.isalnum()))
data = "12345.67"
print("Apakah semua karakter adalah desimal? " + str(data.isdecimal()))
data = "1234567"
print("Apakah semua karakter adalah desimal? " + str(data.isdecimal()))
data = "   \n\t"
print("Apakah semua karakter adalah spasi? " + str(data.isspace()))
data = "ahmadali"
print("Apakah semua karakter adalah huruf kecil? " + str(data.islower()))
data = "AHMADALI"
print("Apakah semua karakter adalah huruf besar? " + str(data.isupper()))
data = "Ahmad Ali"
print("Apakah setiap kata diawali dengan huruf besar? " + str(data.istitle()))

# Contoh 11
# startwith() dan endswith()
data = "Ahmad Ali Murtadlo Asadillah"
print("Apakah string diawali dengan 'Ahmad'? " + str(data.startswith("Ahmad")))
print("Apakah string diakhiri dengan 'Asadillah'? " + str(data.endswith("Asadillah")))
print("Apakah string diawali dengan 'Ali'? " + str(data.startswith("Ali")))
print("Apakah string diakhiri dengan 'Murtadlo'? " + str(data.endswith("Murtadlo")))

# Contoh 12
# Menggabungkan string dengan komponen join() split()
data = ["Ahmad", "Ali", "Murtadlo", "Asadillah"]
pisah = " ".join(data)
print("Menggabungkan string dengan join(): " + pisah)
gabung = pisah.split(" ")
print("Memisahkan string dengan split(): " + str(gabung))

# Contoh 13
# Alokasi karakter dengan rjust(), ljust(), center()
data = "Percobaan"
print("Rjust: '" + data.rjust(20, "_") + "'")
print("Ljust: '" + data.ljust(20, "_") + "'")
print("Center: '" + data.center(20, "_") + "'")

# Contoh 14
# Kebaikan strip(), rstrip(), lstrip()
data = "     Ahmad Ali Murtadlo Asadillah      "
print("Before strip: '" + data + "'")
print("After strip: '" + data.strip() + "'")
print("After rstrip: '" + data.rstrip() + "'")
print("After lstrip: '" + data.lstrip() + "'")

# Contoh 15
# Mengganti karakter dengan replace()
data = "Ahmad Ali Murtadlo Asadillah"
print("Before replace: " + data)
data_baru = data.replace("Ahmad", "Umar")
print("After replace: " + data_baru)

# Contoh 16
# Mengambil bagian string dengan slicing
data = "Ahmad Ali Murtadlo Asadillah"
print("Nama depan: " + data[0:5])
print("Nama tengah: " + data[6:20])
print("Nama belakang: " + data[21:32])
print("Inisial nama: " + data[0] + data[6] + data[13] + data[21])