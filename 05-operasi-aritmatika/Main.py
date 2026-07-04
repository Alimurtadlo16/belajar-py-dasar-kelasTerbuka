# Operasi aritmatika dasar di Python

a = 15
b = 20
c = 35

# Penjumlahan +
hasil = a + b + c
print(a,'+',b,'+',c,'=', hasil)

# Pengurangan -
hasil = c - b - a
print(c,'-',b,'-',a,'=', hasil)

# Perkalian *
hasil = a * b * c
print(a,'*',b,'*',c,'=', hasil)

# Pembagian /
hasil = c / a / b
print(c,'/',a,'/',b,'=', hasil)

# Eksponen (pangkat) **
hasil = a ** b 
print(a,'**',b,'=', hasil)

# Modulus %
hasil = c % a 
print(c,'%',a,'=', hasil)   

# Floor Division //
hasil = c // b 
print(c,'//',b,'=', hasil)

# Operational precedence
"""
    - Eksponen (pangkat) **
    - Perkalian *, Pembagian /, Modulus %, Floor Division //
    - Penjumlahan +, Pengurangan -
"""
hasil = a + b * c - a / b ** a % c // b
print('(',a,'+',b,')','*',c,'-',a,'/',b,'**',a,'%',c,'//',b,'=', hasil)