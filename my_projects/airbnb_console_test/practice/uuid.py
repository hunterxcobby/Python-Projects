#!/usr/bin/python3

import uuid

class unique_id():

    def generate_id(self):
        my_uid = uuid.uuid4()
        uid_str = str(my_uid)
        return uid_str
    
user1 = unique_id()
id = user1.generate_id()
print(id)