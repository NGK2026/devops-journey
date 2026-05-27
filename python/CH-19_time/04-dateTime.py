import datetime, time


print(datetime.datetime.now()) # 2026-04-24 11:02:22.326978
dt = datetime.datetime(2026, 10, 21, 16, 29, 0)
print(dt) # 2026-10-21 16:29:00

print(dt.year, dt.month, dt.day) # 2026 10 21
print(dt.hour, dt.minute, dt.second) # 16 29 0

# returns a datetime object for the moment 1,000,000 seconds after the Unix epoch
print(datetime.datetime.fromtimestamp(1000000)) # 1970-01-12 15:46:40


# returns a datetime object for the current moment.
# same as datetime.now()
print(datetime.datetime.fromtimestamp(time.time())) # 2026-04-24 11:05:07.452553

# compare #
halloween_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)
new_years_2027 = datetime.datetime(2027, 1, 1, 0, 0, 0)
oct_31_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)

print(halloween_2026 == oct_31_2026)
# True
print(halloween_2026 > new_years_2027)
# False
print(new_years_2027 > halloween_2026)
# True
print(new_years_2027 != oct_31_2026)
# True