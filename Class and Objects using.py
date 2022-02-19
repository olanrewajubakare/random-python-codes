class Self:

    def __init__(me, name, age, weight):
        me.name = name
        me.age = age
        me.weight = weight

    def introduce(me):
        print("my name is " + me.name)
        print("my age is " + me.age)
        print("my weight is " + me.weight)


person1 = Self("Bakare", "20", "23")
person1.introduce()

person2 = Self("jerry", "15", "16")
person2.introduce()
