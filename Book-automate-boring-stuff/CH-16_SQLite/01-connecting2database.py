import sqlite3
from pathlib import Path

# path and folder
p = Path(__file__).resolve().parent
(p / 'database').mkdir(exist_ok=True)

# connect / create
conn = sqlite3.connect(p / 'database/example.db', isolation_level=None)

