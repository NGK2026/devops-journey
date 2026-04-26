import random

pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))

print()

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)