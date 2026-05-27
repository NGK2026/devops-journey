name = 'Nazeeh'

age = 38

print(f'My name is {name}. I am {age} years old.')
# My name is Nazeeh. I am 38 years old.

print(f'In ten years I will be {age + 10}')
# In ten years I will be 48

print(f'{name}') # Nazeeh
print(f'{{name}}') # {name}

# Alternatives: % and format()

# %
print('My name is %s. I am %s years old.' % (name, age))
# My name is Nazeeh. I am 38 years old.

print('In 10 years I will be %s' % (age + 10))
# In 10 years I will be 48

# format()
print('My name is {}. I am {} years old.'.format(name, age))
# My name is Nazeeh. I am 38 years old.

print('{1} years ago, {0} was born and named {0}.'.format(name, age))
# 38 years ago, Nazeeh was born and named Nazeeh.