import re

# match any of the strings 
# 'Caterpillar', 'Catastrophe', 'Catch', or 'Category'. 
# Since all of these strings start with Cat, 
# it would be nice if you could specify that prefix only once.

pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')

print(match.group()) # Catch
print(match.group(1)) # ch