#!/usr/bin/python3

"""
>>> print(list(range(20))) # doctest: +ELLIPSIS
[0, 1, 2,..., 18, 19]
"""


'''The +ELLIPSIS directive allows you to use ... to represent 
a sequence of elements, making it easier to handle long lists.'''
if __name__=='__main__':
    import doctest  
    doctest.testmod(verbose=True)
