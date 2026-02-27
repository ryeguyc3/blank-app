import json
import sqlite3
import os

# Optional: Remove old DB to ensure schema updates (Safety check)
# if os.path.exists("users.db"):
#     os.remove("users.db")

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("vehicle_Goldies.db")
cursor = conn.cursor()

# 1. Update Table Schema
# Changed 'email' to 'address'
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_vehicles (
    Key_id INTEGER PRIMARY KEY,
    Model TEXT NOT NULL,
    Partial_Vin TEXT NOT NULL,
    Year TEXT NOT NULL,
    Mileage TEXT NOT NULL
)
""")

# Load JSON data
Count = 0
try:
    with open("data_v.json", "r") as file:
         vehicles_Goldies = json.load(file)

    # 2. Update Insert Logic
    # We now look for 'vehicles' in the JSON and insert into the 'Key_id' column
    for tbl_vehicles in vehicles_Goldies:
        cursor.execute(
            "INSERT OR REPLACE INTO tbl_vehicles (Key_id, Model, Partial_Vin, Year, Mileage) VALUES (?, ?, ?, ?, ?)",
            (tbl_vehicles["Key_id"], tbl_vehicles["Model"], tbl_vehicles["Partial_Vin"], tbl_vehicles["Year"], tbl_vehicles["Mileage"])
                       )
    # Commit and close
    conn.commit()
    print("Data successfully written to database. The below outputs all the records from the database")

except KeyError as e:
    print(f"Error: The JSON data is missing the key {e}. Please check your data.json file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()

conn = sqlite3.connect("vehicle_Goldies.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM tbl_vehicles")
rows = cursor.fetchall()

for row in rows:
    Count = Count + 1
    print(row)
    print(Count)
 
conn.close()
