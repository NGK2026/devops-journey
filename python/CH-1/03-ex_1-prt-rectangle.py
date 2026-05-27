# Write a program that prints a rectangle of capital O characters. 
# For example, the following rectangle has a width of eight and a height of five

print("enter width:")
width = input('> ')
print("enter height")
height = input('> ')

round = 0

while round < int(height):
    print('O' * int(width))
    round = round + 1
