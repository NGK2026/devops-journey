import zipfile
from pathlib import Path

# p = Path(__file__).resolve().parent

# with open(p / 'file1.txt', 'w', encoding='utf-8') as file_obj:
#     file_obj.write('hello' * 1000)

# with zipfile.ZipFile('example.zip', 'w') as example_zip:
#     example_zip.write(p / 'file1.txt', compress_type=zipfile.ZIP_DEFLATED,\
#                       compresslevel=9)
    
# 'w' writes or overwrites
# 'a' appends to

with open('file1.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('hello' * 1000)

with zipfile.ZipFile('example.zip', 'w') as example_zip:
    example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED,\
                      compresslevel=9)