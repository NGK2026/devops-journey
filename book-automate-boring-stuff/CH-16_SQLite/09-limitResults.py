import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# limit results using slicing # inefficient way =/
print(f'\nFirst 3 results, inefficient:')
firstThreeUncool = conn.execute('SELECT * FROM cats').fetchall()[:3]
pprint.pprint(firstThreeUncool)

# limit to first 3 with LIMIT clause! efficient way *Thumbs up!*
print(f'\nFirst 3 results, efficient:')
firstThreeCool = conn.execute('SELECT * FROM cats LIMIT 3').fetchall()
pprint.pprint(firstThreeCool)

# limit must be after WHERE and ORDER clauses
print(f'\nLIMIT must be end clause:')
endClause = conn.execute('''
    SELECT * FROM cats WHERE fur="black"
    ORDER BY birthdate DESC
    LIMIT 4
    ''').fetchall()
pprint.pprint(endClause)

