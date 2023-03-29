# key value pair
person = {
    "name" : "Annay",
    "age" : 25,
    "male" : True,
    "height" : 5.5,
}

# print(person["you"])
# print(person.get("height", True))
person["name"] = "Sourav"
# print(person)

# person["name" : "height"]


"""
clear
copy
fromkeys*
get(key, default)
items, keys, values
pop
popitem*
setdefault(key, default)
update
"""

person2 = person.copy() # Shallow Copy

for i in person2.items():
    print(i)