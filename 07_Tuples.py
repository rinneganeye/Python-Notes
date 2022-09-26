# <------------------------------------Tuples------------------------------------>

# Tuples are are used to store multiple item in a single variable. Tuples are immutable i.e they cannot be changed.

tuple = (
    1,
    2,
    3,
    4,
    4,
    4,
    5,
    6,
    82,
    77,
    7,
)
print(tuple)

# <------------------------------------Tupple Methods------------------------------------>

print(tuple.count(4))  # This will print the occurance of item in a tuple

print(tuple.index(5))  # This will print the index of the item in a tuple

print(tuple[8])  # Printting tuple itme with index

# NOTE: WE CAN ACCESS THE TUPLE ITEM BUT CANNOT MODIFY IT
# tuple[1] = 69 # This will throw an error
