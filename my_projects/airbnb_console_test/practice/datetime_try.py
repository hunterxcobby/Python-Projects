#!/usr/bin/python3


from datetime import datetime, date, time 

class DateTime():

    def components(self):
        current_datetime=datetime.now()
        print(current_datetime.year)
        print(current_datetime.month)
        print(current_datetime.day)
        print(current_datetime.hour)
        print(current_datetime.minute)
        print(current_datetime.second)
        

clock = DateTime()
clock.components()