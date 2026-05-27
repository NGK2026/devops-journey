import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent

conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)
backup_conn = sqlite3.connect(p / 'database/backup.db', isolation_level=None)

conn.backup(backup_conn)