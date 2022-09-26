# <------------------------------------Functions------------------------------------>
# Function are group of instructions to be executed.
# A function can have any number of arguments.

# Function Call -> A function cannot execute itself after defination. We need to invoke the function in order to use. It can be called multiple times.

# Function Body -> Set of instructions to be executed.

# SYNTAX:
# def functionName(arg1, arg2, arg3, ...arg_n):
# function body

# functionName() --> calling the function


# <------------------------------------Types of Functions------------------------------------>

# 1 -> Built-in Functions --> Pre-defined functions in Python --> range(), print()

# 2 -> User Defined Functions --> Defined by user


# <------------------------------------Printing Hello using Function------------------------------------>


def hello_world():
    print("Hello World")


hello_world()


# <------------------------------------Sum of 2 numbers using Function------------------------------------>


def sum(num1, num2):
    print(num1 + num2)


sum(25, 10)


# <------------------------------------Loop in Function------------------------------------>

userInput = int(input("User Input: "))


def printVals(num):
    for number in range(1, num + 1):
        print(number)


printVals(userInput)


# <------------------------------------Default Argument Function------------------------------------>
# If the argument is not passed into function then the function will return the default value we sepcified


def greet(name="Stranger"):
    print("Greetings " + name)


greet()  # Result -> Greetings Stranger
greet("Amey")  # Result -> Greetings Amey
