import tkinter as tk
from tkinter import messagebox
from passenger_login import open_login

from db_connection import connect_database

# Main Window

root = tk.Tk()

root.title("Busly")
root.geometry("1000x700")
root.configure(bg="#F1F5F9")
root.resizable(False, False)


#Heading

title_label=tk.Label(
    root,
    text="Busly",
    font=("Segoe UI", 36, "bold"),
    fg="#2563EB",
    bg="#F1F5F9",
)

title_label.pack(pady=(40,5))

#Subtitle(under heading text)

subtitle_label=tk.Label(
    root,
    text="Your journey begins with Busly." \
    "Book smarter. Travel easier.",
    font=("Segoe UI", 15),
    fg="#64748B",
    bg="#F1F5F9"
)

subtitle_label.pack(pady=(0,30))

#Welcome 

welcome_label=tk.Label(
    root,
    text="Welcome to Busly!",
    font=("Segoe UI", 22, "bold"),
    fg="#1E293B",
    bg="#F1F5F9"
)
welcome_label.pack(pady=20)

# Description

description_label = tk.Label(
    root,
    text="Find your ride, reserve your seat, and get ready to explore.",
    font=("Segoe UI", 12),
    fg="#64748B",
    bg="#F1F5F9"
)

description_label.pack(pady=(0, 30))

# Passenger Login Button

login_button = tk.Button(
    root,
    text="Passenger Login",
    font=("Segoe UI", 13, "bold"),
    bg="#2563EB",
    fg="white",
    width=25,
    height=2,
    cursor="hand2",
    command=open_login,
)

login_button.pack(pady=10)
root.mainloop()



