from pathlib import Path

h = Path(__file__).resolve().parent

(h / 'spam').mkdir(exist_ok=True) # if exist, suppress error
with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')

