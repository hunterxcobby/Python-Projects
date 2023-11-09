#!/usr/bin/python3

# Defining a function named 'add' that accepts a variable number of arguments.
def add(*numbers):  # *numbers allows the function to accept any number of arguments and stores them in a tuple called 'numbers'.
    c = 0  # Initializing a variable 'c' to hold the sum of the numbers.
    for i in numbers:  # Looping through the provided numbers.
        c += i  # Adding each number to the sum 'c'.
    print(f"sum is {c}")  # Printing the final sum.


# Calling the 'add' function with multiple numbers as arguments.
add(4, 9, 0, 19, -3)
