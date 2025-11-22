import tkinter as tk
import p3_osztaly

class KockaApp(p3_osztaly.KockaDobas):
    def __init__(self, master):
        super().__init__(master)

if __name__ == '__main__':
    root = tk.Tk()
    app = KockaApp(root)
    tk.mainloop()