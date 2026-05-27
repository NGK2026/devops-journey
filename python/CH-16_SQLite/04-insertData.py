import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

conn.execute('''
    CREATE TABLE IF NOT EXISTS cats(
        name TEXT NOT NULL,
        birthdate TEXT,
        fur TEXT,
        weight_kg REAL
    ) STRICT
''')

conn.execute('INSERT INTO cats VALUES("Zophie", "2021-01-24", "black", 5.6)')
