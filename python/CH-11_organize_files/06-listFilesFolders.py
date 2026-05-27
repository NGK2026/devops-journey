import os
from pathlib import Path
import pprint

p = Path(__file__).resolve().parent

# store files in list and sort
# dirList = list(os.listdir(p))
dirList = os.listdir(p)
dirList.sort()
print(dirList)

# print each item
for x in dirList:
    print(x)
print()

# list path objects
dirList = list(p.iterdir())
dirList.sort()
# print each item
for x in dirList:
    print(x)
