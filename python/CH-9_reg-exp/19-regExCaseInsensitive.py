import re

# To make your regex case-insensitive, 
# you can pass re.IGNORECASE 
# or re.I as a second argument to re.compile()

pattern = re.compile(r'robocop', re.I)
print(pattern.search('RoboCop is part man, part machine, all cop.').group())
# RoboCop

print(pattern.search('ROBOCOP protects the innocent.').group())
# ROBOCOP

print(pattern.search('Have you seen robocop?').group())
# robocop