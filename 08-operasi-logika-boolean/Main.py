# Operasi logika boolean dalam Python

# Not 
print("==== NOT ====")
a = True
c = not a
print("data a =", a)
print("data c =", c)

# Or
print("==== OR ====")
a = False
b = True
c = not a 
print(a,"or",b,"=",c)
a = True
b = False
c = not a 
print(a,"or",b,"=",c)
a = False
b = False
c = not a 
print(a,"or",b,"=",c)
a = True
b = True
c = not a 
print(a,"or",b,"=",c)

# And
print("==== AND ====")
a = True
b = False
c = a and b
print(a,"and",b,"=",c)
a = False
b = True
c = a and b
print(a,"and",b,"=",c)
a = False
b = False
c = a and b
print(a,"and",b,"=",c)
a = True
b = True
c = a and b
print(a,"and",b,"=",c)

# Xor
print("==== XOR ====")
a = True 
b = False
c = a ^ b
print(a,"xor",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"xor",b,"=",c)
a = False
b = False
c = a ^ b
print(a,"xor",b,"=",c)
a = True
b = True
c = a ^ b
print(a,"xor",b,"=",c)