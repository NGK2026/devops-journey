"""
'   H  e   l   l   o  ,     w  o  r  l  d   !  '
    0  1   2   3   4  5  6  7  8  9 10  11 12
  -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1
"""

greeting = 'Hello, World!'

print(greeting[0]) # H

print(greeting[-1]) # !

print(greeting[0:5]) # Hello

print(greeting[7:-1]) # World

print(greeting[7:]) # World!

greeting_slice = greeting[0:5]

print(greeting_slice) # Hello

print('Hello' in 'Hello, World') # True