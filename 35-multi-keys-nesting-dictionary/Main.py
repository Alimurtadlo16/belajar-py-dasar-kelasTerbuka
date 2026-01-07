# Multi Keys Dan Nesting Dictionary

import datetime
mahasiswa1 = {
    "Nama" : "Ahmad Ali Murtadlo Asadillah",
    "NIM"  : "462025....",
    "Sks Lulus" : "130",
    "Beasiswa" : False,
    "Lahir" : datetime.datetime(2007,11,16)
}
mahasiswa2 = {
    "Nama" : "Joseph",
    "NIM"  : "462025....",
    "Sks Lulus" : "130",
    "Beasiswa" : False,
    "Lahir" : datetime.datetime(2008,5,10)
}
mahasiswa3 = {
    "Nama" : "William",
    "NIM"  : "462025....",
    "Sks Lulus" : "130",
    "Beasiswa" : False,
    "Lahir" : datetime.datetime(2009,8,6)
}
dataMahasiswa = {
    'Mah01' : mahasiswa1,
    'Mah02' : mahasiswa2,
    'Mah03' : mahasiswa3
}
print(f"{'KEY': <6} {'Nama': <36} {'SKS': <3} {'Beasiswa': <9} {'Lahir': <10}")
print("-"*50)
for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    NAMA = dataMahasiswa[KEY]['Nama']
    SKS = dataMahasiswa[KEY]['Sks Lulus']
    BEASISWA = dataMahasiswa[KEY]['Beasiswa']
    LAHIR = dataMahasiswa[KEY]['Lahir'].strftime("%x")
    print(f"{KEY: <6} {NAMA: <36} {SKS: <3} {str(BEASISWA): ^9} {LAHIR: <10}")