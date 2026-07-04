import numpy as np

listA = [1,2,3,4,5,99]
vectorA= np.array([1,2,3,4,5,99])

# List tidak bisa dipangkat
# print(listA**2)
print(f"ListA: {listA}")
print(vectorA**2)
print(f"Vector A: {vectorA}")

# Matrix
matrixB = np.array([(99,699),(2025,1446)])
print(f"Matrix b: \n{matrixB}")
print(f"Matrix b: \n{matrixB**2}")

# Zeros
zerosC = np.zeros((2,2))
print(f"Zeros: \n{zerosC}")

onesD = np.ones((2,2))
print(f"Zeros: \n{onesD}")

jumlah = matrixB + matrixB**2 + onesD
print(f"Jumlah: {jumlah}")