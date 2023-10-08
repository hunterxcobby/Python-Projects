#!/usr/bin/python3

# name = "Cobby Sefah"
# age = 21

# Defining the function
def age_calc(name, yob, current_year): # parameters(placeholderss)
    age = current_year - yob
    print(f"{name}, you are {age} years old")

# Calling the function (positional arguments)
age_calc("Cobby", 2002, 2023) # arguments(values)
age_calc("Ami", 2003, 2023)

# Calling the function (keyword arguments)
age_calc(yob=2002, current_year=2023, name="Cobby")