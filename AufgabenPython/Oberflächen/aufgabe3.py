import tkinter as tk
import tkinter.messagebox as messagebox
root = tk.Tk()
root.geometry("400x300")
class gui:
    listbox = None
    label = None

    def __init__(self, root):
        self.root = root
        self.root.title("Meine GUI")
        self.label = tk.Label(self.root, text="Inhalt der Datei:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=1, column=0, padx=10, pady=10)    
        self.button = tk.Button(self.root, text="Ausgabe", command=self.button_click)
        self.button.grid(row=2, column=0, padx=10, pady=10)
        self.vorname = tk.Entry(self.root, text="Vorname", )
        self.vorname.grid(row=1, column=1, padx=10, pady=10)
        self.nachname = tk.Entry(self.root, text="Nachname")
        self.nachname.grid(row=2, column=1, padx=10, pady=10)
        self.strasse = tk.Entry(self.root, text="Straße")
        self.strasse.grid(row=3, column=1, padx=10, pady=10)
        self.plz = tk.Entry(self.root, text="PLZ")
        self.plz.grid(row=4, column=1, padx=10, pady=10)
        self.ort = tk.Entry(self.root, text="Ort")
        self.ort.grid(row=5, column=1, padx=10, pady=10)
        self.infos = [self.vorname, self.nachname, self.strasse, self.plz, self.ort]
        self.button2 = tk.Button(self.root, text="Hinzufügen", command=self.button2_click)
        self.button2.grid(row=2, column=1, padx=10, pady=10)
    def button2_click(self):
        try:
            neuername = self.infos.get(0, "end")
            with open("C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\namen.txt", "a") as file:
                file.write(neuername + "\n")
            messagebox.showinfo("Erfolg", f"{neuername} wurde hinzugefügt.")
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Die Datei wurde nicht gefunden.")
    def button_click(self):
        self.listbox.delete(0, tk.END)
        try:
            with open("C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\namen.txt", "r") as file:
                content = file.read().splitlines()
            for item in content:
                self.listbox.insert(tk.END, item)
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Die Datei wurde nicht gefunden.")

GUI = gui(root)
root.mainloop()