import re

# Enable “verbose mode” by 
# passing the variable re.VERBOSE as the second argument to re.compile().
# Spread the regular expression over multiple lines 
# and use comments to label its components.

pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)

# I advise you to instead use the Humre module, covered later in this chapter.