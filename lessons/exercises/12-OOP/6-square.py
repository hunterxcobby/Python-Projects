#!/usr/bin/python3

# AUTHOR - Ami Manye

'''A Square class'''


class Square:
    '''Represents a Square'''

    '''constructor for square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        '''getter function for size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''setter function for size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # verify that is a tuple of 2 positive integers
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Update the private instance attribute


    def area(self):
        '''returns the area of the square'''
        res = self.__size ** 2
        return res

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)