# __Main__ untuk top level code environtment

"""
# C
int main(){

}
# Java
class Main(){
    static void main(){
    
    }
}
"""

# __name__ == "__main__"
print(f"Nilai name pada Main.py: {__name__}")

# __name__ pada program external
import Fungsi

# Contoh penggunaan __main__

# Deklarasi
def fungsiTambah(a:int,b:int) -> int:
    return a + b

# Fungsi utama
if __name__ == "__main__":
    angka1 = 9
    angka2 = 99
    hasil = fungsiTambah(angka1,angka2)
    print(f"Hasil tambah: {hasil}")

# python -m Fungsi.py