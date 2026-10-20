
import tkinter as tk
from tkinter import ttk, messagebox

from db_connection import connect_database
from ui_helpers import (
    BG, PANEL, make_window, heading, make_label,
    make_entry, make_button, style_table
)


# My Bookings Window

def open_my_bookings():

    win = make_window("Busly | My Bookings", "1150x600")
    heading(win, "My Bookings", "View and manage your reservations")

    # Search Section

    search = tk.Frame(win, bg=PANEL, padx=15, pady=12)
    search.pack(fill="x", padx=25)

    make_label(search, "Registered Phone:").grid(
        row=0, column=0, padx=8
    )
    phone_entry = make_entry(search)
    phone_entry.grid(row=0, column=1, padx=8, ipady=5)

    # Bookings Table

    columns = (
        "Booking ID", "Bus", "Source", "Destination",
        "Date", "Departure", "Seat", "Fare", "Status"
    )

    frame = tk.Frame(win, bg=BG)
    frame.pack(fill="both", expand=True, padx=25, pady=15)

    style_table()
    table = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=115, anchor="center")

    table.column("Booking ID", width=85)
    table.column("Bus", width=140)

    scrollbar = ttk.Scrollbar(
        frame, orient="vertical", command=table.yview
    )
    table.configure(yscrollcommand=scrollbar.set)
    table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Load Bookings

    def load_bookings():

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
            cursor.execute("""
                SELECT BOOKING.booking_id, BUS.bus_name,
                    ROUTE.source, ROUTE.destination,
                    Schedule.departure_date, Schedule.departure_time,
                    BOOKING.seat_number, Schedule.fare,
                    BOOKING.booking_status
                FROM BOOKING
                JOIN PASSENGER
                    ON BOOKING.passenger_id = PASSENGER.passenger_id
                JOIN Schedule
                    ON BOOKING.schedule_id = Schedule.schedule_id
                JOIN BUS ON Schedule.bus_id = BUS.bus_id
                JOIN ROUTE ON Schedule.route_id = ROUTE.route_id
                WHERE PASSENGER.phone = %s
                ORDER BY BOOKING.booking_id DESC
            """, (phone,))

            rows = cursor.fetchall()
            table.delete(*table.get_children())

            for row in rows:
                table.insert("", tk.END, values=row)

            if not rows:
                messagebox.showinfo(
                    "No Bookings", "No bookings found for this phone.",
                    parent=win
                )

        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Cancel Selected Booking

    def cancel_booking():

        selected = table.selection()
        if not selected:
            messagebox.showwarning(
                "Select Booking", "Select a booking first.", parent=win
            )
            return

        values = table.item(selected[0], "values")
        booking_id, status = values[0], values[8]

        if status != "Booked":
            messagebox.showinfo(
                "Cannot Cancel", "Only active bookings can be cancelled.",
                parent=win
            )
            return

        if not messagebox.askyesno(
            "Confirm", f"Cancel booking #{booking_id}?", parent=win
        ):
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
                UPDATE BOOKING
                JOIN PASSENGER
                    ON BOOKING.passenger_id = PASSENGER.passenger_id
                SET BOOKING.booking_status = 'Cancelled'
                WHERE BOOKING.booking_id = %s
                  AND PASSENGER.phone = %s
                  AND BOOKING.booking_status = 'Booked'
            """, (booking_id, phone_entry.get().strip()))

            if cursor.rowcount == 0:
                conn.rollback()
                messagebox.showwarning(
                    "Not Cancelled", "Booking could not be cancelled.",
                    parent=win
                )
                return

            conn.commit()
            messagebox.showinfo(
                "Success", "Booking cancelled successfully.", parent=win
            )
            load_bookings()

        except Exception as error:
            conn.rollback()
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Buttons

    make_button(
        search, "View Bookings", load_bookings
    ).grid(row=0, column=2, padx=8)

    make_button(
        win, "Cancel Selected Booking", cancel_booking, color="#DC2626"
    ).pack(pady=(0, 18))
