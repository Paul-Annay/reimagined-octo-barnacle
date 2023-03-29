# objects = [
#     "Batman", 
#     {"name" : "Bruce Wayne", "city": "Gotham"},
#     [95,6.2],
#     ("Caped Crussader", "Dark Knight", "Vengeance"),
#     range(2008, 2023)
# ]

# for i in objects:
#     print(str(i))
#     #print(i, type(i))

# ## Task 2
# create a function called my_input()
# - it takes input and prints it
# - 2 arguments: prompt, class_type
# - by default class_type = None
# - if value returned by input() is all numbers -> assign class_type = int
# - return class_type

def my_input(prompt, class_type=None):
    var = input(prompt)
    print(var)
    if var.isdecimal():
        class_type = int
    return class_type
    
print(my_input("Enter a value: "))
    



# def my_input(prompt, class_type=None):
#   var = input(prompt)
#   var








