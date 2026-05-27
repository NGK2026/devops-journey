import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

cat_name = 'Fudge'
cat_bday = '2021-02-24'
fur_color = 'grey'
cat_weight = 5.6

# secure value inserting!
# conn.execute('INSERT INTO cats VALUES (?, ?, ?, ?)',
#              [cat_name, cat_bday, fur_color, cat_weight])

# update 2nd row, weight column
# conn.execute('UPDATE cats SET weight_kg = 6.0 WHERE rowid = 2')

# delete third row
# conn.execute('DELETE FROM cats WHERE rowid = 3')