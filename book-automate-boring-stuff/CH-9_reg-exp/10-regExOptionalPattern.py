import re

# ? as saying, “Match zero or one of the group preceding this question mark.”
# If you need to match an actual question mark character, escape it with \?.

pattern = re.compile(r'42!?')

print(pattern.search('42!'))
# <re.Match object; span=(0, 3), match='42!'>
print(pattern.search('42'))
# <re.Match object; span=(0, 2), match='42'>

pattern = re.compile(r'42?!')

print(pattern.search('42!'))
# <re.Match object; span=(0, 3), match='42!'>
print(pattern.search('4!'))
# <re.Match object; span=(0, 2), match='4!'>
print(pattern.search('42') == None)  # No match
# True

pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')

match1 = pattern.search('My number is 415-555-4242')
print(match1.group())
# 415-555-4242

match2 = pattern.search('My number is 555-4242')
print(match2.group())
# 555-4242