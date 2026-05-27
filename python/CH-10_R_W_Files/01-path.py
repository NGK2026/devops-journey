from pathlib import Path

print(Path('spam', 'bacon', 'eggs'))
# spam/bacon/eggs

print(str(Path('spam', 'bacon', 'eggs')))
# spam/bacon/eggs

# joins names from a list of filenames to the end of a folder’s name
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(Path(r'~/Documents', filename))
"""
~/Documents/accounts.txt
~/Documents/details.csv
~/Documents/invite.docx
"""

