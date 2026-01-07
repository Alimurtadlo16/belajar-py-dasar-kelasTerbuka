# Default argument fungsi dalam python

# Def fungsi(argument):
def say_hello(nama = "Cantik"):
    print(f"Hallo {nama}")
say_hello("Ali murtadlo")
say_hello()

# Contoh 2
def sapa_dia(nama,pesan = "apa kabar?"):
    print(f"Hai {nama}, {pesan}")
sapa_dia("Hai cantik", "Ali murtadlo")
sapa_dia("Cantik")

# Contoh 3
def hitungPangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil
print(hitungPangkat(4,9))
hasil = hitungPangkat(pangkat=9, angka=99)
print(hasil)

# Contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil
print(fungsi())
print(fungsi(input3=99))