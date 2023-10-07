#!usr/bin/python3

import datetime

# display the current date
x = datetime.datetime.now()
print(x)

# the year and name of weekday:
print(x.year)
print(x.strftime("%A"))
