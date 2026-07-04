# Kwargs dalam python

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("Ali murtadlo", 169, 49)

def fungsi_kwargs(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(nama)
fungsi_kwargs(nama="Joseph", tinggi=159, berat=50)

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")
        return 0
    return output

hasil = math(1,2,3,4,5,6,7,8,9,99,option ="tambah")
print(f"Hasil jumlah {hasil}")
hasil = math(1,2,3,4,5,6,7,8,9,99,option ="kali")
print(f"Hasil kali {hasil}")