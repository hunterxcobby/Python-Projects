---

## Introduction

This is the source file name: [3-print_name.py](https://github.com/hunterxcobby/Python-Projects/blob/main/lessons/exercises/3-print_name.py)

These notes cover important concepts in Python programming, designed especially for beginners.

## Displaying Information

In Python, you can use the `print()` function to display information. It's a fundamental way to communicate with the user or to debug your code.

### Basic Print

```python
print("Hello, World!")
```

This simple line of code will display "Hello, World!" on your console.

### Printing Variables

Variables are used to store data in Python. You can display the value of a variable using the `print()` function.

```python
name = "John"
print("My name is", name)
```

In this example, the value of the variable `name` will be displayed along with the provided message.

## Variables

Variables are like containers that can hold different types of information.

### Variable Assignment

```python
first_name = "Cobby"
surname = "Sefah"
```

Here, we've created two variables: `first_name` and `surname`, and assigned them the values "Cobby" and "Sefah" respectively.

## Printing Multiple Things

You can print multiple values in one line using the `end` parameter. This parameter determines what character(s) are printed at the end.

```python
print(first_name, surname, end=" ")
print("comes from", end=" ")
print("Ghana", end=" ")
print("and stays in", end=" ")
print("Accra.", end="\n")
```

In this example, we first print `first_name` and `surname`, and set the `end` parameter to a space. Then we print additional information, controlling how it's displayed.

## Print with Separator

You can specify a separator when printing multiple values.

```python
print(first_name, surname, sep="")
```

By default, `print()` separates values with a space. Here, we've set the separator to an empty string, meaning the values will be concatenated.

## Important Note

Remember to use commas to separate values in the `print()` function. Positional arguments should come before keyword arguments.

```python
print(value1, value2, ..., sep=" ", end="\n")
```

These basics provide a solid foundation for your Python journey. Feel free to explore further and practice regularly to become more comfortable with the language.

---
