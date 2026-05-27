import re

# Hello must be at the start of string ^
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello, world!'))
# <re.Match object; span=(0, 5), match='Hello'>
print(begins_with_hello.search('He said "Hello."'))
# None

# digit must be at end of string $
ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 42'))
# <re.Match object; span=(16, 17), match='2'>
print(ends_with_number.search('Your number is forty two.'))
# None

# digits start middle end of string
whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('1234567890'))
# <re.Match object; span=(0, 10), match='1234567890'>
print(whole_string_is_num.search('12345xyz67890') == None)
# None

# match only word bountry cat... \b
pattern = re.compile(r'\bcat.*?\b')
print(pattern.findall('The cat found a catapult catalog in the catacombs.'))
# ['cat', 'catapult', 'catalog', 'catacombs']

# match not word boundry? \B to find mid word match
pattern = re.compile(r'\Bcat\B')
print(pattern.findall('certificate'))  # Match
# ['cat']
print(pattern.findall('catastrophe'))
# None