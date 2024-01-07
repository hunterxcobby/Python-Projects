#!/usr/bin/python3

from datetime import datetime, date, time 

current_datetime = datetime.now()
print(current_datetime) #some last digits are microseconds

# format time 
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

