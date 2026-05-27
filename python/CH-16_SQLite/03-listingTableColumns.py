import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# list tables
res = conn.execute('SELECT name FROM sqlite_schema WHERE type="table"')
print(res.fetchall())

# obtain info about columns in cats table
info = conn.execute('PRAGMA TABLE_INFO(cats)')
print(info.fetchall())

