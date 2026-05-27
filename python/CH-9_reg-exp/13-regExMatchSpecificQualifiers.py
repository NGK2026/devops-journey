import re

haRegex = re.compile(r'(Ha){3}') # will match just 3
match1 = haRegex.search('HaHaHa')
print(match1.group()) 
# HaHaHa

haRegex = re.compile(r'(Ha){3,5}') # will match from 3 til 5
# (HaHaHa)|(HaHaHaHa)|(HaHaHaHaHa) 

# {3,} # 3 or more
# {,5} # 0 to 5

# '(Ha){3,5}' matches up to and including five instances of the '(Ha)' qualifier.
# uses , not : (like lists)
# {3,5} not [3:5]