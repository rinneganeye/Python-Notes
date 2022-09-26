# <--------------------------------------Conditions-------------------------------------->

# Comparison Operators: >, < , ==, !=, >=, <=
# Logical Operators: and / &&, or / ||, not / ~


# 1--> if-else condition --> simple example
from ast import If


a = 10

if a > 5:
    print("a is greater than 5")
else:
    print("a is less than 5")


# 2--> multiple if condition -->
b = 20

if a > 5:
    print("b is greater than 5")
if b > 10:
    print("b is greater than 10")
if b > 15:
    print("b is greater than 15")
else:
    print("b is lesser than 5,15 and 15")


# 3--> if-elif-else condition
age = 19

if age < 18:
    print("you cannot drive")
elif age > 50:
    print("too old to drive")
else:
    print("you can drive")

# NOTE:
# In if-else or multiple if-else conditions, each condition is executed atleast once.
# In if-elif-else conditions, only one condition is executed.

# 4--> is condition --> This condition directly refrences the condition
d = True
if d is True:
    print("d is True")
else:
    print("d is False")

# 5 --> in condition --> This condition returns a boolean value if satisfied
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in arr)
