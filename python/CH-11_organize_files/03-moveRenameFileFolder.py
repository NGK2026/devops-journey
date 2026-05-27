import shutil
from pathlib import Path

h = Path(__file__).resolve().parent

# create destination folder
(h / 'spam2').mkdir() 
# can add exist_ok=True
# to suppress error if exists.

# move file to other folder (if folder exists)
shutil.move(h / 'spam/file1.txt', h / 'spam2')

# else like so:
# will move and rename, not create new folder 
# and place it in
shutil.move(h / 'spam/file3.txt', h / 'spam3')