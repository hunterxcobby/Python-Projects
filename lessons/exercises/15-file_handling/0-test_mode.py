#!/usr/bin/python3

# Writing in text mode
with open('test.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")

# Reading in text mode
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)
