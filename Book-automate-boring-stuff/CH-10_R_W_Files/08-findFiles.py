import pprint
from pathlib import Path

# p = Path('/home/student/Projects')
# p = Path.cwd()
p = Path(__file__).resolve().parent
# folder = p.parent

print(f"Current folder:\n{p}")

# print(folder.glob('*')) # nothing useful
# print()
# print(f"List:\n{list(folder.glob('*'))}")

files = list(p.glob('*'))

print(f"unsorted list:\n{files}\n")

files.sort()

print(f"sorted list:\n{files}\n")

print("\nLoop of folder glob (unsorted):")
# loop through list and print
view = ''
for name in p.glob('*'):
    # view = view + name.name + '\n'
    print(name.name)

print("\nloop view of the files sorted:")

for file in files:
    print(file.name)