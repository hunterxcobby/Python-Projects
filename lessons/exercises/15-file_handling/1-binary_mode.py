#!/usr/bin/python3

# Writing in binary mode
with open('test.jpg', 'wb') as file:
    file.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR')

# Reading in binary mode
with open('test.jpg', 'rb') as file:
    content = file.read()
    print(content)
