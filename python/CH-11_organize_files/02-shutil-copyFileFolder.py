import shutil
from pathlib import Path

h = Path(__file__).resolve().parent

# copy to parent folder
shutil.copy(h / 'spam/file1.txt', h)

# create copy with other name in same folder
shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')

# create copy of folder with other name
shutil.copytree(h / 'spam', h / 'spam_backup')