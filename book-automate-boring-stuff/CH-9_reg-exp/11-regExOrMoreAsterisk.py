import re

# The * (called the star or asterisk) means “match zero or more.”

pattern = re.compile(r'Eggs( and spam)*')

print(pattern.search('Eggs'))
# <re.Match object; span=(0, 4), match='Eggs'>
print(pattern.search('Eggs and spam'))
# <re.Match object; span=(0, 13), match='Eggs and spam'>
print(pattern.search('Eggs and spam and spam'))
# <re.Match object; span=(0, 22), match='Eggs and spam and spam'>
print(pattern.search('Eggs and spam and spam and spam'))
# <re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>