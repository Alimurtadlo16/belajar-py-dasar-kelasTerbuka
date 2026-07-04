#Tipe casting dalam Python adalah proses mengubah tipe data dari suatu nilai ke tipe data lainnya.

#Contoh int ke float, str, bool
print("=====Int=====")
nilai_int = 99
print("nilai int:", nilai_int, "tipe:", type(nilai_int))

nilai_float_dari_int = float(nilai_int)
nilai_str_dari_int = str(nilai_int)
nilai_bool_dari_int = bool(nilai_int) #Bernilai false ketika nilai int = 0 selain itu bernilai true
print("nilai float:", nilai_float_dari_int, "tipe:", type(nilai_float_dari_int))
print("nilai str:", nilai_str_dari_int, "tipe:", type(nilai_str_dari_int))
print("nilai bool:", nilai_bool_dari_int, "tipe:", type(nilai_bool_dari_int))

#Contoh float ke int, str, bool
print("=====float=====")
nilai_float = 99.99
print("nilai float:", nilai_float, "tipe:", type(nilai_float))

nilai_int_dari_float = int(nilai_float)
nilai_str_dari_float = str(nilai_float)
nilai_bool_dari_float = bool(nilai_float) #Bernilai false ketika nilai float = 0.0 selain itu bernilai true
print("nilai int:", nilai_int_dari_float, "tipe:", type(nilai_int_dari_float))
print("nilai str:", nilai_str_dari_float, "tipe:", type(nilai_str_dari_float))
print("nilai bool:", nilai_bool_dari_float, "tipe:", type(nilai_bool_dari_float))

#Contoh bool ke int, float, str
print("=====bool=====")
nilai_bool = True
print("nilai bool:", nilai_bool, "tipe:", type(nilai_bool))

nilai_int_dari_bool = int(nilai_bool)
nilai_float_dari_bool = float(nilai_bool)
nilai_str_dari_bool = str(nilai_bool)
print("nilai int:", nilai_int_dari_bool, "tipe:", type(nilai_int_dari_bool))
print("nilai float:", nilai_float_dari_bool, "tipe:", type(nilai_float_dari_bool))
print("nilai str:", nilai_str_dari_bool, "tipe:", type(nilai_str_dari_bool))

#Contoh str ke int, float, bool
print("=====str=====")
nilai_str = "100"
print("nilai str:", nilai_str, "tipe:", type(nilai_str))

nilai_int_dari_str = int(nilai_str)
nilai_float_dari_str = float(nilai_str)
nilai_bool_dari_str = bool(nilai_str) #Bernilai false ketika str kosong selain itu bernilai true
print("nilai int:", nilai_int_dari_str, "tipe:", type(nilai_int_dari_str))
print("nilai float:", nilai_float_dari_str, "tipe:", type(nilai_float_dari_str))
print("nilai bool:", nilai_bool_dari_str, "tipe:", type(nilai_bool_dari_str))