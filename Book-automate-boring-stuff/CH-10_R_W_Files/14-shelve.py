import shelve
from pathlib import Path

# folder path
fp = Path(__file__).resolve().parent

# open shelf
shelf_file = shelve.open(fp / 'mydata')

# store values in variables
shelf_file['cats'] = ['zophie', 'pooka', 'simone']

# close
shelf_file.close()

# test
shelf_file = shelve.open(fp / 'mydata')
print(shelf_file['cats'])
# ['zophie', 'pooka', 'simone']

# listing the keys and values
print("Keys:")
print(list(shelf_file.keys()))

print("Values:")
print(list(shelf_file.values()))

shelf_file.close()