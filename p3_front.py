import tkinter as tk
import p3_osztaly

class KockaApp(p3_osztaly.KockaDobas):
    def __init__(self, master):
        super().__init__(master)

        self.api_gomb = tk.Button(self.master, text="Lekérés", command=self.api_lekeres())
        self.api_gomb.grid(row=3, column=0, pady=5)

        self.api_cimke = tk.Label(self.master, text="...")
        self.api_cimke.grid(row=3, column=1)

        self.api_dobas = tk.Button(self.master, text="Dobás a Back-ben", command=self.api_dobas())
        self.api_dobas.grid(row=4, column=0, pady=5)


    def api_lekeres(self):
        pass


    def api_dobas(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = KockaApp(root)
    tk.mainloop()