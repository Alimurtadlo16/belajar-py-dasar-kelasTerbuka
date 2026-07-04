# Operator dictionary dalam python

dataDict = {
    "Li":"Ali",
    "Sep":"Joseph",
    "Steve":"Steven"
}

# Panjang dictionary
LENDICT = len(dataDict)
print(f"Panjang dictionary: {LENDICT}")

# Mengecek key exist
KEY = "Li" # True
CHECKKEY = KEY in dataDict
print(f"Apakah {KEY} ada pada data?: {CHECKKEY}")
KEY = "Ali" # False
CHECKKEY = KEY in dataDict
print(f"Apakah {KEY} ada pada data?: {CHECKKEY}")

# Mengakses value dengan get
print(dataDict["Li"])
print(dataDict.get("Li"))
print(dataDict.get("Ali","Nama tidak ditemukan")) # Mengcroscek data

# Mengupdate data
dataDict["Li"] = "Ali Murtadlo"
print(dataDict)

dataDict.update({"Li":"Ali"})
print(dataDict)
dataDict.update({"Di":"Darmaji"})
print(dataDict)

# Menghapus data pada dictionary
# Catatan: "Ali" adalah value, bukan key. Key yang ada: "Li", "Sep", "Steve", "Di"
# Mengubah untuk menghapus key "Li" yang memiliki value "Ali"
del dataDict["Li"]
print(dataDict)