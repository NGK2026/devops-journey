import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

print(conn.execute('SELECT rowid, * FROM cats WHERE rowid = 14').fetchall())
# [(14, 'Zophie', '2021-01-24', 'gray tabby', 5.6)]

# delete row 14
conn.execute('DELETE FROM cats WHERE rowid = 14')

print(conn.execute('SELECT rowid, * FROM cats WHERE rowid = 14').fetchall())
# []

# ALWAYS USE WHERE, if deleting all use: WHERE 1 / which is (WHERE TRUE)