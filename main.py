
import tkinter as tk
from tkinter import messagebox
from passenger_login import open_login
from db_connection import connect_database
from view_buses import open_bus_window
from book_seat import open_booking_window
from my_bookings import open_my_bookings
from payment import open_payment_window


# Main Window

root = tk.Tk()

root.title("Busly | Bus Booking")
root.geometry("950x850")
root.configure(bg="#111827")
root.resizable(False, True)


# Heading

title_label = tk.Label(
    root,
    text="BUSLY",
    font=("Segoe UI", 38, "bold"),
    fg="#60A5FA",
    bg="#111827"
)

title_label.pack(pady=(30, 0))


# Subtitle

subtitle_label = tk.Label(
    root,
    text="YOUR JOURNEY, SIMPLIFIED.",
    font=("Segoe UI", 11, "bold"),
    fg="#9CA3AF",
    bg="#111827"
)

subtitle_label.pack(pady=(3, 25))


# Welcome

welcome_label = tk.Label(
    root,
    text="Welcome to Busly",
    font=("Segoe UI", 25, "bold"),
    fg="#F9FAFB",
    bg="#111827"
)

welcome_label.pack(pady=(5, 5))


# Description

description_label = tk.Label(
    root,
    text="Find your ride, reserve your seat, and explore.",
    font=("Segoe UI", 12),
    fg="#9CA3AF",
    bg="#111827"
)

description_label.pack(pady=(0, 22))


# Main Panel

main_frame = tk.Frame(
    root,
    bg="#1F2937",
    highlightbackground="#374151",
    highlightthickness=1
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=100,
    pady=(0, 25)
)


# Passenger Login Button

login_button = tk.Button(
    main_frame,
    text="Passenger Login",
    font=("Segoe UI", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    width=30,
    height=2,
    cursor="hand2",
    relief="flat",
    bd=0,
    command=open_login
)

login_button.pack(pady=(25, 8))


# View Buses Button

buses_button = tk.Button(
    main_frame,
    text="View Available Buses",
    font=("Segoe UI", 12, "bold"),
    bg="#0F766E",
    fg="white",
    activebackground="#115E59",
    activeforeground="white",
    width=30,
    height=2,
    cursor="hand2",
    relief="flat",
    bd=0,
    command=open_bus_window
)

buses_button.pack(pady=8)


# Seat Booking

booking_button = tk.Button(
    main_frame,
    text="Book a Seat",
    font=("Segoe UI", 12, "bold"),
    bg="#7C3AED",
    fg="white",
    activebackground="#6D28D9",
    activeforeground="white",
    width=30,
    height=2,
    cursor="hand2",
    relief="flat",
    bd=0,
    command=open_booking_window
)

booking_button.pack(pady=8)


# Bookings

my_bookings_button = tk.Button(
    main_frame,
    text="My Bookings",
    font=("Segoe UI", 12, "bold"),
    bg="#D97706",
    fg="white",
    activebackground="#B45309",
    activeforeground="white",
    width=30,
    height=2,
    cursor="hand2",
    relief="flat",
    bd=0,
    command=open_my_bookings
)

my_bookings_button.pack(pady=8)


# Payment Button

payment_button = tk.Button(
    main_frame,
    text="Payment",
    font=("Segoe UI", 12, "bold"),
    bg="#059669",
    fg="white",
    activebackground="#047857",
    activeforeground="white",
    width=30,
    height=2,
    cursor="hand2",
    relief="flat",
    bd=0,
    command=open_payment_window
)

payment_button.pack(pady=8)


# Footer

footer_label = tk.Label(
    main_frame,
    text="SAFE TRAVELS  |  POWERED BY BUSLY",
    font=("Segoe UI", 9, "bold"),
    fg="#6B7280",
    bg="#1F2937"
)

footer_label.pack(pady=(20, 18))


# Run Application

root.mainloop()
