#!/usr/bin/python3

"""
>>> print(list(range(5)) + list(range(10, 20)) + list(range(30, 40)))
... # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0, ...,    4, 10, ..., 19, 30, ..., 39]
"""


'''Here, we're combining two directives: +ELLIPSIS and +NORMALIZE_WHITESPACE.
This means we can use ellipsis (...) to represent a sequence, 
and extra spaces will be ignored.'''
if __name__=='__main__':
    import doctest  
    doctest.testmod(verbose=True)
