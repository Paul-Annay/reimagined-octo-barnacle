def square(x):
    return x * x

def add_40(x):
    return 40 + x


string_numbers = ["4", "5", "6", "7"]

numbers_ratul = list(map(int,string_numbers)) # Done

numbers_nafisa = list(map(int, string_numbers)) # Done

# for num in string_numbers:
#     numbers.append(int(num))

print(numbers_ratul)
print(numbers_nafisa)

squared_numbers = list(map(square, numbers_ratul))
forty_added_numbers = list(map(add_40, numbers_nafisa))

