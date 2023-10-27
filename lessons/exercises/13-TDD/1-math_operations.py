#!/bin/python3

"""To use doctest to verify the example provided below, 
you'll need to follow these steps:
"""

"""Step 1
Add the Example Code:
Copy the example provided into the a python file(.py). 
Here's the code:
"""
def add(a, b):
    """
    This function adds two numbers together.

    Example:
    >>> add(2, 3)
    5

    >>> add(0, 0)
    0
    """
    return a + b

"""Step 2
Save the File:
Save the Python file
"""

"""Step 3
Run doctest from the Command Line:
Open your terminal or command prompt, and navigate to the directory
where you saved the Python file.
"""

"""Step 4
Run doctest:
In the terminal, run the following command:
"""
'''python3 -m doctest -v 1-math_operations.py'''

"""Here's what this command does:

python -m doctest tells Python to run the doctest module.
-v makes doctest print detailed output, showing which examples pass and which fail.
math_operations.py is the name of the file containing the doctests.
"""


