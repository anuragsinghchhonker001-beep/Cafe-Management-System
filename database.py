import sqlite3

conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT,
total_bill REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")
