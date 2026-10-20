
import tkinter as tk
from tkinter import messagebox

from db_connection import connect_database
from ui_helpers import (
    BG, PANEL, FG, MUTED, make_window,
    heading, make_label, make_entry, make_button
)


# Seat Booking Window

def open_booking_window():

    win = make_window("Busly | Book a Seat", "650x570")
    heading(win, "Book a Seat", "Reserve your seat for an upcoming bus")

    # Booking Form

    form = tk.Frame(win, bg=PANEL, padx=30, pady=25)
    form.pack(padx=60, fill="x")

    make_label(form, "Registered Phone:").grid(
        row=0, column=0, sticky="w", pady=12
    )
    phone_entry = make_entry(form)
    phone_entry.grid(row=0, column=1, padx=10, ipady=5)

    make_label(form, "Schedule ID:").grid(
        row=1, column=0, sticky="w", pady=12
    )
    schedule_entry = make_entry(form)
    schedule_entry.grid(row=1, column=1, padx=10, ipady=5)

    make_label(form, "Seat Number:").grid(
        row=2, column=0, sticky="w", pady=12
    )
    seat_entry = make_entry(form)
    seat_entry.grid(row=2, column=1, padx=10, ipady=5)

    fare_label = tk.Label(
        form, text="Fare: Not checked",
        font=("Segoe UI", 11, "bold"),
        fg="#60A5FA", bg=PANEL
    )
    fare_label.grid(row=3, column=0, columnspan=2, pady=15)

    # Check Booking Details

    def check_details():

        schedule_id = schedule_entry.get().strip()
        if not schedule_id.isdigit():
            messagebox.showwarning(
                "Invalid Schedule", "Enter a valid Schedule ID.",
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
            cursor.execute("""
                SELECT Schedule.fare, BUS.capacity,
                       Schedule.departure_date
                FROM Schedule
                JOIN BUS ON Schedule.bus_id = BUS.bus_id
                WHERE Schedule.schedule_id = %s
                  AND Schedule.departure_date >= CURDATE()
            """, (schedule_id,))

            result = cursor.fetchone()
            if result:
                fare_label.config(
                    text=f"Fare: Rs. {result[0]} | Capacity: {result[1]}"
                )
            else:
                fare_label.config(text="Schedule not found")
                messagebox.showwarning(
                    "Not Found", "No upcoming schedule with that ID.",
                    parent=win
                )

        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Confirm Booking

    def book_seat():

        phone = phone_entry.get().strip()
        schedule_id = schedule_entry.get().strip()
        seat = seat_entry.get().strip()

        if not phone or not schedule_id or not seat:
            messagebox.showwarning(
                "Missing Details", "Fill in all three fields.",
                parent=win
            )
            return

        if not schedule_id.isdigit() or not seat.isdigit():
            messagebox.showwarning(
                "Invalid Details", "Schedule ID and seat must be numbers.",
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
                "SELECT passenger_id FROM PASSENGER WHERE phone = %s",
                (phone,)
            )
            passenger = cursor.fetchone()

            if not passenger:
                messagebox.showwarning(
                    "Passenger Not Found",
                    "Register this phone number first.",
                    parent=win
                )
                return

            cursor.execute("""
                SELECT Schedule.fare, BUS.capacity
                FROM Schedule
                JOIN BUS ON Schedule.bus_id = BUS.bus_id
                WHERE Schedule.schedule_id = %s
                  AND Schedule.departure_date >= CURDATE()
            """, (schedule_id,))
            schedule = cursor.fetchone()

            if not schedule:
                messagebox.showwarning(
                    "Invalid Schedule", "Upcoming schedule not found.",
                    parent=win
                )
                return

            fare, capacity = schedule
            seat_number = int(seat)

            if seat_number < 1 or seat_number > capacity:
                messagebox.showwarning(
                    "Invalid Seat",
                    f"Choose a seat between 1 and {capacity}.",
                    parent=win
                )
                return

            cursor.execute("""
                SELECT booking_id FROM BOOKING
                WHERE schedule_id = %s AND seat_number = %s
                  AND booking_status = 'Booked'
            """, (schedule_id, seat_number))

            if cursor.fetchone():
                messagebox.showwarning(
                    "Seat Unavailable", "That seat is already booked.",
                    parent=win
                )
                return

            cursor.execute("""
                INSERT INTO BOOKING
                    (passenger_id, schedule_id, seat_number,
                     booking_date, booking_status)
                VALUES (%s, %s, %s, CURDATE(), 'Booked')
            """, (passenger[0], schedule_id, seat_number))

            conn.commit()
            messagebox.showinfo(
                "Booking Successful",
                f"Seat {seat_number} booked!\nFare: Rs. {fare}",
                parent=win
            )

            phone_entry.delete(0, tk.END)
            schedule_entry.delete(0, tk.END)
            seat_entry.delete(0, tk.END)
            fare_label.config(text="Fare: Not checked")

        except Exception as error:
            conn.rollback()
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Buttons

    make_button(
        form, "Check Schedule", check_details, color="#0F766E"
    ).grid(row=4, column=0, pady=15)

    make_button(
        form, "Confirm Booking", book_seat
    ).grid(row=4, column=1, pady=15)

    tk.Label(
        win, text="View Available Buses to find a Schedule ID.",
        font=("Segoe UI", 10), fg=MUTED, bg=BG
    ).pack(pady=15)
