#!/usr/bin/python3

"""
>>> print(list(range(20))) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0,    1,  2,..., 18, 19]
"""


'''Here, we're combining two directives: +ELLIPSIS and +NORMALIZE_WHITESPACE.
This means we can use ellipsis (...) to represent a sequence, 
and extra spaces will be ignored.'''
if __name__=='__main__':
    import doctest  
    doctest.testmod(verbose=True)
