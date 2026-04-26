import os
from pathlib import Path

here = Path.cwd()
print(here)
# /home/student/Projects/automate-boring-stuff

# path to script
script_path = Path(__file__).resolve()
print(f"Script path:\n{script_path}")

# path to dir containing script
script_dir = script_path.parent
print(f"Folder containing script:\n{script_dir}")

# create new folders
os.makedirs(script_dir/'test'/'cool')
# also
Path(script_dir/'new').mkdir()
# .mkdir(parents=True) to create folder series


