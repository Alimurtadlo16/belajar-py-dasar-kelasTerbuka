import os

# Membuka file dengan open
# Mencari lokasi folder dari file Main.py ini berada
script_dir = os.path.dirname(__file__) 
# Menggabungkan lokasi folder dengan nama file target
file_path = os.path.join(script_dir, "DataSupra.txt")

print(3*"=", " Membaca file external ", 3*"=")

# PINDAHKAN ATAU TAMBAHKAN DI DALAM BLOK WITH
# Membaca semua baris
with open(file_path, mode="r") as file:
    # Baris ini ditambahkan di sini agar 'file' bisa dikenali
    print(f"Status read: {file.readable()}") 
    print(file.read())
    
# Membaca perbaris
with open(file_path, mode="r") as file:
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    print(file.readline(),end=" ")
    
# Membaca semua baris sebagai list
with open(file_path, mode="r") as file:
    print(file.readlines())

print(f"\nApakah file sudah ditutup? {file.closed}")
file.close()
print(f"Apakah file sudah ditutup? {file.closed}")

# Membuka file dengan with
with open(file_path, mode="r") as file:
    content = file.read()
    print(content,end="")
    print(content)
    print(f"Apakah file sudah ditutup? {file.closed}")
print(f"Apakah file sudah ditutup? {file.closed}")