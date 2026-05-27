import datetime

print(datetime.datetime.strptime('October 21, 2026', '%B %d, %Y'))
# datetime.datetime(2026, 10, 21, 0, 0)
print(datetime.datetime.strptime('2026/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# datetime.datetime(2026, 10, 21, 16, 29)
print(datetime.datetime.strptime("October of '26", "%B of '%y"))
# datetime.datetime(2026, 10, 1, 0, 0)
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
# datetime.datetime(2063, 11, 1, 0, 0)
print(datetime.datetime.strptime("November of '73", "%B of '%y"))
# datetime.datetime(1973, 11, 1, 0, 0)