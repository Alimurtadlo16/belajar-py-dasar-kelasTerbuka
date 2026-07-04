# Break dalam python

# Contoh 1
angka_ = int(input("Hitung sampai: "))
angka = 0
while angka < 100:
    angka += 1
    print(f"Hitungan ke: {angka}")
    if angka == angka_:
        print("Done")
        break
    print("Hahahaha you're stupid")
print("Done\n")

# Contoh 2 latihan looping segitiga dengan for
sisi = 50
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("\n")

# Contoh 3 lopping dengan while
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
print("\n")

# Contoh 4 hanya ganjil
count = 1
while True:
    if (count%2):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
print("\n")

# Contoh 5 sama kaki
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break