from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        print("inside Animal ....")


class Dog(Animal):
    # pass
    def sound(self):
        print(f"Dog Barks..")

d = Dog()

d.sound()

# now I have inherited the Animal class and also implemented that abstract method inside so after creating object now no error like TypeError, and also we have written something inside that does not matter
# THis is just a test