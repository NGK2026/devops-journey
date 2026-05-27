# for supaspeed

import sqlite3
import pprint
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

# load file db
file_db_conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# load memory db
memory_db_conn = sqlite3.connect(':memory:', isolation_level=None)

# backup / put file into memory
file_db_conn.backup(memory_db_conn)

# check it out
pprint.pprint(memory_db_conn.execute('SELECT * FROM cats LIMIT 3').fetchall())

## any error or crash will lose the memory db.
### use try / except statement to mitigate errors and except to save db

