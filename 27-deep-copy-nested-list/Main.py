# Deep Copy Nested List dalam python

# Contoh 1
data0 = [1,2]
data1 = [3,4]
data2D = [data0,data1,10]
data2DCopy = data2D.copy()
print(f"Semua data: {data2D}\n")

# Contoh 2
data = data2D[1][0]
print(f"Data: {data}\n")

# Contoh  3
print(f"Data address asli: {hex(id(data2D))}")
print(f"Data address copy: {hex(id(data2DCopy))}\n")

# Contoh 4
print("Address dari member 1")
print(f"Data address asli: {hex(id(data2D[0]))}")
print(f"Data address copy: {hex(id(data2DCopy[0]))}\n")

# Contoh 5
data = data2D[1][0] = 5
data = data2D[2] = 9
print(f"Data address asli: {hex(id(data2D))}")
print(f"Data address copy: {hex(id(data2DCopy))}\n")

# Contoh 6
from copy import deepcopy
data2D = [data0,data1,10]
data2DDeepCopy = deepcopy(data2D)
print(f"Data address asli: {hex(id(data2D))}")
print(f"Data address copy: {hex(id(data2DDeepCopy))}\n")

print("Address dari member 1")
print(f"Data address asli: {hex(id(data2D[0]))}")
print(f"Data address copy: {hex(id(data2DDeepCopy[0]))}\n")

data2D[1][0] = 30
print(f"Data: {data}")
print(f"Data address asli: {hex(id(data2D))}")
print(f"Data address copy: {hex(id(data2DDeepCopy))}\n")
