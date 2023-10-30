#!/usr/bin/python3

def my_function(a, b):
    """
    You can use reporting options like RPORT_NDIFF
    to show detailed differences.
    >>> my_function(2, 3) #doctest: +REPORT_NDIFF
    6 
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b

'''The first test fails because it interprets the extra space 
after 6 as part of the output.'''

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)