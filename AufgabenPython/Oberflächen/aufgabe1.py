
import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
class guui:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine GUI")
        self.titel = tk.Label(self.root, text="Vorname")
        self.titel.pack()
        self.__vorname = tk.Entry(self.root, text="Vorname")
        self.__vorname.pack()
        self.titel2 = tk.Label(self.root, text="Nachname")
        self.titel2.pack()
        self.__nachname = tk.Entry(self.root, text="Nachname")
        self.__nachname.pack()
        self.__button = tk.Button(self.root, text="Klick mich!", command=self.button_click)
        self.__button.pack()
        self.img = tk.PhotoImage(file="C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Download-removebg-preview.png")
        self.label = tk.Label(self.root, image=self.img)
        self.label.pack()


    def button_click(self):
        setext = self.__vorname.get() 
        self.titel.config(text=setext)
        setext = self.__nachname.get()
        self.titel2.config(text=setext)


GUI = guui(root)
root.mainloop()