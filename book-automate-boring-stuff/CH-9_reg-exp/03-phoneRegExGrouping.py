import re

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')

print(mo.group(1)) # 415
print(mo.group(2)) # 555-4242
print(mo.group(0)) # 415-555-4242
print(mo.group) # 415-555-4242

# retrieve all groups at once
print(mo.groups()) # ('415', '555-4242')

# multiple-assignment trick
area_code, main_number = mo.groups()

print(area_code) # 415
print(main_number) # 555-4242