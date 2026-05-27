# a for loop to print a triangular pine tree of a size the user asks for.
# The tree branches should be printed as a number of rows of ^ characters, 
# while the trunk should always be two # characters.
import random

print('how many branches?')
userInput = int(input('> '))

solidSpace = userInput -1
space = userInput - 1
leaves = 1


for i in range(userInput):
    treeSpace = ' ' * space
    leaf = ''
    for u in range(leaves):
        leafType = random.randint(1, 4)
        if leafType == 1:
            leaf = leaf + 'o'
        else:
            leaf = leaf + '^'

    leaves = leaves + 2
    space = space - 1
    print(treeSpace + leaf)


for j in range(2):
    print((' ' * solidSpace) + '#')