# List dalam python

# Kumpulan data angka
dataAngka = [1,2,3,4,5,6,7,8,9]
print(dataAngka)
print("\n")

# Kumpulan data string
dataString = ["Ahmad","Ali","Murtadlo","Asadillah"]
print(dataString)
print("\n")

# Kumpulan boolean
dataBoolean = [True, False]
print(dataBoolean)
print("\n")

# Kumpulan campuran data
dataCampur = [1,"Ahmad",2,"Ali",3,"Murtadlo",4,"Asadillah"]
print(dataCampur)
print("\n")

# Cara alternatif dalam list
dataRange = range(0,10,2)
dataList = list(dataRange)
print(dataList)
print("\n")

# List dengan loop comprehension
listFor = [i**10 for i in range(0,10)]
print(listFor)
print("\n")

# List dengan for if
listForIf = [i for i in range(0,10) if i != 5]
print(listForIf)
print("\n")

# Ganjil
listForIf = [i for i in range(0,10) if i%2 ==0]
print(listForIf)
print("\n")

# Genap
listForIf = [i**2 for i in range(0,10) if i%2 ==0]
print(listForIf)
print("\n")