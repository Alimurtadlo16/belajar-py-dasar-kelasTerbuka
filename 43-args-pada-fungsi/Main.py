# Args fungsi dalam python

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("Ali murtadlo", 169, 40)

def fungsi_args(data):
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi_args(("Joseph", 165, 59))

def fungsi_args2(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi_args2("William", 159, 38)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output
hasil = tambah(1,2,3,4,5,6,7,8,9,99)
print(f"Hasil = {hasil}")