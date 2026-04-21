import tkinter as tk

root = tk.Tk()
root.title("Dropdown Beispiel")

# Variable für Auswahl
auswahl = tk.StringVar()
auswahl.set("Option 1")  # Standardwert

# Dropdown erstellen
dropdown = tk.OptionMenu(root, auswahl, "Option 1", "Option 2", "Option 3")
dropdown.pack()

# Anzeige der Auswahl
label = tk.Label(root, textvariable=auswahl)
label.pack()

root.mainloop()