# init_db.py

import sqlite3

conn = sqlite3.connect("warehouse.db")
cur = conn.cursor()

# Create staging + dimension + fact tables
# (your full SQL code here...)

conn.commit()
conn.close()
