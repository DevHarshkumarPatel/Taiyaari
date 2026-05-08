class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


d = Dog("Billo", "Laby")
print(f"Name :: {d.name}")          # from Animal
print(f"Breed :: {d.breed}")        # from Dog