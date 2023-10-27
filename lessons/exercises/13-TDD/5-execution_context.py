#!/usr/bin/python3


def add(x, y):
    """This is a function that adds two numbers.

    Example:
    >>> add(x, y)
    30

    """
    return x + y

if __name__ == '__main__':
    import doctest
    custom_dict = {'x': 10, 'y': 20}
    doctest.testmod(globs=custom_dict)

