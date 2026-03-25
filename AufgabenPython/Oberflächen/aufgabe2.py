import tkinter as tk
import tkinter.messagebox as messagebox
root = tk.Tk()
root.geometry("400x300")
class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine GUI")
        self.img = tk.PhotoImage(file="C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Download-removebg-preview.png")
        self.label = tk.Label(self.root, image=self.img)
        self.label.grid(row=0, column=2, padx=10, pady=10)
        self.scale = tk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL, label="Bewertung")
        self.scale.grid(row=0, column=0, padx=10, pady=10)
        self.button = tk.Button(self.root, text="OK", command=self.button_click)
        self.button.grid(row=1, column=0, padx=10, pady=10)
    def button_click(self):
        messagebox.showinfo("Rückmeldung", f"Danke für die Bewertung: {self.scale.get()}")
GUI = gui(root)
root.mainloop()