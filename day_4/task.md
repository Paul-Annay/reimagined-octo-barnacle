## Task 1
objects = [
    "Batman", 
    {"name" : "Bruce Wayne", "city": "Gotham"},
    [95,6.2],
    ("Caped Crussader", "Dark Knight", "Vengeance"),
    range(2008, 2023)
]
    - 1) Iterate over the items and print them with their type 
        - `print(item, type(item))`
    - 2) Iterate over the items and convert each item to str


## Task 2
create a function called my_input()
- it takes input and prints it
- 2 arguments: prompt, class_type
- by default class_type = None
- if value returned by input() is all numbers -> assign class_type = int
- return class_type