
import tkinter as tk
from tkinter import messagebox

from db_connection import connect_database
from ui_helpers import (
    PANEL, make_window, heading,
    make_label, make_entry, make_button
)


# Passenger Registration Window

def open_registration():

    win = make_window("Busly | Registration", "650x570")
    heading(win, "Passenger Registration", "Create your passenger record")

    # Registration Form

    form = tk.Frame(win, bg=PANEL, padx=35, pady=25)
    form.pack(padx=70, fill="x")

    make_label(form, "Full Name:").grid(
        row=0, column=0, sticky="w", pady=12
    )
    name_entry = make_entry(form)
    name_entry.grid(row=0, column=1, padx=12, ipady=5)

    make_label(form, "Phone Number:").grid(
        row=1, column=0, sticky="w", pady=12
    )
    phone_entry = make_entry(form)
    phone_entry.grid(row=1, column=1, padx=12, ipady=5)

    make_label(form, "Age:").grid(
        row=2, column=0, sticky="w", pady=12
    )
    age_entry = make_entry(form)
    age_entry.grid(row=2, column=1, padx=12, ipady=5)

    make_label(form, "Gender:").grid(
        row=3, column=0, sticky="w", pady=12
    )

    gender = tk.StringVar(value="Male")
    gender_menu = tk.OptionMenu(
        form, gender, "Male", "Female"
    )
    gender_menu.config(
        bg="#374151", fg="white",
        activebackground="#0F766E",
        relief="flat", highlightthickness=0
    )
    gender_menu["menu"].config(bg="#374151", fg="white")
    gender_menu.grid(row=3, column=1, sticky="ew", padx=12)

    # Save Passenger

    def register_passenger():

        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        age = age_entry.get().strip()

        if not name or not phone or not age:
            messagebox.showwarning(
                "Missing Details", "Fill in every field.", parent=win
            )
            return

        if len(name) > 20:
            messagebox.showwarning(
                "Name Too Long", "Name must be 20 characters or fewer.",
                parent=win
            )
            return

        if not phone.isdigit() or not 7 <= len(phone) <= 15:
            messagebox.showwarning(
                "Invalid Phone", "Enter a valid phone number.",
                parent=win
            )
            return

        if not age.isdigit() or not 1 <= int(age) <= 100:
            messagebox.showwarning(
                "Invalid Age", "Enter a valid age.", parent=win
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
            cursor.execute("""
                INSERT INTO PASSENGER (full_name, phone, age, gender)
                VALUES (%s, %s, %s, %s)
            """, (name, phone, int(age), gender.get()))

            conn.commit()
            messagebox.showinfo(
                "Registered", "Passenger registered successfully.",
                parent=win
            )

            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)

        except Exception as error:
            conn.rollback()
            messagebox.showerror(
                "Registration Error",
                "Could not register passenger. The phone number may "
                "already be registered.\n\n" + str(error),
                parent=win
            )
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Register Button

    make_button(
        form, "Register Passenger", register_passenger
    ).grid(row=4, column=0, columnspan=2, pady=20, ipadx=12)
