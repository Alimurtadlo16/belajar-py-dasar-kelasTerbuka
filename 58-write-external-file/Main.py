# Mode write (Tetap "w" jika tujuannya memang menimpa/memulai dari awal)
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Ahmad Ali Murtadlo Asadillah\n")

# Mode append (Ganti "w" menjadi "a" agar data bertambah)
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Mahasiswa universitas darussalam gontor\n")

# Untuk data2.txt juga gunakan "a"
with open("data2.txt", "a", encoding="utf-8") as file:
    file.write("\nData tambahan baru")

# Mode r+
with open("data.txt", 'r+', encoding="utf-8") as file:
    # Memindahkan kursor ke ujung akhir file sebelum menulis
    file.seek(0, 2) 
    file.write("Alumni gontor 2025")
    
    file.seek(0)
    data = file.read()
    print(data)