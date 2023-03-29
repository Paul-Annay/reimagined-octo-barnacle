# Examples
bool(0)                      # False
bool("0")                    # True
bool(None)                   # False
bool("")                     # False
bool("False")                # True
bool(0.000000000000000001)   # True
bool(1 / 3)                  # True
bool(1 // 3)                 # False


# Integer Conversion

print(int(True))       # 1
print(int(False))      # 0
print(int(0.1441))     # 0
print(int(-42.761))    # -42
# int(64 - 3j)    # *ERROR*
print(int("67"))       # 67
print(int("  431  "))  # 431
print(int(" -33  "))   # -33

# Floating Conversion (Rules are similar to Integer Conversion)
print(float(True))         # 1.0
print(float(False))        # 0.0
print(float(12))           # 12.0
print(float(-42))          # -42.0
# float(64 - 3j)      # *ERROR*
print(float("67"))         # 67.0
print(float("  4.31  "))   # 4.31
print(float(" -3.3  "))    # -3.3


# String Conversion
"""
String Conversion does not give errors, and works for almost everything!
"""
print(str(132))
print(str(-887.1))
print(str(7j))
print(str(-1.5j))
print(str(True))
print(str(False))

