# Continue and pass dalam python

# Pass berfungsi seperti dummy dan tidak akan dieksekusi
angka = 0
while angka < 100:
    angka += 1
    if angka == 5:
        pass
    print(f"Angka sekarang: {angka}")

# Continue
angka = 0
print(f"\nAngka sekarang: {angka}")
while angka < 5:
    angka += 1
    print(f"Angka sekarang: {angka}")
    if angka == 5:
        print("Done")
        continue
    print("Hey hoo")
print("Done")