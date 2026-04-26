import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# view
print(conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall())

# update fur
conn.execute('UPDATE cats SET fur = "gray tabby" WHERE rowid = 1')

# view
print(conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall())

# update multiple columns
# 'UPDATE cats SET fur = "black", weight_kg = 6 WHERE rowid = 1'

# WHERE any column not just rowid
# but will update all 'Zophie's
# 'UPDATE cats SET fur = "gray tabby" WHERE name = "Zophie"'

# ALWAYS USE WHERE, if updating all use: WHERE 1 / which is (WHERE TRUE)