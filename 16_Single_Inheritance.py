# <------------------------------------Inheritance------------------------------------>
# Inheritance is way of creating new class from existing class.
# Just like parent to child.


# <------------------------------------Types of Inheritance------------------------------------>

# Single Inheritance ----> child class inherits only from 1 parent class.
# Multiple Inheritance ----> child class inherits from more than 1 parent classes.
# Multilevel Inheritance ----> child class becomes parent for another child class.


# <------------------------------------Single Inheritance------------------------------------>

# Parent Class ------------------->
class Student:
    name = "Amey"
    age = 21

    def getInfo(self):
        print(f"The name of the Student is {self.name} and the age is {self.age}.")


# Child Class ------------------->
class Employee(Student):  # here we have inherited the parent class
    age = 28  # here we can overwrite the parent class property

    def getInfo(self):
        # in Employee class, we do not have 'name' but still it will print "Amey" because of inheritance
        print(f"The name of the Employee is {self.name} and the age is {self.age}.")


s = Student()
print(s.name)
print(s.age)
s.getInfo()  # this will print information associated with the student class

print("------------------------------------------")

e = Employee()
print(e.age)
e.getInfo()  # this will print information associated with the employee class
