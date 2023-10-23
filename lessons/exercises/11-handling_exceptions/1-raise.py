#!/usr/bin/python3

'''In addition to handling exceptions that occur naturally
during program execution, you can also deliberately raise
exceptions using the raise statement.'''

try:
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise ValueError("Number must be positive")
except ValueError as ve:
     print(ve)
finally:
    print("Program executed successfully")