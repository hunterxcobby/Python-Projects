#!/usr/bin/python3

import unittest #import the unittest module

# Define the function 'add' that takes two arguments and returns their sum
def add(x,y):
    return x + y

# Create a test class that inherits from unittest.TestCase
class TestAddFunction(unittest.TestCase):
    # Test case for adding positive numbers
    def test_add_positive_numbers(self):
        # Call the 'add' function with arguments 3 and 5
        result = add(3, 5)
        # Check if the result is equal to 8
        self.assertEqual(result, 8)
    
    # Test case for adding negative numbers
    def test_add_negative_numbers(self):
        # Call the 'add' function with arguments -2 and -4
        result = add(-2, -4)
        # Check if the result is equal to -6
        self.assertEqual(result, -6)

    # Test case for adding a number to zero
    def test_add_zero(self):
        # Call the 'add' function with arguments 10 and 0
        result = add(10, 0)
        # Check if the result is equal to 10
        self.assertEqual(result, 10)

    def test_add_positive_and_negative(self):
        result = add(-7, 3)
        self.assertEqual(result, -4)

# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()