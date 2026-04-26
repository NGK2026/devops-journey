import re

at_re = re.compile(r'.at')
match = at_re.findall('The cat in the hat sat on the flat mat.')

print(match)
# ['cat', 'hat', 'sat', 'lat', 'mat']

at_re = re.compile(r'..at')
match = at_re.findall('The cat in the hat sat on the flat mat.')

print(match)
# [' cat', ' hat', ' sat', 'flat', ' mat']