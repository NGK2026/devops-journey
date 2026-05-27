import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# sort by fur color (default = ASC)
print(f'\nFur color:')
furOrder = conn.execute('SELECT * FROM cats ORDER BY fur').fetchall()
pprint.pprint(furOrder)

# first sort by fur, then by birthdate for each color
print(f'\nFur then date of each fur:')
furDate = conn.execute('SELECT * FROM cats ORDER BY fur, birthdate').fetchall()
pprint.pprint(furDate)

# sort by fur 'ascending', then by birthdate for each color 'decending
print(f'\nFur ASC then date of each fur DESC:')
ascDesc = conn.execute('SELECT * FROM cats ORDER BY fur ASC, birthdate DESC')
pprint.pprint(ascDesc.fetchall())
