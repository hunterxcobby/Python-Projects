#!/usr/bin/python3

"""             <===POSITIONAL AND KEYWORD ARGUMENT===>                   """

'''Positional Arguments:
Imagine you're ordering a pizza. 
When you tell the pizza place what kind of pizza you want, 
you say things like "I want a large pepperoni pizza with extra cheese."
Here, you're giving specific instructions in a particular order. 
In programming, this is similar to using positional arguments.'''

def make_pizza(size, topping, extra_cheese):
    print(f"You ordered a {size} pizza with {topping} and {'extra cheese' if extra_cheese else 'no extra cheese'}.")

# Calling the function with positional arguments
make_pizza("large", "pepperoni", True)


'''Keyword Arguments:
Now, imagine ordering a pizza differently. 
Instead of saying "I want a large pepperoni pizza with extra cheese," 
you say "I want a pizza with extra cheese, and make it pepperoni and large." 
Here, you're explicitly specifying what you want by using keywords. 
In programming, this is similar to using keyword arguments.'''

def make_pizza(size="medium", topping="cheese", extra_cheese=False):
    print(f"You ordered a {size} pizza with {topping} and {'extra cheese' if extra_cheese else 'no extra cheese'}.")

# Calling the function with keyword arguments
make_pizza(size="large", extra_cheese=True, topping="pepperoni")

