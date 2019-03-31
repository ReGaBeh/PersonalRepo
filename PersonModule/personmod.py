class Person:
    is_alive = True
    is_employed = ()

    def __init__(self, name, age, gender):
        self. name = name
        self.age = age
        self.gender = gender

    def status(self):
        print(self.name, " is ", self.is_alive)

    def kill(self):
        self.is_alive = False
        print(self.name, "has died.")

    def all_data(self):
        for key, value in vars(self).items():
            print(f"{key}: {value}")


class Child(Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, gender)
        self.title = "Child"

    def graduate(self):
        if self.age < 18:
            print(self.name, "must be 18 to graduate")
            print(self.name, "is", self.age, "and has", 18 - self.age, "years until graduation")

        elif self.age >= 18:
            print(self.name, "has graduated")
            self.title = "Child, Graduated"


class Adult(Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, gender)
        self.title = "Adult"
        self.mpartner = ()

    def employ(self):
        self.title = "Adult, Employed"
        self.job = "Employed"

    def birth(self, name, gender):
        if self.gender == "F" and self.is_alive is True:
            Child(name, 0, gender)
            print(name, "(" + gender + ") has been born")
            print("The mother is:", self.name)

        elif self.gender == "M":
            print("Males are unable to give birth")

    def is_married(self):
        if self.mpartner is None:
            return False
        else:
            return True

    def marriage(self, partner):
        if self.is_married():
            print(self.name, "is already married")
        elif partner.is_married():
            print(partner.name, "is already married")
        else:
            self.mpartner = partner
            partner.mpartner = self

    def divorce(self, partner):
        try:
            self.mpartner = ()
            partner.mpartner = ()
        except Exception as e:
            print(e)
