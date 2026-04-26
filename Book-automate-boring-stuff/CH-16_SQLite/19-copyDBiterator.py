import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

with open(p / 'database/exampledb-queries.txt', 'w', encoding='utf-8') as fileObj:
    for line in conn.iterdump():
        fileObj.write(line + '\n')