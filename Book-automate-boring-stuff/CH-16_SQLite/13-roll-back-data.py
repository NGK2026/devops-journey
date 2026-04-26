import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# start transaction without commit
conn.execute('BEGIN')
# insert data
conn.execute('INSERT INTO cats VALUES ("socks", "2022-04-04", "white", 4.2)')
conn.execute('INSERT INTO cats VALUES ("Fluffy", "2022-10-30", "gray", 4.5)')

pprint.pprint(conn.execute('SELECT * FROM cats WHERE 1').fetchall())
# ('Bingo', '2013-11-07', 'brown', 6.2),
# ('Zophie', '2021-01-24', 'gray tabby', 5.6)
# ('socks', '2022-04-04', 'white', 4.2),
# ('Fluffy', '2022-10-30', 'gray', 4.5)]

# rollback insert statements
conn.rollback()
print()
pprint.pprint(conn.execute('SELECT * FROM cats WHERE 1').fetchall())
# ('Bingo', '2013-11-07', 'brown', 6.2),
# ('Zophie', '2021-01-24', 'gray tabby', 5.6)

print(conn.execute('SELECT * FROM cats WHERE name = "Socks"').fetchall())
# []
print(conn.execute('SELECT * FROM cats WHERE name = "Fluffy"').fetchall())
# []

# re insert data
conn.execute('INSERT INTO cats VALUES ("Socks", "2022-04-04", "white", 4.2)')
conn.execute('INSERT INTO cats VALUES ("Fluffy", "2022-10-30", "gray", 4.5)')

# commit data
conn.commit()

print(conn.execute('SELECT * FROM cats WHERE name = "Socks"').fetchall())
# [('Socks', '2022-04-04', 'white', 4.2)]
print(conn.execute('SELECT * FROM cats WHERE name = "Fluffy"').fetchall())
# [('Fluffy', '2022-10-30', 'gray', 4.5)]
