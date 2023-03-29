def greeting(age, name="guest", height=4):  # Frank
    print("Efti")
    return f"Hello, {name} you age is {age}!"


# f1 = my_func        # Adress 
# f2 = my_func()      # None

print(greeting("John"))     # Hello, John!
print(greeting(30, "Frank"))    # Hello, Frank!
print(greeting(5000, "Bilkis"))   # Hello, Bills!
print(greeting(4))           # Hello, guest!

# Args, Kwargs
# Higher Order Function
# Lambda expressions
# Scoping
# Closure


# ## Task 2
# create a function called my_input()
# - it takes input and prints it
# - 2 arguments: prompt, class_type
# - by default class_type = None
# - if value returned by input() is all numbers -> assign class_type = int
# - return class_type
