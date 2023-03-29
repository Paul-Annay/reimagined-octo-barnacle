menuItems = [
  { "food": "Blue Cheese Salad", "price": 8 },
  { "food": "Spicy Chicken Rigatoni", "price": 18 },
  { "food": "Ponzu Glazed Salmon", "price": 23 },
  { "food": "Philly Cheese Steak", "price": 13 },
  { "food": "Baked Italian Chicken Sub", "price": 12 },
  { "food": "Pan Seared Ribeye", "price": 31 }
]

 # 1)
`for menuItem in menuItems:
    print(menuItem.items())
`


 # 2)

`for menuItem in menuItems:
    if menuItem["price"] < 15:
        menuItem["isAffordable"] = True
        # or, 
        # menuItem.update({"isAffordable":True})
`
