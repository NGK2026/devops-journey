import os
from pathlib import Path

h = Path(__file__).resolve().parent

# delete single files
# dry run, safety reasons
for filename in h.glob('*.txt'):
    print('Deleting', filename.name)
    #os.unlink(filename)