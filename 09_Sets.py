# <------------------------------------Sets------------------------------------>
# A set is a collection of items which are unordered, unindexed and unique.
# A set can have strings, integers and boolean values

set = {1, 5, 3, 58, 87}
print(set)

# There can be no 2 or more same value
set2 = {1, 1, 2, 3, 5, 2}  # wont print 1 twice
print(set2)  # OUTPUT : {1, 2, 3, 5}


# <------------------------------------Set Methods------------------------------------>

set.add(69)  # add a new item to the set

set.update(set2)  # this will join set2 to the end of the set

set.remove(5)  # remove a new item from the set

set.union(set2)  # union of 2 sets

intersection = set.intersection(set)  # intersection between set and set2

set.clear()  # clear the set

set.pop()  # remove random item from set

print(set)
