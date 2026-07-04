# Width dan multiline alignment pada string

# Data string (Biasa)
data = "Ahmad Ali Murtadlo Asadillah"
umur = 18
tinggi = 169
sepatu = 45
dataLengkap = f"Nama: {data}, Umur: {umur}, Tinggi: {tinggi} cm, Ukuran Sepatu: {sepatu}\n"
print(15*"="+" Data Lengkap "+15*"=")
print(dataLengkap)

# Multiline enter
dataLengkap = f"Nama: {data}, \nUmur: {umur}, \nTinggi: {tinggi} cm, \nUkuran Sepatu: {sepatu}\n"
print(15*"="+" Data Lengkap "+15*"=")
print(dataLengkap)

# Multiline kutip
dataLengkap = f"""Nama: {data},
Umur: {umur},
Tinggi: {tinggi} cm,
Ukuran Sepatu: {sepatu}"""
print(15*"="+" Data Lengkap "+15*"=")
print(dataLengkap)

# Mengatur lebar string
dataLengkap = f"""
Nama            : {data:>5},
Umur            : {umur:>3},
Tinggi          : {tinggi:>4} cm,
Ukuran Sepatu   : {sepatu:>3}"""
print(15*"="+" Data Lengkap "+15*"=")
print(dataLengkap)