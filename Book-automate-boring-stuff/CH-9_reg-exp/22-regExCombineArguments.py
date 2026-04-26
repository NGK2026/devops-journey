import re

# You can get around this limitation by combining the 
# re.IGNORECASE, 
# re.DOTALL, 
# and re.VERBOSE variables using the pipe character (|)

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL)

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)