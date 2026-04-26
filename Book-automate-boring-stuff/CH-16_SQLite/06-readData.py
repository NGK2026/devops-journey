import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

print(conn.execute('SELECT * FROM cats').fetchall())
# [('Zophie', '2021-01-24', 'black', 5.6), ('Fudge', '2021-02-24', 'grey', 6.0)]

print(conn.execute('SELECT * FROM cats').fetchall()[0])
# ('Zophie', '2021-01-24', 'black', 5.6)

print(conn.execute('SELECT * FROM cats').fetchall()[1])
# ('Fudge', '2021-02-24', 'grey', 6.0)

# rowID & name
print(conn.execute('SELECT rowid, name FROM cats').fetchall())
# [(1, 'Zophie'), (2, 'Fudge')]

# name, weight_kg
print(conn.execute('SELECT name, weight_kg FROM cats').fetchall())
# [('Zophie', 5.6), ('Fudge', 6.0)]

for row in conn.execute('SELECT * FROM cats'):
    print(f'\nRow data:', row)
    print(row[0], 'is my fav! cat!')

