from pathlib import Path

# folder path
fp = Path(__file__).resolve().parent

# write file
with open(fp / 'data.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello, With!')

# read file
with open(fp / 'data.txt', encoding='utf-8') as file_obj:
    content = file_obj.read()

print(content)