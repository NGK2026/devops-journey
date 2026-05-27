import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

pprint.pprint(conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall())
print()

for row in conn.execute('SELECT * FROM cats WHERE fur = "black"'):
    print(f'{row[0]} has {row[2]} fur.')

print()
# another:
match = """
    SELECT * FROM cats 
    WHERE fur = "black" OR birthdate >= "2024-01-01"
"""

res = conn.execute(match).fetchall()
pprint.pprint(res)

print()
# and another
matching_cats = conn.execute('SELECT * FROM cats WHERE fur = "black"'
'OR birthdate >= "2024-01-01"').fetchall()
pprint.pprint(matching_cats)

print()
# the LIKE wildcard ( case insensitive )
# all that end with "y"
wildY = conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%y"')
pprint.pprint(wildY.fetchall())

print()
# all that start with "B"
bWild = conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "B%"')
pprint.pprint(bWild.fetchall())

print()
# all with "o" in the middle
wildO = conn.execute('SELECT rowid, name FROM cats WHERE name like "%o%"')
pprint.pprint(wildO.fetchall())

print()
# case sensitive match with GLOB
caseSense = conn.execute('SELECT rowid, name FROM cats WHERE name GLOB "*b*"')
pprint.pprint(caseSense.fetchall())