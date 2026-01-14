import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Halo siapa namamu?")

NAMADEPAN = tk.StringVar()
NAMABELAKANG = tk.StringVar()
def tombolClick():
    """print(NAMADEPAN.get())
    print(NAMABELAKANG.get())"""
    pesan = f"Hello {NAMADEPAN.get()} {NAMABELAKANG.get()}, keren"
    showinfo(title="Hello!!",message=pesan)

# Frame
inputFrame = ttk.Frame(window)
inputFrame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen
# Label nama depan
labelNamaDepan = ttk.Label(inputFrame,text="Nama depan:")
labelNamaDepan.pack(fill="x",expand=True)

# Entry nama depan
entryNamaDepan = ttk.Entry(inputFrame,textvariable=NAMADEPAN)
entryNamaDepan.pack(fill="x",expand=True)

# Label nama belakang
labelNamaBelakang = ttk.Label(inputFrame,text="Nama belakang:")
labelNamaBelakang.pack(fill="x",expand=True)

# Entry nama belakang
entryNamaBelakang = ttk.Entry(inputFrame,textvariable=NAMABELAKANG)
entryNamaBelakang.pack(fill="x",expand=True)

# Tombol
tombolSapa = ttk.Button(inputFrame,text="Hello!!!",command=tombolClick)
tombolSapa.pack(fill="x",expand=True,padx=10,pady=10)

# Main loop
window.mainloop()