#!/usr/bin/python3

"""
>>> print(list(range(20)))
[0, 1,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> print(list(range(20))) # doctest: +NORMALIZE_WHITESPACE
[0, 1,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

'''
So in this example, you will realize the fist test fails because it contains 
whitespaces and we did not add the directives to it'''

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

