spam = ['cat', 'dog']
if spam[0] == 'cat': # not stable
    print('A cat is the first item.')
else:
    print('The first item is not a cat.')
# if the list in spam is empty, 
# the spam[0] code will cause an IndexError: list Index out of range error.

# fix:
spam = []
if len(spam) > 0 and spam[0] == 'cat':
    print('A cat is the first item.')
else:
    print('The first item is not a cat.')