#!/usr/bin/python3

def divide(x, y):
    """
    This function divides two numbers.

    Example:
    >>> divide(10, 2)
    5.0

    >>> divide(10, 0)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "exceptions.py", line 6, in divide
            return x / y
        ZeroDivisionError: division by zero
    """
    return x / y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)