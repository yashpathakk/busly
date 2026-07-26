from tkinter import *
from tkinter import messagebox


# -------------------------
# Register Button Function
# -------------------------
def register_passenger():
    messagebox.showinfo("Registration", "Register button clicked!")


# -------------------------
# Clear Button Function
# -------------------------
def clear_fields():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_gender.delete(0, END)
    entry_phone.delete(0, END)
    entry_email.delete(0, END)
    entry_password.delete(0, END)
    entry_confirm_password.delete(0, END)


# -------------------------
# Main Window
# -------------------------
root = Tk()
root.title("Busly - Passenger Registration")
root.geometry("500x550")
root.resizable(False, False)


# -------------------------
# Heading
# -------------------------
heading = Label(
    root,
    text="Passenger Registration",
    font=("Arial", 18, "bold")
)
heading.pack(pady=15)


# -------------------------
# Registration Form Frame
# -------------------------
form_frame = Frame(root)
form_frame.pack(pady=10)


# Passenger Name
Label(form_frame, text="Passenger Name", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=8, sticky="w")
entry_name = Entry(form_frame, width=30)
entry_name.grid(row=0, column=1)

# Age
Label(form_frame, text="Age", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="w")
entry_age = Entry(form_frame, width=30)
entry_age.grid(row=1, column=1)

# Gender
Label(form_frame, text="Gender", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="w")
entry_gender = Entry(form_frame, width=30)
entry_gender.grid(row=2, column=1)

# Phone
Label(form_frame, text="Phone Number", font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=8, sticky="w")
entry_phone = Entry(form_frame, width=30)
entry_phone.grid(row=3, column=1)

# Email
Label(form_frame, text="Email", font=("Arial", 11)).grid(row=4, column=0, padx=10, pady=8, sticky="w")
entry_email = Entry(form_frame, width=30)
entry_email.grid(row=4, column=1)

# Password
Label(form_frame, text="Password", font=("Arial", 11)).grid(row=5, column=0, padx=10, pady=8, sticky="w")
entry_password = Entry(form_frame, width=30, show="*")
entry_password.grid(row=5, column=1)

# Confirm Password
Label(form_frame, text="Confirm Password", font=("Arial", 11)).grid(row=6, column=0, padx=10, pady=8, sticky="w")
entry_confirm_password = Entry(form_frame, width=30, show="*")
entry_confirm_password.grid(row=6, column=1)


# -------------------------
# Buttons
# -------------------------
button_frame = Frame(root)
button_frame.pack(pady=25)

register_button = Button(
    button_frame,
    text="Register",
    width=15,
    command=register_passenger
)
register_button.grid(row=0, column=0, padx=10)

clear_button = Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_fields
)
clear_button.grid(row=0, column=1, padx=10)


root.mainloop()