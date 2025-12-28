# Operator assignment itu operasi yang disingkat di Python

# Operasi aritmatika dengan assignment
a = 10
print('Nilai a =', a)

a += 5
print('Nilai a += 5 adalah', a)

a -= 3
print('Nilai a -= 3 adalah', a)

a *= 2
print('Nilai a *= 2 adalah', a)

a /= 4
print('Nilai a /= 4 adalah', a)

b = 10
print('\nNilai b =', b)
b %= 3
print('Nilai b %= 3 adalah', b)

c = 10
print('\nNilai c =', c)
c //= 3
print('Nilai c //= 3 adalah', c)

a = 5
print('\nNilai a =', a)
a **= 3
print('Nilai a **= 3 adalah', a)

# Operasi bitwise dengan assignment (OR)
c = True
print('\nNilai c =', c)
c |= False
print('Nilai c |= False adalah', c)
c = False
print('\nNilai c =', c)
c |= True
print('Nilai c |= True adalah', c)

# Operasi bitwise dengan assignment (AND)
c = True
print('\nNilai c =', c)
c &= False
print('Nilai c &= False adalah', c)
c = True
print('\nNilai c =', c)
c &= True
print('Nilai c &= True adalah', c)

# Operasi bitwise dengan assignment (XOR)
c = True
print('\nNilai c =', c)
c ^= False
print('Nilai c ^= False adalah', c)
c = True
print('\nNilai c =', c)
c ^= True
print('Nilai c ^= True adalah', c)

# geser geser
d = 0b1100
print('\nNilai d =', format(d,'06b'))
d >>= 2
print('Nilai d >>= 2 adalah', format(d,'06b'))
d <<= 1
print('Nilai d <<= 1 adalah', format(d,'06b'))