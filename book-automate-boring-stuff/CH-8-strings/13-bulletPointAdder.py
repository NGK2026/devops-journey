"""
# copy these first:

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the "lines" list.
    lines[i] = '* ' + lines[i] # Add a star to each string in the "lines" list.

text = '\n'.join(lines)    
pyperclip.copy(text)

print(text)