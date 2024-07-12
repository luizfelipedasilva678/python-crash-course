class Dog:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


dog = Dog("willie", 6)


dog.sit()
