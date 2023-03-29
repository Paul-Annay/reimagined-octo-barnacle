single = 'This is single quote string'
double = "This is double quote string"
triple = """This is triple quote string"""
fmt = f'Example format string'

# Indexing
single[8]       # s
single[-18]     # s


# Indexing
single[5]
single[-len(single)]

# Slicing

# string[start=0:end(+1)=len(string):step]
single[::-1]
single = 'This is single quote string'
#         012345678
single[-19:-13]


"""
CASE: capitalize, upper, lower, swapcase
JUSTIFY: center, ljust, rjust -> X
UTILITY: count, [find, rfind], [index, rindex], join, replace, [removeprefix, removesuffix], zfill
FORMATTING: format
CHECKING: isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper ->HW
TO_LIST: split, rsplit
CHECKING: startswith, endswith
SPACE_REMOVER: strip, rstrip, lstrip
"""

dummy = "Prefix-dummy-dummy Suffix"
cgpa = ".....881..."
splitted_string = dummy.split("-") #['Prefix', 'dummy dummy', 'Suffix']
# print(" ".join(splitted_string))

cgpa.strip(".")
cgpa.lstrip(".")
cgpa.rstrip(".")


# .format ->

var1 = 34
var2 = 3.7
"my age is {age} and my cg is {cg}".format(age=var1, cg=var2)

# f''
f"my age is {var1} and my cg is {var2}" # python 3.7
