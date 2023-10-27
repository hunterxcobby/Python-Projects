#!/usr/bin/python3

def is_even(n):
    """
    Check if a number is even.
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return n % 2 == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True,optionflags=doctest.DONT_ACCEPT_TRUE_FOR_1)

"""In this example, we have a function is_even that checks if a number is even. 
The doctests show that is_even(2) should return True, 
and is_even(3) should return False. With DONT_ACCEPT_TRUE_FOR_1, 
the flag disables the automatic conversion of 1 to True,
so is_even(2) will be tested as expected."""