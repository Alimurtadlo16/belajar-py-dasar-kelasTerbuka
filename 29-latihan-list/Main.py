# Program list buku dalam python

listBuku = []
while True:
    judul = input("\nMasukkan judul buku\t: ").strip()
    penulis = input("Masukkan penulis buku\t: ").strip()
    bukuBaru = [judul,penulis]
    listBuku.append(bukuBaru)
    print(f"{'No.':<5} | {'Judul':<20} | {'Penulis':<15}")
    print("~" * 45)  
    for index,buku in enumerate(listBuku):
        print(f"{index+1:<5} | {buku[0]:<20} | {buku[1]:<15}")
    print("~" * 50)
    isLanjut = input("Apakah mau dilanjutkan?(y/n) ")
    if isLanjut ==  "n":
        break
print("Program diberhentikan")