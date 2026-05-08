class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def bark(self):
        print(f"{self.name} Barks....")

class Cat(Animal):

    def mews(self):
        print(f"{self.name} Mews....")


d = Dog("Billo")
c = Cat("Rani")

d.bark()
c.mews()