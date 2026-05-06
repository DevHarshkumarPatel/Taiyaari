from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass



a = Animal()

# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'sound'
# Note : Now I have abstract class and inside that i have one abstract method as well Now and Rule
# If a class contains even ONE abstract method, Python treats that class as incomplete.
# Animal class have abstractmethod and rule of abstract method is we can write general logic inside that abstarct method but this abstractmethod must have implementation in Child class. So this is the reason Python thinks that Animal class is incomplete.