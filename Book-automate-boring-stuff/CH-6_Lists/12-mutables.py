name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]
print(new_name) # 'Zophie the cat'

eggs = ['A', 'B', 'C']
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append('x')
eggs.append('y')
eggs.append('z')
print(eggs) # ['x', 'y', 'z']