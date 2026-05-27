spam = 'Hello, world!'

print(spam.upper()) # HELLO, WORLD!

print(spam.lower()) # hello, world!

print(spam.islower()) # False

print('HELLO'.isupper()) # True

print('Hello'.upper().lower().upper()) # HELLO

# isX?

print('hello'.isalpha()) # True

print('hello123'.isalpha()) # False

print('hello123'.isalnum()) # True

print('hello'.isalnum()) # True

print('123'.isdecimal()) # True

print('    '.isspace()) # True

print('This Is Title Case'.istitle()) # True