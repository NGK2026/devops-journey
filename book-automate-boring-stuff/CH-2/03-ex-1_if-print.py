# Write code that prints Hello if 1 is stored in spam, 
# prints Howdy if 2 is stored in spam, 
# and prints Greetings! if anything else is stored in spam.

# will make it a user input
print("please enter 1 or 2 or whatever")
userInput = input('> ')

if userInput == '1':
    print("Hello")
elif userInput == '2':
    print("Howdy")
else:
    print("Greetings!")