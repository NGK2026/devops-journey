my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
    print('I dont have a pet named ' + name)
else:
    print(name + ' is my pet.')