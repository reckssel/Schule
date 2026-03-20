import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
class gui:
    def __init__(self, master):
        self.master = master
        self.master.title("Meine GUI")
        self.img = tk.PhotoImage(file="C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Download-removebg-preview.png")
        self.label = tk.Label(self.master, image=self.img)
        self.label.pack()

GUI = gui(root)
root.mainloop()