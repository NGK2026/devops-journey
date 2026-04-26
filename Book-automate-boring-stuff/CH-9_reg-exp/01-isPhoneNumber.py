def is_phone_number(text):
    if len(text) != 12:
        return False # Phone numbers have exactly 12 characters.
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # The first three characters must be numbers.
    if text[3] != '-':
        return False # The fourth character must be a dash.
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # The next three characters must be numbers.
    if text[7] != '-':
        return False # The eighth character must be a dash.
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # The next four characters must be numbers.
    return True

# print('Is 415-555-4242 a phone number?')
# print(is_phone_number('415-555-4242'))

# print('Is Moshi moshi a phone number?')
# print(is_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')