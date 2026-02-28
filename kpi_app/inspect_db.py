import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "kpi_library.db"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# List tables (whole database)
cur.execute("""
    SELECT name FROM sqlite_master WHERE type='table';
    """)


# Example: view first 10 rows from a table
# cur.execute("SELECT * FROM kpi_app_gicssector LIMIT 10;")
cur.execute("SELECT * FROM kpi_app_kpi LIMIT 10;")
print(cur.fetchall())


# cur.execute("DELETE FROM kpi_app_gics_sector;")

#cur.execute(f"PRAGMA table_info(kpi_app_gics_sector);")
# for (name,) in cur.fetchall():
#     print(name)

# cur.execute("DELETE FROM sqlite_sequence WHERE name='kpi_app_gics_sector';")
# cur.execute("DELETE FROM kpi_app_kpi;")
# cur.execute("DELETE FROM kpi_app_kpiindustry;")
# conn.commit()

conn.close()