# <------------------------------------Loops------------------------------------>

# While Loop------------------->
i = 0  # initialization

while i < 10:  # condition
    print(i)  #  loop body
    i = i + 1


# While Loop to print contents of Array------------------->
fruits = ["apple", "orange", "grapes", "strawberry"]

f = 0
while f < len(fruits):  # while f is lesser than length of array
    print(fruits[f])
    f = f + 1


# Infinite while loop------------------->

# while True:  # while the condition is true, do this
# print("This is an infinite while loop")


# For loop using fruit example from above------------------->
for fruit in fruits:
    print(fruit, ">> using for loop")


# For loop using range------------------->
for number in range(1, 11):  # range(start,end) --> end - 1
    print(number)
