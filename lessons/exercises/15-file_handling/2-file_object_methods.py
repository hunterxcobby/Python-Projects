#!/bin/python3

"""Imagine you have a book, and you want to read it using a special magic 
bookmark. This bookmark can either read the entire book, 
or it can read just a certain number of pages at a time."""

'''f.read(): 
This command tells the magic bookmark to read the entire book. 
In computer terms, if we're reading a text file, 
    it will read the whole file and give it to us as one big piece of text. 
    If it's a picture or something, it gives us the whole thing in one go.
For example:'''

with open('2-book.txt', 'r') as f:
    content = f.read()
    print(content)


'''f.read(size): 
Here, we're telling the bookmark to read a specific number of pages at a time.
So, if we tell it to read 10 pages at a time, it'll give us just that, 
and we might need to ask for more if we want to read the whole book.
For example:'''

with open('2-book.txt', 'r') as f:
    content_part1 = f.read(10)  # Read the first 10 pages
    print(content_part1)
    content_part2 = f.read(10)  # Read the next 10 pages
    print(content_part2)



'''f.readline():
This is like asking the bookmark to read one line at a time. 
It's like if you're reading a story and you read one sentence at a time. 
Each time you call this command, it gives you one line of the book.
For example:'''

with open('2-book.txt', 'r') as f:
    line1 = f.readline()  # Read the first sentence
    print(line1)
    line2 = f.readline()  # Read the second sentence
    print(line2)

