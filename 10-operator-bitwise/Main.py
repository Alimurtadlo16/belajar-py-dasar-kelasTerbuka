# Operasi bitwise atau biner atau binary di Python 

a = 99
b = 93

# Bitwise Or (|)
c = a | b
print('\n==== BITWISE OR (|) =====')
print('Nilai :', a,',binary:',format(a, '08b'))
print('Nilai :', b,',binary:',format(b, '08b'))
print('-----------------------(|)')
print('Hasil :', c,',binary:',format(c, '08b'))

# Bitwise And (&)
c = a & b
print('\n==== BITWISE AND (&) =====')
print('Nilai :', a,',binary:',format(a, '08b'))
print('Nilai :', b,',binary:',format(b, '08b'))
print('-----------------------(&)')
print('Hasil :', c,',binary:',format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n==== BITWISE XOR (^) =====')
print('Nilai :', a,',binary:',format(a, '08b'))
print('Nilai :', b,',binary:',format(b, '08b'))
print('-----------------------(^)')
print('Hasil :', c,',binary:',format(c, '08b'))

# Bitwise NOT (~)
c = ~a
print('\n==== BITWISE NOT (~) =====')
print('Nilai :', a,',binary:',format(a, '08b'))
print('-----------------------(~)')
print('Hasil :', c,',binary:',format(c & 0xff, '08b'))
print('-----------------------(^)')
d = 0b00000010011100
e = 0b00000000110111
print('nilai :',e^d,',binary:',format(e^d,'08b'))

# Shift right (>>)
c = a >> 2
print('\n==== SHIFT RIGHT (>>) =====')
print('Nilai :', a,',binary:',format(a, '08b'))
print('-----------------------(>> 2)')
print('Hasil :', c,',binary:',format(c, '08b'))

# Shift left (<<)
c = a << 2
print('\n==== SHIFT LEFT (<<) =====')
print('Nilai :', a,',binary:',format(a, '08b'))
print('-----------------------(<< 2)')
print('Hasil :', c,',binary:',format(c, '08b'))