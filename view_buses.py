
import tkinter as tk
from tkinter import ttk, messagebox

from db_connection import connect_database
from ui_helpers import (
    BG, PANEL, FG, MUTED, make_window,
    heading, make_label, make_entry,
    make_button, style_table
)


# Available Buses Window

def open_bus_window():

    win = make_window("Busly | Available Buses", "1250x650")
    heading(win, "Available Buses", "Find your next journey")

    # Search Section

    search = tk.Frame(win, bg=PANEL, padx=15, pady=12)
    search.pack(fill="x", padx=25)

    make_label(search, "Source:").grid(row=0, column=0, padx=6)
    source_entry = make_entry(search)
    source_entry.grid(row=0, column=1, padx=6, ipady=5)

    make_label(search, "Destination:").grid(row=0, column=2, padx=6)
    destination_entry = make_entry(search)
    destination_entry.grid(row=0, column=3, padx=6, ipady=5)

    # Bus Table

    columns = (
        "Bus Name", "Bus Number", "Type", "Source",
        "Destination", "Distance", "Date", "Departure",
        "Arrival", "Fare", "Schedule ID"
    )

    frame = tk.Frame(win, bg=BG)
    frame.pack(fill="both", expand=True, padx=25, pady=15)

    style_table()
    table = ttk.Treeview(
        frame, columns=columns, show="headings"
    )

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=115, anchor="center")

    table.column("Bus Name", width=140)
    table.column("Schedule ID", width=90)

    ybar = ttk.Scrollbar(
        frame, orient="vertical", command=table.yview
    )
    xbar = ttk.Scrollbar(
        frame, orient="horizontal", command=table.xview
    )

    table.configure(
        yscrollcommand=ybar.set,
        xscrollcommand=xbar.set
    )

    table.grid(row=0, column=0, sticky="nsew")
    ybar.grid(row=0, column=1, sticky="ns")
    xbar.grid(row=1, column=0, sticky="ew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Load Buses

    def load_buses():

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
                SELECT BUS.bus_name, BUS.bus_number, BUS.bus_type,
                    ROUTE.source, ROUTE.destination, ROUTE.distance,
                    Schedule.departure_date, Schedule.departure_time,
                    Schedule.arrival_time, Schedule.fare,
                    Schedule.schedule_id
                FROM Schedule
                JOIN BUS ON Schedule.bus_id = BUS.bus_id
                JOIN ROUTE ON Schedule.route_id = ROUTE.route_id
                WHERE ROUTE.source LIKE %s
                  AND ROUTE.destination LIKE %s
                  AND Schedule.departure_date >= CURDATE()
                ORDER BY Schedule.departure_date,
                         Schedule.departure_time
            """, (
                "%" + source_entry.get().strip() + "%",
                "%" + destination_entry.get().strip() + "%"
            ))

            rows = cursor.fetchall()
            table.delete(*table.get_children())

            for row in rows:
                table.insert("", tk.END, values=row)

            if not rows:
                messagebox.showinfo(
                    "No Buses", "No matching upcoming buses found.",
                    parent=win
                )

        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # Search Controls

    make_button(
        search, "Search", load_buses
    ).grid(row=0, column=4, padx=6)

    def clear_search():
        source_entry.delete(0, tk.END)
        destination_entry.delete(0, tk.END)
        load_buses()

    make_button(
        search, "Clear", clear_search, color="#0F766E"
    ).grid(row=0, column=5, padx=6)

    make_button(
        search, "Refresh", load_buses
    ).grid(row=0, column=6, padx=6)

    load_buses()
