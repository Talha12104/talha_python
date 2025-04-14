fruits= ["Apple","Banana","Orange"]

person = {
    "name" : "Talha",
    "age" : 20,
    "city" : "Karachi",
}
print(fruits)
print(person)

from typing import Union
types = Union[int, float, str]
lst : list[types] = [1,2,"4",4.5,5]
set1 : set = set
print(set1)

# Built-In Module
import random
# print(random.randint(1,10))

# User-Defined Module which User make it and used it efficiently.
import add
print(add.add(4,6))

# Third-Party Module
#Request Module
import pprint
import requests as req
response = req.get("https://www.asharib.xyz/api/profile")
pprint.pprint(req)

# Virtual Enivornment is a area which hold your requirement and specific
# Version of Modules which will be use in your projects.