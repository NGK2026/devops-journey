import datetime
import time

halloween_2039 = datetime.datetime(2039, 10, 31, 0, 0, 0)

while datetime.datetime.now() < halloween_2039:
    time.sleep(1)