import tkinter as tk
import sqlite3


class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabellen Generator")

        self.conn = sqlite3.connect("meinedatenbank.db")
        self.cursor = self.conn.cursor()

        self.txtname = tk.Label(self.root, text="Wie soll die Tabelle heißen?")
        self.txtname.grid(row=0, column=0, padx=10, pady=10)

        self.name = tk.Entry(self.root)
        self.name.grid(row=0, column=1, padx=10, pady=10)

        self.big = tk.Label(self.root, text="Wie viele Spalten soll die Tabelle haben?")
        self.big.grid(row=1, column=0, padx=10, pady=10)

        self.bigEingabe = tk.Entry(self.root)
        self.bigEingabe.grid(row=1, column=1, padx=10, pady=10)

        self.button = tk.Button(self.root, text="Tabellen erstellen", command=self.button_click)
        self.button.grid(row=2, column=0, padx=10, pady=10)

    def button_click(self):
        tabellenname = self.name.get().strip()

        try:
            spaltenanzahl = int(self.bigEingabe.get())
        except ValueError:
            print("Bitte eine gültige Zahl eingeben!")
            return

        if tabellenname == "":
            print("Tabellenname darf nicht leer sein!")
            return

        self.open_second_window(tabellenname, spaltenanzahl)

    def open_second_window(self, name, spalten):
        self.second = tk.Toplevel(self.root)
        self.second.title("Spalten definieren")

        self.entries = []
        self.types = []

        for i in range(spalten):
            label = tk.Label(self.second, text=f"Spalte {i+1}")
            label.grid(row=0, column=i, padx=10, pady=10)

            entry = tk.Entry(self.second)
            entry.grid(row=1, column=i, padx=10, pady=10)
            self.entries.append(entry)

            var = tk.StringVar(value="TEXT")
            dropdown = tk.OptionMenu(self.second, var, "TEXT", "INTEGER")
            dropdown.grid(row=2, column=i, padx=10, pady=10)
            self.types.append(var)

        self.save_button = tk.Button(
            self.second,
            text="In DB speichern",
            command=lambda: self.save_in_db(name, spalten)
        )
        self.save_button.grid(row=3, column=0, padx=10, pady=10)

    def save_in_db(self, name, spalten):
        spalten_sql = []

        for i in range(spalten):
            spaltenname = self.entries[i].get().strip()
            typ = self.types[i].get()

            if spaltenname == "":
                print("Spaltenname darf nicht leer sein!")
                return

            spalten_sql.append(f"{spaltenname} {typ}")

        sql = f"CREATE TABLE IF NOT EXISTS {name} ({', '.join(spalten_sql)});"

        print("SQL:", sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("Tabelle erfolgreich erstellt!")
        except Exception as e:
            print("Fehler:", e)

        self.second.destroy()


root = tk.Tk()
app = Gui(root)
root.mainloop()