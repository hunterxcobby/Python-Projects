#!/usr/bin/python3

fname = input("Firstname: ")
surname = input("Surname: ")
age = int(input("Age: "))

# Display details
# Using old style formatting
details = "Your name is %s %s and you are %d years old" %(fname, surname,age)
print(details)

print
# Using the new style formatting (str.format{})
details = "Your name is {} {} and you are {} years old".format(fname, surname,age)
print(details)