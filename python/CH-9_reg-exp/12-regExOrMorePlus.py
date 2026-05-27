import re

# The + (or plus) means “match one or more.” Unlike the star

pattern = re.compile('Eggs( and spam)+')

print(pattern.search('Eggs'))
# None
print(pattern.search('Eggs and spam').group())
# Eggs and spam
print(pattern.search('Eggs and spam and spam'))
# <re.Match object; span=(0, 22), match='Eggs and spam and spam'>
print(pattern.search('Eggs and spam and spam and spam'))
# <re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>