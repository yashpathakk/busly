
import tkinter as tk
from tkinter import ttk

# Busly Colour Theme

BG = "#111827"
PANEL = "#1F2937"
FIELD = "#374151"
FG = "#F9FAFB"
MUTED = "#9CA3AF"
BLUE = "#2563EB"
LIGHT_BLUE = "#60A5FA"
TEAL = "#0F766E"
RED = "#DC2626"


# Window Design

def make_window(title, size):

    win = tk.Toplevel()
    win.title(title)
    win.geometry(size)
    win.configure(bg=BG)
    win.resizable(False, False)
    return win


# Heading Design

def heading(win, title, subtitle):

    tk.Label(
        win, text=title,
        font=("Segoe UI", 25, "bold"),
        fg=LIGHT_BLUE, bg=BG
    ).pack(pady=(18, 4))

    tk.Label(
        win, text=subtitle,
        font=("Segoe UI", 11),
        fg=MUTED, bg=BG
    ).pack(pady=(0, 15))


# Label Design

def make_label(parent, text):

    return tk.Label(
        parent, text=text,
        font=("Segoe UI", 10),
        fg=FG, bg=PANEL
    )


# Entry Design

def make_entry(parent, width=22):

    return tk.Entry(
        parent, width=width,
        font=("Segoe UI", 11),
        bg=FIELD, fg=FG,
        insertbackground=FG,
        relief="flat"
    )


# Button Design

def make_button(parent, text, command, color=BLUE):

    return tk.Button(
        parent, text=text,
        font=("Segoe UI", 10, "bold"),
        bg=color, fg="white",
        activebackground=TEAL,
        activeforeground="white",
        relief="flat", cursor="hand2",
        command=command, padx=10, pady=6
    )


# Table Design

def style_table():

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Treeview",
        background=PANEL, foreground=FG,
        fieldbackground=PANEL,
        rowheight=30, font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        background=BLUE, foreground="white",
        font=("Segoe UI", 10, "bold")
    )

    style.map(
        "Treeview",
        background=[("selected", TEAL)]
    )
