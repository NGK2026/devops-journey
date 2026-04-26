import sqlite3
import pprint
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# get table name
name = 'SELECT name FROM sqlite_schema WHERE type="table"'
print(conn.execute(name).fetchall())
# [('cats',)]

## rename cats table to 'felines' ##
# conn.execute('ALTER TABLE cats RENAME TO felines')

print(conn.execute(name).fetchall())
# [('felines',)]

# list column 3 info
print(conn.execute('PRAGMA TABLE_INFO(felines)').fetchall()[2])
# (2, 'fur', 'TEXT', 0, None, 0)

## rename fur column to description ##
# conn.execute('ALTER TABLE felines RENAME COLUMN fur TO description')

print(conn.execute('PRAGMA TABLE_INFO(felines)').fetchall()[2])
# (2, 'description', 'TEXT', 0, None, 0)

## add new column is_loved with boolian default to 1 (true) ##
# conn.execute('ALTER TABLE felines ADD COLUMN is_loved INTEGER DEFAULT 1')

pprint.pprint(conn.execute('SELECT * FROM felines LIMIT 3').fetchall())
# [('Zophie', '2021-01-24', 'gray tabby', 5.6, 1),
# ('Fudge', '2021-02-24', 'grey', 6.0, 1),
# ('Thor', '2013-05-14', 'black', 5.2, 1)]

# list all columns
pprint.pprint(conn.execute('PRAGMA TABLE_INFO(felines)').fetchall())
"""
[(0, 'name', 'TEXT', 1, None, 0),
 (1, 'birthdate', 'TEXT', 0, None, 0),
 (2, 'description', 'TEXT', 0, None, 0),
 (3, 'weight_kg', 'REAL', 0, None, 0),
 (4, 'is_loved', 'INTEGER', 0, '1', 0)]
"""

## remove is_loved column ##
# conn.execute('ALTER TABLE felines DROP COLUMN is_loved')

pprint.pprint(conn.execute('PRAGMA TABLE_INFO(felines)').fetchall())
"""
[(0, 'name', 'TEXT', 1, None, 0),
 (1, 'birthdate', 'TEXT', 0, None, 0),
 (2, 'description', 'TEXT', 0, None, 0),
 (3, 'weight_kg', 'REAL', 0, None, 0)]
"""

## backup table and use if not exists ##
backup_table = 'CREATE TABLE IF NOT EXISTS felines_1 AS SELECT * FROM felines'
# conn.execute(backup_table)

# check available tables
print(conn.execute(name).fetchall())
# [('felines',), ('felines_1',)]

## delete felines_1 table ##
# conn.execute('DROP TABLE felines_1')

print(conn.execute(name).fetchall())
# [('felines',)]

# Joining Multiple Tables with Foreign Keys