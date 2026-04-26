import re

greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group()) # HaHaHaHaHa

# question mark can have two meanings 
# in regular expressions: declaring a lazy match 
# or declaring an optional qualifier. 
lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group()) # HaHaHa