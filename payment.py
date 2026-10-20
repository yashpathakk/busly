
import tkinter as tk
from tkinter import messagebox

from db_connection import connect_database
from ui_helpers import (
    BG, PANEL, FG, make_window, heading,
    make_label, make_entry, make_button
)


# Payment Window

def open_payment_window():

    win = make_window("Busly | Payment", "650x500")
    heading(win, "Payment", "Complete payment for your booking")

    # Payment Form

    form = tk.Frame(win, bg=PANEL, padx=30, pady=25)
    form.pack(padx=65, fill="x")

    make_label(form, "Booking ID:").grid(
        row=0, column=0, sticky="w", pady=15
    )
    booking_entry = make_entry(form)
    booking_entry.grid(row=0, column=1, padx=12, ipady=5)

    make_label(form, "Payment Method:").grid(
        row=1, column=0, sticky="w", pady=15
    )

    method = tk.StringVar(value="UPI")
    method_menu = tk.OptionMenu(
        form, method, "UPI", "Card", "Cash"
    )
    method_menu.config(
        bg="#374151", fg="white",
        activebackground="#0F766E",
        relief="flat", highlightthickness=0
    )
    method_menu["menu"].config(
        bg="#374151", fg="white"
    )
    method_menu.grid(row=1, column=1, sticky="ew", padx=12)

    amount_label = tk.Label(
        form, text="Amount: Not checked",
        font=("Segoe UI", 12, "bold"),
        fg="#60A5FA", bg=PANEL
    )
    amount_label.grid(row=2, column=0, columnspan=2, pady=18)

    # Check Booking

    def check_booking():

        booking_id = booking_entry.get().strip()
        if not booking_id.isdigit():
            messagebox.showwarning(
                "Invalid ID", "Enter a numeric Booking ID.", parent=win
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
                SELECT Schedule.fare, BOOKING.booking_status
                FROM BOOKING
                JOIN Schedule
                    ON BOOKING.schedule_id = Schedule.schedule_id
                WHERE BOOKING.booking_id = %s
            """, (booking_id,))

            booking = cursor.fetchone()
            if not booking:
                messagebox.showwarning(
                    "Not Found", "Booking ID was not found.", parent=win
                )
            elif booking[1] != "Booked":
                messagebox.showwarning(
                    "Unavailable", "This booking is not active.", parent=win
                )
            else:
                amount_label.config(text=f"Amount: Rs. {booking[0]}")

        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Save Payment

    def make_payment():

        booking_id = booking_entry.get().strip()
        if not booking_id.isdigit():
            messagebox.showwarning(
                "Invalid ID", "Enter a valid Booking ID.", parent=win
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
                SELECT Schedule.fare, BOOKING.booking_status
                FROM BOOKING
                JOIN Schedule
                    ON BOOKING.schedule_id = Schedule.schedule_id
                WHERE BOOKING.booking_id = %s
            """, (booking_id,))

            booking = cursor.fetchone()
            if not booking or booking[1] != "Booked":
                messagebox.showwarning(
                    "Invalid Booking",
                    "Check that the booking exists and is active.",
                    parent=win
                )
                return

            cursor.execute("""
                SELECT payment_id FROM Payment
                WHERE booking_id = %s AND payment_status = 'Paid'
            """, (booking_id,))

            if cursor.fetchone():
                messagebox.showinfo(
                    "Already Paid", "This booking is already paid for.",
                    parent=win
                )
                return

            payment_method = method.get()
            status = "Cash" if payment_method == "Cash" else "Paid"

            cursor.execute("""
                INSERT INTO Payment
                    (booking_id, amount, payment_method,
                     payment_status, payment_date)
                VALUES (%s, %s, %s, %s, CURDATE())
            """, (
                booking_id, booking[0], payment_method, status
            ))

            conn.commit()
            messagebox.showinfo(
                "Payment Saved",
                f"Payment record saved.\nAmount: Rs. {booking[0]}\n"
                f"Method: {payment_method}",
                parent=win
            )
            booking_entry.delete(0, tk.END)
            amount_label.config(text="Amount: Not checked")

        except Exception as error:
            conn.rollback()
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Buttons

    make_button(
        form, "Check Amount", check_booking, color="#0F766E"
    ).grid(row=3, column=0, pady=12)

    make_button(
        form, "Save Payment", make_payment
    ).grid(row=3, column=1, pady=12)
