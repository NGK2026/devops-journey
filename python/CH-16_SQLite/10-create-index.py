import sqlite3
from pathlib import Path
import pprint

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# create indexes
conn.execute('CREATE INDEX idx_name ON cats (name)')
conn.execute('CREATE INDEX idx_birthdate ON cats (birthdate)')

# see all indexes for a specific table
view = conn.execute('''
    SELECT name FROM sqlite_schema
    WHERE type = "index"
    AND tbl_name = "cats"
''').fetchall()

print(view)
# [('idx_name',), ('idx_birthdate',)]

# delete / drop index
conn.execute('DROP INDEX idx_name')
print(view)
# [('idx_birthdate',)]