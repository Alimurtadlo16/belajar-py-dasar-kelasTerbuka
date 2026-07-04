#Cara meminta input dari user dan menampilkannya kembali

#Data yang dimasukkan pasti string
data = input("Masukkan data: ") 
print("data:", data, "tipe:", type(data))

#Jika ingin mengubah tipe data, bisa dilakukan tipe casting
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))
print("data:", angka, "tipe:", type(angka))

#Contoh boolean
biner = bool(int(input("Masukkan nilai boolean: "))) 
print("data:", biner, "tipe:", type(biner))