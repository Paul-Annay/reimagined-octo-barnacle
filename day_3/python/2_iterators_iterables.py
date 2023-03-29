from collections import Iterable, Iterator
# list(True) # -> Expect Iterable: str, list, tuple, range()
# next("Tru") # -> Expect Iterator: different

"""
Iterate - Assume Meaning Known (Repeat)
Iter-able: An object that can be iterated : __iter__
Iter-ator: An object that iterates : __iter__ + __next__

Iterable -> Iterator
"""

numbers = [3, 54, -2, 1, 8] # Iterable 
numbers_iterator = iter(numbers) # Iterator

print(hasattr(list, "__iter__"))
print(hasattr(numbers_iterator, "__next__"))


print(type(3))

print("is iterable: ",isinstance(True, Iterable))
print("is iterator: ",isinstance("Nafisa", Iterator))
# i = 3
# while i in numbers:
#     print(i)
#     try:
#         i = next(numbers_iterator)
#     except:
#         break


# for i in numbers:
#     print(f"Number is : {i}")



# loosely assigned
# strict : "Nafisa" -> String
# loose: "Nafisa" -> Iterable, Sequence
# print(isinstance(range(4), Iterable)) # True
# print(isinstance(range(4), Iterator)) # False

# student_ids = [97, 61, 13, 19]

# for i in student_ids:
#     print(i)


# print("-------------")

# student_ids_iterator = iter(student_ids)
# j = next(student_ids_iterator)
# while j in student_ids:
#     print(j)
#     try:
#         j = next(student_ids_iterator)
#     except:
#         break