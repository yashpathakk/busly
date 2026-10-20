
import tkinter as tk
from tkinter import messagebox

from db_connection import connect_database
from ui_helpers import (
    PANEL, make_window, heading,
    make_label, make_entry, make_button
)


# Passenger Login Window

def open_login():

    win = make_window("Busly | Passenger Login", "550x400")
    heading(win, "Passenger Login", "Access your passenger account")

    # Login Form

    form = tk.Frame(win, bg=PANEL, padx=30, pady=25)
    form.pack(padx=65, fill="x")

    make_label(form, "Registered Phone:").grid(
        row=0, column=0, sticky="w", pady=15
    )
    phone_entry = make_entry(form)
    phone_entry.grid(row=0, column=1, padx=10, ipady=5)

    # Verify Passenger

    def login():

        phone = phone_entry.get().strip()
        if not phone:
            messagebox.showwarning(
                "Missing Phone", "Enter your registered phone number.",
                parent=win
            )
            return

        conn = connect_database()
        if conn is None:
            messagebox.showerror(
                "Database Error", "Could not connect to database.",
                parent=win
            )
            return

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT full_name FROM PASSENGER WHERE phone = %s",
                (phone,)
            )
            passenger = cursor.fetchone()

            if passenger:
                messagebox.showinfo(
                    "Login Successful",
                    f"Welcome, {passenger[0]}!",
                    parent=win
                )
                win.destroy()
            else:
                messagebox.showwarning(
                    "Passenger Not Found",
                    "Please register before logging in.",
                    parent=win
                )

        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Login Button

    make_button(
        form, "Login", login
    ).grid(row=1, column=0, columnspan=2, pady=20, ipadx=20)
