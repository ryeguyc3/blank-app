import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to database
conn = sqlite3.connect("vehicle_Goldies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_vehicles (
    Key_id INTEGER PRIMARY KEY,
    Model TEXT NOT NULL,
    Partial_Vin TEXT NOT NULL,
    Year TEXT NOT NULL,
    Mileage TEXT NOT NULL,
    Color TEXT NOT NULL
)
""")
conn.commit()

# GUI
root = tk.Tk()
root.title("SQLite CRUD App")

# --- Functions ---

def refresh_data():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM tbl_vehicles")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def add_vehicle():
    cursor.execute("INSERT INTO tbl_vehicles (Key_id, Model, Partial_Vin, Year, Mileage, Color) VALUES (?, ?, ?, ?, ?, ?)",
                   (Key_id.get(), Model.get(), Partial_Vin.get(), Year.get(), Mileage.get(), Color.get()))
    conn.commit()
    refresh_data()

def delete_vehicle():
    selected = tree.focus()
    values = tree.item(selected, "values")
    cursor.execute("DELETE FROM tbl_vehicles WHERE Key_id=?", (values[0],))
    conn.commit()
    refresh_data()

# --- UI Elements ---

tk.Label(root, text="Key_ID").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Model").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Partial_Vin").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Year").grid(row=3, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=3, column=1)

tk.Label(root, text="Mileage").grid(row=4, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=4, column=1)

tk.Label(root, text="Color").grid(row=5, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=5, column=1)


tk.Button(root, text="Add", command=add_vehicle).grid(row=1, column=3)
tk.Button(root, text="Delete", command=delete_vehicle).grid(row=3, column=3)

tree = ttk.Treeview(root, columns=("Key_id", "Model", "Partial_Vin", "Year", "Mileage", "Color"), show="headings")
tree.heading("Key_id", text="Key Number")
tree.heading("Model", text="Model")
tree.heading("Partial_Vin", text="Last 6 of Vin")
tree.heading("Year", text="Year of Manufacture")
tree.heading("Mileage", text="Mileage")
tree.heading("Color", text="Color")
tree.grid(row=6, column=0, columnspan=2)

refresh_data()
root.mainloop()
