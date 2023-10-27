#!/usr/bin/python3

def greet(name):
    """
    Greet a person.

    >>> greet('Alice')
    Hello, Alice!
    >>> greet('Bob')
    <BLANKLINE>
    >>> greet('Charlie')
    Hello, Charlie!
    """
    if name:
        print(f"Hello, {name}!")

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.DONT_ACCEPT_BLANKLINE)
