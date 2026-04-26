# Two arguments. 
# The first is a string that should replace any matches. 
# The second is the string of the regular expression.

import re

agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.'))
# CENSORED contacted CENSORED.

# show just first letter of name
agent_pattern = re.compile(r'Agent (\w)\w*')
print(agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.'))
# A**** contacted B****.

# show second letter only
agent_pattern = re.compile(r'Agent \w(\w)\w*')
print(agent_pattern.sub(r'*\1***', 'Agent Alice contacted Agent Bob.'))
# *l*** contacted *o***.

# show third letter only
agent_pattern = re.compile(r'Agent \w\w(\w)\w*')
print(agent_pattern.sub(r'**\1*', 'Agent Alice contacted Agent Bob.'))
# **i* contacted **b*.

# show first and third only
agent_pattern = re.compile(r'Agent (\w)\w(\w)?\w*') # in case only 2 letter name
print(agent_pattern.sub(r'\1*\2**', 'Agent Alice contacted Agent Bob.'))
# A*i** contacted B*b**.