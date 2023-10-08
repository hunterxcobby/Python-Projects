#!/usr/bin/python3

myList = ["Cobby", 21, 5.9]
names = ["marvel", "cobby", "ami", "ayomide"]
nums = [4, 7, 1, 34, 10, 8]

# adding 20 to the end of the list
nums.append(20)
print(nums)

# adding multiple elements or a list to the list
nums.extend([21, 30, 45])
print(nums)

# reverse the list
nums.reverse()
print(nums)

# insert an item before 5
nums.insert(4, 25)
print(nums)

# insert at an index that does not exist
nums.insert(25, 100)
print(nums)

# for more
# print(help(nums))