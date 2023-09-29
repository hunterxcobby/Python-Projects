
## Introduction

CHeckout the source file: [4-input.py](https://github.com/hunterxcobby/Python-Projects/blob/main/lessons/exercises/4-input.py) 

These notes cover important concepts in Python programming, designed especially for beginners.

## Taking User Input

In Python, you can interact with the user by taking input from them. This is done using the `input()` function.

### Getting User Input

```python
first_name = input("First Name: ")
surname = input("Surname: ")
```

In this example, `input()` is used to prompt the user for their first name and surname. The entered values are then stored in the variables `first_name` and `surname`.

## Displaying Information

Displaying information is crucial for communicating with users or debugging your code.

### Basic Print

```python
print("Hello, World!")
```

This simple line of code will display "Hello, World!" on your console.

### Printing Variables

```python
name = "John"
print("My name is", name)
```

In this example, the value of the variable `name` will be displayed along with the provided message.

## Printing Full Name

You can combine variables and text using the `print()` function.

```python
print("Your full name is", end=" ")
print(first_name, surname)
```

In this code snippet, the user's full name is displayed using the values stored in the `first_name` and `surname` variables. The `end` parameter is used to control the characters printed at the end.

## Important Note

Remember to use commas to separate values in the `print()` function. Positional arguments should come before keyword arguments.

```python
print(value1, value2, ..., sep=" ", end="\n")
```

These basics provide a solid foundation for your Python journey. Feel free to explore further and practice regularly to become more comfortable with the language.

---
