class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("my name is", self.name, "and I am", self.age, "years old")
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print("my name is", self.name, "and I am", self.age, "years old and I am", self.color, "in color")

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")


cat1 = Cat("Cane", 2, "red")
dog1 = Dog("Bingo", 1)
cat1.speak()
dog1.speak()
cat1.show()
dog1.show()