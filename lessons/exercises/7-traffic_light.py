#!/usr/bin/python3

"""Give us directions based on traffic rules"""

# Ask for colour
colour = input("What is the colour of the light? ")

if (colour == "red"):
    print("STOP !!!")
elif (colour == "yellow"):
    print("Get ready !!!")
elif (colour == "green"):
    print("GO !!!")
else:
    print("invalid colour")