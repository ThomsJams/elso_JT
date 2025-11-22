import tkinter as tk
import p3_osztaly
from tkinter import messagebox
import requests

class KockaApp(p3_osztaly.KockaDobas):
    def __init__(self, master):
        super().__init__(master)

        self.api_gomb = tk.Button(self.master, text="Lekérés", command=self.api_lekeres)
        self.api_gomb.grid(row=3, column=0, pady=5)

        self.api_cimke = tk.Label(self.master, text="...")
        self.api_cimke.grid(row=3, column=1)


        self.api_dobas = tk.Button(self.master, text="Dobás a Back-ben", command=self.api_dobas_fgv)
        self.api_dobas.grid(row=4, column=0, pady=5)

    def api_lekeres(self):
        try:
            valasz = requests.get("http://localhost:5000/api/data", timeout=5)
            valasz.raise_for_status()
            adat = valasz.json()
            self.api_cimke.config(text=adat["uzenet"])
            self.dobasok_szama_bemenet.set(adat["uzenet"])
        except Exception as e:
            print(e)
            messagebox.showerror("Hiba", "Kapcsolat létrehozása sikertelen")


    def api_dobas_fgv(self):
        try:
            dbszam = int(self.dobasok_szama_bemenet.get())
            valasz = requests.get(f"http://localhost:5000/api/dobas/{dbszam}", timeout=5)
            valasz.raise_for_status()
            adat = valasz.json()
            eredmenyek = adat["eredmenyek"]
            self.eredmeny_cimke_szoveg.set("\n".join(f"{i+1} -- {eredmenyek[i]}" for i in range(6)))
        except Exception as e:
            print(e)
            messagebox.showerror("Hiba", "Kapcsolat létrehozása sikertelen")

if __name__ == '__main__':
    root = tk.Tk()
    app = KockaApp(root)
    tk.mainloop()