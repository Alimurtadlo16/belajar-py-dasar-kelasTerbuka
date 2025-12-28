# Pembelajaran string di Python
# String adalah tipe data yang digunakan untuk menyimpan teks
# String diapit oleh tanda kutip tunggal (' ') atau tanda kutip ganda (" ")

# Contoh 1
data1 = "Ini adalah string dengan tanda kutip ganda"
data2 = 'Ini adalah string dengan tanda kutip tunggal'
print(data1)
print(data2)
print(type(data1))
print(type(data2))
print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari ahad")

# Contoh 2
# String bisa menggunakan tanda \ untuk karakter khusus
print('Ini adalah hari jum\'at')
print('g\'day, isn\'t it?')

# Contoh 3
# String bisa menggunakan tanda back slash untuk karakter khusus
print("C:\\user\\Ahmad Ali Murtadlo Asadillah\\belajar dasar py")

# Contoh 4
# String bisa menggunakan tab
print("Nama:\tAhmad Ali Murtadlo Asadillah")

# Contoh 5
# String bisa menggunakan backspace
print("Nama:\bAhmad Ali Murtadlo Asadillah")

# Contoh 6
# String bisa menggunakan newline
print("Baris pertama.\nBaris kedua ")
print("Baris pertama\rBaris kedua ")
print("Baris pertama\r\nBaris kedua ")

# Contoh 7
# String bisa menggunakan literal atau raw
# Dengan raw string, karakter backslash tidak diartikan sebagai karakter khusus string
print(r"C:\user\Ahmad Ali Murtadlo Asadillah\belajar dasar py")

# Contoh 8
# String bisa menggunakan multiline string
# Multiline string bisa dibuat dengan tiga tanda kutip tunggal atau tiga tanda kutip g
print("""
Ahmad ALi Murtadlo Asadillah
Mahasiswa
teknik informatika
Unida Gontor.""")