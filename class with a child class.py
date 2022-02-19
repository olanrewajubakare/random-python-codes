class Person:
    def __init__(self, lname, fname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print("My name is " + self.lname + " " + self.fname)


x = Person("Ipinloju", "Isaac")
x.print_name()


class Child2(Person):
    def __init__(self, lname, fname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduation_year)


y = Child2("Ipinloju", "Isaiah", 2024)
y.welcome()
