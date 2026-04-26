# Justify:

print('Hello'.rjust(10)) # total 10 chars of str (5 spaces, 5 letters)
# '     Hello'

print('Hello'.rjust(20)) # total 20 chars of string
#                Hello

print('Hello, World'.rjust(20)) # 9 spaces, 11 chars = 20
#         Hello, World

print('Hello'.rjust(20, '*')) # 15 *, 5 chars = 20 total
# ***************Hello

print('Hello'.ljust(20, '-'))
# Hello---------------

print('Hello'.center(20))
#        Hello        

print('Hello'.center(20, '=')) # 7 + 5 + 8 = 20
# =======Hello========

# Removing Whitespace:

spam = '    Hello, World    '

print(spam.strip())
# Hello, World

print(spam.lstrip())
# 'Hello, World    '

print(spam.rstrip())
# '    Hello, World'

spam = 'SpamSpamBaconSpamEggsSpamSpam'

print(spam.strip('ampS')) # order of letters dont matter
# BaconSpamEggs