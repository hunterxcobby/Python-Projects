#!/usr/bin/python3

def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error

    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')

'''the entire body of the traceback is ignored and can be omitted.'''

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)