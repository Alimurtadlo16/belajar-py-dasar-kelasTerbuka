# Looping dictionary dalam python

manteman = {
    "Dam":"Adam",
    "Kar":"Karbit",
    "sep":"Joseph",
    "Steve":"Steven",
    "Li":"Ali Murtadlo"
}

# Looping pertama adalah key
for teman in manteman:
    print(teman)

# Operator untuk mengambil item
keys = manteman.keys()
print(keys)
for key in manteman.keys():
    print(manteman.get(key))

values = manteman.values()
print(values)
for value in manteman.values():
    print(value)

items = manteman.items()
print(items)
for item in manteman.items():
    print(item)

for key,value in manteman.items():
    print(f"Key: {key}, Value: {value}")