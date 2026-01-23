import sqlite3

conn = sqlite3.connect("kpi_library.db")
cur = conn.cursor()

# List tables (whole database)
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# cur.execute("DELETE FROM kpi_app_gics_sector;")
# Example: view first 10 rows from a table
cur.execute("SELECT * FROM kpi_app_gics_sector LIMIT 10;")
print(cur.fetchall())



#cur.execute(f"PRAGMA table_info(kpi_app_gics_sector);")
for col in cur.fetchall():
    print(col)

# cur.execute("DELETE FROM sqlite_sequence WHERE name='kpi_app_gics_sector';")
# conn.commit()

conn.close()