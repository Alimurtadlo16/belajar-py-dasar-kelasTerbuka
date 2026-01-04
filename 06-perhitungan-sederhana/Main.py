# Konversi satuan temperatur

# Konversi celcius ke satuan lain
print("\nKonversi Celcius ke satuan lain\n")
celcius = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu dalam Celcius:", celcius, "C")
reamur = (4/5) * celcius
print("Suhu dalam Reamur:", reamur, "R")
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit:", fahrenheit, "F")
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin, "K")

# Konversi fahrenheit ke satuan lain
print("\nKonversi Fahrenheit ke satuan lain\n")
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
print("Suhu dalam Fahrenheit:", fahrenheit, "F")
celcius = (5/9) * (fahrenheit - 32)
print("Suhu dalam Celcius:", celcius, "C")
reamur = (4/9) * (fahrenheit - 32)
print("Suhu dalam Reamur:", reamur, "R")
kelvin = (5/9) * (fahrenheit - 32) + 273
print("Suhu dalam Kelvin:", kelvin, "K")

# Konversi reamur ke satuan lain 
print("\nKonversi Reamur ke satuan lain\n")
reamur = float(input("Masukkan suhu dalam Reamur: "))
print("Suhu dalam Reamur:", reamur, "R")
celcius = (5/4) * reamur
print("Suhu dalam Celcius:", celcius, "C")
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit:", fahrenheit, "F")
kelvin = (5/4) * reamur + 273
print("Suhu dalam Kelvin:", kelvin, "K")

# Konversi kelvin ke satuan lain
print("\nKonversi Kelvin ke satuan lain\n")
kelvin = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu dalam Kelvin:", kelvin, "K")
celcius = kelvin - 273
print("Suhu dalam Celcius:", celcius, "C")
fahrenheit = (9/5) * (kelvin - 273) + 32
print("Suhu dalam Fahrenheit:", fahrenheit, "F")
reamur = (4/5) * (kelvin - 273)
print("Suhu dalam Reamur:", reamur, "R")