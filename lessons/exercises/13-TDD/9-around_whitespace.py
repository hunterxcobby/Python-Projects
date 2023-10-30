#!/usr/bin/python3

def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.

    Line two.

    """
    for l in lines:
        print(l)
        print()

'''The test fails because it interprets the blank line 
after the line containing "Line one." 
in the docstring as the end of the sample output. 
To match the blank lines, 
replace them in the sample input with the string <BLANKLINE>.'''


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)