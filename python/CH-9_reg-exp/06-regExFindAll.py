import re

pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # This regex has no groups.
match = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')

print(match) # ['415-555-9999', '212-555-0000']

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # This regex has groups.
match = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')

# will return a list of tuples. Each tuple represents a single match, 
# and the tuple has strings for each group in the regex.
print(match) # [('415', '555', '9999'), ('212', '555', '0000')]

# keep in mind
# doesn’t overlap matches
pattern = re.compile(r'\d{3}')
print(pattern.findall('1234')) # ['123']
print(pattern.findall('12345')) # ['123']
print(pattern.findall('123456')) # ['123', '456']