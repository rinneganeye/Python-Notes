# <------------------------------------Lists------------------------------------>
# Lists are containers for any data type.

# Example:
list = [1, 2, 4, 45, 5, 48, 96]
list2 = [1, "Amey", True, 6.9, 420]

# <------------------------------------Accessing the elemets------------------------------------>
# SYNTAX -> list[index]
# Eg: print(list[4])

# We can replace elements of the list using index
list[0] = 69  # changes element at index 0 to 69

# <------------------------------------Most commonly used List Functions------------------------------------>

list.sort()  # Sorts the list

list.reverse()  # Reverses the list

list.pop()  # Removes the last element from the list

list.append(420)  # Adds element to the end of list

list.remove(1)  # Removes the first occurance of the element from the list

print(list[0:5])  # Slices the list --------> SYNTAX -> list[start index: end index]
print(list[5:])  # By default, it will take the last index of the list as the end
print(list[:5])  # By default, it will take 0 as the start
