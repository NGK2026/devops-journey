from pathlib import Path

p = Path(__file__).resolve().parent

# create folders
(p / 'spam').mkdir(exist_ok=True)
(p / 'spam/eggs').mkdir(exist_ok=True)
(p / 'spam/eggs2').mkdir(exist_ok=True)
(p / 'spam/eggs/bastirma').mkdir(exist_ok=True)

# create files in folders
for f in ['spam/file1.txt', 'spam/eggs/file2.txt',\
          'spam/eggs/file3.txt', 'spam/eggs/bastirma/file4.txt']:
    with open(p / f, 'w', encoding='utf-8') as file:
        file.write('Hellows')

print('\nfolders and files created')



