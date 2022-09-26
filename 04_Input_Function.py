# The input function asks the users about the input and always stores it in a type of a String.

name = input("Enter your name: ")
print("The type of name is ", type(name))

# If the input was 34, it would be stored as "34"

# We can strict the input by specifying the type
number = int(input("Enter a Number: "))
print("The type of number is ", type(number))
