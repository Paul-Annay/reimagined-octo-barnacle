my_string = "The Last of Us s2"
my_list = [97, 13, 19, 61]
my_tuple = (52, 33, 51, -8)
my_dictionary = {
    "value" : 100,
    "distance" : 45
}


# isiterable 

# Iterable : list, tuple, str, dict, range()
# Non-iterable: int, float, complex
# Rule 1: Non iterable -> Iterable X | Exception: **str
# Rule 2: Iterable -> Non iterable X | Exception : **
# Rule 3: Je kono iterale -> Je kono onno iterable

print(list({"Name" : None, "Age" : None}))