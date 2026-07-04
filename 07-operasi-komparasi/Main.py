# Operasi Komparasi dalam Python
# Hasil dari operasi komparasi adalah nilai boolean

a = 80
b = 95

# Lebih dari
hasil = a > b
print(a,'>',b,'=', hasil)  

# Kurang dari
hasil = a < b
print(a,'<',b,'=', hasil)

# Sama dengan
hasil = a == b
print(a,'==',b,'=', hasil)

# Lebih dari sama dengan
hasil = a >= b
print(a,'>=',b,'=', hasil)

# Kurang dari sama dengan
hasil = a <= b
print(a,'<=',b,'=', hasil)

# Tidak sama dengan
hasil = a != b
print(a,'!=',b,'=', hasil)

# "is" sebagai komparasi object identity
x = 99
y = 93
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# "is not" sebagai komparasi object identity
hasil = x is not y
print('x is not y =', hasil)