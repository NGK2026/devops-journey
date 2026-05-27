import re

vowel_pattern = re.compile(r'[aeiouAEIOU]')
match = vowel_pattern.findall('RoboCop eats BABY FOOD.')

print(match) # ['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']

# [a-zA-Z0-9] will match all lowercase, uppercase letters, and numbers

# Negative character class:
# will match all other chars
# includes spaces, newlines, punctuation characters, and numbers.

consonant_pattern = re.compile(r'[^aeiouAEIOU]')
match = consonant_pattern.findall('RoboCop eats BABY FOOD.')

print(match) 
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']