import re

pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = pattern.search('My phone number is (415) 555-4242.')

print(mo.group(1)) # (415)
print(mo.group(2)) # 555-4242