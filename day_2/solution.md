## Task 1
message = "Strive not to be a success, but rather to be of value."
print(message[message.index(message.find("success")) : message.index(message.find("success")) + len("success") ])


## Task 2
`
foods = "Bread Cereal Butter Garlic Cream Mint Milk"
foods_list = foods.split()
print(foods_list[foods_list.index("Butter")].upper())
print(foods_list[foods_list.index("Garlic")].upper())
print(foods_list[foods_list.index("Milk")].upper())
`