#!/usr/bin/python3

import uuid

my_uuid = uuid.uuid1()

your_uuid = uuid.uuid4()

print(my_uuid)
print(your_uuid)


"""
uuid1(): This method generates a UUID based on the current timestamp and
the machine's hardware address. 
It may compromise uniqueness if multiple UUIDs are generated within
the same 100-nanosecond interval."""

"""
uuid4(): This method generates a UUID based on random numbers.
While not guaranteed to be unique, the probability of collision is extremely low
"""

"""
After generating a UUID, you can convert it to a string for practical use:
"""