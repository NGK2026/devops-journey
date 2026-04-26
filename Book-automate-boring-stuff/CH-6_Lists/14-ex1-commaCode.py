spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(item):
    line = ''
    last = item[-1]
    for i in item:
        if i == last:
            line = line + 'and ' + i + '.'
        else:
            line = line + i + ', '
    return line

print(commaCode(spam))

