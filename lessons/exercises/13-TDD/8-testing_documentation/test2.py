#!/usr/bin/python3

def f(x):
    f.counter = getattr(f, "counter", 0) + 1 
    return "Monty Python"
for i in range(10):
    f(i)
print(f.counter)


"""This demonstrates how you can use function attributes 
to create a counter. 
It counts the number of times the function f is called."""