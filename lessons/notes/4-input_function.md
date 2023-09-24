# Introduction to Inputs in Python

In this lesson, you learned about taking user inputs in Python. The following code demonstrates how to prompt the user for their name and then prints a greeting:

## Lesson Overview

- This lesson covers the concept of taking user inputs in Python.
- It demonstrates how to prompt the user for information and use it in your program.

```python
#!/usr/bin/python3

print ("Hello" + " "+ input("What is your name?"))
```

## Explanation
- The line that contains `input("What is your name?")` is replaced by the input the user gives
- `print ("Hello" + " "+ input("What is your name?"))`:
   - This line of code combines the string "Hello" with the result of the `input` function, which prompts the user with the question "What is your name?". The user's input is then concatenated with the string "Hello" and printed.

## How to Use

1. Save the code in a Python file (e.g., [4-input_function.py](https://github.com/hunterxcobby/Python-Projects/blob/main/lessons/exercises/4-input_function.py).
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the Python script using the command `4-input_function.py`.
5. The program will prompt you to enter your name. After entering your name and pressing Enter, it will print a personalized greeting.

Feel free to modify and experiment with this code to further explore user inputs in Python!
