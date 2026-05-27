import pprint
# Join:

print(', '.join(['cats', 'rats', 'bats'])) 
# cats, rats, bats

print(' '.join(['My', 'name', 'is', 'Nazeeh'])) 
# My name is Nazeeh

print('ABC'.join(['My', 'name', 'is', 'Simon']))
# MyABCnameABCisABCSimon

# Split:

print('My name is Nazeeh'.split())
# ['My', 'name', 'is', 'Nazeeh']

print('MyABCnameABCisABCNazeeh'.split('ABC'))
# ['My', 'name', 'is', 'Nazeeh']

print('My name is Nazeeh'.split('m'))
# ['My na', 'e is Nazeeh']

spam = '''Dear Nazeeh,
There is a milk bottle in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Nazeeh'''

print(spam.split('\n'))
# ['Dear Nazeeh,', 'There is a milk bottle in the fridge',
#  'that is labeled "Milk Experiment."', '', 'Please do not drink it.',
#  'Sincerely,', 'Nazeeh']

