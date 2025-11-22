import tkinter as tk
from tkinter import messagebox
import random

def dobas(dobasok):
    eredmenyek = [0 for _ in range(7)]
    for _ in range(dobasok):
        szam = random.randint(1, 6)
        eredmenyek[szam] += 1
    eredmeny_cimke_szoveg.set(
        f"1 -- {eredmenyek[1]}\n"
        f"2 -- {eredmenyek[2]}\n"
        f"3 -- {eredmenyek[3]}\n"
        f"4 -- {eredmenyek[4]}\n"
        f"5 -- {eredmenyek[5]}\n"
        f"6 -- {eredmenyek[6]}\n"
    )

def on_dobas():
    try:
        dobasok_szama = int(dobasok_szama_bemenet.get())
        dobas(dobasok_szama)
    except:
        messagebox.showerror("Hiba", "Rossz értéket adott meg!")


root = tk.Tk()
root.title("Kockadobás statisztika")
root.geometry("600x400")

cim_cimke = tk.Label(text="Kockadobások", font=("Arial", 16))
cim_cimke.grid(column=1, row=0, padx=10, pady=10)

dobasok_szama_bemenet = tk.StringVar(value="10")
dobasszam = tk.Entry(root, textvariable=dobasok_szama_bemenet, width=10)
dobasszam.grid(column=0, row=1, padx=50, pady=10)

eredmeny_cimke_szoveg = tk.StringVar(value="...\n...\...")
eredmeny_cimke = tk.Label(root, textvariable=eredmeny_cimke_szoveg, font=("Arial", 16))
eredmeny_cimke.grid(column=1, row=2, pady=20)

gomb = tk.Button(root, text="Dobás", command = on_dobas)
gomb.grid(row=1, column=2)

kilepes = tk.Button(root, text="Kilépés", command=root.destroy)
kilepes.grid(column=3, row=1, padx=10)

tk.mainloop()