#!/usr/bin/python3

# Ask for details
year_of_birth = input("Year of birth: ")
month_of_birth = input("Month of birth (0-12): ")
day_of_birth = input("Day of the month: ")

# current year
current_year = input("Which year are you?")

# Display details
print("Your date of birth is:", end=" ")
print(day_of_birth, month_of_birth, year_of_birth, sep="-")

# Calculate the age
age = int(current_year) - year_of_birth
