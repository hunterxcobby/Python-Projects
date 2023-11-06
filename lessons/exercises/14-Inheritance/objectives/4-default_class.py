#!/usr/bin/python3

class SimpleRobot:  # It's actually inheriting from 'object', but you don't have to write it explicitly.
    pass

"""The `object` class provides some default behaviors to all classes in Python. Here are a few of them:

1. **`__str__` and `__repr__` methods:**
   - These methods define how an instance of the class should be represented as a string when you print it or use it in a string context.

2. **`__eq__` method:**
   - This method defines how two instances of the class should be compared for equality.

3. **`__hash__` method:**
   - This method provides a unique hash value for instances of the class. It's used in data structures like dictionaries and sets.

4. **`__init__` method:**
   - While you have to explicitly define `__init__` in your classes, the default behavior of `object.__init__` is to do nothing.

5. **`__del__` method:**
   - This method is called when an instance is about to be destroyed. The default behavior of `object.__del__` is to do nothing.

6. **`__class__` attribute:**
   - This attribute refers to the class of an instance. In the case of `object`, `__class__` is set to `object` itself.

Remember, these default behaviors can be overridden or extended in your own classes to provide customized functionality."""