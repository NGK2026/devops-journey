"""
%Y Year with century, as in '2026'

%y Year without century, '00' to '99' (1970 to 2069)

%m Month as a decimal number, '01' to '12'

%B Full month name, as in 'November'

%b Abbreviated month name, as in 'Nov'

%d Day of the month, '01' to '31'

%j Day of the year, '001' to '366'

%w Day of the week, '0' (Sunday) to '6' (Saturday)

%A Full weekday name, as in 'Monday'

%a Abbreviated weekday name, as in 'Mon'

%H Hour (24-hour clock), '00' to '23'

%I Hour (12-hour clock), '01' to '12'

%M Minute, '00' to '59'

%S Second, '00' to '59'

%p 'AM' or 'PM'

%% Literal '%' character
"""

import datetime

oct_21st = datetime.datetime(2026, 10, 21, 16, 29, 0)

print(oct_21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct_21st.strftime('%I:%M %p'))
print(oct_21st.strftime("%B of '%y"))