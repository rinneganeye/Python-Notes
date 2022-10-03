# Class method is bound to the class and not the object of the class.


class Employee:
    company = "Fiat"
    salary = "100"

    # ALTERNATE METHOD WITHOUT USING "self"
    # def changeSalary(self, newSalary):
    # self.salary = newSalary

    @classmethod  # decorator - use 'cls' instead of 'self'
    def changeSalary(cls, newSalary):
        cls.salary = newSalary


e = Employee()

print(e.salary)
e.changeSalary(500)
print(e.salary)
