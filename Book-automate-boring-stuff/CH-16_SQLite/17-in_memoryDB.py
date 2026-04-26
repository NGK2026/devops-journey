import sqlite3
import pprint
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

# create inmemory db
memory_db_conn = sqlite3.connect(':memory:', isolation_level=None)

# create table
memory_db_conn.execute('CREATE TABLE test (name TEXT, number REAL)')
# insert data
memory_db_conn.execute('INSERT INTO test VALUES ("foo", 3.14)')

# create file db
file_db_conn = sqlite3.connect(p / 'database/test.db', isolation_level=None)

# backup/save memory onto file
memory_db_conn.backup(file_db_conn)
