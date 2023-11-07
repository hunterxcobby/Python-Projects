#!/usr/bin/python3

'''Looping Over a File: 
If you want to read a file line by line, you can use a loop. 
This is efficient and easy to do. 
For example, if the file contains a list of names, 
this loop would print each name one after the other:'''

with open('3-names.txt', 'r') as f:
    for line in f:
        print(line, end='') # terminate the newline character



'''Reading all lines into a List: 
If you want to read all the lines of a file and store them in a list, 
you can use either list(f) or f.readlines(). 
It's like making a list of all the names from the file.'''

with open('3-names.txt', 'r') as f:
    names_list = list(f)
    print(names_list)

# to strip off newline, uncomment this
# with open('3-names.txt', 'r') as f:
#     names_list = [name.strip() for name in f]
#     print(names_list)



'''Converting Objects Before Writing: 
If you want to write something other than a string 
(like a number or a tuple), you have to convert it to a string first'''

value = ('the answer', 42)
s = str(value)  # Convert the tuple to a string
with open('3-test.txt', 'w') as f:
    f.write(s)



'''f.tell() and f.seek(): 
These are like using bookmarks in a book.
f.tell() tells you where you are in the file (like "I'm on page 50"). 
f.seek(offset, whence) allows you to jump to a specific place in the file. 
For example, f.seek(5) would jump to the 6th character in the file.'''

with open('test.txt', 'rb+') as f:
    f.write(b'0123456789abcdef')
    f.seek(5)  # Go to the 6th byte in the file
    print(f.read(1))  # This will print b'5'
