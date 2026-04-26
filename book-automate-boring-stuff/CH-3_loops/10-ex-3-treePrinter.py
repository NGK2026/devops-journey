# a for loop to print a triangular pine tree of a size the user asks for.
# The tree branches should be printed as a number of rows of ^ characters, 
# while the trunk should always be two # characters.

print('how many branches?')
userInput = int(input('> '))

solidSpace = userInput -1
space = userInput - 1
leaves = 1


for i in range(userInput):
    print((' ' * space) + ('^' * leaves))
    leaves = leaves + 2
    space = space - 1
    if i == userInput - 1:
        for j in range(2):
            print((' ' * solidSpace) + '#')

    

# for i in range(userInput):
#     branchesTotal = branchesTotal + 2
#     print(branchesTotal)

# print(branchesTotal)

# center = branchesTotal // 2
# centerTrunk = center

# for i in range(userInput):
#     print(' ' * int(center))
#     print('^' * int(branches))
#     branches = branches + 2
#     center = center - 1
#     if i == userInput - 1:
#         for j in range(2):
#             print(' ' * int(centerTrunk) + '#')    

