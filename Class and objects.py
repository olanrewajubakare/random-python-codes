class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def my_func(self):
        print("my name is " + self.name)
        print("my age is " + self.age)
        print("my weight is " + self.weight)


person1 = Person("Bakare", "23", "23")
person1.my_func()


class Isaac(Person):
    pass


person2 = Isaac("Ipinloju", "13", "10kg")
person2.my_func()
