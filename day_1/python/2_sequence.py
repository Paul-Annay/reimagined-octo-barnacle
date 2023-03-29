# Strings
single = 'This is a single quote string'
double = "This is a double quote string"
triple = """This is a triple quote string""" # -> multiline string, doc string

# Lists
# Creating Empty Lists: 2 ways
empty_list_1 = []
empty_list_2 = list()

# Creating Lists with Values: 2 ways
list_1 = [10, 20, 30, 40]
list_2 = list([10, 20, 30, 40])

# Accessing Element from a List
list_1[3]       # 40
list_2[1]       # 20

# Changing List Items
list_1[3] = -44  # Before: [10, 20, 30, 40] After:  [10, 20, 30, -44]


# Tuples
# Creating Empty Tuple: 2 ways
empty_tuple_1 = ()
empty_tuple_2 = tuple()

# Creating Tuple with Values: 2 ways
tuple_1 = (10, 11, 12, 13)
tuple_2 = tuple((10, 11, 12, 13))

# Accessing Element from a Tuple
tuple_1[0]  # 10
tuple_2[3]  # 13


"""
Tuples allow us to PACK and UNPACK multiple items
"""
# Packing:
packed_values = ("John Smith", 32, "john@gmail.com")
# Unpacking:
name, age, email = packed_values

name    # "John Smith"
age     # 34
email   # "john@gmail.com"


