# Penerapan kalkulator sederhana

print(20*"=")
print("Kalkulator sederhana")
print(20*"=" + "\n")

angkaPertama = float(input("Masukkan angka pertama: "))
operator = input("+,-,*,/: ")
angkaKedua = float(input("Masukkan angka kedua: "))
if operator == "+":
    hasil = angkaPertama + angkaKedua
    print(f"Hasilnya adalah: {hasil}")
elif operator == "-":
    hasil = angkaPertama - angkaKedua
    print(f"Hasilnya adalah: {hasil}")
elif operator == "*":
    hasil = angkaPertama * angkaKedua
    print(f"Hasilnya adalah: {hasil}")
elif operator == "/":
    hasil = angkaPertama / angkaKedua
    print(f"Hasilnya adalah: {hasil}")
else:
    print("Masukkan angka terlebih dulu!!!")

print("Terima kasih telah menggunakan programku")