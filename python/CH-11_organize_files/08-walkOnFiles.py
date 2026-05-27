import os, shutil
from pathlib import Path

# p = Path(__file__).resolve().parent

# base dir for relative path name
# more professional
base_dir = Path(__file__).resolve().parent
print()

for folder_name, subfolders, filenames in os.walk(base_dir / 'spam'):
    # optional:
    # convert absolute path to relative
    rel_folder = Path(folder_name).relative_to(base_dir)
    print(f'The current folder is {rel_folder}')


    for subfolder in subfolders:
        print(f'SUBFOLDER of {{{rel_folder}}}: {subfolder}')

    for filename in filenames:
        print(f'FILE INSIDE {{{rel_folder}}}: {filename}')
        # rename file to uppercase
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())
    
    print()

print('Files renamed!')

