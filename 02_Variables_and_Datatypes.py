# <------------------------------------Variables------------------------------------>
# Variables are containers to store a value

# name = "Amey" -> here name is a variable
# n = 6 -> here n is a variable


# <------------------------------------Datatypes------------------------------------>
# Datatypes refer to the type of variable

# There are primarily 5 datatypes used in Pyhon

# 1 -> String
name = "Amey"  # '' / "" / ''' can be used to write a string

# 2 -> Integers
integer = 69

# 3 -> Float
float = 3.14

# 4 -> Boolean
a = True
b = False

# 5 -> None
c = None

# Printing type of varibales
print(type(name))
print(type(integer))
print(type(float))
print(type(a))
print(type(c))


# <------------------------------------Typecasting------------------------------------>
# Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users


d = "420"  # here 420 is stored as a string
print("The type of d right now is ->", type(d))

d = int(
    d
)  # This will change the type of variable "if possible". It cannot change the type if the value was "Amey"
print("The type of d after typecasting is ->", type(d))
