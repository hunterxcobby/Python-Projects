#!/usr/bin/python3

from datetime import timedelta, datetime

current_datetime = datetime.now()

time_difference = timedelta(days=5, hours=3)
new_date = current_datetime + time_difference

print(time_difference)
print(new_date)