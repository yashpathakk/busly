
import tkinter as tk
from tkinter import messagebox


# Login Function

def passenger_login():
    email = entry_email.get()
    password = entry_password.get()

    if email == "" or password == "":
        messagebox.showwarning(
            "Login",
            "Please fill all the fields."
        )
    else:
        messagebox.showinfo(
            "Login",
            "Passenger Login Successful!"
        )


# Clear Function

def clear_fields():
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)


# Open Passenger Login Window

def open_login():

    global entry_email, entry_password

    login_window = tk.Toplevel()
    login_window.title("Busly - Passenger Login")
    login_window.geometry("400x300")
    login_window.resizable(False, False)

    # Heading

    heading = tk.Label(
        login_window,
        text="Passenger Login",
        font=("Arial", 18, "bold")
    )
    heading.pack(pady=20)

    # Login Frame

    login_frame = tk.Frame(login_window)
    login_frame.pack(pady=10)

    # Email

    tk.Label(
        login_frame,
        text="Email ID",
        font=("Arial", 11)
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_email = tk.Entry(login_frame, width=25)
    entry_email.grid(row=0, column=1)

    # Password

    tk.Label(
        login_frame,
        text="Password",
        font=("Arial", 11)
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    entry_password = tk.Entry(
        login_frame,
        width=25,
        show="*"
    )
    entry_password.grid(row=1, column=1)

    # Buttons

    button_frame = tk.Frame(login_window)
    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Login",
        width=12,
        command=passenger_login
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        button_frame,
        text="Clear",
        width=12,
        command=clear_fields
    ).grid(row=0, column=1, padx=10)