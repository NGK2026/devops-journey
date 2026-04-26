import sqlite3
import pprint
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

# create reference / foreign keys
conn.execute('PRAGMA foreign_keys = ON')

print(conn.execute('SELECT name FROM sqlite_schema WHERE type = "table"').fetchall())

# create table cats with primary key
conn.execute("""
    CREATE TABLE IF NOT EXISTS cats (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        birthdate TEXT,
        fur TEXT,
        weight_kg REAL
        ) STRICT             
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS vaccinations (
        vaccine TEXT, 
        date_administered TEXT,
        administered_by TEXT,
        cat_id INTEGER,
        FOREIGN KEY(cat_id) REFERENCES cats(id)
    ) STRICT
""")

print(conn.execute('SELECT name FROM sqlite_schema WHERE type = "table"').fetchall())

# conn.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-06-06", "Dr. Echo", 1)')
# conn.execute('INSERT INTO vaccinations VALUES ("FeLV", "2023-06-06", "Dr. Echo", 1)')

# pprint.pprint(conn.execute('SELECT * FROM vaccinations').fetchall())

# add for muffin
# check id
print(conn.execute('SELECT * from cats WHERE name = "Muffin"').fetchall())
# add vaccine entry
# conn.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-07-11", "Dr. Echo", 11)')
pprint.pprint(conn.execute('SELECT * FROM vaccinations').fetchall())

# inner join print
check_joined = conn.execute("""
    SELECT * FROM cats INNER JOIN vaccinations ON cats.id = vaccinations.cat_id                            
""")

print(check_joined.fetchall())
"""
[(1, 'Zophie', '2021-01-24', 'gray tabby', 5.6, 'rabies', '2023-06-06', 'Dr. Echo', 1), 
(1, 'Zophie', '2021-01-24', 'gray tabby', 5.6, 'FeLV', '2023-06-06', 'Dr. Echo', 1), 
(11, 'Muffin', '2020-01-28', 'gray tabby', 5.7, 'rabies', '2023-07-11', 'Dr. Echo', 11)]
"""

