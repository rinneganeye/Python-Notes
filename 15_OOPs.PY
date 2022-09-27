# <------------------------------------Object Oriented Programming in Python------------------------------------>
# The main motive of using OOPs is increasing the reuseability of the code following the DRY principle.


# <-------------Class------------->
# Class is a blueprint for creating objects. Its like a template.

# SYNATX:-
# class Student:
# method and variables


# <-------------Object------------->
# Object is an instantiation of class.

# amey = Student() --> This is how we create an instance.
# Whatever methods are available in class are now useable with amey.


# <-------------Modelling------------->

# Noun ----> Class ----> Student
# Adjective ----> Attributes ----> name, age, division
# Verbs ----> Methods ----> getScore(), getGrade()


# <------------Combining everything together------------>


class Student:  # Creating a class
    college = "University of Mumbai"  # This is sepcific to each class


amey = Student()  # This is how we create an instance

print(amey.college)
# Since amey = Student(), it will print the name of the college i.e. University of Mumbai


# <-------------Instance Attributes------------->
# An attribute that belongs to the instance. Taking above example:

amey.name = "Amey"
amey.age = "21"  # This is the adding instance attributes

# NOTE: instrance attribute take presence over class
# Example:-

print(amey.age)
# This will print the assigned age
# But if it was not defined as [amey.age = "21"], it will go back to the Student class to check if something exists like 'age', just like 'college'.
# If it finds something like 'age' in Student class, it will print the value assiocated with it else it will throw error.


# <-------------'self' Parameter------------->
# self refers to the instance of the class. It is automatically passed to the function in class.

# amey.getScore() ----> here 'self' refers to the amey ----> equivalent to:- Student.getScore(amey)

# class Student:
#     def getScore(self):     # we can pass argument to the function
#         print("The score is 420")


# <-------------Static Method------------->
# Sometimes we dont want to use self parameter for a simple function. Static method is used in such cases.
# This works only inside the class.


# @staticmethod       # This is a decorator to mark greet as a static method
# def greet():
#     print("Hello World!")


# <-------------'__init__' Constructor------------->
# This is a special constructor. It runs as soon as the object is created. It takes self and other arguments.

# Example:-


class Employee:
    def __init__(self, name):
        print("This is init constructor")
        self.name = name

    def getSalary(self):
        pass


isha = Employee("Isha")  # we just created an instance of the Employee class.
# If we run this program, it will print 'This is init constructor' even if we do nothing.
