# <------------------------------------Strings------------------------------------>
# Strings are used to store a sentences.

# There are 3 ways to write strings.
sq = "This is a string"
db = "This is a double quoted string"
tq = """This is a triple quoted string"""  # we can use this to write a multi-quoted and multi line string

# <------------------------------------Most commonly used String Functions------------------------------------>

# Concatenating Strings------------------>
str1 = "Hello Amey, "
str2 = "Good Morning"

str3 = str1 + str2
print(str3)

# Accessing String Contents------------------>
# SYNTAX -> string[index]
# NOTE --> WE CAN ACCESS THE STRING CONTENTS BY INDEXES BUT CANNOT CHANGE THEM
# string[1] = J --> This wont work
# Indexes start from 0

sentence = "This is a sentence"
print(sentence[0])


# Finding length of a string------------------>
lenth = "We will find the length of this string"
print(len(lenth))  # white spaces included


# Slicing of Sting------------------>
# SYNTAX -> string[start:end]
# The result is always -> end - 1

slicingString = "We will slice this string"
print(slicingString[1:8])  # This will print from 1 to 7, the 8th index is not included
print(slicingString[:8])  # By default it will take 0 as the start index
print(slicingString[1:])  # By default it will take the last index of the string


# Capitalization of Sting------------------>
# This will only capitalized the first letter of the string

cap = "capitalize this string"
print(cap.capitalize())


# Uppercase and Lowercase------------------>
upper = "uppercase this string"
print(upper.upper())

lower = "LOWERCASE THIS STRING"
print(lower.lower())
