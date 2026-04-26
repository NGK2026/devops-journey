# finding values
spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello'))
print(spam.index('heyas'))

# adding values
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam.insert(1, 'chicken')
print(spam)

# removing values
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # will remove only first instance
print(spam)

# sorting values
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
print(spam)
# reverse
spam.sort(reverse=True)
print(spam) # ['Elephants', 'Dogs', 'Cats', 'Badgers', 'Ants']


# capitals first
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam) # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']


# sort by lower
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam) # ['a', 'A', 'z', 'Z']


# reversing values
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam) # ['moose', 'dog', 'cat']