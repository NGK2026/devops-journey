import re

no_newline_re = re.compile('.*')
print(no_newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# Serve the public trust.

newline_re = re.compile('.*', re.DOTALL)
print(newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# Serve the public trust.
# Protect the innocent.
# Uphold the law.