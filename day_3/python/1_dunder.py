num1 = 10
num2 = 32

"""
Magic / Dunder
"""

num1 + num2 == num1.__add__(num2)
num1 - num2 == num1.__sub__(num2)
num1 / num2 == num1.__truediv__(num2)
num1 // num2 == num1.__floordiv__(num2)
num1 * num2 == num1.__mul__(num2)


names = ["John", "James", "Anna"]

# built in functions
# methods list.count, string.upper
# operators +, -, [], in
# Prohibited for programmers to use dunder methods directly


len("Sumaiya Azad Katha") == "Sumaiya Azad Katha".__len__()
dir(12) != int.__dir__(12)


# print(len(num))         # TypeError: object of type 'int' has no len()
# print(num.__len__())    # AttributeError: 'int' object has no attribute '__len__'


