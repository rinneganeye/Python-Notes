# <------------------------------------Multiple Inheritance------------------------------------>

# Parent 1 Class------------------->
class Student:
    name = "Amey Shinde"
    age = 21

    def getInfo(self):
        print(f"\nThe name of the student is {self.name} and the age is {self.age}.")


# Parent 2 Class------------------->
class Employee(Student):  # inherited Student
    age = 30
    company = "Bajaj"

    def getGrownUpInfo(self):
        print(
            f"The name of the employee is {self.name}, the age is {self.age} and the company is {self.company}."
        )

    def moreInfo(self):
        print(f"{self.name} is a programmer at {self.company}.")


# Child Class-------------------> NOTE : The first inheritance will have first priority
class Boss(Employee, Student):  # inherited Employee and Student.
    company = "Yallah Habibi"

    def getCurrentInfo(self):
        print(
            f"The name of the Boss is {self.name}, age {self.age} and has his own company named {self.company}"
        )


s = Student()
s.getInfo()

print("------------------------------------")

e = Employee()
e.getGrownUpInfo()
e.moreInfo()

print("------------------------------------")

b = Boss()
print(b.company)
b.getCurrentInfo()
b.getInfo()  # since getInfo() exists in Student class, the info will be retrived form Student() but the age will be overwritten since the print statement has {self.age} in both classes.
