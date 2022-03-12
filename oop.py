# Python Object-Oriented Programming
#=====================================================================================
# Data which is associated with a class is called an attribute.
#=====================================================================================
# Class variables: same for entire class
# Instance variables: can be same or different for different instances of a class
#=====================================================================================
# Methods are the functions defined within a class.

# __dict__ method tells about the methods and attributed available to a instance or class
# __init__ method runs everytime a new class object is created.

# Regular Methods: Automatically takes instance as the first argument.

# Class Methods: To make a class method we have to use the @classmethod decorator
# class methods can also be used as alternative contructors.

# Static Methods: methods which don't pass instance or class as first argument and behave like normal functions.
# A big giveaway wether a function is static is wether it accesses the instance or class anywhere within the method.
# static method can be created by @staticmethod decorator.
#=====================================================================================
# Class Inheritance: allows us to inherit methods and attributes from parent class.
#=====================================================================================
class Employee:

    raise_amount = 1.04      # Employee.raise_amount is a class variable
    num = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.raise_time = 0

        # num is increased each time an employee object is created.
        Employee.num += 1

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    # Property decorator allows us to access a method like an attribute.

    @property
    def email(self):
        return f"{self.first}.{self.last}@arius.com"

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first, self.last = None, None

    @property
    def apply_raise(self):
        # Self.raise_amount is an instance variable
        if self.raise_time == 0:
            self.pay = round(self.pay * self.raise_amount, 2)
            self.raise_time += 1

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    # Using class method as alternative contructor.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod  # Example of a staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    # we can make changes in our sub-class without worrying about breaking anything in the parent-class.
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Letting the super classes' __init__ method to handle these arguments.
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay), the above statement can also be done this way.
        self.prog_lang = prog_lang

    def __repr__(self):
        return f"Developer('{self.first}', '{self.last}', '{self.pay}', '{self.prog_lang}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def __repr__(self):  # If __str__ doesn't exist in a class, __repr__ method is shown when the instance name is typed without
        # any attribute or method.
        return f"Manager('{self.first}', '{self.last}', '{self.pay}', '{self.employees}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    @property
    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


emp_1 = Employee('Artius', 'Shade', 500000)
emp_2 = Employee('Test', 'User', 50000)

mgr_1 = Manager('Yakuv', 'Solkinsky', 90000, [emp_2])

# issubclass(class, superclass)
# isinstance(instance, class)
# __repr__ method is meant for developers to look at, so it must be detailed for things like debugging and logging.
# __str__ method is shown to the user so it should be more userfriendly

1 + 2
int.__add__(1, 2)
# Arithmethic dunder methods can be specified in classes to change how they behave with the arithmetic operators.
# >>>> https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
str.__add__('a', 'b')
emp_1 + mgr_1
len('test')
'test'.__len__()
len(emp_1)
#=========================================================================================
# @property is the property decorator. It allows us to access a method like an attribute.

# We can set an attribute made by property decorator by the @method.setter decorator.

# if we define a method.deleter, it gets run everytime we delete that attribute.
#=========================================================================================

emp_2 = 'John Carlos'
# Name of emp_2 can changed because we have used the @fullname.setter
# and defined a setter method for this attribute.
