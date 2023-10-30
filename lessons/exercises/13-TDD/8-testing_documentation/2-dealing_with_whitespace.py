#!/usr/bin/python3

def my_function(a, b):
    """Returns a * b.

    >>> my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']

    This does not match because of the extra space after the [ in
    the list.

    >>> my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B',
      'A', 'B', ]
    """
    return a * b

'''When NORMALIZE_WHITESPACE is turned on, 
any whitespace in the actual and expected values is considered a match. 
Whitespace cannot be added to the expected value where none exists
in the output, but the length of the whitespace sequence
and actual whitespace characters do not need to match. 
The first test example gets this rule correct, and passes, 
even though there are extra spaces and newlines. 
The second has extra whitespace after [ and before ], so it fails.'''

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)