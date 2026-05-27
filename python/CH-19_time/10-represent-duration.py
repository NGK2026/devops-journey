import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

print(delta.days, delta.seconds, delta.microseconds)

print(delta.total_seconds())

print(str(delta))

# calculate 1000 days from now

now = datetime.datetime.now()
print(f'\nnow: {now}\n')

thousand_days = datetime.timedelta(days=1000)
print(f'1000 days from now:\n{now + thousand_days}\n')

oct_21st = datetime.datetime(2026, 10, 21, 16, 29, 0)
about_thirty_years = datetime.timedelta(days=365 * 30)

print(f'oct 21st:\n{oct_21st}\n')
print(f'about 30 years less:\n{oct_21st - about_thirty_years}\n')
print(f'about 60 years less:\n{oct_21st - (2 * about_thirty_years)}\n')

