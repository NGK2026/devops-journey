import send2trash
from pathlib import Path

p = Path(__file__).resolve().parent

# create file
with open(p / 'spam/text1.txt', 'w', encoding='utf-8') as file:
    file.write('Hellow')
    print(f'\nFile created.\n')

# send to trash, not perm delete
send2trash.send2trash(p / 'spam/text1.txt')
print('Sent to trash')

