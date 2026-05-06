from abc import ABC, abstractmethod

# full form of ABC is Abstract Base Class
class Animal(ABC):
    pass

# this is not necessary that Every Abstract Class Must have abstract methods

#  here I have used abstract class and it has not abstract method


class Dog(Animal):
    pass

a = Animal()

d = Dog()

