# For and while looping dalam python

# Contoh 1 (List)
angkaList = [0,1,2,3,4,5,6,7,8,9]
print(angkaList)
for i in angkaList:
    print(f"I sekarang : {i}")
print("Akhir program setelah berulang\n")

# Contoh 2 (Range)
angkaRange = range(10)
for i in angkaRange:
    print(f"I sekarang : {i}")
print("Akhir program setelah berulang\n")

# Contoh 3 (String)
str = "Saya belajar python"
for huruf in str:
    print(str)
print("Akhir program setelah berulang\n")

# Contoh 4 (While)
angkaWhile = 0
print(f"Angka sekarang: {angkaWhile}")

while angkaWhile < 100:
    angkaWhile += 1
    print(f"Angka sekarang: {angkaWhile}")
    print("Angkamu kurang dari < 100 ")
print("Akhir program setelah berulang")