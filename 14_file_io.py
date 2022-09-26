# <------------------------------------File I/O------------------------------------>

# File Types------------------>

# 1--> Text File ---> human readable format file
# 2--> Binary File ---> .jpg, .png etc.

# Parameters------------------>

# r --> read
# w --> write
# a --> append

# SYNTAX -->
# open('filename', 'parameter')

# <-------------------Reading a File------------------->

# file = open("sample.txt", "r") # by default it takes 'r' as argument so even if we dont pass 'r' it will work
# readData = file.read()
# print(readData)
# file.close() # very important --> closes file so other processes can work properly


# <-------------------Writing File------------------->

# file = open("sample.txt", "w")
# writeData = "This is a sample file using python"
# data = file.write(writeData) # if we run this code again and again, it will re-write the entire file
# file.close() # very important


# <-------------------Appending File------------------->

# file = open("sample.txt", "a") # this will add data to the next line
# appendData = "\nThis is an appended line"
# data = file.write(appendData)
# file.close() # very important


# <-------------------Operations using 'with'------------------->
# In this syntax, we do not need to close the file like shown above

# with open("sample.txt", "r") as file:
#     read = file.read()
#     print(read)
