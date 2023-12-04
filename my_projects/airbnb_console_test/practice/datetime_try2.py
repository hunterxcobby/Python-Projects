#!/usr/bin/python3 

from datetime import datetime, time, date 

current_datetime = datetime.now()

formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
parsed_date = datetime.strptime("2023-12-04 15:30:00", "%Y-%m-%d %H:%M:%S")

print(formatted_date)
print(parsed_date)