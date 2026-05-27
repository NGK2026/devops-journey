import re

name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
print(name_match.group(1)) # Al
print(name_match.group(2)) # Sweigart

# Non greedy
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.>')
print(match1.group())
# <To serve man>

# Greedy
greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
print(match2.group())
# <To serve man> for dinner.>