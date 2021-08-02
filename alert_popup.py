import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def alert():
    root = tk.Tk()
    root.title("PAWN PROMOTION")
    root.geometry("%dx%d+%d+%d" % (350, 200, 800, 500))
    root.config(background="sky blue")
    string = "PRESS\n'q' for QUEEN\n'k' for KNIGHT\n'b' for BISHOP\n'r' for ROOK"
    message = tk.Label(root, text=string)
    message.config(font=("Helvetica", 15, "bold"))
    message.place(x=100, y=30)
    root.after(5000, lambda: root.destroy())
    root.mainloop()
