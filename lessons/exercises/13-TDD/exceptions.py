#!/usr/bin/python3

def divide(x, y):
    """
    This function divides two numbers.

    Example:
    >>> divide(10, 2)
    5.0

    >>> divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return x / y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)