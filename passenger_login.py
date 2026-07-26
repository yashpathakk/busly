from tkinter import *
from tkinter import messagebox



# Login Function

def passenger_login():
    email = entry_email.get()
    password = entry_password.get()

    if email == "" or password == "":
        messagebox.showwarning("Login", "Please fill all the fields.")
    else:
        messagebox.showinfo("Login", "Passenger Login Successful!")



# Clear Function

def clear_fields():
    entry_email.delete(0, END)
    entry_password.delete(0, END)



# Main Window

root = Tk()
root.title("Busly - Passenger Login")
root.geometry("400x300")
root.resizable(False, False)



# Heading

heading = Label(
    root,
    text="Passenger Login",
    font=("Arial", 18, "bold")
)
heading.pack(pady=20)



# Login Frame

login_frame = Frame(root)
login_frame.pack(pady=10)

# Email
Label(login_frame, text="Email ID", font=("Arial", 11)).grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

entry_email = Entry(login_frame, width=25)
entry_email.grid(row=0, column=1)

# Password
Label(login_frame, text="Password", font=("Arial", 11)).grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

entry_password = Entry(login_frame, width=25, show="*")
entry_password.grid(row=1, column=1)



# Buttons

button_frame = Frame(root)
button_frame.pack(pady=20)

login_button = Button(
    button_frame,
    text="Login",
    width=12,
    command=passenger_login
)
login_button.grid(row=0, column=0, padx=10)

clear_button = Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_fields
)
clear_button.grid(row=0, column=1, padx=10)


root.mainloop()
