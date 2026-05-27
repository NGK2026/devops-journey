# 
# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments
# 

import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    # backup all contents of "folder" into a zip file
    folder = Path(folder).resolve() # folder must be path object, not string

    # We want the ZIP to start from 'spam/', so the base is the folder's parent
    base_dir = folder.parent

    number = 1
    while True:
        zip_filename = f"{folder.name}_{number}.zip"
        if not Path(zip_filename).exists():
            break
        number += 1

    # Create zip file
    print(f'Creating {zip_filename}...')

    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        for folder_name, subfolders, filenames in os.walk(folder):
            folder_path = Path(folder_name)

            # optional: include empty folders
            rel_path = folder_path.relative_to(base_dir)
            backup_zip.write(folder_path, arcname=str(rel_path))

            for filename in filenames:
                file_path = folder_path / filename
                # remove base_dir to clean inner path
                arcname = file_path.relative_to(base_dir)

                print(f'adding file {arcname}...')
                backup_zip.write(file_path, arcname=str(arcname))
    print('done.')


    # backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # # TODO: walk the entire folder and compress files in each folder.
    # for folder_name, subfolders, filenames in os.walk(folder):
    #     folder_name = Path(folder_name)
    #     print(f'Adding files in folder {folder_name}...')

    #     # add all files in this folder to the zip file
    #     for filename in filenames:
    #         print(f'adding file {filename}...')
    #         backup_zip.write(folder_name / filename)
    
    # backup_zip.close()
    # print('Done.')

backup_to_zip(Path(__file__).resolve().parent / 'spam')
