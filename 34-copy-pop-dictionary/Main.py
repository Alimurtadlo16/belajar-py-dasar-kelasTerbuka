# Copy  and pop in dictionary dalam python

manteman = {
    "Dam":"Adam",
    "Kar":"Karbit",
    "Sep":"Joseph",
    "Steve":"Steven",
    "Li":"Ali Murtadlo"
}
friends = manteman.copy()
print(f"Teman teman: {manteman}\n")
print(f"Friends:{friends}\n")
manteman["sep"] = "Joseph ganteng"
print(f"Teman teman: {manteman}\n")
print(f"Friends:{friends}\n")

# Pop dictionary (Berdasarkan keyc)
dataAli = friends.pop("Li")
print(f"Data ali: {dataAli}\n")
print(f"Friends: {friends}\n")

# Popitem dictionary (Yang terakhir)
dataTerakhir = friends.popitem()
print(f"Data akhir: {dataTerakhir}\n")
print(f"Friends: {friends}\n")