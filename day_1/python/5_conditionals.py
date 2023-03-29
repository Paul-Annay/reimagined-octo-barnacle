condition = (10 == 10)
condition2 = (4 > 3)
condition3 = (4 == 5)

if condition or condition3:
    print('Statement 1')
elif condition2:
    print('Statement 2')
else:
    print('Statement 3')


# Preview for Future Classes:

# short circuiting
print(4 or 0/0)

# ternary operator
result = "Yes" if 0 > 1 else "No"
print(result)