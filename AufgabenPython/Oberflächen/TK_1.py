import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
b1= '#ff0000'
l1 = tk.Label(
    root,
    text="Hallo Welt",
    bg=b1
)
l1.pack()
root.mainloop()