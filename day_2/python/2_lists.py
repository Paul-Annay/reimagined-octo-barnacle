national_list = [52, 21, 2, 71, 25, 3, 16, 12, 75, 15, 8]
shodesh = [10, 1]


# print(national_list.sort(reverse=True))
# print(national_list)
"""
append(value), insert(value, index), extend
clear
copy -> Shallow Copy , list[:]
count
index
remove(value), pop(index=len(list)-1)
reverse, list[::-1]
sort
"""



fruits = ["apples", "orange", "banana"]
new_fruits = fruits # deep copy

another_fruits = fruits.copy() # shallow copy
another_fruits.append("watermelon")


# Immutability (unchangeable) - mutation: change

