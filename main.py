import tkinter as tk
from tkinter import messagebox

from db_connection import connect_database

# Main Window

root = tk.Tk()

root.title("Busly")
root.geometry("1000x700")
root.configure(bg="white")
root.resizable(False, False)


#Heading

title_label=tk.Label(
    root,
    text="Busly",
    font=("Arial",32,"bold"),
    fg="blue",
    bg="white"
)

title_label.pack(pady=(40,5))

#Subtitle(under heading text)

subtitle_label=tk.Label(
    root,
    text="Your journey begins with Busly." \
    "Book smarter. Travel easier.",
    font=("Arial",16),
    fg="black",
    bg="white"
)

subtitle_label.pack(pady=(0,30))
root.mainloop()