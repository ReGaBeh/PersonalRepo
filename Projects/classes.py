def dunderExamples():
    class Employee:
        raise_amt = 1.04

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.email = first + "." + last + "@email.com"
            self.pay = pay

        def __repr__(self):
            return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

        def __str__(self):
            return '{} - {}'.format(self.fullname(), self.email)

        def __len__(self):
            return len(self.fullname())

        def fullname(self):
            return "{} {}".format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)

    emp1 = Employee("Test", "Employee", 50000)

    print(repr(emp1))
    print(str(emp1))
    print(len(emp1))


def decorators():
    class Employee:
        def __init__(self, first, last):
            self.first = first
            self.last = last

        @property
        def fullname(self):
            return "{} {}".format(self.first, self.last)

        @fullname.setter
        def fullname(self, name):
            first, last = name.split(" ")
            self.first = first
            self.last = last

        @fullname.deleter
        def fullname(self):
            print("Deleting name")
            self.first = None
            self.last = None

        @property
        def email(self):
            return "{}.{}@email.com".format(self.first, self.last)

    emp1 = Employee("Test", "Employee")

    print(emp1.email)
    emp1.fullname = "Rowan Miller"
    print(emp1.fullname)
    del emp1.fullname


decorators()
