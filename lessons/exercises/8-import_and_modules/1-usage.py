#!/usr/bin/python3

import mymodules as mx

a = mx.person1["country"]
print(a)

# Import only the person1 dictionary from the module:
from mymodules import person1
print(person1["age"])