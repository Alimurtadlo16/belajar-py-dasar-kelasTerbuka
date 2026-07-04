from numbers import Number

def tambah(a, b):
    if not isinstance(a, Number):
        raise TypeError("Input pertama harus angka")
    
    if not isinstance(b, Number):
        raise TypeError("Input kedua harus angka")
        
    # UBAH BAGIAN INI: Hapus tanda kutip agar memanggil variabel a dan b
    return a + b 

try:
    # Sekarang hasilnya akan menjadi 104
    print(tambah(5, 99)) 
except TypeError as e:
    print(f"Eror ditemukan: {e}")