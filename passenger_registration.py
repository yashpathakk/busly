
from tkinter import *
from tkinter import messagebox

from db_connection import connect_database


# Register Passenger Function

def register_passenger():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    gender = entry_gender.get().strip()
    phone = entry_phone.get().strip()

    if name == "" or age == "" or gender == "" or phone == "":
        messagebox.showwarning("Registration", "Please fill all fields.")
        return

    if len(name) > 20:
        messagebox.showwarning("Registration", "Name must be within 20 characters.")
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showwarning("Registration", "Enter a valid age.")
        return

    if gender not in ("Male", "Female"):
        messagebox.showwarning("Registration", "Enter Male or Female.")
        return

    if not phone.isdigit() or len(phone) > 15:
        messagebox.showwarning("Registration", "Enter a valid phone number.")
        return

    conn = connect_database()

    if conn is None:
        messagebox.showerror("Database", "Could not connect to database.")
        return

    cursor = None

    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO PASSENGER
        (full_name, phone, age, gender)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, phone, int(age), gender)

        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo(
            "Registration",
            "Passenger registered successfully!"
        )

        clear_fields()

    except Exception as e:
        conn.rollback()
        messagebox.showerror(
            "Registration Error",
            "Registration failed. Check the phone number or database."
        )
        print("Database error:", e)

    finally:
        if cursor is not None:
            cursor.close()
        conn.close()


# Clear Fields Function

def clear_fields():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_gender.delete(0, END)
    entry_phone.delete(0, END)


# Main Window

root = Tk()
root.title("Busly - Passenger Registration")
root.geometry("500x400")
root.resizable(False, False)


# Heading

heading = Label(
    root,
    text="Passenger Registration",
    font=("Arial", 18, "bold")
)
heading.pack(pady=20)


# Registration Form

form_frame = Frame(root)
form_frame.pack(pady=10)


# Passenger Name

Label(form_frame, text="Passenger Name").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

entry_name = Entry(form_frame, width=30)
entry_name.grid(row=0, column=1)


# Age

Label(form_frame, text="Age").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

entry_age = Entry(form_frame, width=30)
entry_age.grid(row=1, column=1)


# Gender

Label(form_frame, text="Gender (Male/Female)").grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)

entry_gender = Entry(form_frame, width=30)
entry_gender.grid(row=2, column=1)


# Phone Number

Label(form_frame, text="Phone Number").grid(
    row=3, column=0, padx=10, pady=10, sticky="w"
)

entry_phone = Entry(form_frame, width=30)
entry_phone.grid(row=3, column=1)


# Buttons

button_frame = Frame(root)
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Register",
    width=15,
    command=register_passenger
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_fields
).grid(row=0, column=1, padx=10)


root.mainloop()
