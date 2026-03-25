import tkinter as tk
import tkinter.messagebox as messagebox
root = tk.Tk()
root.geometry("400x300")
class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine GUI")
        self.textVorname = tk.Label(self.root, text="Vorname")
        self.textVorname.grid(row=0, column=0, padx=10, pady=10)
        self.Vorname = tk.Entry(self.root)
        self.Vorname.grid(row=0, column=1, padx=10, pady=10)
        self.textNachname = tk.Label(self.root, text="Nachname")
        self.textNachname.grid(row=1, column=0, padx=10, pady=10)
        self.Nachname = tk.Entry(self.root)
        self.Nachname.grid(row=1, column=1, padx=10, pady=10)
        self.textStrasse = tk.Label(self.root, text="Straße")
        self.textStrasse.grid(row=2, column=0, padx=10, pady=10)
        self.Strasse = tk.Entry(self.root) 
        self.Strasse.grid(row=2, column=1, padx=10, pady=10)
        self.textPLZ = tk.Label(self.root, text="PLZ")
        self.textPLZ.grid(row=3, column=0, padx=10, pady=10)
        self.PLZ = tk.Entry(self.root)
        self.PLZ.grid(row=3, column=1, padx=10, pady=10)
        self.textOrt = tk.Label(self.root, text="Ort")
        self.textOrt.grid(row=4, column=0, padx=10, pady=10)
        self.Ort = tk.Entry(self.root)
        self.Ort.grid(row=4, column=1, padx=10, pady=10)
        self.button = tk.Button(self.root, text="Hinzufügen", command=self.button_click)
        self.button.grid(row=5, column=0, padx=10, pady=10)
        self.entfernen = tk.Label(self.root, text="Entfernen")
        self.entfernen.grid(row=1, column=2, padx=10, pady=10)
        self.entfernenEingabe = tk.Entry(self.root)
        self.entfernenEingabe.grid(row=1, column=3, padx=10, pady=10)
        self.button2 = tk.Button(self.root, text="Entfernen", command=self.button2_click)
        self.button2.grid(row=2, column=3, padx=10, pady=10)
        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=0, column=4, padx=10, pady=10)

    def button2_click(self):
        try:
            with open("C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Adressen.txt", "r") as file:
                lines = file.readlines()
            with open("C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Adressen.txt", "w") as file:
                for line in lines:
                    if self.entfernenEingabe.get() not in line:
                        file.write(line)
            messagebox.showinfo("Erfolg", f"{self.entfernenEingabe.get()} wurde entfernt.")
            self.show_addresses()
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Die Datei wurde nicht gefunden.")
    def button_click(self):
        try:
            with open("C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Adressen.txt", "a") as file:
                file.write(f"{self.Vorname.get()} {self.Nachname.get()}, {self.Strasse.get()}, {self.PLZ.get()}, {self.Ort.get()}\n")
            messagebox.showinfo("Erfolg", f"{self.Vorname.get()} {self.Nachname.get()} wurde hinzugefügt.")
            self.show_addresses()
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Die Datei wurde nicht gefunden.")
    def show_addresses(self):
        try:
            with open("C:\\Users\\zinemil\\Documents\\Schule\\AufgabenPython\\Oberflächen\\Adressen.txt", "r") as file:
                self.listbox.delete(0, tk.END)
                content = file.read().splitlines()
            for item in content:
                self.listbox.insert(tk.END, item)
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Die Datei wurde nicht gefunden.")
GUI = gui(root)
root.mainloop()