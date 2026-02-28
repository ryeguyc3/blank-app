import json
import sqlite3
import os

# Optional: Remove old DB to ensure schema updates (Safety check)
# if os.path.exists("users.db"):
#     os.remove("users.db")

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("vehicle_Goldies.db")
cursor = conn.cursor()
#delete with Key_id = 101
cursor.execute("DELETE FROM tbl_vehicles WHERE Key_id = ?;", (84,))
        
# Commit and close
conn.commit()
print("Delete successfully on database. ")
Count = 0
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
