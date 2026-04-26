from pathlib import Path

# specify file path
fp = Path(__file__).resolve().parent / 'spam.txt'

# open file
hello_file = open(fp, encoding='UTF-8')


hello_content = hello_file.read()
print(f"- File reads:\n{hello_content}")

# create sonnet29.txt
# path
sonnetPath = Path(__file__).resolve().parent / 'sonnet29.txt'

# write with write_text()
sonnetPath.write_text("When, in disgrace with fortune and men's eyes,\
    \nI all alone beweep my outcast state,\
    \nAnd trouble deaf heaven with my bootless cries,\
    \nAnd look upon myself and curse my fate,")

print(sonnetPath.read_text() + '\n\n') # cool, done.

# open file and readlines(), returns list
sonnet_file = open(sonnetPath, encoding='UTF-8')
print(f"readlines():\n{sonnet_file.readlines()}")