class Animal:
    def __init__(self, name):
        self.name = name

class Mamal(Animal):
    def __init__(self, name, babies):
        super().__init__(name)
        self.babies = babies

class Dog(Mamal):
    def __init__(self, name, babies, breed):
        super().__init__(name, babies)
        self.breed = breed


    def check_method(self):
        print(f"{self.name} has {self.babies} babies and they are from {self.breed} Family.")


d = Dog("Billo",5,"Laby")

d.check_method()

# this is multilevel inheritance - it is advisable to go max upto 3 to 4 levels.
