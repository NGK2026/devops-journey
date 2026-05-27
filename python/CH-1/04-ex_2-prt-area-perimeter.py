# Write a program that accepts the width and length of a rectangular space 
# from the user and then calculates both the perimeter and area of this space. 

print("enter width:")
width = int(input('> '))
print("enter height")
height = int(input('> '))

print()
print('Area of the rectangle:') 
print(str(width * height))
print('Perimeter of the rectangle:') 
print(str((width + height) * 2))