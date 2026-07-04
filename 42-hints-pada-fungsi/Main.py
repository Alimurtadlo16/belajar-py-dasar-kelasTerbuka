# Type hints pada python

import os
def fungsi(arguments:int) ->int :
    output = 10**arguments
    return output
hasil = fungsi(9)
print(hasil)

def display(argument:str):
    print(argument)
display("Ali murtadlo")

hasil = os.system("cls" if os.name == "nt" else "clear")
print(hasil)