#!/usr/bin/python3

def greeting():
    """
    Generate a greeting.

    >>> greeting()
    'Hello, World!'

    >>> greeting()
    '   Hello,   World!  '
    """
    return 'Hello, World!'

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

"""In this example, the greeting function returns a greeting message.
The second test has extra spaces in the expected output. 
With NORMALIZE_WHITESPACE, the flag treats all sequences of whitespace as equal,
so both tests will pass."""
