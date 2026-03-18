import tkinter as tk

# Farben & Design
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2a2a40"
ACCENT_COLOR = "#6c63ff"
TEXT_COLOR = "#ffffff"
HOVER_COLOR = "#5753c9"

root = tk.Tk()
root.title("Schöne Tkinter UI")
root.geometry("500x400")
root.configure(bg=BG_COLOR)

# Container (Card)
card = tk.Frame(root, bg=CARD_COLOR, bd=0, highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=250)

# Titel
title = tk.Label(
    card,
    text="Willkommen 👋",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=(20, 10))

# Eingabefeld
entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    bd=0,
    bg="#3a3a55",
    fg=TEXT_COLOR,
    insertbackground="white",
    justify="center"
)
entry.pack(pady=10, ipady=8, ipadx=10)

# Hover-Funktion
def on_enter(e):
    button['bg'] = HOVER_COLOR

def on_leave(e):
    button['bg'] = ACCENT_COLOR

# Button-Funktion
def action():
    text = entry.get()
    result_label.config(text=f"Hallo, {text}!")

# Button
button = tk.Button(
    card,
    text="Bestätigen",
    bg=ACCENT_COLOR,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    activebackground=HOVER_COLOR,
    cursor="hand2",
    command=action
)
button.pack(pady=15, ipadx=10, ipady=5)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Ergebnis Label
result_label = tk.Label(
    card,
    text="",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Segoe UI", 12)
)
result_label.pack(pady=10)

root.mainloop()