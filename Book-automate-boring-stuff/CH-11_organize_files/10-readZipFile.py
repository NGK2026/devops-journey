import zipfile
from pathlib import Path

# p = Path(__file__).resolve().parent
print(f'\n{Path.cwd()}')
# root = p.parent
# example_zip = zipfile.ZipFile(root / 'example.zip')
# print()
# print(example_zip.namelist())

# file1_info = example_zip.getinfo(p / 'file1.txt')
# print(f'\n{file1_info}')

example_zip = zipfile.ZipFile('example.zip')
print()
print(example_zip.namelist())

file1_info = example_zip.getinfo('file1.txt')
print(f'\nFile info size:\n{file1_info.file_size}')
print(f'\nfile compress size:\n{file1_info.compress_size}')
print(f'Compressed file is {round(file1_info.file_size / file1_info
    .compress_size, 2)}x smaller!')

example_zip.close()