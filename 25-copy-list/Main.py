# Teknik menduplikat list

# Contoh 1
a = ["Ali", "Joseph", "Adam"]
print(f"a: {a}")
b = a
print(f"b: {b}")

# Contoh 2
a[1] = "Steven"
b.sort()
print(f"a: {a}")
print(f"b: {b}\n")

# Contoh 3
print(f"Address a:  {hex(id(a))}")
print(f"Address b:  {hex(id(b))}\n")

# Contoh 4
c = a.copy()
print(f"Address a:  {hex(id(a))}")
print(f"Address b:  {hex(id(b))}")
print(f"Address c:  {hex(id(c))}\n")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}\n")

# Contoh 5
c[0] = "Eve"
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}\n")

# Contoh 6
a[2] = "John"
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")