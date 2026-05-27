from pathlib import Path

# path of current working dir
p = Path(__file__).resolve().parent

# path of file
# fp = Path(p, 'spam.txt') # first try..
# cleaner way:
fp = p / 'spam.txt'

# write file
print(fp.write_text('Hello, file!'))
# 12 --> number of chars written to file

# read the file
print(fp.read_text())